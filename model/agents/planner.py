from utils.llm import call_llm

def planner_agent(topic):
    prompt = f"""
    Break the topic into 5-7 structured subtopics.

    Topic: {topic}

    Output ONLY a Python list.
    Example:
    ["Intro", "Architecture", "Use Cases"]
    """ 
    
    result = call_llm(prompt)
    return eval(result)  # quick MVP hack (safe later with json)    

def planner_node(state):
    topic = state["topic"]

    subtopics = planner_agent(topic)

    return {
        "subtopics": subtopics
    }