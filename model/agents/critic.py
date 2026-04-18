# agents/critic.py
import json
from utils.llm import call_llm

def critic_agent(notes):
    prompt = f"""
    Evaluate the following notes.

    {notes}

    Return ONLY valid JSON in this format:
    {{
        "score": number between 1-10,
        "strengths": ["..."],
        "weaknesses": ["..."],
        "improvements": ["..."]
    }}
    """

    result = call_llm(prompt)

    try:
        data = json.loads(result)
    except:
        # fallback
        data = {
            "score": 5,
            "strengths": [],
            "weaknesses": ["Parsing failed"],
            "improvements": ["Improve structure"]
        }

    return data

def critic_node(state):
    notes = state["notes"]

    data = critic_agent(notes)

    return {
        "feedback": data,
        "score": data["score"]
    }