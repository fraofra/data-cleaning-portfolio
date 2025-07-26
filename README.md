# Data Cleaning Example (CSV)

This project demonstrates a simple data cleaning task using Python and Pandas.

## Raw Data Issues:
- Missing email addresses
- Inconsistent date formats
- Duplicated rows
- Phone numbers with mixed formats (dashes, spaces)
- Minor data errors (email typos, etc.)

## What this script does:
1. Removes duplicate entries.
2. Fills missing emails with placeholders.
3. Normalizes date formats to YYYY-MM-DD.
4. Cleans phone numbers by removing non-numeric characters.

### Files:
- raw_data.csv → The original messy data.
- clean_data.py → The Python script that processes the data.
- clean_data.csv → The cleaned and structured data.

## How to run:
```bash
python clean_data.py
