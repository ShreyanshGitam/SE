#Weather Prediction Program:
import math

temp = [28, 25, 30, 20, 15]
hum = [65, 70, 60, 80, 20]
wind = [20, 15, 20, 3, 25]

for i in range(len(temp)):
    print(f"Tect Case No.{i+1}:\nTemperature(Celsius):{temp[i]}\nHumidity(%):{hum[i]}\nWind Speed(Kmph):{wind[i]}")
    weather_Pred = (0.5*temp[i]**2) - (0.2*hum[i]) + (0.1*wind[i]) - 15
    print(f"WP: {weather_Pred}")
    weather_Pred = math.ceil(weather_Pred)
    print("Prediction: ", end="")
    if weather_Pred > 300.00:
        print("Weather is Sunny.")
    elif weather_Pred in range(200, 300):
        print("Weather is Cloudy.")
    elif weather_Pred in range(100, 200):
        print("Weather is Rainy.")
    elif weather_Pred in range(0, 100):
        print("Weather is Stormy.")
    else:
        print("Error")
    print("\n")
