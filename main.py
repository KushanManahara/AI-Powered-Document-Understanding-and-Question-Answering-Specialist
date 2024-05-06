import os
import random
import itertools

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Pinecone as pinecone_lang
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import GoogleGenerativeAI

from pinecone import Pinecone, ServerlessSpec

from markdown_utils import to_markdown

# define constants
MODEL_NAME = "gemini-1.5-pro-latest"
EMBEDDING_MODEL_NAME = "models/embedding-001"

# retrieve the environment variables
MODEL_API_KEY = os.environ.get("GOOGLE_API_KEY")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)


# Define the pinecone index name
index_name = "gimhara-pinecone-index"

# initialize the llm model (google gemini model)
llm = GoogleGenerativeAI(model=MODEL_NAME, google_api_key=MODEL_API_KEY)

# Prepare the data
loader = TextLoader(file_path="./data/data.txt")
data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)
texts = text_splitter.split_documents(data)
text_contents = [t.page_content for t in texts]

vector_dim = 768  # number of vector dimension of google gemini embeddings
vector_count = len(texts)


# Initialize embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL_NAME)


def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))


# Example generator that generates many (id, vector) pairs
data_generator = map(
    lambda i: (f"id-{i}", [random.random() for _ in range(vector_dim)]),
    range(vector_count),
)

# create a pinecone instance
pc.create_index(
    name=index_name,
    dimension=vector_dim,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1"),
)

# Initialize the Pinecone index
index = pc.Index(index_name)

# Upsert data with 100 vectors per upsert request
for ids_vectors_chunk in chunks(data_generator, batch_size=100):
    index.upsert(vectors=ids_vectors_chunk)

# create a docserch object for given index
docsearch = pinecone_lang.from_texts(
    [t.page_content for t in texts], embeddings, index_name=index_name
)

# define query
query = "what are the Challenges and Opportunities in Sri Lanka?"

# get the documents from the pinecone db which is similar to the query
docs = docsearch.similarity_search(query)

# create a chain object from langchain for questions and answerings
chain = load_qa_chain(llm, chain_type="stuff")

# run the chain and store the results
chain_output = chain.run(input_documents=docs, question=query)

to_markdown(chain_output)
