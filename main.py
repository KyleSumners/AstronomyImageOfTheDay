import streamlit as st
import requests
import os

api_key = os.getenv("NASA_API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

request = requests.get(url)
print(request)

content = request.json()

