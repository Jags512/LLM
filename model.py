
#LLM Models use:
from langchain_groq import ChatGroq
from dotenv  import load_dotenv
load_dotenv()
import os
model=ChatGroq(model="llama-3.1-8b-instant",api_key=os.getenv("KEY_HF1"))
response=model.invoke("explain llm api")
print(response.content)
