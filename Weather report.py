#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = pd.read_csv(r"C:\Users\PRASANTA PC\Desktop\Excel project\Weather report.csv")


# In[4]:


data


# In[5]:


data.head()


# In[8]:


data.shape


# In[10]:


data.index


# In[13]:


data.columns


# In[14]:


data.dtypes


# In[26]:


data['Weather'].unique()


# In[27]:


data.nunique()


# In[28]:


data.count()


# # Q1. Find all the unique 'wind speed' value in the data 

# In[32]:


data.head(2)


# In[33]:


data.nunique()


# In[34]:


data['Wind Speed_km/h'].nunique()


# # Q2. Find the number of times when the 'wheather is exactly clear'

# In[6]:


data.head(2)


# In[8]:


data.Weather.value_counts()


# In[11]:


data.head(2)
data[data.Weather == 'Clear']


# In[12]:


data.head(2)


# In[14]:


data.groupby('Weather').get_group('Clear')


# # Q3. Find the numbers of time when the 'wind speed exactly 4 Km/h'

# In[19]:


data.head(2)


# In[21]:


data[data['Wind Speed_km/h'] ==4]


# # Q4. Find out all the null value of data

# In[23]:


data.isnull().sum()


# In[24]:


data.notnull().sum()


# # Q5. Rename the colunm name 'weather of the dataframe to weather condition

# In[25]:


data.head(2)


# In[30]:


data.rename(columns ={'Weather' : 'Weather Condition'},inplace =True)


# In[31]:


data.head()


# # Q6.What is the mean visibility 

# In[32]:


data.head(2)


# In[34]:


data.Visibility_km.mean()


# # Q7. What is ther standard vediation of pressures in this data

# In[35]:


data.Press_kPa.std()


# # Q8. What is the variance of relative humidity in this data

# In[36]:


data['Rel Hum_%'].var()


# # Q9.Find all instance when snow was recorded

# In[38]:


data.head(2)
data['Weather Condition'].value_counts()


# In[40]:


data[data['Weather Condition'] == 'Snow']


# In[42]:


data[data['Weather Condition'].str.contains('Snow')].head(50)


# # Q10. Find all instances when wind speed is above 24 and visibility is 25 

# In[43]:


data.head(2)


# In[45]:


data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']== 25)]


# # Q11. What is the mean value of each colum againts eath weather condition ?

# In[46]:


data.head(2)


# In[48]:


data.groupby('Weather Condition').mean()


# # Q12. What is the minimum and maximum value of each column againts eath weather condition ?

# In[49]:


data.head(2)


# In[50]:


data.groupby('Weather Condition').min()


# In[51]:


data.groupby('Weather Condition').max()


# # Q13. Show all the records where weather condition fog 

# In[52]:


data[data['Weather Condition'] == 'Fog']


# # Q14. Find all instance when weather is clear or visibility is above 40

# In[55]:


data[(data['Weather Condition'] == 'Clear')| (data['Visibility_km']>40)].head(50)


# # Q15. Find all instances when :
# A. Weather is clear and relative humidity is greater than 50 
# 
# or
# 
# B. Visibility is 50

# In[56]:


data.head(2)


# In[58]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km']>40)]

