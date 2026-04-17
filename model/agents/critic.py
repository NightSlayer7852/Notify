# agents/critic.py

from utils.llm import call_llm

def critic_agent(notes):
    prompt = f"""
    You are a strict reviewer.

    Evaluate the following notes:

    {notes}

    Give output in this format:

    Strengths:
    - ...

    Weaknesses:
    - ...

    Improvements:
    - ...

    Be specific and critical.
    """

    return call_llm(prompt)

def critic_node(state):
    notes = state["notes"]

    feedback = critic_agent(notes)

    return {
        "feedback": feedback
    }