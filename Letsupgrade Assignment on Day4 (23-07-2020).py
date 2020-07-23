#!/usr/bin/env python
# coding: utf-8

# In[3]:


#initializing string
test_str="what we think we become; we are Python programmers"

#initializing substring
test_sub="we"
#printing original string
print("The original string is : " + test_str)

#printing substring
print("The substring to find :" + test_sub)

# using list comprehension + startwith()
# All occurrences of substring in string

res=[i for i in range(len(test_str)) if test_str.startswith(test_sub,i)]

# printing result
print("The start indices of the substrings are: "+str(res))


# In[5]:


str = "THIS is string example....wow!!!"; 
print (str.islower())


# In[7]:


str = "this is string example....wow!!!";
print (str.islower())


# In[9]:


s = 'this is good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')
  
s = 'this is Good'
if s.islower() == True:
  print('Does not contain uppercase letter.')
else:
  print('Contains uppercase letter.')


# In[10]:


# Case 1: Every character in a string is lowercase also contains whitespaces/numbers/special characters
str_name = "welcome python user"
print(str_name.islower())


# In[11]:


str_name = "welcome 2019"
print(str_name.islower())


# In[12]:


str_name = "welcome @ 2020"
print(str_name.islower())


# In[14]:


#Case 2: String contains only numbers or special characters
str_name = "2020"
print(str_name.islower())   


# In[15]:


str_name = "@$&"
print(str_name.islower())


# In[17]:


#Case 3: Only the first character of every word is uppercase, also contains whitespaces/numbers/special characters
str_name = "Welcome"
print(str_name.islower())


# In[21]:


#Case 5: String is Empty
str_name = ' '
print(str_name.islower())


# In[ ]:




