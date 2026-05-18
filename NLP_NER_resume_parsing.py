#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import pandas as pd


# In[2]:


# Resume Parsing:
# Extract important details from resumes such as:
# Name
# Organization
# Location
# Email

# Goal:
# Convert unstructured resume text into structured format


# In[3]:


resumes = [
    """
    My name is Shabaul Haque.
    I worked as a Data Analyst at Wipro for 2 years.
    My skills include Python, SQL, Tableau, and Machine Learning.
    I am currently based in Delhi.
    Contact: amit.sharma@gmail.com
    """,

    """
    This is Priya Mehta.
    Previously employed at Infosys as a Software Engineer.
    Total experience is 4 years.
    Skilled in Java, Spring Boot, AWS, and Data Structures.
    Location: Pune.
    Email: priya.mehta@outlook.com
    """,

    """
    My name is Rahul Khan.
    I worked as an ML Engineer at TCS for 3 years.
    My skills include NLP, Deep Learning, Python, and TensorFlow.
    I currently live in Hyderabad.
    Contact: rahulkhan@gmail.com
    """,

    """
    This is Sneha Verma.
    Previously employed at Accenture as a Business Analyst.
    Total experience is 5 years.
    Skills include Power BI, Excel, SQL, and Data Analysis.
    Location: Mumbai.
    Email: sneha.verma@yahoo.com
    """,

    """
    My name is Arjun Patel.
    I worked as a Data Scientist at IBM for 6 years.
    My skills include Python, Machine Learning, Statistics, and Pandas.
    I am currently based in Bangalore.
    Contact: arjun.patel@gmail.com
    """
  ]


# In[4]:


get_ipython().system('pip install spacy')
get_ipython().system('python -m spacy download en_core_web_sm')


# In[5]:


import spacy

nlp = spacy.load("en_core_web_sm")


# In[6]:


text = resumes[0]

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)


# In[7]:


structured_data = []


# In[13]:


for resume in resumes:

    doc = nlp(resume)


# In[14]:


name = []
organization = []
location = []


# In[15]:


for ent in doc.ents:

    if ent.label_ == "PERSON":
        name.append(ent.text)

    elif ent.label_ == "ORG":
        organization.append(ent.text)

    elif ent.label_ == "GPE":
        location.append(ent.text)


# In[16]:


email = re.findall(r'\S+@\S+', resume)


# In[18]:


structured_data.append({
    "Name": name,
    "Organization": organization,
    "Location": location,
    "Email": email
})


# In[19]:


df = pd.DataFrame(structured_data)
df


# In[ ]:




