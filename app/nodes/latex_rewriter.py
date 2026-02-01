from app.llm import get_llm

llm = get_llm(0.2)

def latex_rewriter(state):
    prompt = f"""
You are editing a LaTeX resume.

STRICT RULES:
- DO NOT change LaTeX structure
- DO NOT add new experience
- DO NOT invent skills
- Rewrite bullet text ONLY
- Optimize wording for ATS keywords

JOB DESCRIPTION:
{state['cleaned_jd']}

LATEX RESUME:
{state['latex_resume']}

Return valid LaTeX only.
"""
    res = llm.invoke(prompt)
    return {"tailored_latex": res.content}
