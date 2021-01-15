# write a program to display line graph between person and score

import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_group = 4
aditya = (90, 55, 40, 65)
avinash = (85, 62, 54, 20)

# create plot
index = np.arange(n_group)
bar_width = 0.35
opacity = 0.8

rects1 = plt.plot(index, aditya, bar_width,
alpha = opacity,
color = 'b',
label = 'Aditya')

rects2 = plt.plot(index, avinash, bar_width,
alpha = opacity,
color = 'g',
label = 'Avinash')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
plt.legend()

plt.tight_layout()
plt.show()