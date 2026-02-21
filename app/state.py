"""
from typing import TypedDict,Dict,List

class ResumeState(TypedDict):
    job_url: str
    job_description: str

    jd_analysis: Dict
    jd_keywords: List[str]

    latex_resume: str
    resume_sections: Dict

    gaps: Dict
    tailored_latex: str

    ats_score: float
    ats_feedback:Dict

"""
from typing import TypedDict, Optional, Dict

class AgentState(TypedDict):
    #linkedin_url: Optional[str]
    job_description: Optional[str]
    cleaned_jd: Optional[str]
    jd_analysis: Optional[Dict]
    latex_resume: Optional[str]
    tailored_latex: Optional[str]


