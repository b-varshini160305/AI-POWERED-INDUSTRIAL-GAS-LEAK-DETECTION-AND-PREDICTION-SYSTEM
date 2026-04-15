import pandas as pd
import random

data = []

for _ in range(300):
    data.append([random.randint(100, 300), 0])

for _ in range(200):
    data.append([random.randint(400, 800), 1])

df = pd.DataFrame(data, columns=["Gas_Value", "Status"])
df.to_csv("gas_dataset.csv", index=False)

print("Dataset created")

<!--http://127.0.0.1:5000-->
