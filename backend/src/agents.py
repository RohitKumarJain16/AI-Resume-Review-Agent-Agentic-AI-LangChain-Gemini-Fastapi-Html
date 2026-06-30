from langchain_core.output_parsers import StrOutputParser

from src.config import gemini_llm
from src.prompts import (
    ats_prompt,
    skills_prompt,
    project_prompt,
    hr_prompt,
)

# Output Parser
parser = StrOutputParser()

# -------------------------
# ATS Agent
# -------------------------

ats_agent = (
    ats_prompt
    | gemini_llm
    | parser
)

# -------------------------
# Skills Agent
# -------------------------

skills_agent = (
    skills_prompt
    | gemini_llm
    | parser
)

# -------------------------
# Project Agent
# -------------------------

project_agent = (
    project_prompt
    | gemini_llm
    | parser
)

# -------------------------
# HR Agent
# -------------------------

hr_agent = (
    hr_prompt
    | gemini_llm
    | parser
)