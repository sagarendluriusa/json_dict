from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate

llm = ChatOllama(model="llama3.2:latest", temperature=0)
negotiate_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a well python programmer and senior developer, convert user json input format into dict format "),
    
        ("user", "{question}")
    ])
query = {"name":"John", "age":30, "car":"null"}
formatted_prompt = negotiate_prompt.format(question=query)
response = llm.invoke(formatted_prompt )
print(response)