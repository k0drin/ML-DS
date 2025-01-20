import json


def load_json(filename):
    """
    Load JSON data from a file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: The loaded JSON data.
    """

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None


def analyze_daily_weather(day, temp_threshold=30, wind_threshold=15, humidity_threshold=70):
    """
    Analyze weather data for a single day.

    Args:
        day (dict): The weather data for the day.
        temp_threshold (float): The temperature threshold to determine a hot day.
        wind_threshold (float): The wind speed threshold to determine a windy day.
        humidity_threshold (float): The humidity threshold to determine uncomfortable weather.

    Returns:
        dict: A dictionary with analysis results for the day.
    """
    date = day['date']
    max_temp = day['max_temperature']
    min_temp = day['min_temperature']
    precipitation = day.get('precipitation', 0.0)
    wind_speed = day['wind_speed']
    humidity = day['humidity']
    description = day['weather_description']

    is_hot_day = max_temp > temp_threshold
    temp_swing = max_temp - min_temp
    has_temp_swing = temp_swing > 10
    is_windy_day = wind_speed > wind_threshold
    is_uncomfortable = humidity > humidity_threshold
    is_rainy_day = precipitation > 0

    return {
        "date": date,
        "description": description,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "hot_day": is_hot_day,
        "has_temp_swing": has_temp_swing,
        "wind_speed": wind_speed,
        "windy_day": is_windy_day,
        "humidity": is_uncomfortable,
        "rainy_day": is_rainy_day,
        "precipitation": precipitation,
    }


def generate_daily_report(analysis):
    """
    Generate a detailed report based on the analysis results for a single day.

    Args:
        analysis (dict): The analysis results for the day.

    Returns:
        str: A detailed report as a string.
    """
    report = [
        f"Date: {analysis['date']}",
        f"Weather: {analysis['description']}",
        f"Temperature: Max {analysis['max_temp']}°C, Min {analysis['min_temp']}°C"
    ]

    if analysis['hot_day']:
        report.append("It was a hot day.")
    if analysis['windy_day']:
        report.append("It was a windy day.")
    if analysis['humidity']:
        report.append("The humidity made the day uncomfortable.")
    if analysis['rainy_day']:
        report.append(f"It was a rainy day with {analysis['precipitation']} mm of precipitation.")
    else:
        report.append("There was no precipitation.")

    return "\n".join(report)


def summarize_weather_analysis(analyses):
    """
    Summarize the weather analysis over multiple days.

    Args:
        analyses (list of dict): A list of daily analysis results.

    Returns:
        str: A summary report as a string.
    """
    hottest_day = max(analyses, key=lambda x: x['max_temp'])
    windiest_day = max(analyses, key=lambda x: x['wind_speed'])
    most_humid_day = max(analyses, key=lambda x: x['humidity'])
    rainiest_day = max(analyses, key=lambda x: x['precipitation'])

    summary = [
        f"Hottest day: {hottest_day['date']} with a maximum temperature of {hottest_day['max_temp']}°C",
        f"Windiest day: {windiest_day['date']} with wind speeds of {windiest_day['wind_speed']} km/h",
        f"Most humid day: {most_humid_day['date']} with a humidity level of {most_humid_day['humidity']}%",
        f"Rainiest day: {rainiest_day['date']} with {rainiest_day['precipitation']} mm of precipitation"
    ]
    
    return "\n".join(summary)


if __name__ == "__main__":
    # Load the JSON data
    weather_data = load_json("tokyo_weather_complex.json")

    # Analyze the weather data for each day
    analyses = [analyze_daily_weather(day) for day in weather_data['daily']]

    # Generate and print daily reports
    for analysis in analyses:
        report = generate_daily_report(analysis)
        print(report)

    # Generate and print a summary report
    summary_report = summarize_weather_analysis(analyses)
    print(summary_report)
