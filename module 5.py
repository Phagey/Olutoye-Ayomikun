#!/usr/bin/env python
# coding: utf-8

# ## Module 5
# 
# In this assignment, you are going to work on Histograms and Scatterplots.
# 
# We have preprocessed the data as "df" for you. 
# 
# Follow the instructions and finish the rest part.

# In[1]:


get_ipython().run_cell_magic('capture', '', '###########################################################\n### EXECUTE THIS CELL BEFORE YOU TO TEST YOUR SOLUTIONS ###\n###########################################################\nimport imp, os, sys\nsol = imp.load_compiled("solutions", "./solutions.py")\nsol.get_solutions("imdb.xlsx")\nfrom nose.tools import assert_equal\nfrom pandas.util.testing import assert_frame_equal, assert_series_equal')


# In[2]:


# Loading the data
import pandas as pd
import numpy as np

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


df


# In[4]:


"""Q1: 
Is how much a movie makes indicative of how good it is?
Make a simple scatter plot comparing gross to imdb_score for movies during or after 2000 (title_year >= 2000) and before 2000 (title_year < 2000).
It may be useful to scale the x axis demarking gross. (Hint: Divide the gross amount by 1,000,000.)
Remember to put a legend indicating which color corresponds to which years.
What is your verdict?

Save your plot in a variable called plt1, and your dataframes in variables called df_after_2000 and df_before_2000
"""

import matplotlib.pyplot as plt1

# your code here
import matplotlib.pyplot as plt1
# Create dataframes for movies after and before 2000
df_after_2000 = df[df['title_year'] >= 2000]
df_before_2000 = df [df['title_year'] < 2000]

# Divide the gross amount by 1,000,000
df_after_2000.loc[:, 'gross'] = (df_after_2000['gross'] / 1000000).astype(int)
df_before_2000.loc[:,'gross'] = (df_before_2000['gross'] / 1000000).astype(int)

# Create scatter plot
plt1.scatter(df_after_2000['gross'], df_after_2000['imdb_score'], color='blue', label='After 2000') 
plt1.scatter(df_before_2000['gross'], df_before_2000['imdb_score'], color='red', label='Before 2000')

# Set labels and legend
plt1.xlabel ('Gross (in millions)')
plt1.ylabel ('IMDb Score')
plt1.legend ()

# Set the y-axis to a logarithmic scale
plt1.yscale('log' )

# Set title
plt1. title('Scatter Plot of Gross vs IMDb Score')

plt1.show()

# Print your verdict
print("My verdict: There doesn't seem to be a strong correlation between gross and IMDb score.")

sol.df_before_2000.loc[:,'gross'] = (sol.df_before_2000['gross'] / 1000000). astype (int)
sol.df_after_2000.loc[:,'gross'] = (sol.df_after_2000['gross'] / 1000000). astype (int)


# In[5]:


assert_frame_equal(df_before_2000, sol.df_before_2000)
assert_frame_equal(df_after_2000, sol.df_after_2000)
np.testing.assert_array_equal(plt1, sol.plt1)
print("Success!")


# In[6]:


"""Q2: 
Using numpy and pyplot, make an overlapping histogram that shows the score distribution vs. count of R-Rated movies and PG-13 ones.
Describe your plot. 

Save your plot in a variable called plt2, and your dataframes in variables called df_R and df_PG13
"""

import matplotlib.pyplot as plt2

# your code here

# Separate R-Rated and PG-13 movies
df_R = df[df['content_rating'] == 'R']
df_PG13 = df[df['content_rating'] == 'PG-13']

df_R['gross'] = df_R['gross'].astype(int)
df_PG13['gross'] = df_PG13['gross'].astype(int)

# Create histograms
plt2.hist(df_R['imdb_score'], alpha=0.7, label='R-Rated', bins=20)
plt2.hist(df_PG13['imdb_score'], alpha=0.7, label='PG-13', bins=20)

# Add labels and legend
plt2.xlabel('IMDb Score')
plt2.ylabel('Count')
plt2.legend()

# Set title
plt2.title('Score Distribution of R-Rated vs PG-13 Movies')

# Show the plot
plt2.show()

# Save the plot in a variable
#plt2 = plt


plt2.show()


sol.df_R.loc[:,'gross'] = (sol.df_R['gross'])
sol.df_PG13.loc[:,'gross'] = (sol.df_PG13['gross'])


# In[7]:


assert_frame_equal(df_R, sol.df_R)
assert_frame_equal(df_PG13, sol.df_PG13)
np.testing.assert_array_equal(plt2, sol.plt2)
print("Success!")


# In[ ]:




