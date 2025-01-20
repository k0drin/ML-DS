import xml.etree.ElementTree as ET
import csv


def parse_weather_xml(xml_file):
    """
    Parse weather data from an XML file.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        list of dict: A list of dictionaries with parsed weather data.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    weather_data = []
    for day in root.findall('day'):
        date = day.find('date').text
        temperature = float(day.find('temperature').text)
        humidity = float(day.find('humidity').text)
        precipitation = float(day.find('precipitation').text)

        weather_data.append({
            "date": date,
            "temperature": temperature,
            "humidity": humidity,
            "precipitation": precipitation
        })
    
    return weather_data


def save_to_csv(data, filename="parsed_weather_data.csv"):
    """
    Save parsed weather data to a CSV file.

    Args:
        data (list of dict): Parsed weather data.
        filename (str): Name of the CSV file.
    """
    fieldnames = [key.capitalize() for key in data[0].keys()] if data else []
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            row_capitalized = {key.capitalize(): value for key, value in row.items()}
            writer.writerow(row_capitalized)


if __name__ == "__main__":
    # Parse the XML file
    weather_data = parse_weather_xml("weather_data.xml")

    # Save the parsed data to a CSV file
    save_to_csv(weather_data)
    print("Data has been successfully parsed and saved to parsed_weather_data.csv.")
