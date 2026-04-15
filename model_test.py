import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("gas_dataset.csv")
X = df[["Gas_Value"]]
y = df["Status"]

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[150]]))  # Safe
print(model.predict([[600]]))  # Leak
