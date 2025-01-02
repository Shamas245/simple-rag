# Simple RAG (Retrieval-Augmented Generation) System

This project demonstrates a basic Retrieval-Augmented Generation (RAG) pipeline by integrating a Pinecone vector store and a Google Generative AI model. It highlights how information can be retrieved and augmented with generated content for better understanding and enhanced results.

---

## Key Features
1. **Environment Variable Management**: Use
s `.env` for securely storing sensitive API keys.
2. **Vector Store Creation**: Demonstrates how to create and manage a Pinecone index for storing embeddings.
3. **Embedding Generation**: Converts textual data into numerical embeddings using `GoogleGenerativeAIEmbeddings`.
4. **Document Similarity Search**: Retrieves relevant documents based on user queries.
5. **LLM Integration**: Generates human-like responses using a Google Generative AI model.
6. **End-to-End RAG Workflow**: Combines retrieval and generation for intelligent query responses.

---

## How the Code Contributes to RAG Understanding

### 1. **Environment Setup**
- Uses a `.env` file to securely store API keys (`PINECONE_API_KEY` and `GOOGLE_API_KEY`), showcasing best practices for managing sensitive credentials.
- Encourages modular and reusable code design.

### 2. **Data Storage and Retrieval**
- **Vector Store**: 
  - Creates a Pinecone index to store embeddings. This step teaches the basics of how retrieval systems are built.
  - Stores documents with metadata, such as the source of information, providing traceability for retrieved content.
- **Similarity Search**: 
  - Demonstrates how to retrieve relevant documents from the vector store based on user queries.

### 3. **Embedding Models**
- Leverages the `GoogleGenerativeAIEmbeddings` model to generate embeddings, explaining how text is transformed into vector representations for efficient similarity comparison.

### 4. **Integration with Language Model (LLM)**
- The `ChatGoogleGenerativeAI` model generates responses by combining user queries with retrieved documents.
- Highlights the integration of retrieval and generation phases, a key concept in RAG systems.

### 5. **End-to-End Workflow**
- **Input**: User query initiates the retrieval process.
- **Processing**: Pinecone retrieves relevant documents, which are then passed to the LLM for response generation.
- **Output**: Outputs a comprehensive answer that is grounded in the retrieved data.

---

## Installation and Setup

1. **Clone the repository:**
   Replace `<repository_url>` with the actual URL of your GitHub repository, and `<repository_name>` with your repository name.

   ```bash
   git clone https://github.com/Shamas245/simple-rag.git
   cd simple-rag


