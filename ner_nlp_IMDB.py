#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ## Import Libraries

import numpy as np
import pandas as pd


# In[2]:


# ## Load Dataset

df = pd.read_csv("IMDB Dataset.csv")


# In[3]:


# ## View Dataset

df.head()


# In[4]:


# ## Check Null Values

df.isnull().sum()


# In[5]:


# ## Check Sentiment Counts

df["sentiment"].value_counts()


# In[6]:


# ## Import Spacy and Load Model

import spacy

nlp = spacy.load("en_core_web_sm")


# In[7]:


# ## Select Any One Review Row

sample_review = df["review"][10]

print(sample_review)


# In[8]:


# ## Clean HTML Tags

import re

clean_text = re.sub(r"<.*?>", "", sample_review)

print(clean_text)


# In[9]:


# ## Convert Text into NLP Doc

doc = nlp(clean_text)


# In[10]:


# ## Apply NER on Review

for ent in doc.ents:
    print(ent.text, "->", ent.label_)


# In[11]:


# ## Detailed NER Output

for ent in doc.ents:
    print(
        "Entity:", ent.text,
        "| Label:", ent.label_
    )


# In[12]:


# ## Visualizing NER

from spacy import displacy

displacy.render(doc, style="ent", jupyter=True)


# In[ ]:





# In[ ]:




