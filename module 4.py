#!/usr/bin/env python
# coding: utf-8

# ## Module 4
# 
# #### In this assignment, you will continue working on the movie data from IMDB.
# - The data includes movies and ratings from the IMDB website
# - Data File(s): imdb.xlsx
# 
# #### Data file contains 3 sheets:
# - “imdb”: contains records of movies and ratings scraped from IMDB website
# - “countries”: contains the country (of origin) names
# - “directors”: contains the director names
# 
# We have loaded and joined the data as "df" for you. Follow the instructions and finish the rest part.

# In[19]:


###########################################################
### EXECUTE THIS CELL BEFORE YOU TO TEST YOUR SOLUTIONS ###
###########################################################

import imp, os, sys
sol = imp.load_compiled("solutions", "./solutions.py")
sol.get_solutions("imdb.xlsx")
from nose.tools import assert_equal
from pandas.util.testing import assert_frame_equal, assert_series_equal


# In[1]:


# Loading the data
import pandas as pd

xls = pd.ExcelFile('imdb.xlsx')
df = xls.parse('imdb')
df_directors = xls.parse('directors')
df_countries = xls.parse('countries')

df = pd.merge(left=df, right=df_countries, 
              how='inner', left_on='country_id', 
              right_on='id')

df = pd.merge(left=df, right=df_directors, 
              how='inner', left_on='director_id', 
              right_on='id')

print("Finished.")


# In[3]:


""" Q1: 
Get the summary statistics for imdb_score and gross, then use the describe() function to summarize this visually. Save the
result in a variable called score_gross_description and print it.
"""

# your code here

score_gross_description = df[['imdb_score', 'gross']].describe()

print(score_gross_description)


# In[4]:


assert_frame_equal(score_gross_description, sol.score_gross_description)
print("Success!")


# In[6]:


"""Q2:
What is the average rating of the director Christopher Nolan's movies? Save this value in a variable called nolan_mean and 
print.
"""

# your code here


nolan_movies = df[df['director_name'] == 'Christopher Nolan']


nolan_mean = nolan_movies['imdb_score'].mean()

print("Average rating of Christopher Nolan's movies:", nolan_mean)


# In[7]:


assert_equal(nolan_mean, sol.nolan_mean)


# ##### """Q3: 
# Create a series called 'directors' that contains each director's name and his or her average rating.  Print out the type of your variable.
# Use the 'directors' series to find the average rating for Steven Spielberg.  Print the value.
# """
# 
# # your code here
# 
# directors = df.groupby('director_name')['imdb_score'].mean()
# 
# print("Type of the 'directors' Series:", type(directors))
# 
# print(directors)
# 
# spielberg_avg_rating = directors.get('Steven Spielberg')
# 
# print("Average rating for Steven Spielberg:", spielberg_avg_rating)
# 
# 

# In[11]:


assert_series_equal(directors, sol.directors)
print("Success!")


# In[13]:


"""Q4:
Select the non-USA movies made after 1960 by Hayao Miyazaki.
Save the result in a DataFrame called 'miyazaki', then print it.

Here are the steps:
1. Query the data ('df' DataFrame) based on the following conditions:
- Non-USA movies (country_id != 1)
- Movies made after 1960 (title_year > 1960)
- Movies made by director Hayao Miyazaki (director_id == 46)
2. Save the filtered data in a DataFrame called 'miyazaki' and print it

"""

# your code here

miyazaki = df[(df['country_id'] != 1) & (df['title_year'] > 1960) & (df['director_id'] == 46)]

print(miyazaki)


# In[14]:


assert_frame_equal(miyazaki, sol.miyazaki)
print("Success!")


# In[17]:


"""Q5: 
Create a Pivot Table that shows the median rating for each director, grouped by their respective countries. Name your variable
'pivot_agg'
"""

# your code here

pivot_agg = df.pivot_table(index='country_id', columns='director_id', values='imdb_score', aggfunc='median')

print(pivot_agg)


# In[18]:


assert_frame_equal(pivot_agg, sol.pivot_agg)
print("Success!")


# In[20]:


"""Q6:
How long did the movie Gladiator aim to keep your attention? Save the series with this information
in a variable called 'gladiator_duration', then print it.
"""

# your code here

gladiator_movie = df[df['movie_title'] == 'Gladiator']

gladiator_duration = gladiator_movie['duration']

print("Duration of the movie Gladiator:", gladiator_duration)


# In[21]:


assert_series_equal(gladiator_duration, sol.gladiator_duration)
print("Success!")


# In[ ]:




