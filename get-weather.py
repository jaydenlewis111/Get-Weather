import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def get_city():
    city = input("Which city's weather would you like to know? ")
    return city

def main():
    configure()

    api_key = os.getenv('api_key')

    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    city = get_city()

    request_url = f"{base_url}?q={city}&appid={api_key}" 

    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        weather = data["weather"][0]["description"]
        print(f"weather: {weather}")
        temperature = round(data["main"]["temp"] - 273.15, 2)
        print(f"temperature: {temperature} C")
    else:
        print(f"An error occurred {response.status_code}")


if __name__ == '__main__':
    main()
