# agents/researcher.py

from utils.llm import call_llm
from tools.web_search import search_web
import asyncio

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

async def process_subtopic(topic, sub):
    print(f"Researching: {sub}")

    results = await asyncio.to_thread(search_web, f"{topic}{sub}")
    formatted = format_results(results)

    prompt = """
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

    explanation = await asyncio.to_thread(call_llm, prompt)
    return sub, {
        "content": explanation,
        "sources": [r.get("url") for r in results]
    }

async def researcher_agent_async(topic, subtopics):
    tasks = [
        process_subtopic(topic, subtopic)
        for subtopic in subtopics
    ]

    results = await asyncio.gather(*tasks)

    return dict(results)

def researcher_node(state):
    topic = state["topic"]
    subtopics = state["subtopics"]

    research_data = asyncio.run(
        researcher_agent_async(topic, subtopics)
    )

    return {
        "research_data" : research_data
    }