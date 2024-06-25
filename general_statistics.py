import pandas as pd

# load the dataset
df = pd.read_csv("diabetes.csv")

# show the min and max value for each column
for col in df.columns:
    print(f"{col}: min={df[col].min()}, max={df[col].max()}")
