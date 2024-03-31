import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


class Browser:
    def __init__(self):
        self.session = requests.Session()
        self.response = None
        self.soup = None

    def go_to(self, url):
        self.response = self.session.get(url)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def get_html(self):
        return self.response.text if self.response else None

    def get_markdown(self):
        return md(self.get_html()) if self.response else None

    def extract_text(self):
        return self.soup.get_text() if self.soup else None

    def close(self):
        self.session.close()
