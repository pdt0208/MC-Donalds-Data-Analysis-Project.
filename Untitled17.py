#!/usr/bin/env python
# coding: utf-8

# In[134]:


import pandas as pd 
import numpy as np


# In[135]:


df=pd.read_csv("McDonald_s_Reviews.csv")


# In[136]:


df.head(22143)


# In[137]:


df.isnull().sum()


# In[138]:


df.size


# In[139]:


df.fillna(0, inplace=True)


# In[140]:


df.head(22143)


# In[141]:


df.size


# In[158]:


df['store_address'] = df['store_address'].str.replace('Kalï¿½', '', regex=True)


# In[159]:


df.head(22143)


# In[160]:


df['store_address'] = df['store_address'].str.replace('2476 Kal', '2476 Kali', regex=True)


# In[161]:


df.head(22143)


# In[162]:


df['review'] = df['review'].str.replace('ï¿½', '', regex=True)


# In[163]:


df


# In[164]:


df['review'] = df['review'].str.replace('i', '', regex=True)


# In[165]:


df.head(22143)


# In[167]:


df.size


# In[168]:


df.isnull().sum()


# In[ ]:




