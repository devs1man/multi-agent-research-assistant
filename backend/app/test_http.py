import xml.etree.ElementTree as ET

xml_data = """
<entry>
    <title>Computer Vision in Autonomous Vehicles</title>
    <author>
        <name>Alice</name>
    </author>
    <published>2026-03-15</published>
    <summary>Applications of computer vision in autonomous driving.</summary>
</entry>
"""

root = ET.fromstring(xml_data)

title = root.find("title").text
author = root.find("author/name").text
date = root.find("published").text
summary = root.find("summary").text

print("Title:", title)
print("Author:", author)
print("Published:", date)
print("Summary:", summary)