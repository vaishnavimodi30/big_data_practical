#!/usr/bin/env python
# coding: utf-8

# In[1]:


# EXPERIMENT NO:08
# Aim: To perfrom and find the accuracy of K-Nearest Neighbors Algorithm ie.KNN Classifier
# Name =VAISHNAVI MODI
# Roll No:41(B)


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')


# In[3]:


import os


# In[4]:


os.getcwd()


# In[5]:


os.chdir('C:\\Users\\user\\OneDrive\\Desktop')


# In[6]:


df=pd.read_csv("framingham.csv")


# In[7]:


df.head()


# In[8]:


df.tail()


# In[9]:


df.describe()


# In[10]:


df.info()


# In[11]:


df.isna().sum()


# In[12]:


df


# # Missing Value Treatment

# In[13]:


df['glucose'].fillna(value = df['glucose'].mean(),inplace=True)


# In[14]:


df['education'].fillna(value = df['education'].mean(),inplace=True)


# In[15]:


df['heartRate'].fillna(value = df['heartRate'].mean(),inplace=True)


# In[16]:


df['BMI'].fillna(value = df['BMI'].mean(),inplace=True)


# In[17]:


df['cigsPerDay'].fillna(value = df['cigsPerDay'].mean(),inplace=True)


# In[18]:


df['totChol'].fillna(value = df['totChol'].mean(),inplace=True)


# In[19]:


df['BPMeds'].fillna(value = df['BPMeds'].mean(),inplace=True)


# In[20]:


df.isna().sum()


# In[21]:


#Splitting the dependent and independent variables.
x = df.drop("TenYearCHD",axis=1)
y = df['TenYearCHD']


# In[22]:


x #checking the features


# # Train Test Split

# In[24]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


# In[25]:


y_train


# # KNN Classifier

# In[26]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
knn.fit(x_train, y_train)
acc = knn.score(x_test,y_test)*100
print(acc)


# In[ ]:




