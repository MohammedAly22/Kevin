import re
import json
from jinja2 import Environment, BaseLoader

from src.llm import Cohere


project_creator_prompt = (
    open("Kevin/src/agents/project_creator/prompt.jinja2").read().strip()
)


class ProjectCreator:
    def __init__(self):
        self.llm = Cohere()

    def render(self, project_name, full_code):
        env = Environment(loader=BaseLoader)
        template = env.from_string(project_creator_prompt)
        return template.render(project_name=project_name, full_code=full_code)

    def validate_response(self, response):
        try:
            json_response = json.loads(response)
        except Exception as _:
            return False

        if "code" not in json_response and "reply" not in json_response:
            return False
        else:
            # Define regular expression pattern to match code content
            pattern = re.compile(r"```\w+\s+(.*?)\s+```", re.DOTALL)
            match = pattern.search(json_response["code"])
            if match:
                json_response["code"] = match.group(1)

            return json_response

    def execute(self, project_name, full_code):
        prompt = self.render(project_name, full_code)
        response = self.llm.inference(prompt)

        valid_response = self.validate_response(response)

        while not valid_response:
            print("Invalid response from the project creator, trying again...")
            return self.execute(project_name, full_code)

        return valid_response
