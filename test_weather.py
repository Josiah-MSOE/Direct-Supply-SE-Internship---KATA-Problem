# Direct Supply Kata Problem 2  -  Weather API UNIT TESTS
# Josiah Mathews - MSOE Computer Science Sophomore

import unittest
from weather_api.weather import get_lat_lon, get_weather

class TestWeatherFunctions(unittest.TestCase):
    """
    Please use the simple, effective tests below for my Weather API calls. Make sure valid API Key is set please.
    """

    def test_get_lat_lon_valid_city(self):
        lat, lon = get_lat_lon("Milwaukee")
        self.assertIsNotNone(lat)
        self.assertIsNotNone(lon)

    def test_get_lat_lon_invalid_city(self):
        lat, lon = get_lat_lon("InvalidCityNameXYZ")
        self.assertIsNone(lat)
        self.assertIsNone(lon)

    def test_get_weather_valid_coords(self):
        # TEST coordinates for Milwaukee
        result = get_weather("43.0389", "-87.9065")
        self.assertIn("Milwaukee", result)

    def test_full_user_run(self):
        lat, lon = get_lat_lon("Kenosha")
        result = get_weather(lat, lon)
        self.assertIn("Kenosha", result)  # further table OUTPUT tests below

        lat, lon = get_lat_lon("Houston")
        result = get_weather(lat, lon)
        self.assertIn("Houston", result)  # further table OUTPUT tests below

    def test_get_weather_table_format(self):
        # Mock valid coordinates for Milwaukee
        result = get_weather("43.0389", "-87.9065")
        self.assertIn("Weather Detail", result)
        self.assertIn("Current Value", result)
        self.assertIn("Temperature", result)
        self.assertIn("Min. (LOW) Temperature (°F)", result)
        self.assertIn("Max (HIGH) Temperature (°F)", result)
        self.assertIn("Humidity", result)
        self.assertIn("Description", result)


if __name__ == "__main__":
    unittest.main() # run all tests above
