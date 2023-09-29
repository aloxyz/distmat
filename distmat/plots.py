import csv
import matplotlib.pyplot as plt
import numpy as np

# read data from csv
data = []
with open("output.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        data.append([float(val) for val in row])

# extract data
sizes = [run[0] for run in data]
means = [np.mean(runs) for runs in data]
std_devs = [np.std(runs) for runs in data]

# plot data
plt.errorbar(sizes, means, yerr=std_devs, fmt='o-', label='Execution Time')
plt.xlabel('Matrix Size (n)')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time vs. Matrix Size')
plt.grid()
plt.legend()
plt.savefig('test_dot_size_2_16_4.png')
plt.show()
