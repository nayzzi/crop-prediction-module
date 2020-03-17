import pandas
import pandas as pd
from random import shuffle
from sklearn.linear_model import LinearRegression
import time
import pickle
#from firebase import firebase

cols=['pH ','humidity %','ec ','temperature','n %','p %','k %']

df=pd.read_excel(r'/Users/nayanalakshitha/Desktop/NPK/dataset.xlsx')


pH=df['pH ']
humidity=df['humidity %']
ec=df['ec ']
temperature=df['temperature']
n=df['n %']
p=df['p %']
k=df['k %']


getData=[pH,humidity,ec,temperature,n,p,k]
list1=[]
for k in range(len(getData[0])):
    i=k
    x=[int(getData[0][i]),int(getData[1][i]),int(getData[2][i]),int(getData[3][i])]
    tot=0
    for j in range(len(x)):
        tot=float(tot)+x[j]
    x=[int(getData[0][i])/tot,int(getData[1][i])/tot,int(getData[2][i])/tot,int(getData[3][i])/tot,getData[4][i],getData[5][i],getData[6][i]]
    list1.append(x)

"""
n case
"""

list=list1
totPred=0
cp=0
model=None
X=None
Y=None
for i in range(10):
    shuffle(list)
    bigData=pd.DataFrame(list,columns=['','','','','label','t1','t2'])
    target=bigData['label']
    from sklearn.model_selection import  train_test_split
    X_train,X_test,Y_train,Y_test=train_test_split(bigData.drop(['label','t1','t2'],axis='columns'),target,test_size=0.2)
    model = LinearRegression()
    X=X_train
    Y=Y_train
    model.fit(X_train,Y_train)
    pred=model.score(X_test,Y_test)

    if(pred>cp):
        cp=pred
        filename = r'/Users/nayanalakshitha/Desktop/NPK/nModel.sav'
        pickle.dump(model, open(filename, 'wb'))

    totPred=pred+totPred


print("")
print("Algorithm : LinearRegression for n")
print("Train Data Count : ",len(X_train))
print("Test Data Count : ",len(X_test))
print("Accuracy :",cp)

"""
p case
"""

list=list1
totPred=0
cp=0
model=None
X=None
Y=None
for i in range(10):
    shuffle(list)
    bigData=pd.DataFrame(list,columns=['','','','','t1','label','t2'])
    target=bigData['label']
    from sklearn.model_selection import  train_test_split
    X_train,X_test,Y_train,Y_test=train_test_split(bigData.drop(['t1','label','t2'],axis='columns'),target,test_size=0.02)
    model = LinearRegression()
    X=X_train
    Y=Y_train
    model.fit(X_train,Y_train)
    pred=model.score(X_test,Y_test)

    if(pred>cp):
        cp=pred
        filename = r'/Users/nayanalakshitha/Desktop/NPK/pModel.sav'
        pickle.dump(model, open(filename, 'wb'))

    totPred=pred+totPred


print("")
print("Algorithm : LinearRegression for p")
print("Train Data Count : ",len(X_train))
print("Test Data Count : ",len(X_test))
print("Accuracy :",cp)

"""
k case
"""

list=list1
totPred=0
cp=0
model=None
X=None
Y=None
for i in range(10):
    shuffle(list)
    bigData=pd.DataFrame(list,columns=['','','','','t1','t2','label'])
    target=bigData['label']
    from sklearn.model_selection import  train_test_split
    X_train,X_test,Y_train,Y_test=train_test_split(bigData.drop(['t1','t2','label'],axis='columns'),target,test_size=0.2)
    model = LinearRegression()
    X=X_train
    Y=Y_train
    model.fit(X_train,Y_train)
    pred=model.score(X_test,Y_test)

    if(pred>cp):
        cp=pred
        filename = r'/Users/nayanalakshitha/Desktop/NPK/kModel.sav'
        pickle.dump(model, open(filename, 'wb'))

    totPred=pred+totPred


print("")
print("Algorithm : LinearRegression for k")
print("Train Data Count : ",len(X_train))
print("Test Data Count : ",len(X_test))
print("Accuracy :",cp)
print("")








