#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


df=pd.read_csv("IMDB DataSet.csv")


# In[4]:


df.head()


# In[5]:


df['review'][3]


# In[6]:


df['review'][3].lower()


# In[7]:


#If i want to convert all movies review into lowercase then
df['review'] = df['review'].str.lower()


# In[8]:


df


# In[47]:


#STEP 2: Remove HTML Tags
import re
def remove_html_tags(text):
    pattern=re.compile(r'<.*?>')
    return pattern.sub(r'', text)


# In[ ]:


# import re

# def remove_html_tags(text):
#     pattern = re.compile(r'<.*?>')
#     return pattern.sub('', text)

# text = "<html><body><p> Movie1 </p><p> Click here to <a href='http://google.com'>download</a></p>"

# print(remove_html_tags(text))


# In[48]:


text="<html><body><p> Movie1 </p><p> Click here to <a href = 'http://google.com'>download</a></p>"


# In[49]:


remove_html_tags(text)


# In[15]:


#now we remove tags from IMDB Datasets
df['review']=df['review'].apply(remove_html_tags)


# In[16]:


df


# In[17]:


#if we want to remove urls from text then

def remove_url(text):
    pattern=re.compile(r'https?://\S+')
    return pattern.sub(r'', text)


# In[18]:


#text1= 'Check out my notebook https://www.deture.com/delta/note1234acc'
#text2= 'Check out my notebook https://www.deture.com/delta/note1234acc'
#text3= 'Google search here www.google.com'
text4='For notebook click https://'


# In[19]:


#STEP 4 Remove Punctuation
import string
string.punctuation


# In[20]:


exclude=string.punctuation


# In[21]:


def remove_punc(text):
    for char in exclude:
        text=text.replace(char,'')
    return text


# In[22]:


text1='string. With. Punctuation?'


# In[23]:


remove_punc(text1)


# In[24]:


df['review']=df['review'].apply(remove_punc)


# In[25]:


print(remove_punc(text))


# In[26]:


#Step 5: Chatword treatment


# In[28]:


chat_words={'u2' : 'you too', 'BBL':'Be Back Later', 'GAL':'Get A Life'}


# In[29]:


chat_words


# In[30]:


def chat_conversation(text):
    new_text=[]
    for w in text.split():
        if w.upper() in chat_words:
            new_text.append(chat_words[w.upper()])
        else:
            new_text.append(w)
    return "".join(new_text)


# In[31]:


chat_conversation('BBL')


# In[32]:


chat_words


# In[38]:


#Step 6: Spelling Correction
get_ipython().system('pip install TextBlob')


# In[40]:


from textblob import TextBlob


# In[41]:


incorrect_text="ceertain conditionas seveal ggenerations aree modified in the saame maner."

textBlb=TextBlob(incorrect_text)

textBlb.correct().string


# In[42]:


#STEP 7: Removing step words
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


# In[43]:


STOPWORDS=set(stopwords.words('english'))


# In[45]:


STOPWORDS


# In[46]:


#manually work
def remove_stopwords(text):
    new_text=[]
    for word in text.split():
        if word in set(stopwords.words('english')):
            new_text.append('')
        else:
            new_text.append(word)
    x=new_text[:]
    new_text.clear()
    return "".join(x)
remove_stopwords('probably my all-time favorite movie, a story of selflessness, sacrifice and dedication to a noble cause.')


# In[ ]:




