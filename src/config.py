import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    FILE_PATH = r"C:\Users\DhananjaiSingh\Desktop\PythonTutorials\Gen-AI\input\lambda-dg.pdf"
    GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY')
    GEMINI_MODEL = os.getenv('GOOGLE_MODEL_NAME')
