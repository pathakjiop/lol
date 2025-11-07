import pandas as pd

# 1. Creating DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney'],
    'Salary': [50000, 60000, 70000, 55000, 65000]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# 2. Inspecting Data
print("\nFirst 2 rows:")
print(df.head(2))
print("\nLast 2 rows:")
print(df.tail(2))
print("\nDataFrame Info:")
print(df.info())

# 3. Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# 4. Sorting Records
print("\nSorted by Age:")
print(df.sort_values('Age'))
print("\nSorted by Salary (descending):")
print(df.sort_values('Salary', ascending=False))

# 5. Slicing Records
print("\nName column:")
print(df['Name'])
print("\nName and Salary columns:")
print(df[['Name', 'Salary']])
print("\nSecond row:")
print(df.iloc[1])
print("\nSecond row, second column:")
print(df.iloc[1, 1])

# 6. Renaming Columns
df_renamed = df.rename(columns={'Salary': 'Annual_Salary', 'City': 'Location'})
print("\nAfter renaming columns:")
print(df_renamed.columns)

# 7. Data Wrangling
print("\nAverage salary by city:")
print(df.groupby('City')['Salary'].mean())

# Merge
df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Frank'],
    'Department': ['IT', 'HR', 'Finance']
})
merged_df = pd.merge(df, df2, on='Name', how='left')
print("\nAfter merge:")
print(merged_df)

# Concatenation
df3 = pd.DataFrame({
    'Name': ['Frank', 'Grace'],
    'Age': [40, 29],
    'City': ['Berlin', 'Toronto'],
    'Salary': [80000, 52000]
})
concatenated_df = pd.concat([df, df3], ignore_index=True)
print("\nAfter concatenation:")
print(concatenated_df)

# 8. Additional Functions
print("\nUnique cities:")
print(df['City'].unique())
print("\nValue counts for cities:")
print(df['City'].value_counts())
print("\nData types:")
print(df.dtypes)

print("\nPeople with salary > 60000:")
print(df[df['Salary'] > 60000])