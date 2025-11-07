import pandas as pd
import numpy as np

print("=== Experiment 3: Pandas Library Functions ===\n")

# 1. Series Creation
print("1. Pandas Series Creation:")

# Creating empty series
empty_series = pd.Series()
print("Empty Series:", empty_series)

# Creating series from list
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)
print("Series from list:\n", series_from_list)

# Creating series from numpy array
data_np = np.array(['s', 's', 'g', 'm', 'c', 'e'])
series_from_np = pd.Series(data_np)
print("Series from numpy array:\n", series_from_np)

# Creating series with custom index
series_custom = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print("Series with custom index:\n", series_custom)

# 2. DataFrame Creation
print("\n2. Pandas DataFrame Creation:")

# Creating DataFrame from dictionary
data_dict = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "exercise": ["running", "swimming", "cycling"]
}

df = pd.DataFrame(data_dict)
print("DataFrame from dictionary:\n", df)

# Creating DataFrame with custom index
df_indexed = pd.DataFrame(data_dict, index=['day1', 'day2', 'day3'])
print("\nDataFrame with custom index:\n", df_indexed)

# 3. DataFrame Operations
print("\n3. DataFrame Operations:")

# Accessing columns
print("Calories column:\n", df['calories'])

# Accessing rows
print("\nFirst row:\n", df.iloc[0])

# Adding new column
df['calories_per_minute'] = df['calories'] / df['duration']
print("\nDataFrame with new column:\n", df)

# Basic statistics
print("\nDataFrame statistics:")
print(df.describe())

# 4. Data Selection and Filtering
print("\n4. Data Selection and Filtering:")

# Selecting specific columns
print("Selected columns:\n", df[['exercise', 'calories']])

# Filtering data
high_calories = df[df['calories'] > 390]
print("\nExercises with calories > 390:\n", high_calories)

# 5. Handling Missing Data
print("\n5. Handling Missing Data:")

# Creating DataFrame with missing values
data_with_na = {
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
    'C': [9, 10, 11, 12]
}

df_na = pd.DataFrame(data_with_na)
print("DataFrame with missing values:\n", df_na)
print("\nDataFrame info:")
print(df_na.info())
print("\nSum of null values:\n", df_na.isnull().sum())

# Fill missing values
df_filled = df_na.fillna(0)
print("\nDataFrame after filling missing values:\n", df_filled)