# Direct-Supply-SE-Internship---KATA-Problem
A Python application for my Direct Supply Take Home Kata problem. This script fetches real-time weather data for a given city using the OpenWeatherMap API and displays temperature, humidity, and conditions in a clean format. 

# Weather Fetcher (Python)

## Description
A Python script that fetches current weather data for a given city using the OpenWeatherMap API and displays it in a clean, tabular format.

## Features
- Fetch temperature, humidity, and other weather conditions for Cities requested.
- Displays data in a formatted table using Tabulate.

## Setup
1. Either Clone the repository or download weather-API and install proper libraries needed.
2. Create and activate a virtual environment (this was tricky for me make sure the Virtual Environment is activated, then run python script):
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

## Running the Project
Navigate to your folder containing `weather.py` and run:
```bash
python weather.py
```

### Important for CMD Users (I ran into this issue as well)
If you activated `.venv` inside `Scripts`, navigate back to the project root before running:
```bash
cd ..\..
cd weather_api
python weather.py
```

## Sample Output
```
Enter City (or "DONE" to exit Weather Program): Kenosha
+-----------------------------+-----------------+
| Weather Detail              | Current Value   |
+=============================+=================+
| City                        | Kenosha         |
+-----------------------------+-----------------+
| Condition                   | Mist            |
+-----------------------------+-----------------+
| Temperature (°F)            | 45.68          |
+-----------------------------+-----------------+
| Min. (LOW) Temperature (°F) | 44.33          |
+-----------------------------+-----------------+
| Max (HIGH) Temperature (°F) | 46.81          |
+-----------------------------+-----------------+
| Humidity (%)                | 92             |
+-----------------------------+-----------------+
| Description                 | Light rain     |
+-----------------------------+-----------------+
```

## KEY Notes
- Ensure API_KEY is set in `weather.py`.
- I tested my script on Python 3.11 in a virtual environment (.venv).

## Potential Future Enhancements
- Support multiple cities in one table?
- Add charts using matplotlib for Temperature graphs?
- Add some sort of WEB Interface?

## Development Notes
Focused on API integration, error handling, and clean structure. Project evolved through refinements like improving error handling and adding tabular table output.
