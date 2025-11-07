import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
df = pd.read_csv('titanic.csv')

# Display the first few rows of the training data
print(df.head())

# Get information about the dataset
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Fill missing Age values with the median age
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing Embarked values with the most frequent port
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Survival by Sex
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title('Survival by Sex')
plt.show()

# Survival by Pclass
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title('Survival by Pclass')
plt.show()

# Distribution of Age
sns.histplot(df['Age'], kde=True)
plt.title('Distribution of Age')
plt.show()

# Age distribution by Sex and Pclass
sns.violinplot(x='Pclass', y='Age', hue='Sex', data=df)
plt.title('Age Distribution by Pclass and Sex')
plt.show()

# Correlation heatmap of numerical features
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()