import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_MODEL_NAME = os.getenv("GOOGLE_MODEL_NAME")

llm = GoogleGenerativeAI(model="gemini-2.0-flash", temperature = 0)
    
# # Simple text invocation
result = llm.invoke("Whats the Capital of India?")
print(result)

# # Multimodal invocation with gemini-pro-vision
# message = HumanMessage(
#     content=[
#         {
#             "type": "text",
#             "text": "What's in this image?",
#         },
#         {"type": "image_url", "image_url": "https://picsum.photos/seed/picsum/200/300"},
#     ]
# )
# result = llm.invoke([message])
# print(result.content)