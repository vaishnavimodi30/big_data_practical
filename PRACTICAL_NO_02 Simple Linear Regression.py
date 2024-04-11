#!/usr/bin/env python
# coding: utf-8

# In[1]:


# EXPERIMENT NO:02
# Aim:To perfrom simple linear regression and find out the coefficients of it.
# Name =VAISHNAVI MODI
# Roll No:41(B)


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[3]:


import os 


# In[4]:


os.getcwd()


# In[5]:


os.chdir('C:\\Users\\user\\OneDrive\\Desktop')


# In[6]:


df=pd.read_csv("Salary_dataset.csv")


# In[7]:


df.head()


# In[8]:


df.tail()


# In[9]:


df.info()


# In[10]:


df.head(30)


# In[11]:


df[5:10]


# In[12]:


df.describe()


# In[13]:


df.shape


# In[14]:


df.size


# In[15]:


df.ndim


# In[16]:


df.columns


# In[17]:


df.isnull().sum()


# In[18]:


# Assiging values in X & Y
x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values


#x=df['year of experience']
#y=df['salary']


# In[19]:


print(x)


# In[20]:


print(y)


# In[21]:


# Splitting testdata into x_train,x_test,y_train,y_test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.3,random_state=42)


# In[22]:


print(x_train)


# In[23]:


print(y_train)


# In[26]:


print(y_test)


# In[29]:


from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)


# In[30]:


#Assigning Coefficient (slope) to m
m = lr.coef_


# In[31]:


print("Coefficient  :" , m)


# In[32]:


#Assigning Y-intercept to a
c = lr.intercept_


# In[33]:


print("Intercept : ", c)


# In[34]:


lr.score(x_test,y_test) * 100


# In[35]:


df.isnull().any()


# In[ ]:




