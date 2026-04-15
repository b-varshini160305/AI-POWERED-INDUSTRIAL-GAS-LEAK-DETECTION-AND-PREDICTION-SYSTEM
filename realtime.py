import time
import random
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("gas_dataset.csv")
X = df[["Gas_Value"]]
y = df["Status"]

model = LogisticRegression()
model.fit(X, y)

while True:
    gas = random.randint(100, 800)
    result = model.predict([[gas]])

    if result[0] == 1:
        print(f"🚨 LEAK DETECTED | {gas}")
    else:
        print(f"✅ SAFE | {gas}")

    time.sleep(2)
