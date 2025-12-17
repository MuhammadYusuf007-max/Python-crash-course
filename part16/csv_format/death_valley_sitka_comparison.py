from pathlib import Path
import csv
from matplotlib import pyplot as plt
from datetime import datetime

path1 = Path('weather_data/sitka_weather_2021_full.csv')
path2 = Path('weather_data/death_valley_2021_full.csv')
lines1 = path1.read_text(encoding='utf-8').splitlines()
lines2 = path2.read_text(encoding='utf-8').splitlines()

reader1 = csv.reader(lines1)
reader2 = csv.reader(lines2)
header_row1 = next(reader1)
header_row2 = next(reader2)

dates, sitka, valley_temps = [], [], []
for row in reader2:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        temp = int(row[6])
    except ValueError:
        print(f'We are missing  valley temperature in this date{current_date}')
    else:
        valley_temps.append(temp)
        dates.append(current_date)
    
for row in reader1:
    try:
        temp = int(row[7])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f'We are missing this date tempurature{current_date}')
    else:
        sitka.append(temp)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, valley_temps, color='blue', alpha=0.5)
ax.plot(dates, sitka, color='red', alpha=0.5)
ax.fill_between(dates, valley_temps, sitka, color='green', alpha=0.1)

ax.set_title('Comparison between Death Valley and Sitka', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)

plt.show()
