#!/usr/bin/env python
# coding: utf-8

# In[42]:


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


china1965 = pd.read_csv('C:/Users/99810471/Desktop/dados/income-1965-china.csv')
china2015 = pd.read_csv('C:/Users/99810471/Desktop/dados/income-1965-usa.csv')
usa1965 = pd.read_csv('C:/Users/99810471/Desktop/dados/income-2015-china.csv')
usa1965 = pd.read_csv('C:/Users/99810471/Desktop/dados/income-2015-usa.csv')


# In[5]:


china1965.income.plot(kind='box')


# In[6]:


gapminder = pd.read_csv('C:/Users/99810471/Desktop/dados/gapminder.csv')


# In[8]:


gapminder.info()


# In[9]:


italy = gapminder.query('country == "Italy"')


# In[10]:


italy.head()


# In[11]:


italy.plot.scatter("year", "population")


# In[14]:


gapminder.query('country == "India"').plot.scatter("year", "population")


# In[16]:


italy.plot.scatter("year", "gdp_per_day", logy=True)


# In[17]:


italy.plot.scatter("gdp_per_day", "life_expectancy", logx=True)


# In[19]:


size = np.where(italy.year % 10 == 0,30,2)

italy.plot.scatter("gdp_per_day", "life_expectancy", logx=True, s=size)


# In[23]:


data = gapminder.query('(country == "Italy") or (country == "United States")')
                       
size = np.where(data.year % 10 == 0,30,2)
color = np.where(data.country == 'Italy', 'blue', 'orange')

data.plot.scatter("gdp_per_day", "life_expectancy", logx=True, s=size, c=color)


# In[25]:


data = gapminder.query('(country == "China") or (country == "United States")')
                       
size = np.where(data.year % 10 == 0,30,2)
color = np.where(data.country == 'China', 'red', 'orange')

ax = data.plot.scatter("gdp_per_day", "life_expectancy", logx=True, s=size, c=color)

data[data.country == 'China'].plot.line(x="gdp_per_day", y="life_expectancy", ax=ax)


# In[26]:


gapminder = pd.read_csv('C:/Users/99810471/Desktop/dados/gapminder.csv')


# In[27]:


def plotyear(year):
    data = gapminder[gapminder.year == year]
    
    data.plot.scatter("gdp_per_day", "life_expectancy", logx=True)
    
plotyear(1965)


# In[31]:


def plotyear(year):
    data = gapminder[gapminder.year == year].sort_values('population', ascending=False)
    area = 5e-6 * data.population
    color = data.age5_surviving
    
    data.plot.scatter("gdp_per_day", "life_expectancy", logx=True, 
                      s=area, c=color,
                      colormap=matplotlib.cm.get_cmap('Purples_r'), vmin=55, vmax=100,
                      linewidths=1, edgecolors='k')
    
plotyear(1965)


# In[34]:


def plotyear(year):
    data = gapminder[gapminder.year == year].sort_values('population', ascending=False)
    area = 5e-6 * data.population
    color = data.age5_surviving
    edgecolor = data.region.map({'Africa': 'skyblue', 'Europe': 'gold', 'America': 'palegreen', 'Asia': 'coral'})
    
    data.plot.scatter("gdp_per_day", "life_expectancy", logx=True, 
                      s=area, c=color,
                      colormap=matplotlib.cm.get_cmap('Purples_r'), vmin=55, vmax=100,
                      linewidths=1, edgecolors=edgecolor, sharex=False,
                      figsize=(10,6.5))
    
    pp.axis(xmin=1, xmax=500, ymin=30, ymax=100)
    
plotyear(1965)


# In[35]:


interact(plotyear,year=range(1965, 2016,10))


# In[36]:


gapminder[gapminder.year == 2015].population.sum()


# In[37]:


gapminder[gapminder.year == 2015].groupby('region').population.sum()


# In[38]:


def plotyear(year):
    data = gapminder[gapminder.year == year].sort_values('population', ascending=False)
    area = 5e-6 * data.population
    color = data.age5_surviving
    edgecolor = data.region.map({'Africa': 'skyblue', 'Europe': 'gold', 'America': 'palegreen', 'Asia': 'coral'})
    
    data.plot.scatter("gdp_per_day", "life_expectancy", logx=True, 
                      s=area, c=color,
                      colormap=matplotlib.cm.get_cmap('Purples_r'), vmin=55, vmax=100,
                      linewidths=1, edgecolors=edgecolor, sharex=False,
                      figsize=(10,6.5))
    
    for level in [4, 16,64]:
        pp.axvline(level, linestyle=':', color='k')
    
    pp.axis(xmin=1, xmax=500, ymin=30, ymax=100)
    
plotyear(1965)


# In[44]:


def plotyear(year):
    data = gapminder[gapminder.year == year].sort_values('population', ascending=False)
    area = 5e-6 * data.population
    color = data.age5_surviving
    edgecolor = data.region.map({'Africa': 'skyblue', 'Europe': 'gold', 'America': 'palegreen', 'Asia': 'coral'})
    
    data.plot.scatter("gdp_per_day", "life_expectancy", logx=True, 
                      s=area, c=color,
                      colormap=matplotlib.cm.get_cmap('Purples_r'), vmin=55, vmax=100,
                      linewidths=1, edgecolors=edgecolor, sharex=False,
                      figsize=(10,6.5))
    
    for level in [4, 16,64]:
        pp.axvline(level, linestyle=':', color='k')
    
    pp.axis(xmin=1, xmax=500, ymin=30, ymax=100)
    
plotyear(2015)


# In[ ]:





# In[ ]:




