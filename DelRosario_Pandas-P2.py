#!/usr/bin/env python
# coding: utf-8

# ### PROBLEM 2: 
# Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and
# indexing operations.
# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
# Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# In[1]:


import pandas as pd


# In[2]:


cars=pd.read_csv('Cars.csv')


# In[3]:


cars


# In[4]:


cars.iloc[:5, ::2]


# In[5]:


cars[cars["Model"] == "Mazda RX4"]


# In[6]:


cars.loc[cars["Model"] == "Camaro Z28", ["Model", "cyl"]]


# In[7]:


cars.loc[[1,28,18],['Model','gear']]


# In[ ]:




