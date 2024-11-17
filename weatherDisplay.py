import pygame
import requests
import os
from dotenv import load_dotenv

# Colors
WHITE = (255, 255, 255)
TEXT_COLOR = (200, 200, 200)
BACKGROUND_COLOR = (30, 30, 30)

# Load API Key
load_dotenv()
API_KEY = os.getenv("api_key")

# Function to fetch weather data
def get_weather_data(latitude, longitude):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": f"{data['main']['temp']}°C",
            "feels_like": f"{data['main']['feels_like']}°C",
            "humidity": f"{data['main']['humidity']}%",
            "wind_speed": f"{data['wind']['speed']} m/s",
            "description": data['weather'][0]['description'].capitalize().split()[0]
        }
    else:
        return {"error": "Unable to fetch weather data"}

# Function to display weather in the 4th quadrant
def weather(screen, latitude, longitude):
    # Fetch weather data
    weather_data = get_weather_data(latitude, longitude)

    # Set up font and positioning
    font = pygame.font.Font(None, 36)
    label_font = pygame.font.Font(None, 28)
    x_position = screen.get_width() * 3 // 4  # Start drawing in the 4th quadrant
    y_position = screen.get_height() * 3 // 4 -50  # Adjust Y position for quadrant

    # Draw a background box for better visibility
    box_width, box_height = 240, 180
    pygame.draw.rect(screen, BACKGROUND_COLOR, (x_position, y_position, box_width, box_height), border_radius=10)

    # Render weather data
    if "error" not in weather_data:
        weather_text = [
            f"Temperature: {weather_data['temperature']}",
            f"Feels Like: {weather_data['feels_like']}",
            f"Humidity: {weather_data['humidity']}",
            f"Wind Speed: {weather_data['wind_speed']}",
            f"Description: {weather_data['description'].split()[0]}"
        ]
    else:
        weather_text = [weather_data["error"]]

    # Display weather information
    for i, text in enumerate(weather_text):
        label = label_font.render(text, True, TEXT_COLOR)
        screen.blit(label, (x_position + 10, y_position + 20 + (i * 30)))  # Adjust line spacing

def weatherTwo(screen, latitude, longitude):
    # Fetch weather data
    weather_data = get_weather_data(latitude, longitude)

    # Set up font and positioning
    font = pygame.font.Font(None, 36)
    label_font = pygame.font.Font(None, 28)
    x_position = screen.get_width() * 3 // 4 -280 # Start drawing in the 4th quadrant
    y_position = screen.get_height() * 3 // 4 -50 # Adjust Y position for quadrant

    # Draw a background box for better visibility
    box_width, box_height = 240, 180
    pygame.draw.rect(screen, BACKGROUND_COLOR, (x_position, y_position, box_width, box_height), border_radius=10)

    # Render weather data
    if "error" not in weather_data:
        weather_text = [
            f"Temperature: {weather_data['temperature']}",
            f"Feels Like: {weather_data['feels_like']}",
            f"Humidity: {weather_data['humidity']}",
            f"Wind Speed: {weather_data['wind_speed']}",
            f"Description: {weather_data['description']}"
        ]
    else:
        weather_text = [weather_data["error"]]

    # Display weather information
    for i, text in enumerate(weather_text):
        label = label_font.render(text, True, TEXT_COLOR)
        screen.blit(label, (x_position + 10, y_position + 20 + (i * 30)))  # Adjust line spacing
