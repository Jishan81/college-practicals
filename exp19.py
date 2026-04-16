# Aim = Data Analysis using Pandas and Matplot
# Coder = Mayuresh Mene
# Class = F.E.Computers 1
# UIN/Roll no = 251P016 / 15
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv(r"C:\Users\mayur\Downloads\product_sales.csv")
# Display first 5 rows
print(df.head())

# Data types
print(df.dtypes)

# Basic statistics
print(df.describe())

# Check missing values
print(df.isnull().sum())
# Fill missing values
df.fillna(0, inplace=True)
# Remove duplicates
df.drop_duplicates(inplace=True)
print("\nCleaned Data:")
print(df.head())

product_sales = df.groupby("Product")["Revenue"].sum()
print(product_sales)

category_sales = df.groupby("Category")["Units_Sold"].sum()
print(category_sales)

plt.figure()
plt.plot(df["Date"], df["Revenue"])
plt.title("Revenue Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

plt.figure()
product_sales.plot(kind="bar")
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

plt.figure()
plt.hist(df["Revenue"])
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

plt.figure()
plt.scatter(df["Units_Sold"], df["Revenue"])
plt.xlabel("Units Sold")
plt.ylabel("Revenue")
plt.title("Units Sold vs Revenue")
plt.show()