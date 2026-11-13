import httpx
import xml.etree.ElementTree as ET

BASE_URL = "https://export.arxiv.org/api/query"

params = {
    "search_query": "all:robotics",
    "start": 0,
    "max_results": 5
}

response = httpx.get(BASE_URL, params=params, timeout=30)

response.raise_for_status()

print("Status: ", response.status_code)
print("Final URL: ", response.url)
print("Response: ", response.text[:2000])

root = ET.fromstring(response.text)
ATOM = "{http://www.w3.org/2005/Atom}"

entries = root.findall(f"{ATOM}entry")

for entry in entries:
    paper_id = entry.find(f"{ATOM}id").text
    title = entry.find(f"{ATOM}title").text
    summary = entry.find(f"{ATOM}summary").text
    published = entry.find(f"{ATOM}published").text
    authors = [
        author.find(f"{ATOM}name").text
        for author in entry.findall(f"{ATOM}author")
    ]

    print("\n------------------------")
    print("Title:", title)
    print("Authors:", authors)
    print("Published:", published)
    print("ID:", paper_id)
    print("Abstract:", summary)