import os
from langchain_community.chat_models import ChatCohere
from langchain_core.output_parsers import StrOutputParser


os.environ["COHERE_API_KEY"] = "ENTER_COHERE_API_KEY_HERE"


class Cohere:
    def __init__(self) -> None:
        self.model = ChatCohere()

    def inference(self, prompt):
        chain = self.model | StrOutputParser()
        response = chain.invoke(prompt)

        return response
