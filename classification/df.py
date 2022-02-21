import pandas as pd

df = pd.read_csv("InferenceTime.csv", index_col=False)
res = df['time (ms)']
print(max(res))
print(min(res))