import pandas as pd

# Load raw data
df = pd.read_csv('raw_data.csv')

# Drop duplicate rows
df = df.drop_duplicates()

# Fill missing emails with placeholder
df['Email'] = df['Email'].fillna('noemail@unknown.com')

# Normalize Date of Birth to YYYY-MM-DD
df['Date of Birth'] = pd.to_datetime(df['Date of Birth'], errors='coerce').dt.strftime('%Y-%m-%d')

# Standardize phone numbers (remove spaces and dashes)
df['Phone'] = df['Phone'].astype(str).str.replace(r'\D', '', regex=True)

# Save cleaned data
df.to_csv('clean_data.csv', index=False)

print("Data cleaning completed. Output saved to 'clean_data.csv'.")
