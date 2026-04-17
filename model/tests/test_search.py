from models.tools.web_search import search_web

results = search_web("Devops")

for r in results:
    print(r["title"])
    print(r["url"])
    print(r["content"])
    print("-" * 50)