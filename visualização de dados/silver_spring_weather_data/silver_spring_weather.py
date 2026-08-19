from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('visualização de dados/silver_spring_weather_data/silver_spring_weather.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

prcps, dates = [], []
for row in reader:
    current_date = datetime.strptime(row[5], '%Y-%m-%d')
    prcp = row[8]
    prcps.append(prcp)
    dates.append(current_date)

print(prcps)

fig, ax = plt.subplots()
ax.plot(dates, prcps, color='blue')
ax.set_title("quantidades diarias de chuva", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("ml por dia", fontsize=16, labelpad=100)
plt.show()