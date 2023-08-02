import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=" + API_KEY

def get_weather(date):
    url = BASE_URL
    response = requests.get(url)
    data = response.json()
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['temp']

def get_wind_speed(date):
    url = BASE_URL
    response = requests.get(url)
    data = response.json()
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['wind']['speed']

def get_pressure(date):
    url = BASE_URL
    response = requests.get(url)
    data = response.json()
    for forecast in data['list']:
        if date in forecast['dt_txt']:
            return forecast['main']['pressure']

def main():
    while True:
        print("\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather(date)
            print(f"Temperature on {date}: {temperature}°C")

        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(date)
            print(f"Wind Speed on {date}: {wind_speed} m/s")

        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(date)
            print(f"Pressure on {date}: {pressure} hPa")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()