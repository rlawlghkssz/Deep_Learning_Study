#!/usr/bin/env python
# coding: utf-8

# In[1]:


#간단한 구현
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    


# In[2]:


AND(0, 0)


# In[3]:


AND(0, 1)


# In[4]:


AND(1, 0)


# In[5]:


AND(1, 1)


# In[6]:


#가중치와 편향 도입
import numpy as np

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
w * x


# In[7]:


np.sum(w * x)


# In[8]:


np.sum(w * x) + b


# In[9]:


np.sum(w * x) - b


# In[10]:


#가중치와 편향 구현

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    
    tmp = np.sum(w * x) + b
    
    if tmp <= 0:
        return 0
    else:
        return 1
    


# In[11]:


#NAND 게이트 구현

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5,  -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    
    if tmp <= 0:
        return 0
    else:
        return 1
    


# In[12]:


#OR게이트 구현

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    
    if tmp <= 0:
        return 0
    else:
        return 1
    


# In[17]:


#XOR 게이트 구현

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y


# In[ ]:




