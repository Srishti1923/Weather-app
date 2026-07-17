import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

st.set_page_config(page_title="Weather App", page_icon="🌧️")

st.title("Weather App ☁️", )

st.write("Enter a city name and click on the button to get the current weather data.")

city =st.text_input("Enter city name")

API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"


if st.button("Fetch Weather Data"):
    response = requests.get(API_URL)

    if(response.status_code == 200):
        st.success("Weather data fetched successfully!")
        data = response.json()

        #fetch the weather data in the variables
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather = data["weather"][0]["main"]

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        col1.metric(label="Temperature", value=f"🌡️{temperature}°C")
        col2.metric(label="Humidity", value=f"💧{humidity}%")
        col3.metric(label="Wind Speed", value=f"🍃{wind_speed}m/s")
        col4.metric(label="Weather", value=f"⛅{weather}")
    else:
        st.error("Invalid city name.")