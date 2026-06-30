from pathlib import Path

# ==============================
# Project Paths
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

UPLOAD_DIR = DATA_DIR / "uploads"

REPORT_DIR = DATA_DIR / "reports"

# ==============================
# Supported Files
# ==============================

SUPPORTED_FILE_TYPES = [".pdf"]

# ==============================
# AI Models
# ==============================

GEMINI_MODEL = "gemini-2.5-flash"

MISTRAL_MODEL = "mistral-small-2506"

# ==============================
# App
# ==============================

APP_NAME = "AI Resume Review Agent"