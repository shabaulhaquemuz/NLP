#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ## POS Tagging in NLP

# POS Tagging means Part of Speech Tagging.
# It is an NLP technique where each word in a sentence is assigned its grammatical role such as:
# Noun
# Verb
# Adjective
# Adverb
# Pronoun
# Preposition
# Conjunction


# In[3]:


# ## Why POS Tagging is Important?

# POS Tagging is used in:
# Text Classification
# Chatbots
# Machine Translation
# Named Entity Recognition (NER)
# Sentiment Analysis
#Speech Recognition
#Grammar Checking


# In[4]:


# ## Common POS Tags
# | POS Tag | Meaning         |
# |---------|-----------------|
# | NN      | Noun            |
# | NNS     | Plural Noun     |
# | NNP     | Proper Noun     |
# | VB      | Verb            |
# | VBD     | Verb Past Tense |
# | VBG     | Verb Gerund     |
# | JJ      | Adjective       |
# | RB      | Adverb          |
# | PRP     | Pronoun         |
# | IN      | Preposition     |


# In[5]:


# ## Working Process of POS Tagging::::

# 1.Sentence is divided into tokens.
# 2.NLP model checks grammar/context.
# 3.Appropriate POS tag is assigned to each word.


# In[6]:


get_ipython().system('pip install spacy')
get_ipython().system('python -m spacy download en_core_web_sm')


# In[7]:


import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Input text
doc = nlp("Saurabh is learning NLP")

# POS tagging
for token in doc:
    print(token.text, "---->", token.pos_)


# In[8]:


# ## Example -2
import spacy

# Load model
nlp = spacy.load("en_core_web_sm")

text = "Saurabh plays cricket"
doc = nlp(text)

for token in doc:
    print(token.text, "---->", token.pos_)


# In[9]:


# ## Example -3
import spacy

nlp = spacy.load("en_core_web_sm")

text = "Saurabh is learning NLP"

doc = nlp(text)

for token in doc:
    print(
        "Word:", token.text,
        "| POS:", token.pos_,
        "| TAG:", token.tag_
    )


# In[ ]:


# ## Visualizing POS Tagging
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

text = "Saurabh is learning NLP"

doc = nlp(text)

displacy.serve(doc, style="dep")


# In[ ]:




