import pandas as pd

# Function to load and process health data

def load_data():
    # Read the CSV file
    df = pd.read_csv('data/health_data.csv')
    
    
    # Handle missing values intelligently
    
    # Fill missing 'Steps' with median value
    df['Steps'].fillna(df['Steps'].median(), inplace=True)
    
    # Fill missing 'Sleep_Hours' with 7.0
    df['Sleep_Hours'].fillna(7.0, inplace=True)
    
    # Verify if 'Heart_Rate_bpm' exists before filling
    if 'Heart_Rate_bpm' in df.columns:
        # Fill missing 'Heart_Rate_bpm' with 68
        df['Heart_Rate_bpm'].fillna(68, inplace=True)
    else:
        print("Warning: 'Heart_Rate_bpm' column not found.")
    
    # Fill missing data in other columns with their median values
    for column in df.columns:
        if df[column].isnull().any():
            df[column].fillna(df[column].median(), inplace=True)

    # Convert 'Date' column to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Return the cleaned DataFrame
    return df

def calculate_recovery_score(df):
    # Initialize the Recovery_Score column with a base score of 50
    df['Recovery_Score'] = 50

    # Adjust the score based on Sleep_Hours
    # Good sleep (7+) improves the score by 20 points
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_Score'] += 20
    # Poor sleep (less than 6) decreases the score by 20 points
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_Score'] -= 20

    # Modify the score based on Heart_Rate_bpm
    # Lower heart rates improve recovery (linearly scaled)
    df['Recovery_Score'] -= (df['Heart_Rate_bpm'] - 50) / 2

    # Adjust the score based on Steps
    # Moderate activity is beneficial but over 14000 might reduce recovery
    df['Recovery_Score'] -= (df['Steps'] - 14000) / 1000

    # Ensure the Recovery_Score is between 0 and 100
    df['Recovery_Score'] = df['Recovery_Score'].clip(0, 100)

    # Return the DataFrame with the new Recovery_Score column
    return df

def process_data():
    # Load and clean the data
    df = load_data()

    # Calculate and add the Recovery Score
    df = calculate_recovery_score(df)

    # Return the final processed DataFrame
    return df

# process_data function integrates cleaning and recovery score calculation
# It serves as the main function to prepare data for the Streamlit dashboard.

