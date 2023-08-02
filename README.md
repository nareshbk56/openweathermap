# openweathermap

The provided Python code is a sample program that interacts with the OpenWeatherMap API to retrieve weather data for London. It allows the user to select from four options: get weather, get wind speed, get pressure, or exit the program. Depending on the chosen option, the program prompts the user for a date (in the format YYYY-MM-DD) and fetches the relevant weather data from the API.

The functions get_weather, get_wind_speed, and get_pressure make API requests to obtain the required data based on the user's input date. The data is extracted from the API response, and the program prints the temperature, wind speed, or pressure accordingly.

To run the code, you need to have Python installed on your system. Save the code in a file with a .py extension (e.g., OpenWeatherMap-London.py) and execute it using the command python OpenWeatherMap-London.py. The program will then prompt you for input and provide the requested weather data for London.

Remember to install the requests library using pip install requests before running the code, as it is used to make HTTP requests to the OpenWeatherMap API.
