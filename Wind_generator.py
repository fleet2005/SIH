import pandas as pd
import pickle

# Load the CSV file into a DataFrame
df = pd.read_csv('final.csv')

# Extract the required columns
data_to_save = df[['longitude', 'latitude', 'wind_direction_10m_dominant']]

# Save the extracted columns to a .pkl file
with open('longitude_latitude_wind_direction.pkl', 'wb') as f:
    pickle.dump(data_to_save, f)

print("Data has been saved to longitude_latitude_wind_direction.pkl")
