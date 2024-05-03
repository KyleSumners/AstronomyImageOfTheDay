import streamlit as st
import requests
import os

api_key = os.getenv("NASA_API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)

content = request.json()
title = content["title"]
description = content["explanation"]

image_url = content["url"]
image = requests.get(image_url)
with open("image.png", "wb") as file:
    file.write(image.content)

st.title(title)
st.image("image.png")
st.write(description)
