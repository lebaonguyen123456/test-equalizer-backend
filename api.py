"""
api.py

FastAPI backend for Audio Equalizer
"""

import os
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from ml.predict import predict_genre

from audio.audio_io import load_audio, save_audio
from audio.equalizer import apply_equalizer

app = FastAPI(title="Audio Equalizer Backend", version="1.0")

# ===== CORS (CHO REACT) =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # khi deploy có thể giới hạn domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== DIRECTORIES =====
INPUT_DIR = "dataset/input"
OUTPUT_DIR = "dataset/output"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.post("/equalizer")
async def equalizer(
    file: UploadFile = File(...), bass: float = 0, mid: float = 0, treble: float = 0
):
    """
    Apply FFT-based equalizer to uploaded audio file
    """

    input_path = os.path.join(INPUT_DIR, file.filename)
    output_filename = f"eq_{file.filename}"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    # Save uploaded file
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Load & process audio
    signal, sr = load_audio(input_path)
    output = apply_equalizer(signal, sr, bass, mid, treble)

    # Save output
    save_audio(output_path, output, sr)

    return {
        "message": "Equalizer applied successfully",
        "download_url": f"/download/{output_filename}",
    }


@app.get("/download/{filename}")
def download_file(filename: str):
    """
    Download processed audio file
    """
    file_path = os.path.join(OUTPUT_DIR, filename)

    if not os.path.exists(file_path):
        return {"error": "File not found"}

    return FileResponse(path=file_path, media_type="audio/mpeg", filename=filename)


@app.post("/classify")
async def classify(file: UploadFile = File(...)):
    """
    Predict music genre from uploaded audio file
    """
    genre, confidence = predict_genre(file.file)

    return {"genre": genre, "confidence": round(float(confidence), 4)}
