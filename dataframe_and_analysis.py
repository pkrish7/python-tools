import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 75000, 80000, 90000]
}

df = pd.DataFrame(data)

# Display the dataset
print("Original Dataset:")
print(df)

# Calculate basic statistics using Pandas and NumPy
print("\nStatistics:")
print("Mean Age:", df['Age'].mean())
print("Max Salary:", df['Salary'].max())
print("Name with Max Salary:", df.loc[df['Salary'].idxmax(), 'Name'])

# Filtering data
print("\nPeople below 40 years old:")
print(df[df['Age'] < 40])

# Add a new column using NumPy
df['Bonus'] = np.where(df['Salary'] > 60000, 'Yes', 'No')
print("\nDataset with Bonus column:")
print(df)
