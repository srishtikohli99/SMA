# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 00:10:58 2019

@author: srishti
"""

import matplotlib.pyplot as plt




labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 100, 45, 10]
#explode=[0,0,0,0]
explode = [0, 0.1, 0, 0]  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

