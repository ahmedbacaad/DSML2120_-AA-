
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime

st.title("🌤️ Denver Live Weather Dashboard")
st.write("Temperature over time using the Open-Meteo API.")

LAT = 39.7392
LON = -104.9903

URL = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={LAT}&longitude={LON}"
    "&current=temperature_2m,wind_speed_10m"
    "&temperature_unit=fahrenheit"
    "&timezone=America%2FDenver"
)

@st.cache_data(ttl=600, show_spinner=False)
def get_weather():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    current = response.json()["current"]

    return {
        "time": pd.to_datetime(current["time"]),
        "temperature": current["temperature_2m"],
        "wind": current["wind_speed_10m"]
    }

st.subheader("Refresh Settings")
refresh_sec = st.slider("Refresh every (seconds)", 10, 120, 60)
auto_refresh = st.toggle("Enable auto-refresh", value=False)

if "weather_history" not in st.session_state:
    st.session_state.weather_history = []

if st.button("Refresh weather now"):
    get_weather.clear()
    st.rerun()

@st.fragment(run_every=refresh_sec if auto_refresh else None)
def show_weather():
    try:
        weather = get_weather()
        st.success("Open-Meteo weather data loaded")

        history = st.session_state.weather_history

        # Avoid duplicate readings with the same timestamp
        if not history or history[-1]["time"] != weather["time"]:
            history.append(weather)

        # Keep only the most recent 30 readings
        st.session_state.weather_history = history[-30:]

        col1, col2 = st.columns(2)
        col1.metric(
            "Denver Temperature",
            f"{weather['temperature']:.1f} °F"
        )
        col2.metric(
            "Wind Speed",
            f"{weather['wind']:.1f} km/h"
        )

        history_df = pd.DataFrame(st.session_state.weather_history)

        fig = px.line(
            history_df,
            x="time",
            y="temperature",
            markers=True,
            title="Denver Temperature Over Time",
            labels={
                "time": "Time",
                "temperature": "Temperature (°F)"
            }
        )

        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(history_df, use_container_width=True)

        st.caption(f"Page updated: {datetime.now():%H:%M:%S}")

    except (requests.RequestException, KeyError, ValueError) as e:
        st.error(f"Could not load weather data: {e}")

show_weather()

