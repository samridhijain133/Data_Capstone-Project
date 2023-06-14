#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


# In[3]:


df=pd.read_csv('911.csv')


# In[4]:


df.info()


# In[5]:


df.head()


# In[6]:


df['zip'].value_counts().head(5)


# In[7]:


df['twp'].value_counts().head(5)


# In[8]:


df['title'].nunique()


# In[9]:


def first_letter(stringg):
    return stringg.split(':')[0]
df['title'].apply(first_letter)


# In[10]:


df['reasons']=df['title'].apply(first_letter)


# In[11]:


df['reasons'].value_counts()


# In[12]:


sns.countplot(x=df['reasons'],data=df)


# In[13]:


type(df['timeStamp'].iloc[0])


# In[14]:


df['zip'].value_counts().head(5)


# In[15]:


df['timeStamp']=pd.to_datetime(df['timeStamp'])


# In[16]:


type(df['timeStamp'].iloc[0])


# In[17]:


time=df['timeStamp'].iloc[0]


# In[18]:


time.dayofweek


# In[19]:


df['Hour']=df['timeStamp'].apply(lambda time:time.hour)


# In[20]:


df['Month']=df['timeStamp'].apply(lambda time:time.month
                                 )


# In[21]:


df['Month']


# In[22]:


df['DayOfWeek']=df['timeStamp'].apply(lambda time:time.dayofweek)


# In[23]:


df.head()


# In[158]:


NameOfDay=dict({0:'Mon',1:'Tue',2:'Wed',3:'Fri',4:'Thu',5:'Sat',6:'Sun'})


# In[24]:


df['DayOfWeek']=df['DayOfWeek'].map(NameOfDay)


# In[25]:


df.head()


# In[26]:


sns.countplot(x='DayOfWeek',hue='reasons',data=df)


# In[27]:


sns.countplot(x='Month',hue='reasons',data=df)


# In[28]:


byMonth=df.groupby(by='Month').count()

byMonth.head()


# In[29]:


byMonth['lng'].plot()


# In[30]:


sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# In[31]:


df['Date']=df['timeStamp'].apply(lambda time:time.date())


# In[32]:


df.head()


# In[33]:


tzuyu=df.groupby(by='Date').count()


# In[34]:


tzuyu['lat'].plot()


# In[35]:


df[df['reasons']=='Traffic'].groupby('Date').count()['lat'].plot()


# In[36]:


df[df['reasons']=='EMS'].groupby('Date').count()['lat'].plot()


# In[37]:


df[df['reasons']=='Fire'].groupby('Date').count()['lat'].plot()


# In[38]:


sf=df.groupby(by=['DayOfWeek','Hour']).count()['reasons'].unstack()


# In[39]:


sf


# In[40]:


sns.heatmap(sf)


# In[41]:


sns.clustermap(sf)


# In[42]:


pf=df.groupby(by=['DayOfWeek','Month']).count()['reasons'].unstack()


# In[43]:


pf


# In[44]:


sns.heatmap(pf)


# In[45]:


sns.clustermap(pf)


# In[ ]:




