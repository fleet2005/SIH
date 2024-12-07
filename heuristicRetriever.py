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
            return 0.5  # Default value if the coordinate is not found


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
