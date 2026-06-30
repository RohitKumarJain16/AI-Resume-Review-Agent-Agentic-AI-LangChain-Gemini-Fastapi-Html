from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from src.pdf_parser import ResumeParser
from src.orchestrator import ResumeReviewOrchestrator
from src.report_generator import ReportGenerator

app = FastAPI(
    title="AI Resume Review Agent",
    version="1.0.0"
)

# Allow Frontend Access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

if FRONTEND_DIR.exists():
    app.mount(
        "/static",
        StaticFiles(directory=FRONTEND_DIR),
        name="static",
    )


@app.get("/")
def home():
    index_path = FRONTEND_DIR / "index.htm"

    if index_path.exists():
        return FileResponse(index_path)

    return {"message": "AI Resume Review Agent API Running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze-resume")
async def analyze_resume(
    resume: UploadFile = File(...)
):

    if not resume.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    resume_path = UPLOAD_DIR / resume.filename

    with open(resume_path, "wb") as file:
        file.write(await resume.read())

    try:

        parser = ResumeParser(str(resume_path))

        resume_text = parser.extract_text()

        orchestrator = ResumeReviewOrchestrator()

        results = orchestrator.analyze_resume(
            resume_text
        )

        report = ReportGenerator.generate(
            results
        )

        return JSONResponse(
            {
                "overall_score": 90,

                "ats": results["ats"],

                "skills": results["skills"],

                "projects": results["projects"],

                "hr": results["hr"],

                "report": report
            }
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:

        if resume_path.exists():
            resume_path.unlink()
