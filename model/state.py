# state.py

from typing import TypedDict, List, Dict

class GraphState(TypedDict):
    topic: str
    subtopics: list
    research_data: dict
    notes: str
    summary: str
    feedback: str