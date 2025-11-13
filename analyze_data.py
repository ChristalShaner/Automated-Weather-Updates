import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("temperature_data.csv")

plt.bar(df["City"], df["Temperature"])
plt.title("Temperature in Different Cities")
plt.xlabel("City")
plt.ylabel("Temperature (Kelvin)")
plt.show()