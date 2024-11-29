import pickle

def load_heuristics(filename="heuristics_data.pkl"):
    """
    Load the heuristics and wind deviation dictionaries from a pickle file.
    
    Args:
        filename (str): Name of the pickle file.
    
    Returns:
        dict: The heuristics dictionary.
    """
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            return data["heuristics"]
    except FileNotFoundError:
        print("No saved heuristics data found. Please ensure the file exists.")
        return None

def get_heuristic_value(latitude, longitude, filename="heuristics_data.pkl"):
    """
    Retrieve the heuristic value for a given latitude and longitude.
    
    Args:
        latitude (float): Latitude of the coordinate.
        longitude (float): Longitude of the coordinate.
        filename (str): Name of the pickle file to load heuristics data.
    
    Returns:
        float: Heuristic value for the coordinate. Returns 0.5 if the value is not found.
    """
    heuristics = load_heuristics(filename)
    
    if heuristics is None:
        print("Heuristics data is unavailable.")
        return 0.5  # Default value if heuristics data is not loaded

    # Check if the coordinate exists in the heuristics dictionary
    coordinate = (longitude, latitude)  # Keys are stored as (longitude, latitude)
    if coordinate in heuristics:
        return heuristics[coordinate]
    else:
        print(f"No heuristic value found for ({latitude}, {longitude}). Returning default value 0.5.")
        return 0.5  # Default value if the coordinate is not found
