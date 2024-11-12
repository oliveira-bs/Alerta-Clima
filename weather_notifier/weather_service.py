import json
import os

import requests
from dotenv import load_dotenv

from config.settings import CITIES_FILE

load_dotenv()  # Carrega variáveis do .env
API_KEY = os.getenv("API_KEY")


def load_cities():
    """Função para carregar as cidades do arquivo JSON"""
    with open(CITIES_FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data["cities"]


def get_weather_data():
    """Função para fazer a consulta na API e obter os dados climaticos para \
        cada cidade
    """
    cities = load_cities()
    weather_data = []

    for city in cities:
        city_name = f"{city['name']},{city['state']}"
        url = f"""https://api.hgbrasil.com/weather?\
key={API_KEY}&city_name={city_name}"""

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # print(data)
            results = data.get("results", {})
            # Coletando os parâmetros de interesse
            city_weather = {
                "city": city["name"],
                "date": results["date"],
                "time": results["time"],
                "temp": results["temp"],
                "max": results.get("forecast", [{}])[0].get("max"),
                "min": results.get("forecast", [{}])[0].get("min"),
                "currently": results.get("currently"),
                "condition_slug": results.get("condition_slug"),
                "description": results.get("description"),
                "humidity": results.get("humidity"),
                "rain": results.get("rain"),
                "rain_probability": results.get("forecast", [{}])[0].get(
                    "rain_probability"),
                "wind_speedy": results.get("wind_speedy"),
                "wind_cardinal": results.get("wind_cardinal"),
                "cloudiness": results.get("cloudiness"),
                "sunrise": results.get("sunrise"),
                "sunset": results.get("sunset")
            }
            weather_data.append(city_weather)
        else:
            print(f"Erro ao obter dados para {city['name']}")

    return weather_data
