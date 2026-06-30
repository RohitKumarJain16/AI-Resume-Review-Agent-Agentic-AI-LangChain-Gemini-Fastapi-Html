from src.report_generator import ReportGenerator

dummy = {
    "ats": "ATS Score: 84/100",
    "skills": "Strong Python and ML skills.",
    "projects": "Projects need more measurable impact.",
    "hr": "Resume formatting is professional."
}

report = ReportGenerator.generate(dummy)

print(report)