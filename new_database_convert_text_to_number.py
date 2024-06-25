import pandas as pd

# Load the dataset
df = pd.read_csv("new_dataset.csv")


# Define the conversion function
def convert_cell(cell):
    cell_lower = str(cell).lower()
    if cell_lower in ["male", "yes", "positive"]:
        return 1
    elif cell_lower in ["female", "no", "negative"]:
        return 0
    else:
        return cell


# Apply the conversion to each cell
df = df.applymap(convert_cell)

# Save the converted dataset to a new CSV file
df.to_csv("converted_dataset.csv", index=False)
