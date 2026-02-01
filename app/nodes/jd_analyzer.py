from app.llm import get_llm
import json

llm = get_llm(0.1)

def jd_analyzer(state):
    prompt = f"""
Extract ATS-relevant information as JSON.

Fields:
- role
- seniority
- required_skills
- preferred_skills
- tools
- keywords

JOB DESCRIPTION:
{state['cleaned_jd']}
"""
    res = llm.invoke(prompt)

    try:
        data = json.loads(res.content)
    except:
        data = {"raw": res.content}

    return {"jd_analysis": data}
