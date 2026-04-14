# Task 3: Analysis with Pandas & NumPy
# This script loads cleaned CSV, performs analysis, and adds new columns

import pandas as pd
import numpy as np


# Step 1: Load and Explore


file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)

# Print basic info
print(f"Loaded data: {df.shape}")

print("\nFirst 5 rows:")
print(df.head())

# Average values
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print(f"\nAverage score   : {avg_score}")
print(f"Average comments: {avg_comments}")



# Step 2: NumPy Analysis


scores = df["score"].to_numpy()

mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

max_score = np.max(scores)
min_score = np.min(scores)

print("\n--- NumPy Stats ---")
print(f"Mean score   : {mean_score}")
print(f"Median score : {median_score}")
print(f"Std deviation: {std_score}")
print(f"Max score    : {max_score}")
print(f"Min score    : {min_score}")

# Category with most stories
category_counts = df["category"].value_counts()
top_category = category_counts.idxmax()
top_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# Most commented story
max_comments_row = df.loc[df["num_comments"].idxmax()]

print(f"\nMost commented story: \"{max_comments_row['title']}\" — {max_comments_row['num_comments']} comments")


# Step 3: Add New Columns


# Engagement formula
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular flag
df["is_popular"] = df["score"] > avg_score


# Step 4: Save CSV


output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print(f"\nSaved to {output_file}")
