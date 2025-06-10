import streamlit as st
import random

games = [
    "Teardown",
    "Asphalt Legends Unite",
    "Minecraft",
    "Forza Horizon 5",
    "Rocket League",
    "Among Us",
    "PC Building Simulator"
]

st.set_page_config(page_title="Game Chooser 🎮", page_icon="🎲")
st.title("🎮 What Should I Play?")
st.write("Click the button below to get a random game suggestion.")

if st.button("🎲 Spin the Wheel!"):
    choice = random.choice(games)
    st.success(f"🕹️ You should play: **{choice}**")

