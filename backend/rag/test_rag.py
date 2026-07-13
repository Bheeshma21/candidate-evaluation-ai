from rag.retriever import Retriever

retriever = Retriever()

query = "How do you optimize FastAPI performance?"

results = retriever.retrieve(query)

print("\n===== RAG RESULTS =====\n")

for doc in results:
    print(doc)
    print("-" * 60)