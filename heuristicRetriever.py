import pickle

class HeuristicRetriever:
    def __init__(self, filename="heuristics_data.pkl"):
        self.filename = filename
        self.heuristics = self.load_heuristics()

    def load_heuristics(self):
        """
        Load the heuristics and wind deviation dictionaries from a pickle file.
        
        Args:
            filename (str): Name of the pickle file.
        
        Returns:
            dict: The heuristics dictionary or None if loading fails.
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

# Usage
heuristic_retriever = HeuristicRetriever()  # Load heuristics once during initialization
 