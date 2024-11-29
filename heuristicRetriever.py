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
        float: Heuristic value for the coordinate, or None if not found.
    """
    heuristics = load_heuristics(filename)
    
    if heuristics is None:
        print("Heuristics data is unavailable.")
        return None
    
    # Check if the coordinate exists in the heuristics dictionary
    coordinate = (longitude, latitude)  # Keys are stored as (longitude, latitude)
    if coordinate in heuristics:
        print(f"Heuristic value for ({latitude}, {longitude}): {heuristics[coordinate]}")
        return heuristics[coordinate]
    else:
        print(f"No heuristic value found for ({latitude}, {longitude}).")
        return None

def main():
    """
    Main function to test the retrieval of heuristic values.
    """
    print("Welcome to Heuristic Value Retriever!")
    
    # Input coordinates for testing
    try:
        latitude = float(input("Enter latitude: "))
        longitude = float(input("Enter longitude: "))
    except ValueError:
        print("Invalid input! Please enter numeric values for latitude and longitude.")
        return

    # Retrieve and display the heuristic value
    heuristic_value = get_heuristic_value(latitude, longitude)
    if heuristic_value is not None:
        print(f"Retrieved Heuristic Value: {heuristic_value}")
    else:
        print("Could not retrieve heuristic value.")

if __name__ == "__main__":
    main()
