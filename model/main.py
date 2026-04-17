# main.py

from graph import build_graph

def run(topic):
    graph = build_graph()

    result = graph.invoke({
        "topic": topic
    })

    print("\n=== FINAL NOTES ===\n")
    print(result["notes"])

    print("\n=== SUMMARY ===\n")
    print(result["summary"])


if __name__ == "__main__":
    topic = input("Enter topic: ")
    run(topic)