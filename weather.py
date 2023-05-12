import requests
import json
from datetime import datetime
import pandas as pd

def main():

    API_key = 'demo'
    lat = '34.0522'
    lon = '118.2437'
    url = f'https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API_key}'

    response = requests.get(url)

if __name__ == '__main__':
    main()
