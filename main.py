import streamlit as st
import requests
import os

IMAGE_FILEPATH = "image.png"

api_key = os.getenv("NASA_API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
content = response.json()

title = content["title"]
description = content["explanation"]
image_url = content["url"]

image = requests.get(image_url)
with open(IMAGE_FILEPATH, "wb") as file:
    file.write(image.content)

st.title(title)
st.image(IMAGE_FILEPATH)
st.write(description)
