import random
import math

# Generate 1000 random data points
data = []

for i in range(1000):
    data.append(random.randint(1, 1000))

# ---------------- Mean ----------------
mean = sum(data) / len(data)

# ---------------- Median ----------------
data.sort()
n = len(data)

if n % 2 == 0:
    median = (data[n // 2 - 1] + data[n // 2]) / 2
else:
    median = data[n // 2]

# ---------------- Standard Deviation ----------------
variance_sum = 0

for x in data:
    variance_sum += (x - mean) ** 2

variance = variance_sum / n

standard_deviation = math.sqrt(variance)

# ---------------- Output ----------------
print("Total Data Points =", n)

print("\nMean =", mean)

print("Median =", median)

print("Standard Deviation =", standard_deviation)