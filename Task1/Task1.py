import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your actual CSV file (use full name and skip 4 header rows)
df = pd.read_csv(r'c:/Users/DELL/Desktop/Task1/population.csv', skiprows=4)

# Display first few rows to confirm it's loaded correctly
print(df.head())

# Step 1: Select only the columns we need
latest_year = '2022'
df_clean = df[['Country Name', latest_year]]

# Step 2: Drop rows with missing values
df_clean = df_clean.dropna()

# Step 3: Sort by population in descending order
df_sorted = df_clean.sort_values(by=latest_year, ascending=False)

# Step 4: Take top 10 countries
top10 = df_sorted.head(10)

# Step 5: Plot the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x=top10[latest_year], y=top10['Country Name'], palette='viridis', legend=False)
plt.title(f'Top 10 Most Populous Countries in {latest_year}')
plt.xlabel('Population')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

plt.savefig("top10_population_2022.png")

# Remove NaNs first
all_data = df[['Country Name', '2022']].dropna()

# Histogram of population distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=top10[latest_year], y=top10['Country Name'], hue=top10['Country Name'], palette='viridis', legend=False)

plt.title('Distribution of Population Across All Countries (2022)')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.tight_layout()
plt.show()

top10.to_csv("top10_population_2022.csv", index=False)