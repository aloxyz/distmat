import csv
import matplotlib.pyplot as plt
import numpy as np

def serial_parallel_comparison(csv_name, func_name):
    # Read data from serial CSV file
    serial_data = []
    with open(f"test_results/serial/{csv_name}", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            serial_data.append([float(val) for val in row])

    # Read data from parallel CSV file
    parallel_data = []
    with open(f"test_results/parallel/{csv_name}", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            parallel_data.append([float(val) for val in row])

    # Extract serial data
    serial_sizes = [run[0] for run in serial_data]
    serial_means = [np.mean(runs) for runs in serial_data]
    serial_std_devs = [np.std(runs) for runs in serial_data]

    # Extract parallel data
    parallel_sizes = [run[0] for run in parallel_data]
    parallel_means = [np.mean(runs) for runs in parallel_data]
    parallel_std_devs = [np.std(runs) for runs in parallel_data]

    # Plot data
    plt.errorbar(serial_sizes, serial_means, yerr=serial_std_devs, fmt='o-', label='Serial Execution Time')
    plt.errorbar(parallel_sizes, parallel_means, yerr=parallel_std_devs, fmt='x-', label='Parallel Execution Time')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Execution Time (s)')
    plt.title(f'Serial vs. parallel execution time ({func_name})')
    plt.grid()
    plt.legend()
    plt.savefig(csv_name.replace("csv", "png"))
    plt.show()

def rank_serial_parallel_comparison(csv_name):
    # Read data from serial CSV file
    serial_data = []
    with open(f"test_results/serial/{csv_name}", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            serial_data.append([float(val) for val in row])

    # Read data from parallel CSV file
    parallel_data = []
    with open(f"test_results/parallel/{csv_name}", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            parallel_data.append([float(val) for val in row])

    # Extract serial data
    serial_sizes = [run[0] for run in serial_data]
    serial_means = [np.mean(runs) for runs in serial_data]
    serial_std_devs = [np.std(runs) for runs in serial_data]

    # Extract parallel data
    parallel_sizes = [run[0] for run in parallel_data]
    parallel_means = [np.mean(runs) for runs in parallel_data]
    parallel_std_devs = [np.std(runs) for runs in parallel_data]

    # Downsample the data (e.g., take every nth point)
    n = 10  # Adjust this value as needed
    serial_sizes = serial_sizes[::n]
    serial_means = serial_means[::n]
    serial_std_devs = serial_std_devs[::n]
    parallel_sizes = parallel_sizes[::n]
    parallel_means = parallel_means[::n]
    parallel_std_devs = parallel_std_devs[::n]

    # Plot data with transparency for points
    plt.errorbar(serial_sizes, serial_means, yerr=serial_std_devs, fmt='o-', label='Serial Execution Time')
    plt.errorbar(parallel_sizes, parallel_means, yerr=parallel_std_devs, fmt='x-', label='Parallel Execution Time')

    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Execution Time (s)')
    plt.title('Serial vs. parallel execution time (rank)')
    plt.grid()
    plt.legend()
    plt.savefig(csv_name.replace("csv", "png"))
    plt.show()


# Call the function with your CSV file name
serial_parallel_comparison("det_2_10_3.csv", "determinant")
serial_parallel_comparison("dot_2_30_5.csv", "dot product")
serial_parallel_comparison("inv_2_8_3.csv", "inverse")


rank_serial_parallel_comparison("rank_2_500_5.csv")

