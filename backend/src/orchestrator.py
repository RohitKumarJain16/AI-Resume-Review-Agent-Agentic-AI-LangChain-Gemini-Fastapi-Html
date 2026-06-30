from langchain_core.runnables import RunnableLambda, RunnableParallel

from src.agents import (
    ats_agent,
    skills_agent,
    project_agent,
    hr_agent,
)


class ResumeReviewOrchestrator:
    """
    Runs all resume review agents and combines their outputs.
    """

    def __init__(self):

        self.workflow = RunnableParallel(
            ats=RunnableLambda(
                lambda x: ats_agent.invoke({"resume": x["resume"]})
            ),

            skills=RunnableLambda(
                lambda x: skills_agent.invoke({"resume": x["resume"]})
            ),

            projects=RunnableLambda(
                lambda x: project_agent.invoke({"resume": x["resume"]})
            ),

            hr=RunnableLambda(
                lambda x: hr_agent.invoke({"resume": x["resume"]})
            ),
        )

    def analyze_resume(self, resume_text: str):

        return self.workflow.invoke(
            {
                "resume": resume_text
            }
        )