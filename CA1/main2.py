import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

raw_data = [[25, 3, 8.2], [30, 5, 7.9], [35, 10, 9.1], [40, 12, 8.5], [45, 15, 9.3]]
print("2-1")
data = np.array(raw_data).reshape(5, 3)
print(data)

print("2-2")
avg_rating = np.mean(data[:, 2])
print("Average Performance Rating:", avg_rating)

print("2-3")

salaries = np.array([50000.0, 60000.0, 80000.0, 85000.0, 95000.0])

high_performers = data[:, 2] >= 8

salaries[high_performers] *= 1.10
print("Updated Salaries", salaries)
