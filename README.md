## AI Resume Review Agent

A FastAPI + LangChain app that analyzes a PDF resume with four specialized AI review agents:

- ATS analysis
- Skills assessment
- Project review
- HR review

The backend extracts text from the uploaded PDF, sends it through Gemini-powered prompts, and returns a combined markdown report. The frontend provides a simple upload flow and renders the results in the browser.

## Features

- Upload a resume in PDF format
- Extract resume text from the PDF
- Run parallel AI reviews for ATS, skills, projects, and HR feedback
- Display the combined analysis in a web UI
- Download the final report as a markdown file
- Automatically delete the uploaded file after processing

## Tech Stack

- Python
- FastAPI
- LangChain
- Google Gemini via `langchain-google-genai`
- PyPDF
- Vanilla HTML, CSS, and JavaScript

## Project Structure

```text
ai-resume-review-agent/
├── backend/
│   ├── main.py
│   └── src/
│       ├── agents.py
│       ├── config.py
│       ├── constants.py
│       ├── orchestrator.py
│       ├── pdf_parser.py
│       ├── prompts.py
│       ├── report_generator.py
│       └── utils.py
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.10 or newer
- A Google Gemini API key

## Setup

1. Create and activate a virtual environment.

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependencies.

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the `backend/` directory with your API key.

   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Run the App

Start the FastAPI server from the `backend/` directory:

```bash
uvicorn main:app --reload
```

Then open the app in your browser:

- `http://127.0.0.1:8000`

## How It Works

1. The frontend lets the user choose a PDF resume.
2. The file is uploaded to the backend through `POST /analyze-resume`.
3. `ResumeParser` extracts text from the PDF.
4. `ResumeReviewOrchestrator` runs four LangChain review chains in parallel.
5. `ReportGenerator` combines the results into a markdown report.
6. The frontend displays the analysis and allows downloading the report.

## API Endpoints

### `GET /health`

Returns a basic health check response.

### `POST /analyze-resume`

Accepts a PDF file field named `resume` and returns:

- `overall_score`
- `ats`
- `skills`
- `projects`
- `hr`
- `report`

## Notes

- Only PDF files are accepted.
- Uploaded files are deleted after analysis.
- The frontend expects the backend to be running on the same origin.
- The current UI checks `/health` on page load and shows API status.

## Troubleshooting

- If the app starts without the Gemini key, confirm `GOOGLE_API_KEY` is set in `backend/.env`.
- If PDF parsing fails, make sure the file is a valid, text-readable PDF.
- If the frontend does not load from `/`, verify that the backend is serving `frontend/index.html`.

## License

No license file is currently included.
