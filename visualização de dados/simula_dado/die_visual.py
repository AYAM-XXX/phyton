from dado import Die
# import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

die_1 = Die()
die_2 = Die(8)
die_3 = Die(8)
results= []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(1, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
fig, ax = plt.subplots()

ax.bar(poss_results, frequencies, width=1, edgecolor="white", linewidth=0.7)
plt.show()
# title = "resultados da rolagem dos dados"
# labels = {'x': 'resultados', 'y': 'frequencia de resultados'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.update_layout(xaxis_dtick=1)
# fig.write_html('dice_visual_d6d10.html')
# fig.show()