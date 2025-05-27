import pandas as pd

# Load the dataset
df = pd.read_csv("athlete_events.csv")

print(df['Sport'].value_counts().head())
print(df['Sex'].value_counts())