import pandas as pd

# Replace 'your_file.csv' with the desired path for the output CSV file
output_csv_path = "C:/Users/pardi/OneDrive/Desktop/bank-additional-full-output.csv"

# Read the CSV data into a DataFrame
df = pd.read_csv("C:/Users/pardi/OneDrive/Desktop/bank-additional-full.csv", sep=';', quoting=3)

# Display the DataFrame
print(df)

# Save the DataFrame to a new CSV file
df.to_csv(output_csv_path, index=False)
