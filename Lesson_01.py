#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy.stats
import pandas as pd


# In[2]:


import matplotlib
import matplotlib.pyplot as pp

from IPython import display
from ipywidgets import interact, widgets

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import re
import mailbox
import csv


# In[4]:


gapminder = pd.read_csv('C:/Users/99810471/Desktop/dados/gapminder.csv')


# In[6]:


gapminder.info()


# In[7]:


gapminder.loc[0:200:20]


# In[8]:


gapminder[gapminder.year == 1965].plot.scatter('babies_per_woman', 'age5_surviving')


# In[15]:


def plotyear(year):
    data = gapminder[gapminder.year == year]
    area = 5e-6 * data.population
    colors = data.region.map({'Africa': 'skyblue', 'Europe': 'gold', 'America': 'palegreen', 'Asia': 'coral'})
    
    data.plot.scatter('babies_per_woman', 'age5_surviving',
                      s=area,c=colors,
                     linewidths=1,edgecolors='k',
                     figsize=(12,9))
    pp.axis(ymin=50, ymax=105, xmin=0, xmax=8)
    pp.xlabel('babies per woman')
    pp.ylabel('% children alive at 5')


# In[16]:


plotyear(1965)


# In[17]:


interact(plotyear,year=widgets.IntSlider(min=1950,max=2015,step=1,value=1965))


# In[ ]:




