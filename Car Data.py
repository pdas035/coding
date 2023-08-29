#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


car=pd.read_csv(r"C:\Users\PRASANTA PC\Desktop\Excel project\2nd project.csv")


# In[5]:


car.head()


# In[6]:


car.shape


# # Data cleaning
# .Find all null value in the dataset. if there is any null value in any column, then fill it with the mean of that column.

# In[18]:


car.isnull().sum()


# In[16]:


car['Cylinders'].fillna(car['Cylinders'].mean(),inplace=True)


# In[17]:


car


# # .Check what are the different type of make are there in our dataset ,and what is count (occurence) of each make in the data.

# In[19]:


car.head(2)


# In[21]:


car['Make'].value_counts()


# # .Show all the recorsd where origin is asia or Europe.

# In[22]:


car.head(2)


# In[24]:


car[car['Origin'].isin(['Asia','Europe'])]


# # Remove all the records (Row) where weight is above 4000

# In[25]:


car.head(2)


# In[28]:


car[~(car['Weight'] >4000)]


# # Increase all the values of 'MPG_City' column by 3

# In[29]:


car.head(2)


# In[30]:


car['MPG_City']= car['MPG_City'].apply(lambda x:x+3)


# In[31]:


car

