from sentence_transformers import SentenceTransformer, util
import json

with open("ai/config/permissions.json", "r") as f:
    permissions = json.load(f)
    
# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Permission labels
permissions = [
    "camera",
    "microphone",
    "location",
    "contacts",
    "photos",
    "storage",
    "clipboard",
    "notifications",
    "screen sharing",
    "third party data sharing",
    "cookies",
    "auto renewal"
]

# Convert permission labels into embeddings
permission_embeddings = model.encode(
    permissions,
    convert_to_tensor=True
)

# Example clause
clause = "The application may capture images using your device."

# Convert clause into embedding
clause_embedding = model.encode(
    clause,
    convert_to_tensor=True
)

# Compute similarities
scores = util.cos_sim(
    clause_embedding,
    permission_embeddings
)[0]

# Find best match
best_index = scores.argmax().item()

print("Clause:")
print(clause)

print("\nPredicted Permission:")
print(permissions[best_index])

print("\nSimilarity Score:")
print(float(scores[best_index]))