from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentence = "We may access your camera during video calls."

embedding = model.encode(sentence)

print("Embedding Dimension:", len(embedding))
print(embedding[:10])