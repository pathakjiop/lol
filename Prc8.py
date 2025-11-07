import numpy as nm  
import matplotlib.pyplot as mtp
import pandas as pd  

#importing datasets  
data_set= pd.read_csv('User_Data.csv')  
print(data_set)

## Understanding of data_set
print(data_set.info())

print(data_set['User ID'].unique())

print(data_set['User ID'].nunique())
print(data_set.shape)
print(data_set.describe())

# perform a=data understaiding for each feature
# Null Value analysis
print(data_set.isna())
print(data_set.isna().sum())

#Extracting Independent and dependent Variable  
x= data_set.iloc[:, [2,3]].values  
y= data_set.iloc[:, 4].values  

# Splitting of Data for trainingand testing
# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.20, random_state=0)

print(x_train.shape)

from sklearn.preprocessing import StandardScaler    
st_x= StandardScaler()    
x_train= st_x.fit_transform(x_train)    
x_test= st_x.transform(x_test)  

# Fitting Logistic Regression to the training set  
from sklearn.linear_model import LogisticRegression  
classifier= LogisticRegression(random_state=0)  
classifier.fit(x_train, y_train)
#Predicting the test set result  
y_pred = classifier.predict(x_test)  
#Predicting the training set result  
y_pred_train = classifier.predict(x_train) 


from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve
#accuracy score
acc_score=accuracy_score(y_test,y_pred)
print('Accuracy Score:',acc_score)
print('*'*70)

#Creating the Confusion matrix  
from sklearn.metrics import confusion_matrix  
cm= confusion_matrix(y_test,y_pred)  
print('Confusion Matrix\n',cm)
print('*'*70)

#Classification Report
clf_report=classification_report(y_test,y_pred)
print('CR',clf_report)


#Training Data Evaluation
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve

#accuracy score
acc_score=accuracy_score(y_train,y_pred_train)
print('Accuracy Score:',acc_score)
print('*'*65)

#Creating the Confusion matrix  
from sklearn.metrics import confusion_matrix  
cm= confusion_matrix(y_train,y_pred_train)  
print('Confusion Matrix\n',cm)
print('*'*65)

#Classification Report
clf_report=classification_report(y_train,y_pred_train)
print('CR', clf_report)
