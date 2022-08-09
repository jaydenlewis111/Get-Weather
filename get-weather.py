import requests
from dotenv import load_dotenv
import os

def configure() -> None:
    load_dotenv()

def get_city() -> str:
    city = input("Which city's weather would you like to know? ")
    return city

def get_weather(base_url: str, city: str, api_key: str) -> None:
    request_url = f"{base_url}?q={city}&appid={api_key}&units=metric" 

    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        print(f"Weather: {weather}")
        
        temperature = data["main"]["temp"]
        print(f"Temperature: {temperature} C")

    else:
        print(f"An error occurred {response.status_code}")

def main():
    configure()

    api_key = os.getenv('api_key')

    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    city = get_city()

    get_weather(base_url, city, api_key)


if __name__ == '__main__':
    main()
