import time
import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def constant_time(n):
    return 'hello world'

def linear_time(n):
    for i in range(n):
        pass

def quadratic_time(n):
    for i in range(n):
        for j in range(n):
            pass

def logarithmic_time(n):
    i = 1
    while i < n:
        i *= 2

def linearithmic_time(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 2

# Timing the functions
def time_function(func, n):
    start_time = time.time()
    func(n)
    return time.time() - start_time

# Set the range for n
n_values = np.arange(1, 101, 5)  # Values of n from 1 to 100, step 5

# Collect execution times for each function
constant_times = [time_function(constant_time, n) for n in n_values]
linear_times = [time_function(linear_time, n) for n in n_values]
quadratic_times = [time_function(quadratic_time, n) for n in n_values]
logarithmic_times = [time_function(logarithmic_time, n) for n in n_values]
linearithmic_times = [time_function(linearithmic_time, n) for n in n_values]

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(n_values, constant_times, label="O(1) Constant Time", color='blue', marker='o')
plt.plot(n_values, linear_times, label="O(n) Linear Time", color='green', marker='o')
plt.plot(n_values, quadratic_times, label="O(n^2) Quadratic Time", color='red', marker='o')
plt.plot(n_values, logarithmic_times, label="O(log n) Logarithmic Time", color='purple', marker='o')
plt.plot(n_values, linearithmic_times, label="O(n log n) Linearithmic Time", color='orange', marker='o')

# Adding labels and title
plt.xlabel("n (Input Size)")
plt.ylabel("Time (Seconds)")
plt.title("Time Complexity of Different Functions")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
