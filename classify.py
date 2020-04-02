# dataset ref: https://github.com/Te-k/malware-classification
# dataset is generated using pefile
import pandas as pd
import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler


np.random.seed(7)
# load the dataset
dataframe = read_csv('data.csv', sep='|')

dataX = dataframe.iloc[: , 2:-1]
dataY = dataframe.iloc[:,-1]

tfr = MinMaxScaler()
tfr.fit(dataX)
dataX = tfr.transform(dataX)

# corelation matrix
plt.imshow(np.corrcoef(dataX.T))
plt.show()

# split dataset
X_train, X_test, y_train, y_test = train_test_split(dataX, dataY, test_size=0.3, random_state=42)


# classifier
# clf = SVC(gamma='auto')
clf = RandomForestClassifier(n_estimators=100, criterion='gini')
# clf = DecisionTreeClassifier(criterion='gini')
# clf = LogisticRegression()
clf.fit(X_train,y_train)


train_pred = clf.predict(X_train)
test_pred = clf.predict(X_test)

# evaluate on training set
print('confusion matrix on training set')
print(confusion_matrix(y_train, train_pred))
tn_train, fp_train, fn_train, tp_train = confusion_matrix(y_train, train_pred).ravel()

precision_train = tp_train/(tp_train + fp_train)
Accuracy_train= (tp_train + tn_train)/(tp_train + tn_train + fn_train + fp_train)
Recall_train = tp_train/ (tp_train + fn_train)

F1Score_train = 2*(Recall_train* precision_train)/(Recall_train + precision_train)

print('precision: ', precision_train)
print('accuracy: ', Accuracy_train)
print('Recall: ', Recall_train)
print('f1:', F1Score_train)


# evaluate on validation set
print('confusion matrix on testing set')
print(confusion_matrix(y_test, test_pred))
tn_test, fp_test, fn_test, tp_test = confusion_matrix(y_test, test_pred).ravel()

precision_test = tp_test/(tp_test + fp_test)
Accuracy_test= (tp_test + tn_test)/(tp_test + tn_test + fn_test + fp_test)
Recall_test = tp_test/ (tp_test + fn_test)

F1Score_test = 2*(Recall_test* precision_test)/(Recall_test + precision_test)

print('precision: ', precision_test)
print('acc: ', Accuracy_test)
print('recall: ', Recall_test)
print('f1: ', F1Score_test)
