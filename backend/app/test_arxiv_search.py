from backend.app.tools.arxiv_search import arxiv_search

papers = arxiv_search("robotics", max_results=5)

print("Total papers:", len(papers))

for paper in papers:
    print("\nTitle:", paper["title"])
    print("Authors:", paper["authors"])