from app.llm import get_llm

llm = get_llm(0.1)

def jd_cleaner(state):
    prompt = f"""
Clean the job description for resume matching.

Remove:
- Company marketing text
- EEO / legal boilerplate
- Culture-only sections

Keep:
- Responsibilities
- Skills
- Tools
- Qualifications

Return clean plain text only.

JOB DESCRIPTION:
{state['job_description']}
"""
    res = llm.invoke(prompt)
    return {"cleaned_jd": res.content}
