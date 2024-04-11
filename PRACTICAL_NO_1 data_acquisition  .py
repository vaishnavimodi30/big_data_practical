#!/usr/bin/env python
# coding: utf-8

# In[1]:


# DATA ACQUISITION
# EXPERIMENT NO:01
# Aim: To perfrom the operation  of data acquisition
# Name =VAISHNAVI MODI
# Roll No:41(B)


# In[4]:


# importing the basic libary.
import pandas as pd


# In[5]:


import os


# In[6]:


os.getcwd()


# In[7]:


os.chdir('C:\\Users\\user\\OneDrive\\Desktop')


# In[8]:


df=pd.read_csv("diabetes.csv")


# In[9]:


df.head(10)


# In[10]:


df.tail(10)


# In[11]:


df.info


# In[12]:


df.shape


# In[13]:


df.size


# In[15]:


df.ndim


# In[17]:


df.columns


# In[ ]:




