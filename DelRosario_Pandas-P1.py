#!/usr/bin/env python
# coding: utf-8

# ### PROBLEM 1: 
# Using knowledge obtained from the experiment and demonstrations:
# a. Load the corresponding .csv file into a data frame named cars using pandas
# b. Display the first five and last five rows of the resulting cars

# In[1]:


import pandas as pd


# In[2]:


cars=pd.read_csv('Cars.csv')


# In[3]:


cars


# In[4]:


pd.concat([cars.head(), cars.tail()])

