from utils.llm import call_llm

def refine_notes(notes, feedback):
    prompt = f"""
    Improve the following notes using the feedback.

    Notes:
    {notes}

    Feedback:
    {feedback}

    Instructions:
    - Fix weaknesses
    - Apply improvements
    - Keep structure clean

    Output improved notes only.
    """

    return call_llm(prompt)

def refine_node(state):
    notes = state["notes"]
    feedback = state["feedback"]

    improved_notes = refine_notes(notes, feedback)

    return {
        "notes": improved_notes
    }