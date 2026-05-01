import pandas as pd


def load_data():
    # Read the CSV file
    df = pd.read_csv("data/health_data.csv")

    # Fill missing Steps with the median value
    df["Steps"] = df["Steps"].fillna(df["Steps"].median())

    # Fill missing Sleep_Hours with 7.0
    df["Sleep_Hours"] = df["Sleep_Hours"].fillna(7.0)

    # Fill missing Heart_Rate_bpm with 68 if the column exists
    if "Heart_Rate_bpm" in df.columns:
        df["Heart_Rate_bpm"] = df["Heart_Rate_bpm"].fillna(68)
    else:
        print("Warning: 'Heart_Rate_bpm' column not found.")

    # Fill missing numeric columns with their median values
    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        if df[column].isnull().any():
            df[column] = df[column].fillna(df[column].median())

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    return df


def calculate_recovery_score(df):
    df = df.copy()

    # Start with a base recovery score
    df["Recovery_Score"] = 50

    # Sleep impact
    df.loc[df["Sleep_Hours"] >= 7, "Recovery_Score"] += 20
    df.loc[df["Sleep_Hours"] < 6, "Recovery_Score"] -= 20

    # Heart rate impact
    df["Recovery_Score"] -= (df["Heart_Rate_bpm"] - 50) / 2

    # Step impact
    df["Recovery_Score"] -= (df["Steps"] - 14000) / 1000

    # Keep score between 0 and 100
    df["Recovery_Score"] = df["Recovery_Score"].clip(0, 100)

    return df


def process_data():
    df = load_data()
    df = calculate_recovery_score(df)
    return df