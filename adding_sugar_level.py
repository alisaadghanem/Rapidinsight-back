import pandas as pd
import numpy as np

# Load the converted dataset
df = pd.read_csv("converted_dataset.csv")

# Create copies for each dataset
fbs_df = df.copy()
rbs_df = df.copy()
hba1c_df = df.copy()

# Add the "sugar_level" column to each dataset
fbs_df.insert(len(fbs_df.columns) - 1, "sugar_level", np.nan)
rbs_df.insert(len(rbs_df.columns) - 1, "sugar_level", np.nan)
hba1c_df.insert(len(hba1c_df.columns) - 1, "sugar_level", np.nan)

# Set sugar levels for FBS dataset
for index, row in fbs_df.iterrows():
    if row["class"] == 0:
        fbs_df.loc[index, "sugar_level"] = np.random.randint(0, 100)
    else:
        fbs_df.loc[index, "sugar_level"] = np.random.randint(100, 200)

# Set sugar levels for RBS dataset
for index, row in rbs_df.iterrows():
    if row["class"] == 0:
        rbs_df.loc[index, "sugar_level"] = np.random.randint(0, 140)
    else:
        rbs_df.loc[index, "sugar_level"] = np.random.randint(140, 280)

# Set sugar levels for HbA1c dataset
for index, row in hba1c_df.iterrows():
    if row["class"] == 0:
        hba1c_df.loc[index, "sugar_level"] = np.random.randint(0, 57)
    else:
        hba1c_df.loc[index, "sugar_level"] = np.random.randint(57, 100)

# Save each dataset to a separate CSV file
fbs_df.to_csv("FBS_dataset.csv", index=False)
rbs_df.to_csv("RBS_dataset.csv", index=False)
hba1c_df.to_csv("HbA1c_dataset.csv", index=False)
