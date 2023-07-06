import matplotlib.pyplot as plt
import numpy as np
import csv
import math

from src.data.storage_manager import load_data

mongo = []
neo = []
queryn = 4

for i in range(25, 101, 25):
    single_data = load_data('single')
    parallel_data = load_data('parallel')


labels = ['25%', '50%', '75%', '100%']
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(x - width / 2, neo, width, label='Neo4j')
rects2 = ax.bar(x + width / 2, mongo, width, label='MongoDB')

# Add some text for labels, title and custom x-axis tick labels, etc.

ax.set_ylabel('Tempo (Millisecondi)')
ax.set_title('3 WHERE 2 JOIN')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()