import pandas as pd

df = pd.read_csv("data/data.csv")
print(df.shape)
print(df.columns)
print(df.columns.dtype)
print(df.isnull().sum())
print(df.fillna('yt').sample())
print(df.duplicated().sum())
print(df.columns.str.lower().str.replace(" ", "_"))
print(df.dtypes)
import sqlite3

# create connection
conn = sqlite3.connect("database.db")

if_exists="replace"   # OK for now

print("Data loaded into database")
query = "SELECT * FROM cars LIMIT 3"
result = pd.read_sql(query, conn)
print(result)


query = """
SELECT Make, AVG(MSRP) 
FROM cars 
GROUP BY Make 
ORDER BY AVG(MSRP) DESC 
LIMIT 5
"""

result = pd.read_sql(query, conn)

print(result)
import matplotlib.pyplot as plt

# Rename columns for easy use
result.columns = ["Make", "Avg_Price"]

# Create bar chart
plt.bar(result["Make"], result["Avg_Price"])

# Labels and title
plt.title("Top 5 Expensive Car Brands")
plt.xlabel("Car Brand")
plt.ylabel("Average Price")

# Rotate x labels (for readability)
plt.xticks(rotation=45)

# Show chart
plt.show()