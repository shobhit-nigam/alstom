#!/usr/bin/env python
# coding: utf-8

# In[1]:


avengers = ['ironman', 'captain', 'hulk', 'thor']


# In[2]:


type(avengers)


# In[3]:


avengers = ('ironman', 'captain', 'hulk', 'thor')


# In[4]:


type(avengers)


# In[5]:


print(avengers[1])


# In[6]:


print(avengers[1:3])


# In[7]:


avengers.sort()


# In[8]:


avengers.count('hulk')


# In[9]:


avengers = ('ironman', 'captain', 'hulk', ['antman', 'wasp'], 'thor')


# In[10]:


avengers[3] = "nigam"


# In[11]:


avengers[3][0] = "nigam"


# In[12]:


print(avengers)


# In[13]:


avengers[3][0][0] = "N"


# In[14]:


#  examples = coordinates of a location
#           = rows & columns of excel sheet or database


# In[15]:


seta = {'orange', 'banana', 'apple', 'mango', 'banana', 'kiwi'}
setb = {'pear', 'apple', 'grape'}


# In[16]:


print(seta)


# In[17]:


print(setb)


# In[18]:


print(seta | setb)


# In[19]:


print(seta & setb)


# In[20]:


seta.add('watermelon')


# In[21]:


print(seta)


# In[22]:


setc = {'kiwi', ['banana', 'orange'], 'apple'}


# In[23]:


setc = {'kiwi', ('banana', 'orange'), 'apple'}


# In[36]:


dicta = {'ironman':'suit', 'hawkeye':'arrows', 'thor':'hammer'}


# In[25]:


#   key_value pair


# In[27]:


dicta['ironman']


# In[28]:


print(dicta['thor'])


# In[29]:


dicta['ironman'] = 'SUIT'


# In[30]:


print(dicta)


# In[37]:


dicta['captain'] = ['hammer', 'shield']


# In[32]:


print(dicta)


# In[33]:


dicta = {'dc':['batman', 'aquaman'], 'marvel':dicta}


# In[34]:


print(dicta)


# In[35]:


len(dicta)


# In[38]:


dictb = {'dc':['batman', 'aquaman'], 'marvel':dicta}


# In[39]:


print(dicta)


# In[40]:


print(dictb)


# In[41]:


print(dictb['marvel']['captain'][0][0])


# In[42]:


#  dictb['marvel']['captain'][0] = 


# In[ ]:




