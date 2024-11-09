import requests
from bs4 import BeautifulSoup

def get_weather(country, city):
    """
    Fetches weather details (temperature and condition) for a specified country and city.
    
    Args:
        country (str): The name of the country (e.g., 'israel').
        city (str): The name of the city (e.g., 'tel-aviv').
    
    Returns:
        tuple: A tuple containing temperature and condition (e.g., '25°C', 'Sunny').
    """
    # Format the URL for the country and city
    url = f"https://www.timeanddate.com/weather/{country.lower().replace(' ', '-')}/{city.lower().replace(' ', '-')}"
    
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract temperature
        temp_element = soup.find("div", class_="h2")
        temperature = temp_element.text.strip() if temp_element else "Temperature not found"
        
        # Extract condition
        condition_element = soup.find("p", class_="my-city__weather")
        condition = condition_element.text.strip() if condition_element else "Condition not found"
        
        return temperature, condition
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"An error occurred: {e}")
        return "N/A", "N/A"


def get_weather_from_metaweather(city):
    """
    Fetches weather details from MetaWeather API for a given city.
    
    Args:
        city (str): The name of the city (e.g., 'tel aviv').
    
    Returns:
        tuple: A tuple containing temperature, condition, and humidity.
    """
    try:
        # Step 1: Get the location ID (woeid) for the city
        location_url = f"https://www.metaweather.com/api/location/search/?query={city}"
        location_response = requests.get(location_url)
        location_response.raise_for_status()
        location_data = location_response.json()
        
        if not location_data:
            return "N/A", "N/A"
        
        woeid = location_data[0]["woeid"]
        
        # Step 2: Get the weather data using the location ID
        weather_url = f"https://www.metaweather.com/api/location/{woeid}/"
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        # Extract weather details
        today_weather = weather_data["consolidated_weather"][0]
        temperature = f"{today_weather['the_temp']:.1f}°C"
        condition = today_weather["weather_state_name"]
        
        return temperature, condition
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with MetaWeather API: {e}")
        return "N/A", "N/A"
