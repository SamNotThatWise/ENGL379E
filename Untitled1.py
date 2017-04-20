
# coding: utf-8

# In[2]:

def tax(subtotal):
    return subtotal * 0.08875
tax(1500)


# In[3]:

200 + 1000 + tax(50000)


# In[7]:

def set_a():
    a = 10
    print 'The value of a:', a


# In[10]:

set_a()
a = 20
print 'Initially, the value of a:', a
set_a()
print 'Finally. the value of a:', a


# In[20]:

def scoped(first, second):
    third = second + second - first
    return third

first = 10
second = 11
third = 12
scope_


# In[25]:

x = 5
type(x)


# In[28]:

x = 'word'
type(x)


# In[29]:

x = 'hello'
print(x)


# In[30]:

x = [1,2,3,4,5,6]
type(x)


# In[33]:

a = 'hello '
b = 'world'
print(a + b)


# In[34]:

len([1,2,3])


# In[45]:

volume = [4.0, 2.0, 3.0, 5.5]
result = []
for element in volume:
    result = result + [element *2]


# In[40]:

words = ['hello' , 'world']
def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
    return result
double(words)


# In[46]:

def(double(sequence):


# In[ ]:



