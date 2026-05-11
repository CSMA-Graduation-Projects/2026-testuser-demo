# AI-Powered Undergraduate Graduation Project Demo

AI-Powered Undergraduate Graduation Project Demo is a modern full-stack template tailored for undergraduate AI graduation project showcases and thesis defenses. The system adopts a frontend-backend separation architecture, supports image upload, calls a FastAPI service, and returns simulated AI detection results for demonstration and future model integration.

## 1. Project Introduction

This repository provides a presentation-ready engineering template for AI undergraduate graduation projects. It emphasizes:

- modern UI for demo and defense scenarios
- clean frontend-backend separation
- deployable architecture for Vercel and Render
- extensibility for real computer vision or multimodal inference pipelines

The current backend returns mock detection results and can later be replaced with YOLO, OCR, CLIP, SAM, or custom trained models.

## 2. Tech Stack

### Frontend

- Vue 3
- Vite
- Element Plus
- Axios
- Vue Router
- Pinia

### Backend

- FastAPI
- Uvicorn
- Pydantic

### Deployment

- Frontend: Vercel
- Backend: Render / Railway / Docker

## 3. Project Structure

```text
2026-testuser-demo/
├── backend/
│   ├── app/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── start.sh
├── datasets/
├── docs/
├── frontend/
│   ├── src/
│   ├── .env
│   ├── index.html
│   ├── package.json
│   ├── vercel.json
│   └── vite.config.js
├── screenshots/
├── .gitignore
└── README.md
```

## 4. Local Startup

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend default address:

```text
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend default address:

```text
http://127.0.0.1:5173
```

The frontend reads `frontend/.env` by default:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## 5. Frontend Vercel Deployment

1. Push the repository to GitHub.
2. Import the repository into Vercel.
3. Set the project root directory to `frontend`.
4. Add environment variable `VITE_API_BASE_URL` and point it to the deployed backend URL.
5. Build command: `npm run build`
6. Output directory: `dist`

Vercel CLI deployment example:

```bash
cd frontend
npm install
npx vercel --prod
```

## 6. Backend Render Deployment

1. Create a new Web Service on Render.
2. Set the root directory to `backend`.
3. Runtime: `Python 3`
4. Build command:

```bash
pip install -r requirements.txt
```

5. Start command:

```bash
./start.sh
```

6. After deployment, copy the Render public URL and update `VITE_API_BASE_URL` in Vercel.

### Docker Deployment

```bash
cd backend
docker build -t ai-grad-demo-backend .
docker run -p 8000:8000 ai-grad-demo-backend
```

## 7. Git Submission Workflow

```bash
git status
git add .
git commit -m "feat: initialize AI graduation project demo template"
git push origin main
```

## 8. API Overview

### `GET /api/health`

Checks whether the backend service is running.

### `POST /api/upload`

Accepts image uploads and returns a simulated AI detection payload:

```json
{
  "success": true,
  "message": "Detection completed",
  "result": {
    "person_detected": true,
    "truck_detected": true,
    "risk_level": "high",
    "confidence": "96%"
  }
}
```

## 9. Suitable Graduation Project Extensions

- object detection and scene risk assessment
- campus safety monitoring
- industrial safety warning system
- smart transportation vision analysis
- multimodal AI graduation defense demonstrations
