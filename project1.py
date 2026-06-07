import pandas as pd

# Load Excel file
df = pd.read_excel("Car_Data_Analysis.xlsx")

print("Dataset")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values with column average
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Mileage"] = df["Mileage"].fillna(df["Mileage"].mean())

print("\nAfter Cleaning:")
print(df.isnull().sum())

# Save cleaned file
df.to_excel("Cleaned_Car_Data.xlsx", index=False)
print()