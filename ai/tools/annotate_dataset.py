import csv

OUTPUT_FILE = "ai/datasets/labeled/clauses.csv"

company = input("Company: ")
document_type = input("Document Type: ")

while True:
    clause = input("\nClause (type 'exit' to quit): ")

    if clause.lower() == "exit":
        break

    permissions = input(
        "Permissions (comma separated): "
    )

    with open(
        OUTPUT_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "",
            company,
            document_type,
            clause,
            permissions
        ])

print("Dataset updated successfully.")