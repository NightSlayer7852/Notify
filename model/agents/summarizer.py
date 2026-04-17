# agents/summarizer.py

from utils.llm import call_llm

def summarizer_agent(notes):
    prompt = f"""
    Summarize the following into quick revision notes:

    - Keep it short
    - Use bullet points
    - Max 100 words

    Notes:
    {notes}
    """

    return call_llm(prompt)

def summarizer_node(state):
    notes = state["notes"]

    summary = summarizer_agent(notes)

    return {
        "summary": summary
    }