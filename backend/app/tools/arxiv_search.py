import httpx
import xml.etree.ElementTree as ET

BASE_URL = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"

def arxiv_search(query: str, max_results: int = 5 ):

    if not isinstance(query, str):
        raise TypeError("Query must be a string")
    
    if not query.strip():
        raise ValueError("Search query cannot be empty")

    if isinstance(max_results, bool) or not isinstance(max_results, int):
        raise TypeError("max_results must be an integer")

    if max_results<=0:
        raise ValueError("max_results should be greater than zero")

    if max_results>100:
        raise ValueError("max_results should not be greater than 100")
    
    params = {
        "search_query" : "all:" + query,
        "start": 0,
        "max_results": max_results
    }

    response = httpx.get(BASE_URL, params=params, timeout=30)

    response.raise_for_status()

    root = ET.fromstring(response.text)

    entries = root.findall(f"{ATOM}entry")

    papers = []
    for entry in entries:
        paper_id = entry.find(f"{ATOM}id").text
        title = entry.find(f"{ATOM}title").text
        summary = entry.find(f"{ATOM}summary").text
        published = entry.find(f"{ATOM}published").text
        authors = [
            author.find(f"{ATOM}name").text
            for author in entry.findall(f"{ATOM}author")
        ]

        paper_dict = {
            "paper_id": paper_id,
            "title": title,
            "summary": summary,
            "published": published,
            "authors": authors
        }

        papers.append(paper_dict)
    return papers
        