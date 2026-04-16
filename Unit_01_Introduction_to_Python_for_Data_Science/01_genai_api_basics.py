import os
from google import genai
import pathlib
import textwrap
from dotenv import load_dotenv
from IPython.display import Markdown, display


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



# print("--- Available Models ---")
# # This lists all models your API key has access to
# for model in client.models.list():
#     if 'generateContent' in model.supported_actions:
#         print(f"Name: {model.name}")
#         print(f"Display Name: {model.display_name}")
#         print("-" * 20)


response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Tell me a short joke about Python programming."
)

print(response.text)