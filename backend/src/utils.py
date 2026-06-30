from pathlib import Path
import shutil
import uuid
from datetime import datetime

from src.constants import (
    UPLOAD_DIR,
    REPORT_DIR,
)

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)


def save_uploaded_file(uploaded_file):

    file_name = f"{uuid.uuid4().hex}_{uploaded_file.name}"

    destination = UPLOAD_DIR / file_name

    with open(destination, "wb") as file:
        shutil.copyfileobj(uploaded_file, file)

    return destination


def save_report(report: str):

    file_name = (
        f"report_{datetime.now():%Y%m%d_%H%M%S}.md"
    )

    report_path = REPORT_DIR / file_name

    report_path.write_text(
        report,
        encoding="utf-8"
    )

    return report_path


def delete_file(path: Path):

    if path.exists():
        path.unlink()


def current_timestamp():

    return datetime.now().strftime(
        "%d %B %Y %I:%M %p"
    )