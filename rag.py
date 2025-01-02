# Install dependencies
# Run this in your terminal or include as comments for manual execution
# pip install langchain_google_genai
# pip install langchain_pinecone

import os
import time
from getpass import getpass
from pinecone import Pinecone, ServerlessSpec
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access API key
pinecone_api_key = os.getenv("PINECONE_API_KEY")
if not pinecone_api_key:
    raise ValueError("PINECONE_API_KEY is not set in the .env file")

#Acess google_api_key
google_api_key = os.getenv("GOOGLE_API_KEY")
if not pinecone_api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the .env file")

# Pinecone setup
pc = Pinecone(api_key=pinecone_api_key)
index_name = "simple-rag-index"  # Change if desired

existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

index = pc.Index(index_name)

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Initialize Vector Store
vector_store = PineconeVectorStore(index=index, embedding=embeddings)

# Example documents
documents = [
    Document(
        page_content="I had chocolate chip pancakes and scrambled eggs for breakfast this morning.",
        metadata={"source": "tweet"},
    ),
    Document(
        page_content="The weather forecast for tomorrow is cloudy and overcast, with a high of 62 degrees.",
        metadata={"source": "news"},
    ),
    Document(
        page_content="Building an exciting new project with LangChain - come check it out!",
        metadata={"source": "tweet"},
    ),
    Document(
        page_content="Robbers broke into the city bank and stole $1 million in cash.",
        metadata={"source": "news"},
    )
]

# Adding documents to the vector store
for doc in documents:
    vector_store.add_documents([doc])

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
sys_message = SystemMessage(content="You are an AI assistant to get the query and vector_store result to answer the question.")

# Function to query vector store
def ask_from_document(query: str):
    result = vector_store.similarity_search(query, k=2)
    final_result = llm.invoke([sys_message] + [HumanMessage(content=(result[0].page_content + query))])
    return final_result.content

# Example query
response = ask_from_document("let me know about weather?")
print(response)
