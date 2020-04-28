#!/usr/bin/env python
# coding: utf-8

# In[1]:


#   lists


# In[2]:


avengers = ['ironman', 'captain', 'hulk', 'thor']


# In[3]:


print(avengers[0])


# In[4]:


print(len(avengers))


# In[5]:


print(avengers[-2]) 


# In[6]:


print(avengers[0:2])


# In[7]:


lista = [5, 8, 1, 28, 5, 6]


# In[8]:


listb = [7, 9, 3, 2, 1]


# In[9]:


print(lista)


# In[10]:


listc = [3, 6.7, "hi", lista, 23]


# In[11]:


print(listc[1])


# In[12]:


print(listc[2])


# In[13]:


print(listc[2][0])


# In[14]:


print(lista)


# In[15]:


listc = [3, 6.7, "hi", lista, 23]


# In[16]:


print(listc)


# In[17]:


print(listc[3][3])


# In[18]:


avengers = ['ironman', 'captain', 'hulk', 'thor']


# In[19]:


marvel = ['woverine', 'magneto', avengers]


# In[20]:


print(marvel)


# In[21]:


len(marvel)


# In[22]:


print(marvel[2][2][1])


# In[23]:


avengers = ['ironman', 'captain', 'hulk', 'thor']


# In[24]:


hero1 = 'captain'


# In[25]:


print(id(avengers))


# In[26]:


print(id(hero1))


# In[27]:


print(id(avengers[1]))


# In[28]:


#   list


# In[29]:


avengers = ['ironman', 'captain', 'hulk', 'thor']


# In[30]:


avengers[1]


# In[31]:


avengers[1] = 'captain America'


# In[32]:


print(avengers)


# In[33]:


avengers.append('spiderman')


# In[34]:


print(avengers)


# In[35]:


avengers.remove('hulk') # removed by value


# In[36]:


print(avengers)


# In[37]:


avengers.pop(3)


# In[38]:


print(avengers)


# In[39]:


avengers.insert(2, 'black widow')


# In[40]:


print(avengers)


# In[41]:


print(avengers[-1])


# In[42]:


print(avengers)


# In[43]:


avengers.reverse()


# In[44]:


print(avengers)


# In[45]:


avengers.sort()


# In[46]:


print(avengers)


# In[47]:


avengers.sort(reverse=True)


# In[48]:


print(avengers)


# In[49]:


superhero = ['batman', 'wonderwoman', 'shaktiman']


# In[50]:


superhero.append(avengers)


# In[51]:


print(superhero)


# In[52]:


print(len(superhero))


# In[53]:


superhero.pop(-1)


# In[54]:


print(len(superhero))


# In[55]:


superhero.extend(avengers)


# In[56]:


print(superhero)


# In[57]:


print(len(superhero))


# In[58]:


superhero = ['batman', 'wonderwoman', 'shaktiman']
superhero.append(avengers)


# In[59]:


print(superhero[3][2])


# In[60]:


#   regular expressions


# In[63]:


superhero[3].count('ironman')


# In[62]:


print(superhero)


# In[64]:


sh = ['batman', 'wonderwoman', 'shaktiman', 'thor', 'ironman', 'captain America', 'black widow']


# In[65]:


print(sh)


# In[66]:


sh.index('thor')


# In[67]:


sh.index('panther')


# In[68]:


#  for


# In[70]:


print(avengers[3])


# In[71]:


listx = [5, 8, 12, 4, 9]


# In[72]:


listy = listx


# In[73]:


listx.remove(8)


# In[74]:


listx.sort()


# In[75]:


print(listx)


# In[76]:


print(listy)


# In[77]:


#   references of each other


# In[78]:


listx = [5, 8, 12, 4, 9]
listy = listx
listz = listx.copy()


# In[79]:


listx.sort()


# In[80]:


print("listx =", listx)
print("listy =", listy)
print("listz =", listz)


# In[81]:


listx.clear()


# In[82]:


print(listx)


# In[83]:


#   empty list


# In[84]:


len(listx)


# In[85]:


help(listz.remove)


# In[86]:


print(listy)
print(listz)


# In[87]:


listx = [5, 8, 12, 4, 9]
listx.remove(5)


# In[88]:


listx.sort(reverse=True)


# In[89]:


print(listx)


# In[90]:


print(sh)


# In[91]:


sh[1] = 'diana'


# In[92]:


print(sh)


# In[94]:


sh[1][0] = 'D'   #not possible cause strings are immutable


# In[ ]:




