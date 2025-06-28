import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("C:/Users/pardi/OneDrive/Desktop/bank-additional-full-output.csv")

# Remove quotes from the first row
df.iloc[0] = df.iloc[0].apply(lambda x: x.replace("'", "").replace('"', '') if isinstance(x, str) else x)

# Remove quotes from the rest of the DataFrame
df = df.applymap(lambda x: x.replace("'", "").replace('"', '') if isinstance(x, str) else x)

# Save the modified DataFrame back to a CSV file
df.to_csv('output_file.csv', index=False)
