import requests
import json


def fetch_weather_data():
    """
    Fetch the maximum temperature forecast for Tokyo using the Open-Meteo API.

    Returns:
        dict: A dictionary containing the date and the maximum temperature.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 35.6895,
        "longitude": 139.6917,
        "daily": "temperature_2m_max",
        "timezone": "Asia/Tokyo",
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if "daily" in data and "temperature_2m_max" in data["daily"]:
            date = data["daily"]["time"][0]
            max_temp = data["daily"]["temperature_2m_max"][0]
            return {"date": date, "temperature_2m_max": max_temp}

        raise ValueError("Required data not found in API response.")
    except requests.RequestException as e:
        print(f"An error occurred while fetching weather data: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error extracting weather data: {e}")
        return None
   

def save_to_json(data, filename):
    """
    Save the extracted weather data to a JSON file.

    Args:
        data (dict): The data to be saved.
        filename (str): The name of the JSON file.
    """
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"An error occurred while saving the data: {e}")


if __name__ == "__main__":
    # Fetch the weather data
    weather_data = fetch_weather_data()

    # Save the data to a JSON file
    save_to_json(weather_data, "tokyo_weather.json")

    print("Data successfully saved to tokyo_weather.json")
