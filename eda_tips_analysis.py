import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

df = sns.load_dataset('tips')

print("--- FIRST 5 ROWS ---")
print(df.head())
print("\n")

print("--- DATASET SHAPE (Rows, Columns) ---")
print(df.shape)
print("\n")

print("--- DATA TYPES & MISSING VALUES ---")
print(df.info())
print("\n")

print("--- STATISTICAL SUMMARY ---")
print(df.describe())
print("\n")

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='total_bill', y='tip', hue='day', style='sex', s=70)
plt.title('Total Bill vs. Tip Amount by Day and Gender', fontsize=14)
plt.xlabel('Total Bill ($)', fontsize=12)
plt.ylabel('Tip Amount ($)', fontsize=12)
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df['total_bill'], kde=True, bins=20, color='skyblue')
plt.title('Distribution of Total Bills', fontsize=14)
plt.xlabel('Total Bill ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='day', y='tip', palette='viridis')
plt.title('Average Tip Amount by Day of the Week', fontsize=14)
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Average Tip ($)', fontsize=12)
plt.show()