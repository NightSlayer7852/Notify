# agents/writer.py

from utils.llm import call_llm

def writer_agent(topic, research_data):
    combined = ""

    for sub, data in research_data.items():
        content = data["content"]
        sources = data["sources"]

        sources_text = "\n".join(
            f"- {s}" for s in sources
        )

        combined += f"""
        ## {sub}

        {content}

        Sources:
        {sources_text}
        """

    prompt = f"""
    Create clean, structured notes for:

    {topic}

    Use:
    - Headings
    - Bullet points
    - Clear formatting

    Content:
    {combined}

        - Keep sources at the end of each section
        - Do not remove or modify links
    """

    return call_llm(prompt)


def writer_node(state):
    topic = state["topic"]
    research_data = state["research_data"]

    notes = writer_agent(topic, research_data)

    return {
        "notes": notes
    }