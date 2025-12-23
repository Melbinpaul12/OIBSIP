import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    try:
        # ---- Geocoding ----
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo = requests.get(geo_url).json()

        if "results" not in geo or len(geo["results"]) == 0:
            messagebox.showerror("Error", "City not found")
            return

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        # ---- Weather ----
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current_weather=true"
        )
        data = requests.get(weather_url).json()
        weather = data["current_weather"]

        temp.set(f"{weather['temperature']} °C")
        wind.set(f"{weather['windspeed']} km/h")
        code.set(weather["weathercode"])

        city_label.config(text=city.title())

    except Exception:
        messagebox.showerror("Error", "Unable to fetch weather data")

# ---------------- Window ----------------
root = tk.Tk()
root.title("Weather App")
root.geometry("450x420")
root.configure(bg="#eef2f5")
root.resizable(False, False)

# ---------------- Card ----------------
card = tk.Frame(root, bg="white")
card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=360)

# ---------------- Title ----------------
tk.Label(
    card,
    text="Weather Dashboard",
    bg="white",
    font=("Segoe UI", 18, "bold"),
    fg="#333"
).pack(pady=15)

# ---------------- Search ----------------
search_frame = tk.Frame(card, bg="white")
search_frame.pack(pady=10)

city_entry = tk.Entry(
    search_frame,
    font=("Segoe UI", 12),
    width=20,
    justify="center"
)
city_entry.pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Search",
    command=get_weather,
    bg="#1976d2",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    width=10
).pack(side="left")

# ---------------- City ----------------
city_label = tk.Label(
    card,
    text="--",
    bg="white",
    font=("Segoe UI", 16, "bold")
)
city_label.pack(pady=10)

# ---------------- Weather Info ----------------
temp = tk.StringVar(value="--")
wind = tk.StringVar(value="--")
code = tk.StringVar(value="--")

info_frame = tk.Frame(card, bg="white")
info_frame.pack(pady=10)

tk.Label(info_frame, text="🌡 Temperature", bg="white").grid(row=0, column=0, padx=20, pady=5)
tk.Label(info_frame, textvariable=temp, bg="white", font=("Segoe UI", 12, "bold")).grid(row=0, column=1)

tk.Label(info_frame, text="💨 Wind Speed", bg="white").grid(row=1, column=0, padx=20, pady=5)
tk.Label(info_frame, textvariable=wind, bg="white", font=("Segoe UI", 12, "bold")).grid(row=1, column=1)

tk.Label(info_frame, text="🔢 Weather Code", bg="white").grid(row=2, column=0, padx=20, pady=5)
tk.Label(info_frame, textvariable=code, bg="white", font=("Segoe UI", 12, "bold")).grid(row=2, column=1)

# ---------------- Footer ----------------
tk.Label(
    card,
    text="Powered by Open-Meteo API",
    bg="white",
    fg="#777",
    font=("Segoe UI", 9)
).pack(side="bottom", pady=10)

root.mainloop()
