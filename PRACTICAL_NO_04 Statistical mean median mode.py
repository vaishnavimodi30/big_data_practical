#!/usr/bin/env python
# coding: utf-8

# In[1]:


# EXPERIMENT NO:04
# Aim:To perform Finding Statistical mean, median, mode, standard  deviation, variance using Numpy and scipy
# Name =VAISHNAVI MODI
# Roll No:41(B)


# In[2]:


import numpy as np
x=np.array([1,2,3,4,5,6,7,2,6,2,1,4,2,2,6])


# In[3]:


x


# In[4]:


print(np.mean(x))


# In[5]:


print(np.median(x))


# In[6]:


print(np.mode(x))


# In[7]:


from scipy import stats


# In[8]:


print(stats.mode(x))


# In[9]:


print(np.std(x))


# In[10]:


print(np.var(x))


# In[11]:


import numpy as np
x=np.array([1,100,200,300,4000,5000])
y=np.array([2,4,6,8,10]),


# In[12]:


print(np.std(x))


# In[13]:


print(np.std(y))


# In[14]:


print(np.var(x))


# In[15]:


print(np.var(y))


# In[16]:


from matplotlib import pyplot as plt
plt.hist(x)
plt.show()


# In[17]:


from matplotlib import pyplot as plt
plt.hist(y)
plt.show()


# In[18]:


from statsmodels.stats.weightstats import ztest as ztest
#enter IQ levels for 20 patients
data = [88, 92, 94, 94, 96, 97, 97, 97, 99, 99,
105, 109, 109, 109, 110, 112, 112, 113, 114, 115]
#perform one sample z-test
ztest(data)
(1.5976240527147705, 0.1101266701438426)


# In[ ]:




