import pandas as pd
import os

# Define the data folder path
data_folder = "data"

# File paths
stock_market_data_path = os.path.join(data_folder, "stock_market_data_large.csv")
symbols_meta_path = os.path.join(data_folder, "symbols_valid_meta.csv")
stock_data_path = os.path.join(data_folder, "Stock_data (1).csv")

# Load datasets
stock_market_data = pd.read_csv(stock_market_data_path)
symbols_meta = pd.read_csv(symbols_meta_path)
stock_data = pd.read_csv(stock_data_path)

# Display dataset information
print("Stock Market Data:")
print(stock_market_data.info())
print("\nSymbols Metadata:")
print(symbols_meta.info())
print("\nStock Data:")
print(stock_data.info())

# Handling missing values (forward fill where applicable)
stock_market_data.ffill(inplace=True)
symbols_meta.ffill(inplace=True)
stock_data.ffill(inplace=True)

# Standardize column names by stripping spaces
stock_market_data.columns = stock_market_data.columns.str.strip()
symbols_meta.columns = symbols_meta.columns.str.strip()
stock_data.columns = stock_data.columns.str.strip()

# Convert date columns to datetime format (if applicable)
for df in [stock_market_data, symbols_meta, stock_data]:
    for col in df.columns:
        if "Date" in col:
            df[col] = pd.to_datetime(df[col], errors='coerce')

# Ensure 'Symbol' column exists before merging
if 'Symbol' in stock_market_data.columns and 'NASDAQ Symbol' in symbols_meta.columns:
    merged_data = stock_market_data.merge(symbols_meta, how='left', left_on='Symbol', right_on='NASDAQ Symbol')
    print("\nMerged Data Preview:")
    print(merged_data.head())
    
    # Save cleaned data
    output_path = os.path.join(data_folder, "processed_stock_data.csv")
    merged_data.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")
else:
    print("Error: Required columns for merging are missing. Check column names.")