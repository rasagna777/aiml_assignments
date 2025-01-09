#!/usr/bin/env python
# coding: utf-8

# In[1]:


greet = lambda name : print(f"Good Morning {name}!")


# In[3]:


greet("Rasagna")


# In[5]:


product = lambda x,y,z : x*y*z
product(2, 3, 4)


# In[7]:


even = lambda L : [x for x in L if x%2 == 0]


# In[9]:


my_list = [100,3,9,38,43,56,20]
even(my_list)


# In[ ]:




