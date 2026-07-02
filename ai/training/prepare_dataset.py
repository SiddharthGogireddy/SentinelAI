import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("ai/datasets/labeled/clauses.csv")

# Split dataset
train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

# Save
train_df.to_csv(
    "ai/datasets/labeled/train.csv",
    index=False
)

test_df.to_csv(
    "ai/datasets/labeled/test.csv",
    index=False
)

print(f"Training samples: {len(train_df)}")
print(f"Testing samples: {len(test_df)}")