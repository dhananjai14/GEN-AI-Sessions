import os
from config import Config 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

llm = ChatGoogleGenerativeAI(
    model=Config.GEMINI_MODEL,
    temperature=0,
    api_key = Config.GEMINI_API_KEY,
    )

embeddings_model = GoogleGenerativeAIEmbeddings(model = "models/embedding-001", 
                                                google_api_key = Config.GEMINI_API_KEY )


if __name__ == "__main__":
    # Sample usage
    response = llm.invoke("What is the capital of France?")
    print(response.content)