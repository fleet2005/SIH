import pickle

class HeuristicRetriever:
    def __init__(self, filename="heuristics_data.pkl"):
        self.filename = filename
        self.heuristics = self.load_heuristics()

    def load_heuristics(self):
        """
        Load the heuristics dictionary from a pickle file.
        
        Returns:
            dict: The heuristics dictionary or an empty dictionary if loading fails.
        """
        try:
            with open(self.filename, "rb") as f:
                data = pickle.load(f)
                return data.get("heuristics", {})
        except FileNotFoundError:
            print(f"No saved heuristics data found at {self.filename}. Please ensure the file exists.")
            return {}

    def get_heuristic_value(self, latitude, longitude):
        """
        Retrieve the heuristic value for a given latitude and longitude.

        Args:
            latitude (float): Latitude of the coordinate.
            longitude (float): Longitude of the coordinate.
        
        Returns:
            float: Heuristic value for the coordinate. Returns 0.5 if the value is not found.
        """
        coordinate = (longitude, latitude)
        if coordinate in self.heuristics:
            return self.heuristics[coordinate]
        else:
            print(f"No heuristic value found for ({latitude}, {longitude}). Returning default value 0.5.")
            return 0.1  # Default value if the coordinate is not found


# Test the retrieval directly
heuristic_retriever = HeuristicRetriever("heuristics_data.pkl")  # Initialize with existing file

# Test cases
test_coordinates = [
    (5.25, 68.875),  # Example coordinate that may exist in the file
    (6.75, 70.125),  # Example coordinate that may exist in the file
    (7.25, 72.875),  # Example coordinate that may exist in the file
    (8.0, 73.0)      # Example coordinate that may not exist
]

# Retrieve and print heuristic values
for lat, lon in test_coordinates:
    heuristic = heuristic_retriever.get_heuristic_value(lat, lon)
    print(f"Heuristic value for ({lat}, {lon}): {heuristic}")


# Heuristic value for (5.25, 68.875): 0.21252335608005524
# Heuristic value for (6.75, 70.125): 0.13584813475608826
# Heuristic value for (7.25, 72.875): 0.13651037216186523
# No heuristic value found for (8.0, 73.0). Returning default value 0.5.
# Heuristic value for (8.0, 73.0): 0.5

# Heuristic value for (5.25, 68.875): 0.18759778141975403
# Heuristic value for (6.75, 70.125): 0.10977120697498322
# Heuristic value for (7.25, 72.875): 0.13537858426570892
# No heuristic value found for (8.0, 73.0). Returning default value 0.5.
# Heuristic value for (8.0, 73.0): 0.5