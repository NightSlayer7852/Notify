# agents/researcher.py

from utils.llm import call_llm
from tools.web_search import search_web

def format_results(results):
    """Convert Tavily results into clean text for LLM"""
    
    formatted = ""
    
    for i, r in enumerate(results, 1):
        formatted += f"""
        Source {i}:
        Title: {r.get('title')}
        URL: {r.get('url')}
        Content: {r.get('content')}
        """

    return formatted


def researcher_agent(topic, subtopics):
    research_data = {}

    for sub in subtopics:
        print(f"\nResearching: {sub}")

        # Step 1: Search
        results = search_web(f"{topic} {sub}")

        # Step 2: Format results
        formatted_data = format_results(results)

        # Step 3: Send to LLM
        prompt = f"""
        You are a research assistant.

        Use ONLY the information provided below to explain the topic.

        Topic: {topic}
        Subtopic: {sub}

        Data:
        {formatted_data}

        Instructions:
        - Give a clear explanation
        - Be structured
        - Do NOT add outside knowledge
        - If data is insufficient, say so

        Output:
        """

        explanation = call_llm(prompt)

        research_data[sub] = {
            "content": explanation,
            "sources": [r["url"] for r in results]
        }

    return research_data

def researcher_node(state):
    topic = state["topic"]
    subtopics = state["subtopics"]

    research_data = researcher_agent(topic, subtopics)

    return {
        "research_data": research_data
    }