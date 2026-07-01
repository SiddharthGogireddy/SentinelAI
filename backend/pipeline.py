from text_extractor import extract_text
from clause_splitter import split_into_clauses


sample_text = """
We may access your camera during video calls.

We collect your location to recommend nearby events.

Your subscription automatically renews every month unless cancelled.
"""

clean_text = extract_text(sample_text)

clauses = split_into_clauses(clean_text)

print("Detected Clauses:\n")

for index, clause in enumerate(clauses, start=1):
    print(f"{index}. {clause}")