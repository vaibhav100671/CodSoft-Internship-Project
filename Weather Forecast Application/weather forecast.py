import tkinter as tk
from tkinter import messagebox
import requests

def clear_all():
    location_entry.delete(0, tk.END)
    result_label.config(text="")

def get_weather():
    location = location_entry.get()

    api_key = "4d31219aeb45689d281203f96fbc4ed2"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        result_label.config(text=f"Weather in {location}:\n"
                                 f"Temperature: {temperature}°C\n"
                                 f"Humidity: {humidity}%\n"
                                 f"Description: {description}",
                            font=('Courier New', 12), fg='blue', bg='white', width=40, height=40)
    else:
        messagebox.showerror("Error", "Weather data not found!")

root = tk.Tk()
root.title("Weather Forecast Application")

root.geometry("400x400")
root.resizable(0, 0)

location_label = tk.Label(root, text="Enter a city name or zip code:", font='Helvetica 16 bold', anchor="w")
location_label.pack(pady=10, padx=10, anchor="w")

location_entry = tk.Entry(root, width=40, font='Helvetica 14')
location_entry.pack(pady=10, padx=10, anchor="w")

fetch_button = tk.Button(root, text="Fetch Weather", command=get_weather, padx=6, pady=6, font='Helvetica 16 bold', bg='#0080ff', width=13)
fetch_button.pack(pady=18)

reset_button = tk.Button(root, text="Clear", padx=6, pady=6, font='Helvetica 16 bold', background="#ff7f00", command=clear_all, width=13)
reset_button.pack()

result_label = tk.Label(root, text="", wraplength=300)
result_label.pack(pady=18)

root.mainloop()
