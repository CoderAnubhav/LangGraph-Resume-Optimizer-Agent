from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import agent
from app.linkedin import fetch_linkedin_jd

app = FastAPI()

class ResumeRequest(BaseModel):
    linkedin_url: str
    resume_tex_path: str

@app.post("/tailor-resume")
def tailor_resume(req: ResumeRequest):
    # 1. Fetch JD
    jd = fetch_linkedin_jd(req.linkedin_url)

    # 2. Read LaTeX file
    with open(req.resume_tex_path, "r", encoding="utf-8") as f:
        latex_resume = f.read()

    # 3. Run agent
    result = agent.invoke({
        "linkedin_url": req.linkedin_url,
        "job_description": jd,
        "latex_resume": latex_resume
    })

    # 4. Write tailored LaTeX to new file
    output_path = req.resume_tex_path.replace(".tex", "_tailored.tex")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["tailored_latex"])

    return {
        "output_tex_path": output_path,
    }
