# import requests
# from bs4 import BeautifulSoup

# def get_weather(city):
#     # URL for weather information
#     url = f"https://www.timeanddate.com/weather/usa/{city.lower().replace(' ', '-')}"
    
#     # Fetch the page content
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Extract temperature
#     temp_element = soup.find("div", class_="h2")
#     temperature = temp_element.text.strip() if temp_element else "N/A"
    
#     # Extract condition
#     condition_element = soup.find("p")
#     condition = condition_element.text.strip() if condition_element else "N/A"
    
#     return temperature, condition

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

