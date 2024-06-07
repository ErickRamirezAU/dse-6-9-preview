import openai, cassio
from cassandra.cluster import Cluster
from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.vector_stores.cassandra import CassandraVectorStore

openai.api_key = "sk-..."

cluster = Cluster(["127.0.0.1"])
session = cluster.connect()
cassio.init(session=session, keyspace="demo",)

storage_context = StorageContext.from_defaults(vector_store=CassandraVectorStore(table='ragdemo', embedding_dimension=1536, insertion_batch_size=15))

documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
