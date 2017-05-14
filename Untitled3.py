
# coding: utf-8

# In[4]:

source = open('straka_chapter.txt')
straka = source.read()
print (straka[:1000])


# In[8]:

print (straka)


# In[9]:

def pal(word):
    return word.lower() == word[::-1].lower()


# In[10]:

pal(prep(straka))


# In[11]:

def prep(text):
    return re.sub('\W+', '', text)


# In[12]:

pal(prep(straka))


# In[14]:

pal(straka)


# In[20]:

x = ('racecar')


# In[21]:

pal(x)


# In[24]:

y = ('asefirghrigirhgrifesa')
pal(y)


# In[25]:

pal(prep(x))


# In[35]:

def palmulti(name):
    result = ''
    names = name.split()
    for word in names:
        wordrevised = re.sub('\W+', '', word)
        if wordrevised == 'Ss':
            result = result
        elif len(wordrevised) == 1:
            result = result
        elif wordrevised.lower() == 'did':
            result = result
        elif wordrevised.lower() == wordrevised[::-1].lower():
            result = result + ' ' + wordrevised
    return result


# In[28]:

z = ('words backwards are backwards words')


# In[29]:

pal(z)


# In[36]:

palmulti(z)


# In[ ]:



