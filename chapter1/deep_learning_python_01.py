#!/usr/bin/env python
# coding: utf-8

# In[4]:


#산술 연산 

1 + 2


# In[5]:


1 - 2


# In[6]:


4 * 5


# In[7]:


7 / 5


# In[8]:


3 ** 2


# In[9]:


#자료형 

type(10)


# In[10]:


type(2.718)


# In[11]:


type("Hello")


# In[12]:


#변수

x = 10
print(x)


# In[13]:


x = 100
print(x)


# In[14]:


y = 3.14
x * y


# In[15]:


type(x * y)


# In[16]:


#list 리스트

a = [1,2,3,4,5]
print(a)


# In[17]:


len(a)


# In[18]:


a[0]


# In[19]:


a[4]


# In[20]:


a[4] = 99
print(a)


# In[21]:


a[0:2]


# In[22]:


a[1:]


# In[23]:


a[:3]


# In[24]:


a[:-1]


# In[25]:


a[:-2]


# In[26]:


#딕셔너리

me = {'height' : 180}
me['height']


# In[29]:


me['weight'] = 70


# In[30]:


print(me)


# In[31]:


#bool

hungry = True #배고프다
sleepy = False #안 졸리다

type(hungry)


# In[32]:


not hungry


# In[33]:


hungry and sleepy #배고프고 안졸리다


# In[34]:


hungry or sleepy #배고프거나 안 졸리다


# In[35]:


hungry = True
if hungry:
    print("I'm hungry")


# In[36]:


#if문

hungry = False
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")
    print("I'm sleepy")


# In[37]:


#for문

for i in[1,2,3]:
    print(i)


# In[38]:


#함수

def hello():
    print("Hello World!")


# In[39]:


hello()


# In[40]:


def hello(object):
    print("Hello " + object + "!")


# In[41]:


hello("cat")


# In[43]:


#클래스

class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")
        
    def hello(self):
        print("Hello " + self.name + "!")
    
    def goodbye(self):
        print("Good-Bye " + self.name + "!")

m = Man("Kim ji hwan")
m.hello()
m.goodbye()


# In[44]:


#numpy 넘파이

import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)


# In[45]:


type(x)


# In[46]:


x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
x + y


# In[47]:


x - y


# In[48]:


x * y


# In[49]:


x / y


# In[50]:


x = np.array([1.0, 2.0, 3.0])
x / 2.0


# In[52]:


#numpy의 N차원 배열

A = np.array([[1, 2], [3, 4]])
print(A)


# In[53]:


A.shape


# In[54]:


A.dtype


# In[55]:


B = np.array([[3, 0], [0, 6]])
A + B


# In[56]:


A * B


# In[57]:


print(A)


# In[58]:


A * 10


# In[59]:


#broadcast 브로드캐스트

A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
A * B


# In[60]:


#원소 접근

X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)


# In[62]:


X[0] #0행


# In[63]:


X[0][1] #위치 원소


# In[64]:


for row in X:
    print(row)


# In[65]:


X = X.flatten()
print(X)


# In[68]:


X[np.array([0,2,4])]


# In[69]:


X > 15


# In[70]:


X[X > 15]


# In[73]:


#matplotlib

import numpy as np
import matplotlib.pyplot as plt

#데이터 생성
x = np.arange(0, 6, 0.1) #0에서 6까지 0.1 간격 생성
y = np.sin(x)

#그래프 생성
plt.plot(x, y)
plt.show()


# In[74]:


#pyplot의 기능

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1) #0에서 6까지 0.1 간격 생성
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label = "sin")
plt.plot(x, y2, linestyle = "-", label = "cos") # cos함수는 점선으로 그리기
plt.xlabel("x")
plt.ylabel("y")
plt.title('sin & cos')
plt.legend()
plt.show()


# In[ ]:




