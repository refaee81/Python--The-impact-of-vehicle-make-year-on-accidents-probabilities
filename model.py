# Spyder project settings
.spyderproject
.spyproject

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 13:01:14 2018

@author: ramsey
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

os.chdir(r'D:\DataMining\another set') 

check=pd.read_csv("motor-vehicle-crashes-vehicle-information-three-year-window-1.csv", na_values='')

list(check.columns.values)

check['Contributing Factor 1'].unique()
check['Contributing Factor 1 Description'].unique()


Accidents=pd.read_csv("motor-vehicle-crashes-vehicle-information-three-year-window-1.csv", 
                      na_values='', usecols=[2, 4, 8, 10, 11, 13], 
                           header=0, names=['Vehicle_Body_Type', 'Action_Prior_Accident',
                                            'Make_Year','Number of Occupants', 'Cylinders', 'Contributing Factor'])

Accidents= Accidents.sample(n=10000,replace="False")### the file was heavy on python specially when doing mathmatical calcualtions, so I had to create random sample 


### DV: make year: 2000+ or 2000-

Accidents['Make_Year'].unique()

from collections import Counter
data = Counter(Accidents['Make_Year'])
data.most_common(1)  # Returns all unique items and their counts

Accidents['Make_Year'] = Accidents['Make_Year'].fillna(2013.0) 
np.array(Accidents['Make_Year']).astype(int)

Accidents['Make_Year'].unique()
min(Accidents.Make_Year)# 1901 in sample 
max(Accidents.Make_Year)# 2016 in sample 


bins = [1901., 1999., 2016.]
labels = ['1901.-1999.', '2000.-2016.']
Make_Year_Coded = {0:'1901.-1999.', 1: '2000.-2016.'}

Accidents['Make_Year_Grouped'] = pd.cut(Accidents.Make_Year, bins, labels = labels,include_lowest = True)
Accidents['Make_Year_Coded'] = pd.cut(Accidents.Make_Year, bins, labels = Make_Year_Coded,include_lowest = True)


from matplotlib import pyplot
pyplot.hist(Accidents.Make_Year)
pyplot.ylabel('Frequency')
pyplot.xlabel('Make_Year')
pyplot.title('Accidents of Vehciles Make Year')
pyplot.show()

from matplotlib import pyplot
pyplot.hist(Accidents.Make_Year_Coded)
pyplot.ylabel('Frequency')
pyplot.xlabel('Make_Year_Coded')
pyplot.title('Accidents of Vehciles Make Year')
pyplot.show()

from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot
qqplot(Accidents.Make_Year, line='s')
pyplot.show()

##################################### Descriptive Statistics, Plotting and scattering 


"""'Make_Year','Number of Occupants', 'Cylinders', 'Contributing Factor'
'Vehicle_Body_Type', 'Action_Prior_Accident', 'Action Prior to Accident'"""


import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns

sns.jointplot(x="Number of Occupants", y="Make_Year", data=Accidents, kind="reg");
plt.show()###  

sns.jointplot(x="Cylinders", y="Make_Year", data=Accidents, kind="reg");
plt.show()###  

#### rough regression for initial evaluation 
#dealing with noisy data and na's 

from collections import Counter
data = Counter(Accidents['Number of Occupants'])
data.most_common(1)  # Returns all unique items and their counts ### mode 
Accidents['Number of Occupants'] = Accidents['Number of Occupants'].fillna(1.0) 
np.array(Accidents['Number of Occupants']).astype(int)

data = Counter(Accidents['Cylinders'])
data.most_common(1)  # Returns all unique items and their counts ### mode 
Accidents['Cylinders'] = Accidents['Cylinders'].fillna(4.0) 
np.array(Accidents['Cylinders']).astype(int)

data = Counter(Accidents['Contributing Factor'])
data.most_common(1)  # Returns all unique items and their counts ### mode 
Accidents['Contributing Factor'] = Accidents['Contributing Factor'].fillna('HUMAN') 

data = Counter(Accidents['Vehicle_Body_Type'])
data.most_common(1)  # Returns all unique items and their counts ### mode 
Accidents['Vehicle_Body_Type'] = Accidents['Vehicle_Body_Type'].fillna('4 DOOR SEDAN') 

data = Counter(Accidents['Action_Prior_Accident'])
data.most_common(1)  # Returns all unique items and their counts ### mode 
Accidents['Action_Prior_Accident'] = Accidents['Action_Prior_Accident'].fillna('Going Straight Ahead') 




Rough_OLS = smf.ols('Make_Year ~  Cylinders', data=Accidents).fit()
print(Rough_OLS.summary())
plt.rc('figure', figsize=(12, 7))
#plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 12}) old approach
plt.text(0.01, 0.05, str(Rough_OLS.summary()), {'fontsize': 5}, fontproperties = 'monospace') # approach improved by OP -> monospace!
plt.axis('off')
plt.savefig('output.png')
plt.show()

Rough_OLS = smf.ols('Make_Year ~  C(Vehicle_Body_Type)', data=Accidents).fit()
print(Rough_OLS.summary())
plt.rc('figure', figsize=(12, 7))
#plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 12}) old approach
plt.text(0.01, 0.05, str(Rough_OLS.summary()), {'fontsize': 5}, fontproperties = 'monospace') # approach improved by OP -> monospace!
plt.axis('off')
plt.savefig('output.png')
plt.show()

Rough_OLS = smf.ols('Make_Year ~  Action_Prior_Accident', data=Accidents).fit()
print(Rough_OLS.summary())
plt.rc('figure', figsize=(12, 7))
#plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 12}) old approach
plt.text(0.01, 0.05, str(Rough_OLS.summary()), {'fontsize': 5}, fontproperties = 'monospace') # approach improved by OP -> monospace!
plt.axis('off')
plt.savefig('output.png')
plt.show()

Rough_OLS = smf.ols('Make_Year ~  Cylinders + Action_Prior_Accident + Vehicle_Body_Type', data=Accidents).fit()
print(Rough_OLS.summary())
plt.rc('figure', figsize=(12, 7))
#plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 12}) old approach
plt.text(0.01, 0.05, str(Rough_OLS.summary()), {'fontsize': 5}, fontproperties = 'monospace') # approach improved by OP -> monospace!
plt.axis('off')
plt.savefig('output.png')
plt.show()

##### 



Accidents.to_csv("Accidents Sample1.csv")
Accidents.shape


from sklearn.model_selection import train_test_split

X = Accidents.iloc[:, 0:6] ####Split the data into training and test sets###DV loc 3
y = Accidents.iloc[:, [7]]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

X_train.shape#### Check out training data is sufficient
X_test.shape 


dummy_set = pd.core.reshape.reshape.get_dummies(X, prefix=None, prefix_sep='_', dummy_na=True, columns=None, sparse=False, drop_first=False, dtype=None)

dummy_set.head()

Dummy =pd.concat([dummy_set, Accidents.Make_Year_Coded], axis=1)

Dummy.to_csv("Dummy.csv")


Dummy.columns
Dummy.shape 


sns.heatmap(Dummy.corr())
plt.show()

from sklearn.model_selection import train_test_split

X = Dummy.iloc[:, 0:74] ####Split the data into training and test sets
y = Dummy.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

X_train.shape#### Check out training data is sufficient
X_test.shape 

from sklearn import preprocessing
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
import seaborn as sns


classifier = LogisticRegression(random_state=0) ###Fit logistic regression to the training set
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test) ###Predicting the test set results and creating confusion matrix

from sklearn.metrics import confusion_matrix ###The confusion_matrix() function will calculate a confusion matrix and return the result as an array.
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_test, y_test)))  ### Accuracy

from sklearn.metrics import classification_report ### Compute precision, recall, F-measure and support
print(classification_report(y_test, y_pred))


from sklearn.metrics import roc_auc_score
ROC_AUC= roc_auc_score(y_test, y_pred)

from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(y_test, y_pred)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, color='darkorange', label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Make Year ROC')
plt.legend(loc="lower right")
plt.show()


# the average precision can be calculated by calling the average_precision_score() function and passing it the true class values and the predicted class values.
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import f1_score
from sklearn.metrics import auc
from sklearn.metrics import average_precision_score
from matplotlib import pyplot
# generate 2 class dataset
X, y = make_classification(n_samples=5000, n_classes=2, weights=[1,1], random_state=1)
# split into train/test sets
trainX, testX, trainy, testy = train_test_split(X, y, test_size=0.5, random_state=2)
# fit a model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(trainX, trainy)# predict probabilities
probs = model.predict_proba(testX)# keep probabilities for the positive outcome only
probs = probs[:, 1]# predict class values
yhat = model.predict(testX)# calculate precision-recall curve
precision, recall, thresholds = precision_recall_curve(testy, probs)# calculate F1 score
f1 = f1_score(testy, yhat)# calculate precision-recall AUC
auc = auc(recall, precision)# calculate average precision score
ap = average_precision_score(testy, probs)


print('f1=%.3f auc=%.3f ap=%.3f' % (f1, auc, ap))
pyplot.plot([0, 1], [0.5, 0.5], linestyle='--')# plot the roc curve for the model
pyplot.plot(recall, precision, marker='.')
plt.title('f1=0.81 auc=0.82 ap=0.853')
pyplot.show()
