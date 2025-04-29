import pandas as pd

# Load the dataset
file_path = "drsi.csv"
df = pd.read_csv(file_path)

# Remove rows from 2 to 192 (zero-based index 1 to 191)
df_cleaned = df.iloc[192:].reset_index(drop=True)

# Rename "Title" column to "Date"
df_cleaned.rename(columns={"Title": "Date"}, inplace=True)

df_cleaned["Date"] = pd.to_datetime(df_cleaned["Date"], format="%Y %b", errors="coerce")


# Manually specify the columns to keep
columns_to_keep = [
    "Date",  # Assuming this is the Date column. Change if necessary.

    # Technology
    "RSI:Retail of computer and telecomms equipment (val sa):All Business Index",

    # Food
    "RSI:Predominantly food stores (val sa):All Business Index",

    # Cosmetic
    "RSI:Retail cosmetic & toilet articles (val sa):All Business Index",

    # Clothing
    "RSI:Retail sale of clothing (val sa):All Business Index",
]

# Check which of the selected columns actually exist in the dataset
existing_columns = [col for col in columns_to_keep if col in df_cleaned.columns]

# Keep only selected columns
df_cleaned = df_cleaned[existing_columns]

# Print first few rows to verify
print(df_cleaned.head())

# Save the cleaned dataset
cleaned_file_path = "cleaned_drsi.csv"
df_cleaned.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
