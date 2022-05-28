import tkinter as tk
import requests
import time

def getWeatherFromCity():
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=ee68c808a64391fa89a19dc2acc40a7e"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['main']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    output_info = condition



canvas = tk.Tk()
canvas.geometry("500x400")
canvas.title("Umbrella")

f = ("dm sans", 15 , "bold")
t = ("dm sans", 35, "bold")


textfield = tk.Entry(canvas, font = t)
textfield.pack (pady = 20)
textfield.focus()

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()