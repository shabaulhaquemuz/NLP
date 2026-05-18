#!/usr/bin/env python
# coding: utf-8

# In[10]:


#NER:

# Named Entity Recognition (NER) is an NLP technique used to find important names and information in
# text—such as people, places, organizations, dates, and amounts—and label them with their correct
# type.

# In short:
# NER helps a machine understand “who”, “what”, and “where” from text.

# Example (Very Simple)
# Text:
# “Rohit Sharma lives in Mumbai.”

# NER Output:
# Rohit Sharma → PERSON
# Mumbai → LOCATION (GPE)

# Why Do We Use NER?
# We use NER to convert unstructured text into meaningful, structured data.


# In[4]:


get_ipython().system('pip install spacy')
get_ipython().system('python -m spacy download en_core_web_sm')


# In[11]:


#load NER Model


# In[13]:


import spacy
#load english NLP Model
nlp=spacy.load("en_core_web_sm")


# In[14]:


# ex-1
text = "Barack Obama was born in Hawaii and became President of the United States."

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)


# In[15]:


# Ex-2
text = """
Google CEO Sundar Pichai announced a $10 billion investment
in India on 15th July 2020.
"""

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)


# In[16]:


# Ex-3: Person & Location
text = "Sachin Tendulkar was born in Mumbai."

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)


# In[17]:


text="Microsoft was founded in 1975 by Bill Gates"
doc=nlp(text)
for ent in doc.ents:
    print(ent.text, "->", ent.label_)


# In[18]:


#Visualizing NER


# In[22]:


from spacy import displacy
displacy.render(doc, style="ent", jupyter=True)


# In[24]:


text = """
Shabaul Haque, Data Science Intern from Regex Software Services is currently studying NLP under the supervision of
Mr. Sourabh Soni.
"""


# In[25]:


# Process paragraph using NLP model
doc = nlp(text)


# In[26]:


# Print detected entities
for ent in doc.ents:
    print(ent.text, "->", ent.label_)


# In[27]:


from spacy import displacy

displacy.render(doc, style="ent", jupyter=True)


# In[ ]:




