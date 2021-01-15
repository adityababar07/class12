# write a program to display a pie chart

import matplotlib.pyplot as plt
c = (23, 16, 43, 24, 53)
zones = ('East', 'West', 'North', 'South', 'Central')
plt.axis("equal")
plt.pie(c,labels=zones, explode=[0,0,1,0,0], autopct="%1.2f%%")
plt.show()