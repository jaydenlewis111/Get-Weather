import imp
import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()


def main():
    headers = {}

    api_key = os.getenv('api_key')

    site = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'


if __name__ == '__main__':
    main()
