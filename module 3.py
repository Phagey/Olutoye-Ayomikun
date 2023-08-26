#!/usr/bin/env python
# coding: utf-8

# ## 
# 
# #### In this project, I will continue working on the movie data from IMDB.
# - The data includes movies and ratings from the IMDB website
# - Data File(s): imdb.xlsx
# 
# #### Data file contains 3 sheets:
# - “imdb”: contains records of movies and ratings scraped from IMDB website
# - “countries”: contains the country (of origin) names
# - “directors”: contains the director names
# 
# I have loaded the data as "df" for you. 

# In[74]:


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

print("Data Loading Finished.")


# In[3]:


""" : 
To join three Dataframes: df, df_directors, and df_countries with an inner join.
Store the joined DataFrames in df.


"""

# my code here

df = df.merge(df_countries, how='inner', left_on='country_id', right_on='id')
df = df.merge(df_directors, how='inner', left_on='director_id', right_on='id')
print(df)

# After the join, the resulting Dataframe should have 12 columns.
df.shape


# In[4]:


assert_equal(df.shape, sol.df.shape)
print("Success!")


# In[6]:


""": 
To save the first ten rows of movie titles in a variable called first10, then print it
"""

# my code here

first10 = df['movie_title'][:10]
print(first10)


# In[7]:


assert_series_equal(first10, sol.first10)
print("Success!")


# In[11]:


""" : 
There's an extra character at the end of each movie title. 
I want to remove it from the data using str.replace.
And print the first ten rows of movie titles again. 
"""

# my code here

df['movie_title'] = df['movie_title'].str.replace('Ê', '')
print(df['movie_title'][:10])


# In[12]:


assert_frame_equal(df, sol.df)
print("Success!")


# In[14]:


""" :
Who is the director with the most movies? First get the number of movies per "director_name", then save the director's name
and counts a series of length 1 called "director_with_most"
"""

# my code here


director_counts = df['director_name'].value_counts()

director_with_most = director_counts.head(1)

print("Director with the most movies:")
print(director_with_most)


# In[15]:


assert_series_equal(director_with_most, sol.director_with_most)
print("Success!")


# In[47]:


"":
To save all of this director's movies and their ratings in a variable called all_movies_ratings, then print this variable.
(The director with the most movies you got from the last question.)
"""

# my code here

director_counts = df['director_name'].value_counts()


director_with_most = director_counts.idxmax()

all_movies_ratings = df[df['director_name'] == director_with_most][['movie_title', 'imdb_score']]

print("All Movies and Ratings for Director:", director_with_most)
print(all_movies_ratings)


# In[48]:


assert_frame_equal(all_movies_ratings, sol.all_movies_ratings)
print("Success!")


# In[76]:


""":
To recommend a **random** movie that has a rating of over 8.3. 
Store the random recommendation in a variable called "rand_goodmovie".
What is the title and imdb_score of your recommendation?
 
The steps:
1. Query the data ('df' DataFrame) for movies with a rating over 8.3 (imdb_score > 8.3)
2. Create a random integer index location to get a single movie recommendation
3. Save the random movie recommendation in a DataFrame called 'rand_goodmovie'
4. Save the title of the random movie recommendation in a variable "random_title" and print it
5. Save the imdb_score of the random movie recommendation in a variable "random_imdb_score" and print it

"""
# Do not modify this part, it's needed for grading
import random
random.seed(0)

# my code here


# Step 1: Query the data for movies with a rating over 8.3
high_rated_movies = df[df['imdb_score'] > 8.3]

# Step 2: Create a random integer index location
random_index = random.randint(0, len(high_rated_movies) - 1)

# Step 3: Save the random movie recommendation in a DataFrame
rand_goodmovie = high_rated_movies.iloc[random_index:random_index+1]

# Step 4: Save the title of the random movie recommendation in a variable
random_title = rand_goodmovie['movie_title'].values[0]
print("Random Movie Recommendation Title:", random_title)

# Step 5: Save the imdb score of the random movie recommendation in a variable
random_imdb_score = rand_goodmovie['imdb_score'].values[0]
print("Random Movie Recommendation IMDb Score:", random_imdb_score)


# In[77]:


from nose.tools import assert_in
assert_in(rand_goodmovie[["movie_title", "imdb_score"]].values, sol.possible_goodmovies[["movie_title", "imdb_score"]].values)
assert_equal(random_title.iloc[0], rand_goodmovie["movie_title"].iloc[0])
assert_equal(random_imdb_score.iloc[0], rand_goodmovie["imdb_score"].iloc[0])
print("Success!")


# In[ ]:




