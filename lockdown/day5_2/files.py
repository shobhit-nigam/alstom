#!/usr/bin/env python
# coding: utf-8

# In[1]:


fa = open("books.txt", "r")


# In[2]:


#   io_wrappers


# In[3]:


import os


# In[4]:


os.listdir()


# In[5]:


stra = fa.read(4)


# In[6]:


print(stra)


# In[8]:


pass


# In[9]:


strb = fa.read(17)


# In[10]:


print(strb)


# In[11]:


strb


# In[12]:


fa.tell()


# In[13]:


fa.seek(0)


# In[14]:


strc = fa.readline()


# In[15]:


print(strc)


# In[16]:


strc


# In[17]:


fa.close()


# In[18]:


fa.read(3)


# In[19]:


fa.closed


# In[20]:


fa = open("books.txt", "r")


# In[21]:


fa.readable()


# In[22]:


fa.writable()


# In[23]:


strd = fa.read()


# In[24]:


print(strd)


# In[25]:


listd = strd.split()   # space, newline, tab etc...


# In[26]:


listd


# In[27]:


len(strd.split())


# In[28]:


len(strd.splitlines())


# In[29]:


fa.close()


# In[30]:


fb = open("library.txt", "w")   #w is dangerous


# In[31]:


listd = strd.splitlines()


# In[32]:


listd.sort()


# In[34]:


listd


# In[35]:


fb.write("hey, books sorted alphabetically\n")


# In[36]:


fb.close()


# In[38]:


fb.closed


# In[39]:


fb = open("library.txt", "a")


# In[40]:


for line in listd:
    fb.write(line)
    fb.write("\n")


# In[41]:


fb.close()


# In[43]:


print(strd)


# In[44]:


fr = open('registration.txt', 'r')


# In[45]:


strr = fr.read()


# In[46]:


fr.seek(0)


# In[47]:


strs = fr.readlines()


# In[48]:


type(strs)


# In[50]:


len(strs)


# In[51]:


strs = strr.splitlines()


# In[55]:


names = []
for line in strs:
    temp = line.split()
    names.append(temp[0])


# In[56]:


names


# In[59]:


email = []
for line in strs:
    temp = line.split()
    email.append(temp[-1])


# In[60]:


email


# In[61]:


fr.close()


# In[62]:


fr = open('registration.txt', 'r')
strr = fr.read()
strs = strr.splitlines()

email = []
for line in strs:
    temp = line.split()
    email.append(temp[-1])


# In[63]:


#{'alstomgroup.com': 28, 'gmail.com': 2, 'ftdinfocom.com':1}


# In[64]:


dicta = {}
temp = []

for mail in email:
    temp = mail.split('@')
    if temp[1] in dicta:
        dicta[temp[1]] = dicta[temp[1]] + 1
    else:
        dicta[temp[1]] = 1


# In[65]:


dicta


# In[67]:


fr = open('registration.txt', 'r')
strr = fr.read()
strs = strr.splitlines()

email = []
for line in strs:
    temp = line.split()
    email.append(temp[-1])


# In[68]:


email


# In[70]:


dicta = {}
temp = []
import time

for mail in email:
    temp = mail.split('@')
    if temp[1] in dicta:
        dicta[temp[1]] = dicta[temp[1]] + 1
    else:
        dicta[temp[1]] = 1
    time.sleep(1)
    print(dicta)


# In[71]:


fr.close()


# In[76]:


fr = open('registration.txt', 'r')
strr = fr.read()
strs = strr.splitlines()

for line in strs:
    name = line.split()
    for n in name[0:-1]:
        print(n, end=' ')
    print()


# In[78]:


#   find("numbers.txt", 2, "avg")
import os


# In[79]:


def find(file, col, action):
    if (~os.path.exists(file)):
        print("file", file, "does not exist")


# In[80]:


find("random.txt", 2, "avg")


# In[90]:


def find(file, col, action):
    if (not os.path.exists(file)):
        print("file", file, "does not exist")
        return
    temp = []
    data = []
    d = []
    fa = open(file, "r")
    stra = fa.read()
    temp = stra.splitlines()
    for line in temp:
        d = line.split()
        data.append(int(d[col-1]))
    print(data)
    if action == "avg":
        return (sum(data)/len(data))
    elif action == "sum":
        return (sum(data))
    elif action == "min":
        return min(data)
    elif action == "max":
        return max(data)
    else:
        print("giving you the average, as could not understand your need")
        return (sum(data)/len(data))


# In[91]:


n = find("numbers.txt", 2, "avg")


# In[92]:


n


# In[93]:


n = find("numbers.txt", 1, "sum")


# In[94]:


n


# In[ ]:




