import numpy as np
import matplotlib.pyplot as plt

f = open("data.txt", 'r')
data = []
for line in f:
    s = [x for x in line.split(',')]
    if s[0] == "GCAG":
        data.append([int(s[1]), float(s[2])])

print(data)
temp_by_year = np.transpose(data)
year = temp_by_year[0]
temperature = temp_by_year[1]
# print(temp_by_year)

plt.plot(year, temperature, color='blue')

z = temperature
x = [1]
deltaT = 0.1
gamma = 5
name = "ΔT = " + str(deltaT) + ", γ = " + str(gamma)
plt.title(name)

iterations = len(z)-1
for n in range(0, iterations):
    current = (1 - deltaT * gamma) * x[n] + deltaT * gamma * z[n + 1]
    print("x^[", n + 1, "]=", current)
    x.append(current)

print("z:", z)
print("x:", x)

plt.plot(year, x, color='green')
plt.show()