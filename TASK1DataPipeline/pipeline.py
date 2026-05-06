import pandas as pd
from sklearn.preprocessing import StandardScaler

def extract(filepath):
    df = pd.read_csv(filepath)
    print("Extracted data shape:", df.shape)
    return df

def transform(df):
    df['Region'].fillna(df['Region'].mode()[0], inplace=True)
    df['Sales'].fillna(df['Sales'].mean(), inplace=True)
    df['Profit'].fillna(df['Profit'].mean(), inplace=True)

    df['ProfitMargin'] = (df['Profit'] / df['Sales']).round(2)

    scaler = StandardScaler()
    df[['Sales', 'Profit']] = scaler.fit_transform(df[['Sales', 'Profit']])

    return df

def load(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Data loaded to {output_path}")

def run_pipeline():
    raw_path = "data/rawsales.csv"
    output_path = "data/cleanedsales.csv"

    df_raw = extract(raw_path)
    df_clean = transform(df_raw)
    load(df_clean, output_path)

    print("ETL Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()