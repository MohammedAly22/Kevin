import json
from jinja2 import Environment, BaseLoader

from src.llm import LLM


decision_prompt = open("src/agents/decision_taker/prompt.jinja2").read().strip()


class DecisionTaker:
    def __init__(self, base_model, api_key) -> None:
        self.llm = LLM(base_model, api_key)

    def render(self, prompt: str) -> str:
        env = Environment(loader=BaseLoader())
        template = env.from_string(decision_prompt)

        return template.render(prompt=prompt)

    def validate_response(self, response):
        response = response.strip().replace("```json", "```")

        if response.startswith("```") and response.endswith("```"):
            response = response[3:-3].strip()

        try:
            response = json.loads(response)
        except Exception as _:
            return False

        for item in response:
            if "function" not in item or "args" not in item or "reply" not in item:
                return False

        return response

    def execute(self, prompt):
        rendered_prompt = self.render(prompt)
        response = self.llm.inference(rendered_prompt)

        valid_resposne = self.validate_response(response)

        while not valid_resposne:
            print("The Decision Taker has made an error, trying again...\n")
            return self.execute(prompt)

        return valid_resposne
