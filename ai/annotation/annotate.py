import sys
from pathlib import Path
from label_suggester import suggest_labels
project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from backend.preprocess.clause_splitter import is_heading
import csv

AVAILABLE_LABELS = [
    "camera",
    "microphone",
    "location",
    "contacts",
    "photos",
    "storage",
    "clipboard",
    "notifications",
    "screen_sharing",
    "cookies",
    "analytics",
    "device_information",
    "device_fingerprinting",
    "account_information",
    "personal_information",
    "payment_information",
    "third_party_sharing",
    "advertising",
    "account_security",
    "two_factor_authentication",
    "auto_renewal",
]


CLAUSES_FILE = Path("ai/datasets/processed/Discord/clauses.txt")
OUTPUT_FILE = Path("ai/datasets/labeled/clauses.csv")

COMPANY = "Discord"
DOCUMENT_TYPE = "Privacy Policy"


def get_next_id():
    if not OUTPUT_FILE.exists():
        return 1

    with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    if len(rows) <= 1:
        return 1

    return int(rows[-1][0]) + 1


def main():

    next_id = get_next_id()

    # Read all clauses
    clauses = []

    with open(CLAUSES_FILE, "r", encoding="utf-8") as file:

        for line in file:

            clause = line.strip()

            if not clause:
                continue

            if is_heading(clause):
                continue

            clauses.append(clause)

    # Open CSV once
    with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile)

        for index, clause in enumerate(clauses):

            print("\n" + "=" * 60)
            print(f"Clause {index + 1} / {len(clauses)}")
            print("=" * 60)
            print(clause)
            print("=" * 60)
            print("\nAvailable Labels:")
            print(" | ".join(AVAILABLE_LABELS))
            suggested = suggest_labels(clause)

            print("\nSuggested Labels:")

            if suggested:
                print(" | ".join(suggested))
            else:
                print("None")

            if labels == "":
                continue
            labels = input("\nLabels (| separated or Enter to skip): ").strip()

            

            entered = [x.strip() for x in labels.split("|")]

            invalid = [x for x in entered if x not in AVAILABLE_LABELS]

            if invalid:
                print(f"Invalid labels: {invalid}")
                continue
            writer.writerow([
                next_id,
                COMPANY,
                DOCUMENT_TYPE,
                clause,
                labels
            ])

            next_id += 1


if __name__ == "__main__":
    main()