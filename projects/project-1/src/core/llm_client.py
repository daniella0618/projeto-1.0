import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

class AzureModel:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        self.deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")

    def invoke(self, prompt: str):
        response = self.client.chat.completions.create(
            model=self.deployment_name,  # ✅ aqui que usa o deployment
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response
