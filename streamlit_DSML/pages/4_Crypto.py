
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime

st.title("📡 Live Cryptocurrency Prices")
st.write("Live Bitcoin and Ethereum prices from CoinGecko.")

COINS = ["bitcoin", "ethereum"]
URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum&vs_currencies=usd"
)

HEADERS = {
    "User-Agent": "msudenver-dataviz-class/1.0",
    "Accept": "application/json"
}

@st.cache_data(ttl=300, show_spinner=False)
def fetch_prices():
    response = requests.get(URL, headers=HEADERS, timeout=10)
    response.raise_for_status()
    data = response.json()

    return pd.DataFrame([
        {"coin": coin, "price": data[coin]["usd"]}
        for coin in COINS
    ])

st.subheader("Refresh Settings")
refresh_sec = st.slider("Refresh every (seconds)", 10, 120, 30)
auto_refresh = st.toggle("Enable auto-refresh", value=False)

if st.button("Refresh now"):
    fetch_prices.clear()
    st.rerun()

@st.fragment(run_every=refresh_sec if auto_refresh else None)
def show_crypto():
    try:
        df = fetch_prices()
        st.success("Live CoinGecko data loaded")
    except (requests.RequestException, KeyError, ValueError) as e:
        st.warning(f"API unavailable: {e}. Showing demo data.")
        df = pd.DataFrame([
            {"coin": "bitcoin", "price": 68000},
            {"coin": "ethereum", "price": 3500}
        ])

    col1, col2 = st.columns(2)

    for col, coin in zip([col1, col2], COINS):
        price = df.loc[df["coin"] == coin, "price"].iloc[0]
        col.metric(coin.title(), f"${price:,.2f}")

    st.dataframe(df, use_container_width=True)

    fig = px.bar(
        df,
        x="coin",
        y="price",
        title="Current Cryptocurrency Prices (USD)",
        labels={"price": "Price (USD)", "coin": "Coin"}
    )

    st.plotly_chart(fig, use_container_width=True)
    st.caption(f"Page updated: {datetime.now():%H:%M:%S}")

show_crypto()
