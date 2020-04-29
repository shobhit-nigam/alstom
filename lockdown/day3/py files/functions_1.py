#!/usr/bin/env python
# coding: utf-8

# In[1]:


def greet():
    print("hello")
    print("good day")


# In[2]:


greet()


# In[3]:


def funca(la, lb):
    lc = la+lb
    print(lc)


# In[4]:


funca(4, 6)


# In[5]:


x = 10


# In[6]:


x = "hi"


# In[7]:


def funca(la, lb, lc):
    ld = la+lb+lc
    print(ld)


# In[8]:


#    can't have multiple definitions of function
#    latest definition is applicable


# In[10]:


funca(7, 8, 12)


# In[11]:


def funca(la, lb, lc):
    ld = la+lb+lc
    print(ld)
def funca(la, lb):
    lc = la+lb
    print(lc)


# In[12]:


funca(5,6,7)


# In[13]:


funca = "hello"


# In[14]:


funca(4,5)


# In[15]:


def append_values(la, x, y, z):
    la.append(x)
    la.append(y)
    la.append(z)


# In[16]:


lista = [8, 1, 4, 6]


# In[17]:


append_values(lista, 8, 2, 4)


# In[18]:


print(lista)


# In[19]:


def append_values(la, x, y, z):
    la.append(x)
    la.append(y)
    la.append(z)
    return None


# In[20]:


lista = [8, 1, 4, 6]


# In[21]:


x = append_values(lista, 99, 88, 77)


# In[22]:


print(x)


# In[23]:


lista = [8, 1, 4, 6]
print(append_values(lista, 99, 88, 77))


# In[24]:


print(lista)


# In[25]:


#   not written return, it will return None


# In[26]:


def funca(la, lb):
    lc = la+lb
    print(lc)


# In[27]:


x = funca(4, 5)


# In[28]:


print(x)


# In[29]:


def funcc(la, lb):
    lc = la+lb
    return lc


# In[31]:


y = funcc(10, 100)


# In[32]:


print(y)


# In[33]:


def funcc(la, lb):
    lc = la+lb
    return 12, "hrx", 88.9


# In[34]:


a,b,c = funcc(3,4)


# In[35]:


a,b = funcc(3,4)


# In[36]:


a = funcc(3,4)


# In[37]:


print(a)


# In[38]:


b = 12, 13, 14


# In[39]:


print(b)


# In[40]:


a, b, c, = 12, 13, 14


# In[41]:


a = b = c = 14


# In[42]:


a = 12, 13, 14


# In[43]:


type(a)


# In[44]:


#    garbage collection is automatic in python


# In[45]:


#    CPython


# In[46]:


def funcx():
    #   do lots of things
    return 6, "hi", 2


# In[47]:


x, y, z = funcx()


# In[48]:


print(x)


# In[49]:


def funcx():
    #   do lots of things
    return 6


# In[50]:


x = funcx()


# In[51]:


print(x)


# In[53]:


def funcx():
    #   do lots of things
    pass


# In[54]:


x = funcx()


# In[55]:


#   return value is None


# In[56]:


print(x)


# In[ ]:




