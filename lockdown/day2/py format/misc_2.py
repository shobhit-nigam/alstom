#!/usr/bin/env python
# coding: utf-8

# In[1]:


stra = "earth"


# In[2]:


stra = "world"


# In[3]:


strb = "world"


# In[4]:


x = 30


# In[5]:


del x


# In[6]:


print(x)


# In[7]:


#    FYI


# In[8]:


stra = "earth"
strb = "world"


# In[9]:


print(id(stra))


# In[10]:


print(id(strb))


# In[11]:


strc = "earth"
print(id(strc))


# In[12]:


stra = "world"


# In[13]:


print(id(stra))


# In[15]:


stra = "hi" 
strb = "hi" 
stra = stra.upper() 
strc = "HI"


# In[16]:


print(id(stra))
print(id(strb))
print(id(strc))


# In[17]:


#   dont do this 
#   id(stra) == id(strb)


# In[18]:


vara = None 


# In[19]:


#     void


# In[20]:


print(vara)


# In[21]:


varb = 0 #integer with value zero


# In[22]:


vara = None # variable with no value 


# In[ ]:




