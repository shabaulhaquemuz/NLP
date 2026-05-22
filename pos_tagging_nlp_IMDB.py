#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv("IMDB Dataset.csv")


# In[3]:


df.head()


# In[4]:


df.isnull().sum()


# In[5]:


df["sentiment"].value_counts()


# In[6]:


# ## Select Any One Review Row

sample_review = df["review"][10]

print(sample_review)


# In[7]:


# ## Import Spacy

import spacy

nlp = spacy.load("en_core_web_sm")


# In[8]:


# ## Convert Review into NLP Doc

doc = nlp(sample_review)


# In[9]:


# ## POS Tagging on Selected Review

for token in doc:
    print(token.text, "---->", token.pos_)


# In[10]:


# ## Detailed POS Tagging

for token in doc:
    print(
        "Word:", token.text,
        "| POS:", token.pos_,
        "| TAG:", token.tag_
    )


# In[ ]:


# ## Visualizing POS Tagging

from spacy import displacy

displacy.serve(doc, style="dep")


# In[ ]:




