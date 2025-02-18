import requests

def get_weather(api_key, lat, lon):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'imperial'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    api_key = "1e3ee0902e1726f4f56d9fa73556a91d"
    lat = 39.7137  # Latitude for Lancaster, Ohio
    lon = -82.5993  # Longitude for Lancaster, Ohio
    weather_data = get_weather(api_key, lat, lon)
    if weather_data:
        print(f"Temperature: {weather_data['main']['temp']}°F")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to fetch weather data")