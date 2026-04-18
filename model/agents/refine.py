from utils.llm import call_llm

def refine_notes(notes, feedback):
    improvements = "\n".join(feedback["improvements"])

    prompt = f"""
    Improve the notes using these improvements:

    {improvements}

    Notes:
    {notes}

    Output improved notes only.
    """

    return call_llm(prompt)


def refine_node(state):
    notes = state["notes"]
    feedback = state["feedback"]

    improved = refine_notes(notes, feedback)

    return {
        "notes": improved,
        "iteration": state.get("iteration", 0) + 1
    }