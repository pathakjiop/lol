# Linear Regression Model

# Problem statement:
# To identify value of PetalWidthCm from rest of features
# Dependent Var >> PetalWidthCm 
# Independent var >> SepalWidthCm, PetalLengthCm, SepalLengthCm
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

# Iris Datase
# DataFrame
import pandas as pd
df=pd.read_csv('iris.csv')

print(df)
print(df['Species'].unique())
print(df.info())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.isna())
print(df.isna().sum())

##### EDA
print(df['Id'].nunique())
print(df.drop('Id', axis =1))
print(df)
print(df.drop('Id', axis =1 ,inplace=True))
print(df)
print(df['SepalLengthCm'].unique())
print(df['SepalLengthCm'].nunique())
sns.histplot(df['SepalWidthCm'])
sns.distplot(df['SepalWidthCm'])
print(df['Species'].unique())
print(df['Species'].nunique())
print(df['Species'].nunique())

sns.countplot(df['Species'])
df.plot()
df.plot(x = 'SepalLengthCm', y = 'PetalWidthCm', kind = 'scatter')

df.plot(x = 'SepalWidthCm', y = 'PetalWidthCm', kind = 'scatter')
df.plot(x = 'PetalLengthCm', y = 'PetalWidthCm', kind = 'scatter')
sns.pairplot(df)
df.dtypes
# Encoding  >> converting categorical features to numeric
df['Species'].replace({'Iris-setosa':0,'Iris-versicolor':1, 'Iris-virginica':2},inplace=True)
print(df)
print(df.dtypes)
corr = df.corr()
sns.pairplot(df)
plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True)
plt.savefig('Correlation_Matrix.jpg')
x = df.drop('PetalWidthCm', axis=1)  # 2D
y = df['PetalWidthCm']  # 1D
x_train , x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
print(x_train.info())

### Creating Model
lr_model = LinearRegression()
lr_model.fit(x_train, y_train)    # used to train the model
y_pred = lr_model.predict(x_test)
print(y_pred)
print(y_test)
residual = y_test - y_pred
print(residual)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
print('MSE is :', mse)
rmse = np.sqrt(mse)
print('RMSE is :', rmse)
mae = mean_absolute_error(y_test, y_pred)
print('MAE is :', mae)
r2_value = r2_score(y_test,y_pred)
r2_value