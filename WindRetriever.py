import pickle
import pandas as pd

class WindDirectionRetriever:
    def __init__(self, pkl_file='longitude_latitude_wind_direction.pkl'):
        # Load the data once during initialization
        with open(pkl_file, 'rb') as f:
            self.data = pickle.load(f)

    def retrieve_wind_direction(self, longitude, latitude):
        # Filter the data based on the provided longitude and latitude
        result = self.data[(self.data['longitude'] == longitude) & (self.data['latitude'] == latitude)]

        # Return the wind direction or the default value of 0
        if not result.empty:
            return result['wind_direction_10m_dominant'].values[0]
        else:
            return 0  # Default value

# Example usage:
retriever = WindDirectionRetriever()  # Load the pickle file only once

longitude = 69.875
latitude = 5.25
wind_direction = retriever.retrieve_wind_direction(longitude, latitude)

print(f"Wind direction at longitude {longitude} and latitude {latitude}: {wind_direction}")
