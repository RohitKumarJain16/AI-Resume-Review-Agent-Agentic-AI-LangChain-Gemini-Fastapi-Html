from datetime import datetime


class ReportGenerator:
    """
    Creates a professional resume review report.
    """

    @staticmethod
    def generate(results: dict) -> str:
        """
        Generate a markdown report from all agent outputs.
        """

        report = f"""
# AI Resume Review Report

Generated on: **{datetime.now().strftime("%d %B %Y %I:%M %p")}**

---

# ATS Analysis

{results["ats"]}

---

# Skills Assessment

{results["skills"]}

---

# Project Review

{results["projects"]}

---

# HR Review

{results["hr"]}

---

## Overall Recommendation

This report combines feedback from four specialized AI agents.
Review the suggestions carefully and improve your resume before applying for jobs.

Good luck with your applications!
"""

        return report.strip()
