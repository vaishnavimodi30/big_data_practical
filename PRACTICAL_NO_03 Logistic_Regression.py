#!/usr/bin/env python
# coding: utf-8

# In[1]:


# EXPERIMENT NO:03
# Aim:To perfrom and find the accuracy of Logistic Regression.
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


# In[6]:


os.chdir('C:\\Users\\user\\OneDrive\\Desktop')


# In[7]:


df=pd.read_csv("framingham.csv")


# In[8]:


df.head()


# In[9]:


df.tail()


# In[10]:


df.describe()


# In[11]:


df.info()


# In[12]:


df.isna().sum()


# df

# # Missing Value Treatment

# In[15]:


df['glucose'].fillna(value = df['glucose'].mean(),inplace=True)


# In[16]:


df['education'].fillna(value = df['education'].mean(),inplace=True)


# In[17]:


df['heartRate'].fillna(value = df['heartRate'].mean(),inplace=True)


# In[18]:


df['BMI'].fillna(value = df['BMI'].mean(),inplace=True)


# In[19]:


df['cigsPerDay'].fillna(value = df['cigsPerDay'].mean(),inplace=True)


# In[20]:


df['totChol'].fillna(value = df['totChol'].mean(),inplace=True)


# In[21]:


df['BPMeds'].fillna(value = df['BPMeds'].mean(),inplace=True)


# In[22]:


df.isna().sum()


# In[23]:


#Splitting the dependent and independent variables.
x = df.drop("TenYearCHD",axis=1)
y = df['TenYearCHD']


# In[24]:


x #checking the features


# # Train Test Split

# In[25]:


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


# In[26]:


y_train


# # Logistic Regression Algorithm

# In[27]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression().fit(x_train,y_train)
model.score(x_train, y_train)


# In[ ]:




