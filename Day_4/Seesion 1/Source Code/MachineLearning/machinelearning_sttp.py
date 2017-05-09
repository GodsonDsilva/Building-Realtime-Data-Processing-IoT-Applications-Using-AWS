
# coding: utf-8

# In[6]:

# loading libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
#from sklearn.metrics import classification_report
#from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# In[8]:

# loading dataset
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
path = r"E:\My Files\SJCET\workshop\python\1 Data Science\MAchineLearningMastery"
c = path+"\iris.data.txt"
dataset = pandas.read_csv(c, names=['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class'])
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
#dataset = pandas.read_csv(url, names=names)


# In[9]:

type(dataset)


# In[10]:

# viewing data
dataset


# In[11]:

# Dimensions of Dataset
dataset.shape


# In[12]:

#Peek at the Data
dataset.head(20)


# In[13]:

dataset.tail(20)


# In[14]:

dataset['sepal-width']


# In[15]:

#Statistical Summary
dataset.describe()


# In[16]:

dataset['sepal-width'].min()


# In[17]:

# what is percentiles
#For example, suppose you have 25 test scores, and in order from lowest to highest they look like this: 43, 54, 56, 61, 62, 66, 68, 69, 69, 70, 71, 72, 77, 78, 79, 85, 87, 88, 89, 93, 95, 96, 98, 99, 99.
#To find the 90th percentile for these (ordered) scores, start by multiplying 90% times the total number of scores, 
#which gives 90% ∗ 25 = 0.90 ∗ 25 = 22.5 (the index). Rounding up to the nearest whole number, you get 23.

#Counting from left to right (from the smallest to the largest value in the data set), you go until you find the 23rd value 
#in the data set. That value is 98, and it’s the 90th percentile for this data set.

#Now say you want to find the 20th percentile. Start by taking 0.20 x 25 = 5 (the index); this is a whole number, 
#so the 20th percentile is the average of the 5th and 6th values in the ordered data set (62 and 66). The 20th percentile then comes to (62 + 66) ÷ 2 = 64.


# In[18]:

#Class Distribution
#Let’s now take a look at the number of instances (rows) that belong to each class
print(dataset.groupby('class').size())


# In[19]:

# understanding groupby
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df1 = pandas.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])
list(df1['preTestScore'].groupby(df1['company']))


# In[20]:

dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
#the central box of the boxplot represents the middle 25%,75% and 50% of the observations, the central bar is the median and the bars at the end of the dotted lines (whiskers) encapsulate the great majority of the observations. 
#Circles that lie beyond the end of the whiskers are data points that may be outliers.


# In[21]:

#creating histogram
dataset.hist()
plt.show()


# In[28]:

# to show the correlation between different attributes
scatter_matrix(dataset, figsize=(10,10))
plt.show()


# In[29]:

#Note the diagonal grouping of some pairs of attributes. This suggests a high correlation and a predictable relationship


# In[30]:

#Evaluate Some Algorithms
#Separate out a validation dataset.
#Set-up the test harness to use 10-fold cross validation.
#Build 5 different models to predict species from flower measurements
#Select the best model.


# In[22]:

array = dataset.values


# In[23]:

array


# In[24]:

X = array[:,0:4]
Y = array[:,-1]


# In[25]:

X, Y


# In[26]:

validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


# In[27]:

x = len(X_train)
xx = len(X_validation)
y = len(Y_train)
yy = len(Y_validation)


# In[28]:

x, xx, y, yy


# In[29]:

seed = 7
scoring = 'accuracy'


# In[30]:

models = LogisticRegression()
kfold = model_selection.KFold(n_splits=10, random_state=seed)
cv_results = model_selection.cross_val_score(models, X_train, Y_train, cv=kfold, scoring=scoring)
print(cv_results.mean(), cv_results.std())


# In[31]:

#Let’s build and evaluate our five models:
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)  #KFold(n_splits=3, shuffle=False, random_state=None)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)


# In[32]:

#make predictions
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))


# In[33]:

X_validation


# In[34]:

knn.predict([6.9, 2.4, 6.0, 3.0])


# In[ ]:




# In[ ]:



