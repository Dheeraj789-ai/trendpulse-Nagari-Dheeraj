# Task 4: Visualizations using Matplotlib
# This script creates charts and saves them as PNG files

import pandas as pd
import matplotlib.pyplot as plt
import os


# Step 1: Load data & setup


file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

# Create outputs folder if not exists
if not os.path.exists("outputs"):
    os.makedirs("outputs")



# Chart 1: Top 10 Stories by Score


# Sort by score and take top 10
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles
top10["title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure()
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")

# Save BEFORE show
plt.savefig("outputs/chart1_top_stories.png")
plt.close()



# Chart 2: Stories per Category


category_counts = df["category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.close()



# Chart 3: Score vs Comments (Scatter)


popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure()
plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()



# Bonus: Dashboard


fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Chart 1 inside dashboard
axs[0].barh(top10["title"], top10["score"])
axs[0].set_title("Top Stories")

# Chart 2 inside dashboard
axs[1].bar(category_counts.index, category_counts.values)
axs[1].set_title("Categories")

# Chart 3 inside dashboard
axs[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axs[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axs[2].set_title("Score vs Comments")

fig.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.close()


print("All charts saved in outputs/ folder")
