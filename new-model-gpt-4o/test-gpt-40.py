import os

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

import openai

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o")

res = llm.invoke(
    [
        HumanMessage(
            content=[
                {"type": "text", "text": "What is in the image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Garcia-lorca-retrato-de-salvador-dali-1927.jpg"
                    },
                },
            ]
        )
    ]
)

print(res.content)
