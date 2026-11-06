import requests

# Free public API key or placeholder. You can swap this with your own OpenWeatherMap key.
API_KEY = "your_openweathermap_api_key_here"

def get_weather_data(city_name):
    # Using OpenWeatherMap Current Weather Data endpoint
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # Metric for Celsius
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        
        # If user hasn't put a valid API key yet, handle gracefully with a mock demonstration fallback
        if response.status_code == 401:
            print("\n[Notice]: Invalid or missing API Key. Providing a simulated response for testing!")
            return get_mock_weather(city_name)
            
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.RequestException as e:
        print(f"Network error or invalid city: {e}")
        return None

def get_mock_weather(city_name):
    # Mock fallback so the code structure executes cleanly even before plugging an API key
    return {
        "name": city_name.capitalize(),
        "sys": {"country": "IN"},
        "main": {
            "temp": 28.5,
            "feels_like": 31.0,
            "humidity": 65,
            "pressure": 1012
        },
        "weather": [{"description": "scattered clouds"}],
        "wind": {"speed": 3.6}
    }

def display_weather(data):
    if not data:
        return
    
    city = data.get("name")
    country = data.get("sys", {}).get("country", "")
    main_info = data.get("main", {})
    weather_desc = data.get("weather", [{}])[0].get("description", "N/A")
    wind_info = data.get("wind", {})
    
    temp = main_info.get("temp")
    feels_like = main_info.get("feels_like")
    humidity = main_info.get("humidity")
    pressure = main_info.get("pressure")
    wind_speed = wind_info.get("speed")

    print("\n" + "="*40)
    print(f"  WEATHER REPORT FOR: {city}, {country}")
    print("="*40)
    print(f" • Condition   : {weather_desc.capitalize()}")
    print(f" • Temperature : {temp}°C (Feels like: {feels_like}°C)")
    print(f" • Humidity    : {humidity}%")
    print(f" • Pressure    : {pressure} hPa")
    print(f" • Wind Speed  : {wind_speed} m/s")
    print("="*40)

def main():
    print("\n--- Project 05: Weather App with Live OpenWeather API ---")
    if API_KEY == "your_openweathermap_api_key_here":
        print("Tip: Replace `API_KEY` in the script with a free key from openweathermap.org for live data.")
        print("     (If left as-is, it will gracefully run a simulated demo output).")
        
    while True:
        print("\n1. Check City Weather")
        print("2. Exit")
        
        choice = input("Choose an option (1-2): ").strip()
        
        if choice == '1':
            city = input("Enter city name (e.g., Mumbai, London, Tokyo): ").strip()
            if city:
                print(f"Fetching weather for {city}...")
                data = get_weather_data(city)
                display_weather(data)
            else:
                print("City name cannot be empty.")
        elif choice == '2':
            print("Exiting Weather App. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1 or 2.")

if __name__ == "__main__":
    main()
