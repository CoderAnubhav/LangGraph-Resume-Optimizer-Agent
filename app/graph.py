from langgraph.graph import StateGraph
from app.state import AgentState
from app.nodes.jd_cleaner import jd_cleaner
from app.nodes.jd_analyzer import jd_analyzer
from app.nodes.latex_rewriter import latex_rewriter
#from app.nodes.ats_checker import ats_checker

graph = StateGraph(AgentState)

graph.add_node("clean_jd", jd_cleaner)
graph.add_node("analyze_jd", jd_analyzer)
graph.add_node("rewrite_latex", latex_rewriter)
#graph.add_node("ats_check", ats_checker)

graph.set_entry_point("clean_jd")

graph.add_edge("clean_jd", "analyze_jd")
graph.add_edge("analyze_jd", "rewrite_latex")
#graph.add_edge("rewrite_latex", "ats_check")

agent = graph.compile()
