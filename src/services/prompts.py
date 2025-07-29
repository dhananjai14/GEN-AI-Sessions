from langchain_core.prompts import ChatPromptTemplate

prompt_template  = ChatPromptTemplate([
    ("system", "You Based on the provided context, give the answer to foloowing question {context}"),
    ("user", "{user_query}")
])