## Automated Weather Data ETL & Visualization

This project demonstrates a simple data engineering workflow inspired by Uma Rajagopalan. It extracts, transforms, and loads weather data from the OpenWeatherMap API, automates storage in a CSV file, and visualizes temperature trends across multiple cities.

_Features_

Fetch hourly temperature data for multiple cities using Python

Store and append data in a CSV file for easy analysis

Visualize temperature trends using Matplotlib

Automate data collection using task scheduling

_Purpose_

This project is a beginner-friendly introduction to ETL pipelines, automation, and data visualization. It’s ideal for anyone learning data engineering or building a portfolio.

_Getting Started_

Clone this repository

Install dependencies:

pip install requests pandas matplotlib


_Get a free API key from OpenWeatherMap_
Link here! https://openweathermap.org

Update fetch_data.py with your API key and desired cities

_Run the scripts:_

python fetch_data.py
python analyze_data.py
