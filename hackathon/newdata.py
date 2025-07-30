import pandas as pd
import numpy as np

np.random.seed(42)

# Simulate normal data
normal_data = {
    "pH": np.random.normal(7.2, 0.3, 100),  # mean=7.2, std=0.3
    "turbidity": np.random.normal(2.0, 1.0, 100),  # NTU
    "temperature": np.random.normal(22.0, 1.5, 100),  # °C
    "DO": np.random.normal(7.5, 0.5, 100),  # mg/L
    "anomaly": np.zeros(100, dtype=int)
}

# Simulate anomaly data
anomaly_data = {
    "pH": np.random.choice([np.random.uniform(3.0, 5.5), np.random.uniform(9.0, 11.0)], 30),
    "turbidity": np.random.uniform(10, 100, 30),
    "temperature": np.random.choice([np.random.uniform(10, 15), np.random.uniform(30, 40)], 30),
    "DO": np.random.uniform(2.0, 5.0, 30),
    "anomaly": np.ones(30, dtype=int)
}

# Combine into a DataFrame
df_normal = pd.DataFrame(normal_data)
df_anomaly = pd.DataFrame(anomaly_data)
df = pd.concat([df_normal, df_anomaly], ignore_index=True)

# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save it
df.to_csv("simulated_river_data_large.csv", index=False)

print(" Dataset simulated and saved!")