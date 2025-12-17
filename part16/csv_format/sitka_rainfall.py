from matplotlib import pyplot as plt
import csv

from pathlib import Path
from datetime import datetime
path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

rainfalls, dates = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rain = float(row[5])
    except ValueError:
        print(f'We are missing info about this date: {current_date}')
    else:
        dates.append(current_date)
        rainfalls.append(rain)
    
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, color='blue')

ax.set_title('Rainfall in Sitka', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Precipitation Amount (in)', fontsize=16)

plt.show()