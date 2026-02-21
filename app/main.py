from fastapi import FastAPI, Form, UploadFile,File
from app.graph import agent

app = FastAPI()

@app.post("/tailor-resume")
async def tailor_resume(
    raw_job_description: str = Form(...),
    resume_file: UploadFile = File(...)
):
    # 1. Read LaTeX file
    latex_bytes = await resume_file.read()
    latex_resume = latex_bytes.decode("UTF-8")

    # 2. Run agent
    result = agent.invoke({
        "job_description": raw_job_description,
        "latex_resume": latex_resume
    })

    # 3. Write tailored LaTeX
    output_path = resume_file.filename.replace(".tex", "_tailored.tex")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["tailored_latex"])

    return {"output_tex_path": output_path}
