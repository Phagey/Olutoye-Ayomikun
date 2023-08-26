#!/usr/bin/env python
# coding: utf-8

# #

# #### In this project, I will work with ufo sightings data.
# - The data includes various data points about individual ufo sightings
# - Data File(s): ufo-sightings.csv

# In[21]:


###########################################################
### EXECUTE THIS CELL BEFORE YOU TO TEST YOUR SOLUTIONS ###
###########################################################

import imp, os, sys
sol = imp.load_compiled("solutions", "./solutions.py")
sol.get_solutions("ufo-sightings.csv")
from nose.tools import assert_equal


# In[3]:


'''
1. I will import the csv module. Load and read the UFO sightings data set, from the ufo-sightings.csv file, 
into a DictReader inside a with statement.  Assume the data file is in the same directory as the code. 

Print the field names of the data set. Iterate over the reader to put the data into a list name "ufosightings".

'''

import csv
filepath = "ufo-sightings.csv"
ufosightings = [] 


with open(filepath, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    field_names = csv_reader.fieldnames
    print("Field Names:", field_names)

    for row in csv_reader:
        ufosightings.append(row)

print("ufoSightings Data:")
for i, sighting in enumerate(ufosightings[:5], start=1):
    print(f"Row {i}: {sighting}")


# In[4]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(ufosightings, sol.ufosightings)
print("Success!")


# In[6]:


'''
2. YTo find how many sightings were there in total? I will put the count in "ufosightings_count" and print the result.
'''

ufosightings_count = len(ufosightings)
print("Total UFO Sightings:", ufosightings_count)


assert_equal(ufosightings, sol.ufosightings)
print("Success!")


# In[7]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(ufosightings_count, sol.ufosightings_count)
print("Success!")


# In[9]:


'''
3. To find how many sightings were there in the US?  I will put the US sightings in "sightings_us" and print.


'''


us_sightings_count = 0

sightings_us = []

for sighting in ufosightings:
    if sighting['country'].lower() == 'us':
        us_sightings_count += 1
        sightings_us.append(sighting)

print("Total UFO Sightings in the US:", us_sightings_count)

print("US UFO Sightings:")
for i, sighting in enumerate(sightings_us[:5], start=1):
    print(f"US Sighting {i}: {sighting}")


# In[10]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(sightings_us,  sol.sightings_us)
print("Success!")


# In[12]:


'''
4. To find the "fireball" sighting(s) that lasted more than ten seconds in US. 
Print the the datetime and state of each.  Put the data in "fball" and print the result.

Note: Consider only the US sightings stored in "sightings_us".

- Cast the duration in seconds to a float (decimal). 
- Check if duration is greater than 10. 
- Check if the shape is "fireball".

'''

fball = []

for sighting in sightings_us:
    shape = sighting.get('shape', '').lower()  # Convert to lowercase
    duration = float(sighting.get('duration(seconds)', '0'))
    
    if shape == 'fireball' and duration > 10.0:
        fball.append({
            'datetime': sighting['datetime'],
            'state': sighting['state']
        })

print("Fireball Sightings Lasting More Than 10 Seconds:")
for i, sighting in enumerate(fball, start=1):
    print(f"Fireball Sighting {i}: Datetime: {sighting['datetime']}, State: {sighting['state']}")









# In[13]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(fball, sol.fball)
print("Success!")


# In[15]:


'''
5. To sort the above list by duration. What was the datetime and duration of the longest sighting?  
Put the sorted list in "fballsorted" and print the result.

- Cast the duration in seconds to a float (decimal). 
- Sort in reverse order.

'''

fballsorted = sorted(fball, key=lambda x: float(x.get('duration(seconds)', '0')), reverse=True)


print("Sorted Fireball Sightings:")
for i, sighting in enumerate(fballsorted, start=1):
    print(f"Fireball Sighting {i}: Datetime: {sighting['datetime']}, Duration: {sighting.get('duration(seconds)', '0')} seconds")

if fballsorted:
    longest_sighting = fballsorted[0]
    print("\nLongest Sighting:")
    print(f"Datetime: {longest_sighting['datetime']}, Duration: {longest_sighting.get('duration(seconds)', '0')} seconds")
else:
    print("\nNo fireball sightings found.")


# In[16]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(fballsorted, sol.fballsorted)
print("Success!")


# In[27]:


'''
6. To find what state had the longest lasting "fireball"?   Put the state in "state" and print the result.

- Check if the shape is "fireball".
- Cast the duration in seconds to a float (decimal).
- Get the record with the largest (max) duration in seconds.
- Get the state for the record.

'''

max_duration = 0.0
state = None


for sighting in fballsorted:
    shape = sighting.get('shape', '').lower() 
    duration = float(sighting.get('duration(seconds)', '0'))
    
   
    if shape == 'fireball' and duration > max_duration:
        max_duration = duration
        state = sighting['state']

if state:
    print("State with Longest Lasting Fireball:", state)
else:
    print("No fireball sightings found.")


# In[ ]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(state, sol.state)
print("Success!")


# In[20]:


'''
7. Let's assume that any sighting (of any shape) of 0 seconds is insignificant. 
I want to write code to filter out these extraneous records and get the shortest sighting overall now.  
Put the minimum duration in "min_duration" and print the result.  
Use ufosightings
Note: Consider all sightings stored in "ufosightings".

'''
min_duration = float('inf')  


for sighting in ufosightings:
    duration = float(sighting.get('duration(seconds)', '0.001'))
    
  
    if duration > 0:
        min_duration = min(min_duration, duration)

if min_duration != float('inf'):
    print("Minimum Duration:", min_duration, "seconds")
else:
    print("No significant sightings found.")


# In[19]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(min_duration, sol.min_duration)
print("Success!")


# In[22]:


'''
8. To find what are the top 3 shapes sighted, and how many sightings were there for each? 

Note: Consider all sightings stored in "ufosightings".

- Create a new list "sightings_shapes" containing values from the "shape" column in ufosightings.  
- Create a new dictionary "count" with values of that column as keys and the counts as values.
- Get a list of the dictionary keys and values using the items() method.  This will return a list of key:value pairs.
Sort the list of key:value pairs in reverse order, from greatest (most sightings) to least.

Get the top 3 and store in "top3shapes".  Print the result.

'''

sightings_shapes = [sighting['shape'] for sighting in ufosightings]

count = {}
for shape in sightings_shapes:
    count[shape] = count.get(shape, 0) + 1

sorted_counts = sorted(count.items(), key=lambda x: x[1], reverse=True)

top3shapes = sorted_counts[:3]

print("Top 3 Shapes Sightings:")
for shape, count in top3shapes:
    print(f"Shape: {shape}, Count: {count}")


# In[23]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(sightings_shapes, sol.sightings_shapes)
print("Success!")


# In[24]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(count, sol.count)
print("Success!")


# In[25]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(top3shapes, sol.top3shapes)
print("Success!")


# In[ ]:




