from loaders.text_loader import extract_text, load_text
from preprocess.clause_splitter import split_into_clauses


INPUT_FILE = "ai/datasets/raw/Discord/privacy_policy.txt"
OUTPUT_FILE = "ai/datasets/processed/Discord/clauses.txt"

def main():

    raw_text = load_text(INPUT_FILE)

    clean_text = extract_text(raw_text)

    clauses = split_into_clauses(clean_text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:

        for clause in clauses:
            file.write(clause + "\n\n")

    print(f"{len(clauses)} clauses extracted.")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()