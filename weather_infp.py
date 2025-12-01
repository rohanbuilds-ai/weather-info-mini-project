import requests  # This library helps us talk to websites and APIs

def get_weather():
    print("🌤️ Welcome to the Weather Info App!")
    print("----------------------------------")
    # 1️⃣ Get city name from the user
    city = input("Enter city name: ")

    # 2️⃣ Your unique API key (you can get one for free from OpenWeatherMap)
    api_key = "7e8cdda87ef482b04bdcd9594bbd3d80"  
    
    # 3️⃣ Base URL for the OpenWeatherMap API
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # 4️⃣ Complete URL with city name, API key, and units
    url = f"{base_url}?q={city}&appid={api_key}&units=metric"

    # 5️⃣ Send the request to the API
    response = requests.get(url)

    # 6️⃣ Convert the response to JSON format (like a Python dictionary)
    data = response.json()

    # 7️⃣ Check if the response was successful (code 200 = OK)
    if data["cod"] == 200:
        # Extract weather data from the JSON
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        # 8️⃣ Display the weather information
        print("----------------------------------")
        print(f"Weather Information for {city.title()}")
        print("----------------------------------")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {weather.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print("----------------------------------")

    else:
        # 9️⃣ If the city name is invalid or API key is wrong
        print("⚠️ City not found or invalid API key! Please try again.")

# 🔟 Run the program
if __name__ == "__main__":
    get_weather()