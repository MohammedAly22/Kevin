import re
import time

from src.browser import GoogleSearch
from src.browser import Browser


browser = Browser()
google_search = GoogleSearch()


def stream_text(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.01)


def search_queries(queries):
    results = {}

    for query in queries:
        query = query.strip().lower()

        google_search.search(query)
        link = google_search.get_first_link()

        browser.go_to(link)

        results[query] = {"link": link, "content": browser.extract_text().strip()}

    return results


def prepare_coding_files(coder_output):
    pattern = re.compile(r"```\w+\s+(.*?)\s+```", re.DOTALL)
    prepared_code_files = []

    for item in coder_output:
        match = pattern.search(item["code"])
        if match:
            item["code"] = match.group(1)

        prepared_code_files.append(item)

    return prepared_code_files
