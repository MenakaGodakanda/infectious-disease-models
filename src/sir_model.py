import numpy as np
import matplotlib.pyplot as plt

# Parameters
beta = 0.3    # Infection rate
gamma = 0.1   # Recovery rate
S, I, R = 990, 10, 0  # Initial populations
N = S + I + R
days = 100

# Lists to store values
S_list, I_list, R_list = [S], [I], [R]

# Simulation loop
for _ in range(days):
    new_infected = (beta * S * I) / N
    new_recovered = gamma * I

    S -= new_infected
    I += new_infected - new_recovered
    R += new_recovered

    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# Plot results
plt.plot(S_list, label="Susceptible")
plt.plot(I_list, label="Infected")
plt.plot(R_list, label="Recovered")
plt.xlabel("Days")
plt.ylabel("Population")
plt.legend()
plt.show()

