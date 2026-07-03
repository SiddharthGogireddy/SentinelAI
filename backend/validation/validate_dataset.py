import pandas as pd

VALID_LABELS = {
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
}

df = pd.read_csv("ai/datasets/labeled/clauses.csv")

print(f"Total rows: {len(df)}")

print(f"Duplicate clauses: {df['clause'].duplicated().sum()}")

print(f"Missing labels: {df['permissions'].isna().sum()}")

invalid = []

for _, row in df.iterrows():

    labels = str(row["permissions"]).split("|")

    for label in labels:

        label = label.strip()

        if label not in VALID_LABELS:
            invalid.append(label)

print("\nInvalid Labels:")

if invalid:
    print(sorted(set(invalid)))
else:
    print("None")