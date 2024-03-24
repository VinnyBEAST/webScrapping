# Importing necessary libraries
from bs4 import BeautifulSoup
import requests


# Function to scrape weather data
def scrape_weather_data(url):
    # Sending HTTP GET request
    response = requests.get(url)

    # Parsing HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting weather details
    temperature = soup.find('span', class_='CurrentConditions--tempValue--MHmYY').get_text()
    time = soup.find('span', class_='CurrentConditions--timestamp--1ybTk').get_text()
    weather_conditions = soup.find('div', class_='CurrentConditions--phraseValue--mZC_p').get_text()

    # Returning weather data
    return {
        'temperature': temperature,
        'time': time,
        'weather_conditions': weather_conditions
    }


# Function to execute main logic
def main():
    # URL for specific location
    url = 'https://weather.com/weather/today/l/aa0cfbbf27654104df53cb7b9f2ed626e6d7a550c2ab39433644ee8a1e6fe481'

    # Scraping weather data for the specified location URL
    weather_data = scrape_weather_data(url)

    # Printing weather information
    print("Weather Information:")
    print(f"Temperature: {weather_data['temperature']}")
    print(f"Time: {weather_data['time']}")
    print(f"Weather Conditions: {weather_data['weather_conditions']}")


# Calling the main function
main()
