import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for data generation
start_date = datetime(2025, 1, 1)
days = 365

# Generate date range
dates = [start_date + timedelta(days=i) for i in range(days)]

# Generate data using specified distributions
steps = np.random.normal(loc=8500, scale=2500, size=days).clip(3000, 18000)
sleep_hours = np.random.normal(loc=7.2, scale=1, size=days).clip(4.5, 9.5)
heart_rate = np.random.normal(loc=68, scale=10, size=days).clip(48, 110)
calories_burned = np.random.uniform(1800, 4200, size=days)

active_minutes = np.random.uniform(20, 180, size=days)

# Create DataFrame
data = pd.DataFrame({
    'Date': dates,
    'Steps': steps,
    'Sleep_Hours': sleep_hours,
    'Heart_Rate_bpm': heart_rate,
    'Calories_Burned': calories_burned,
    'Active_Minutes': active_minutes
})

# Introduce missing values (5% of data)
for column in data.columns[1:]:  # skip "Date" column for NaN introduction
    data.loc[data.sample(frac=0.05).index, column] = np.nan

# Save to CSV
data.to_csv('data/health_data.csv', index=False)