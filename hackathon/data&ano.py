import random
import time
import csv
from datetime import datetime

# Control how often to inject an anomaly (e.g., 20% of the time)
ANOMALY_PROBABILITY = 0.2

def inject_anomaly(value, param):
    """Injects an anomaly based on parameter type"""
    if param == "pH":
        return round(random.choice([random.uniform(3.0, 5.0), random.uniform(9.0, 11.0)]), 2)
    elif param == "turbidity":
        return round(random.uniform(120.0, 300.0), 2)
    elif param == "temperature":
        return round(random.choice([random.uniform(5.0, 10.0), random.uniform(40.0, 50.0)]), 2)
    elif param == "dissolved_oxygen":
        return round(random.uniform(0.5, 2.5), 2)
    return value

def simulate_value(normal_func, param):
    value = normal_func()
    if random.random() < ANOMALY_PROBABILITY:
        value = inject_anomaly(value, param)
    return value

# Normal sensor simulation
def simulate_ph(): return round(random.uniform(6.0, 8.5), 2)
def simulate_turbidity(): return round(random.uniform(5.0, 50.0), 2)
def simulate_temperature(): return round(random.uniform(15.0, 35.0), 2)
def simulate_dissolved_oxygen(): return round(random.uniform(5.0, 10.0), 2)

# Setup CSV
filename = "simulated_river_data_with_anomalies.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "pH", "turbidity", "temperature", "dissolved_oxygen", "anomaly_flag"])

# Generate 20 entries with some anomalies
for _ in range(20):
    timestamp = datetime.now().isoformat()

    ph = simulate_value(simulate_ph, "pH")
    turbidity = simulate_value(simulate_turbidity, "turbidity")
    temp = simulate_value(simulate_temperature, "temperature")
    do = simulate_value(simulate_dissolved_oxygen, "dissolved_oxygen")

    # Flag as anomaly if any value is outside normal range
    is_anomaly = (
        ph < 6.0 or ph > 8.5 or
        turbidity > 100 or
        temp < 10 or temp > 40 or
        do < 3
    )

    print(f"{timestamp} | pH: {ph}, Turbidity: {turbidity}, Temp: {temp}, DO: {do} | Anomaly: {'⚠ Yes' if is_anomaly else 'No'}")

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, ph, turbidity, temp, do, int(is_anomaly)])

    time.sleep(1)