from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel


APP_VERSION = "1.0.0"
UPLOAD_DIR = Path(__file__).resolve().parent / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class HealthResponse(BaseModel):
    status: str
    message: str
    version: str


class DetectionResult(BaseModel):
    person_detected: bool
    truck_detected: bool
    risk_level: str
    confidence: str


class UploadResponse(BaseModel):
    success: bool
    message: str
    result: DetectionResult


app = FastAPI(
    title="AI Graduation Project Demo API",
    version=APP_VERSION,
    description="FastAPI backend for AI-powered undergraduate graduation project demo."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def build_mock_result(filename: str, file_size: int) -> DetectionResult:
    lower_name = filename.lower()
    person_detected = any(keyword in lower_name for keyword in ["person", "student", "people", "human"])
    truck_detected = any(keyword in lower_name for keyword in ["truck", "car", "traffic", "vehicle"])

    if not person_detected and file_size % 2 == 0:
        person_detected = True
    if not truck_detected and file_size % 3 == 0:
        truck_detected = True

    if person_detected and truck_detected:
        risk_level = "high"
        confidence = "96%"
    elif person_detected or truck_detected:
        risk_level = "medium"
        confidence = "89%"
    else:
        risk_level = "low"
        confidence = "82%"

    return DetectionResult(
        person_detected=person_detected,
        truck_detected=truck_detected,
        risk_level=risk_level,
        confidence=confidence,
    )


@app.get("/api/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(status="ok", message="Backend service is running", version=APP_VERSION)


@app.post("/api/upload", response_model=UploadResponse)
async def upload_image(file: UploadFile = File(...)) -> JSONResponse:
    if not file.filename:
        raise HTTPException(status_code=400, detail="File name is missing.")

    extension = Path(file.filename).suffix.lower()
    if extension not in {".png", ".jpg", ".jpeg"}:
        raise HTTPException(status_code=400, detail="Only PNG, JPG, and JPEG files are supported.")

    target_path = UPLOAD_DIR / f"{uuid4().hex}{extension}"
    file_bytes = await file.read()

    if not file_bytes:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    target_path.write_bytes(file_bytes)
    result = build_mock_result(file.filename, len(file_bytes))

    response = UploadResponse(
        success=True,
        message="Detection completed",
        result=result
    )
    return JSONResponse(content=response.model_dump())
