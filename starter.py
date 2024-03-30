from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
import logging
import sys
import os.path
from dotenv import dotenv_values
import openai

# You can set to DEBUG to see more detailed logs
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Load by default the .env file in the current directory and get the OPENAI_API_KEY
openApiKey = dotenv_values(".env")["OPENAI_API_KEY"]
openai.api_key=openApiKey

# Store the vector index in the storage directory
PERSIST_DIR = "./storage"
if not os.listdir(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data_example").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print("Response : ", response)