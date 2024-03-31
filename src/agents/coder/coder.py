from jinja2 import Environment, BaseLoader

from src.llm import Cohere


coder_prompt = open("Kevin/src/agents/coder/prompt.jinja2").read().strip()


class Coder:
    def __init__(self):
        self.llm = Cohere()

    def render(self, step_by_step_plan, user_prompt, search_results):
        env = Environment(loader=BaseLoader())
        template = env.from_string(coder_prompt)
        return template.render(
            step_by_step_plan=step_by_step_plan,
            user_prompt=user_prompt,
            search_results=search_results,
        )

    def validate_response(self, response):
        response = response.strip()

        response = response.split("~~~", 1)[1]
        response = response[: response.rfind("~~~")]
        response = response.strip()

        result = []
        current_file = None
        current_code = []
        code_block = False

        for line in response.split("\n"):
            if line.startswith("File: "):
                if current_file and current_code:
                    result.append(
                        {"file": current_file, "code": "\n".join(current_code)}
                    )
                current_file = line.split("`")[1].strip()
                current_code = []
                code_block = False

            elif line.startswith("```"):
                current_code.append(line)
                code_block = not code_block
            else:
                current_code.append(line)

        if current_file and current_code:
            code = "\n".join(current_code)
            code += "```"

            result.append({"file": current_file, "code": code})

        return result

    def execute(self, step_by_step_plan: str, user_prompt: str, search_results: dict):
        prompt = self.render(step_by_step_plan, user_prompt, search_results)
        response = self.llm.inference(prompt)

        valid_response = self.validate_response(response)

        while not valid_response:
            print("Invalid response from the model, trying again...")
            return self.execute(step_by_step_plan, user_prompt, search_results)

        return valid_response
