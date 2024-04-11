#!/usr/bin/env python
# coding: utf-8

# In[1]:


# EXPERIMENT NO:06
# AIM:To perform hypothesis testing using To perform T-test.
# Name =VAISHNAVI MODI
# Roll No:41(B)


# In[2]:


#T Test A t-test is a type of inferential statistic which is used to determine if there is a significant difference between the means of two groups which may be related in certain
ages=[10,20,35,50,28,40,55,18,16,55,30,25,43,18,30,28,14,24,16,17,32,35,26,27,65,18,43,23,21,20,19,70]


# In[3]:


len(ages)


# In[4]:


import numpy as np
ages_mean=np.mean(ages)
print(ages_mean)


# In[5]:


## Lets take sample
sample_size=10
age_sample=np.random.choice(ages,sample_size)


# In[6]:


age_sample


# In[7]:


from scipy.stats import ttest_1samp


# In[8]:


ttest,p_value=ttest_1samp(age_sample,30)


# In[9]:


print(p_value)


# In[10]:


if p_value < 0.05: # alpha value is 0.05 or 5%
    print(" we are rejecting null hypothesis")
else:
    print("we are accepting null hypothesis")


# In[ ]:




