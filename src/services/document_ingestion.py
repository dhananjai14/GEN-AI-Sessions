import os
from typing import List
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def load_pdf(file_path: os.path) -> str:
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    all_texts = ''
    for doc in docs:
        all_texts = all_texts + doc.page_content
    return all_texts


def create_langchain_docs(text:str) -> List[Document]:
    """
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(text)
    document_list = []
    for txt in texts:
        metadata = {'file_name':'AWS_Lambda documentation'}
        document_list.append(Document(page_content=txt, metadata = metadata))
    return document_list


if __name__ == "__main__":
    # Sample usage 
    file_path = r"C:\Users\DhananjaiSingh\Desktop\PythonTutorials\Gen-AI\input\lambda-dg.pdf"
    file_content = load_pdf(file_path)
    print(file_content[:1000])
