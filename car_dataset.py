#!/usr/bin/env python
# coding: utf-8

# # Car Dataset_01

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


car=pd.read_csv(r'C:\Users\mujjj\Downloads\2. Cars Data1.csv')


# In[16]:


car


# In[17]:


car.shape


# In[22]:


car.columns


# # Remove column that only contains missing values

# In[23]:


car.isnull().sum()


# In[26]:


car['Cylinders'].fillna(car['Cylinders'].mean(),inplace=True)


# In[27]:


car


# In[28]:


car.isnull().sum()


# In[39]:


car.fillna(method='ffill')


# In[40]:


car.isnull().sum()


# In[44]:


car.dropna(how='all',inplace=True)


# In[45]:


car


# In[46]:


car.isnull().sum()


# # check different type of make are there in dataset

# In[48]:


car.head()


# In[50]:


car['Make'].value_counts()


# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# show all record where origin is asia and Europe

# In[51]:


car.head()


# In[52]:


car.columns


# In[53]:


car[car['Origin'].isin(['Asia','Europe'])]


# # Remove all record where weight is above to 4000

# In[54]:


car.columns


# In[59]:


car[~(car['Weight']>4000)]


# # increase value of MPG_City column by 3

# In[60]:


car.columns


# In[62]:


car['MPG_City']=car['MPG_City'].apply(lambda x:x+3)


# In[63]:


car['MPG_City']


# In[64]:


car.columns


# In[ ]:


car['Type'].value_

