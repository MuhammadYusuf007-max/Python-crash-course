from plotly import express as px
from die import Die

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# Analize the results
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results
title = "Results of Rolling One D6 1,000 Times"
labels = {'x':'Result', 'y': 'Frequeny of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
    
print(frequencies)