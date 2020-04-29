#!/usr/bin/env python
# coding: utf-8

# In[1]:


place = "earth"


# In[2]:


i = 0


# In[4]:


while i<5 :
    print(place[i])
    i = i+1


# In[5]:


#   i += 1    i=i+1 


# In[6]:


print(i)


# In[8]:


i = 0
while i<5 :
    print(place[i])
    i = i+1
print("hi")


# In[9]:


varx = 10
vary = 20
varz = 30


# In[10]:


if varx<vary:
    print("hello")
    print("good day")
else:
    print("namaste")


# In[12]:


if varx>vary:
    print("hello")
    print("good day")
elif varx>vary and varx>varz:
    print("varx is the greatest")
elif varx<vary<varz:
    print("varz is greatest")
else:
    print("namaste")


# In[13]:


#   no switch case


# In[14]:


cities = ['bengaluru', 'hyderabad', 'mumbai', 'chennai']


# In[15]:


for c in :     #c=cities[0], c=cities[1], c=cities[2], c=cities[3]
    print(c)


# In[16]:


for c in place:
    print(c)


# In[17]:


type(c)


# In[18]:


for c in cities[0:3]:
    print(len(c), '\t', c)


# In[20]:


listx = []
place = "earth"
for c in place:        
    listx.append(c)


# In[21]:


print(listx)


# In[22]:


print(c)


# In[23]:


listy = list(place)


# In[24]:


print(listx)
print(listy)


# In[25]:


cities = ['bengaluru', 'hyderabad', 'mumbai', 'chennai', 'kochi']


# In[26]:


for val in cities:
    print(val)
    if val == 'mumbai':
        break


# In[29]:


cities2 = ['ahemdabad', 'kolkota', 'mumbai', 'delhi', 'kochi']


# In[30]:


for one in cities:
    for two in cities2:
        if one == two:
            print(one)


# In[31]:


list_common =[]


# In[32]:


for one in cities:
    for two in cities2:
        if one == two:
            list_common.append(one)


# In[33]:


print(list_common)


# In[34]:


list1=[] 
strb="earth"
 
for c in strb:
    print(list1.append(c), list1)


# In[36]:


for i in range(4):
    print("i =",i)


# In[37]:


for i in range(4, 9):        #upper range not included
    print("i =",i)


# In[38]:


for i in range(0, 14, 3):     #0,1,2,3,4,5,6,7,8,9,10,11,12,13
    print("i =", i)


# In[39]:


for i in range(2, 14, 2):     #0,1,2,3,4,5,6,7,8,9,10,11,12,13
    print("i =", i)


# In[40]:


cities = ['bengaluru', 'hyderabad', 'mumbai', 'chennai', 'kochi']


# In[41]:


for i in range(len(cities)):
    print("i =", i, "and cities[i] =", cities[i])


# In[43]:


for i in range(3):
    for j in range(3):
        print("i = ", i, " j = ", j)


# In[44]:


for i in range(3):
    for j in range(3):
        if i==j:
            print("tea break")
            break
        else:
            print("no tea break")


# In[45]:


"""for i in range(3):
    for j in range(3):
        if i==j:
            print("tea break")
            continue
        else:
            print("no tea break")
        print("coffee break")
    print("coffee break")"""


# In[46]:


#   enumerate()


# In[47]:


pass    #does nothing


# In[48]:


if varx > vary:
    print("x is great")
else:
    pass


# In[50]:


if varx > vary:
    print("x is great")
else:
    #  comments


# In[54]:


cities = ['bengaluru', 'hyderabad', 'mumbai', 'chennai', 'kochi']
cities2 = ['ahemdabad', 'kolkota', 'mumbai', 'delhi', 'kochi']
cities3 = ['jaipur', 'pune', 'indore', 'agartala', 'patna']


# In[56]:


for one in cities:
    if one in cities3:
        print(one)


# In[53]:


'h' in 'hello'


# In[57]:


for one in cities:
    if one in cities3:
        print(one)
    else:
        print("no output")


# In[59]:


city = "mumbai"#"srinagar"


# In[60]:


for one in cities:
    if one == city:
        print("found")
        break


# In[62]:


city = "srinagar"
for one in cities:
    if one == city:
        print("found")
        break
    else:
        print("not found")


# In[63]:


city = "mumbai"
for one in cities:
    if one == city:
        print("found")
        break
    else:
        print("not found")


# In[64]:


#  else with for
city = "mumbai"
for one in cities:
    if one == city:
        print("found")
        break
else:
    print("not found")


# In[65]:


#  else with for
city = "srinagar"
for one in cities:
    if one == city:
        print("found")
        break
else:
    print("not found")


# In[66]:


#    continue
#    enumerate
#    for-else with multiple list (exercise)
#    while-else


# In[69]:


city = "mumbai"
for one in cities:
    if one == city:
        print("found")
else:
    print("not found")


# In[70]:


city = "mumbai"
for one in cities:
    if one == city:
        print("found")
    else:
        print("not found")


# In[71]:


for h in "hello":
    print(h)
print("-----")


# In[72]:


seta = {'amitabh', 'rajni', 'ntr', 'dada kondke', 'uttam', 'mohanlal'}


# In[73]:


for val in seta:
    print(val)


# In[74]:


print(seta)


# In[75]:


dicta = {'US':'washington', 'UK':'london', 'australia':'canberra', 'japan':'tokyo'}


# In[76]:


for k in dicta:
    print(k)


# In[78]:


for k in dicta:
    print(k, '\t\t', dicta[k])


# In[79]:


print(dicta.keys())


# In[80]:


print(dicta.values())


# In[81]:


list_keys = list(dicta.keys())


# In[82]:


print(list_keys)


# In[83]:


print(dicta.items())


# In[84]:


for k, v in dicta.items():
    print(k)
    print(v)
    print("-----")


# In[ ]:




