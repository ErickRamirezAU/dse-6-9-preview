import openai, cassio
from cassandra.cluster import Cluster
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.cassandra import CassandraVectorStore

openai.api_key = "sk-..."

cluster = Cluster(["127.0.0.1"])
session = cluster.connect()
cassio.init(session=session, keyspace="demo",)

cassandra_store=CassandraVectorStore(table='ragdemo', embedding_dimension=1536)
index = VectorStoreIndex.from_vector_store(vector_store=cassandra_store)

query_engine = index.as_query_engine()
response = query_engine.query("What is vector search?")
print(response)
