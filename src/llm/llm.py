import os
from langchain_community.chat_models import ChatCohere
from langchain_core.output_parsers import StrOutputParser
import google.generativeai as genai


class LLM:
    def __init__(self, base_model, api_key) -> None:
        self.base_model = base_model

        if base_model == "Gemini-Pro":
            os.environ["GOOGLE_API_KEY"] = api_key
            genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
            self.model = genai.GenerativeModel("gemini-pro")
        else:
            os.environ["COHERE_API_KEY"] = api_key
            self.model = ChatCohere()

    def inference(self, prompt):
        if self.base_model == "Gemini-Pro":
            response = self.model.generate_content(prompt).text
        elif self.base_model == "Cohere":
            chain = self.model | StrOutputParser()
            response = chain.invoke(prompt)

        return response
