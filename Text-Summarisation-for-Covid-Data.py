#!/usr/bin/env python
# coding: utf-8

# <H4>Some basic poitnts about NLP</H4>
# <br>
# Natural Language Processing or NLP is basically a sub-field of artificial intelligence in which we make computer system learn, analyse and generate natural language
# <hr style="height: 2pt;background-color: red">
# NLP : consists of NLU and NLG<br>
#        NLU - Natural Language Understanding
#        NLG - Natural Language Generation
# <h5>5 different phases of NLU and NLG</h5>
# <ol>
# <li>Lexical Processing:- tokenisation. morphological analysis, processing on individual words</li>
# <li>Syntactic Processing :- Internal representation of the text, example a parse tree representation.</li>
# <li>Semantic Processing :- Clarifying the meaning of the word, meaning of words may be different in different context, for example, Federal Bank, bank of a river</li>
# <li>Disposal/Pragmatic Processing:- Former deals with emotions (like text to speech) and Pragmatic deals with stories (eg John is a monk. He goes to Church Daily. He is a Catholic.)</li>
# </ol>
# <hr style="height: 2pt;background-color: blue">

# <h1>Text Summmarisation System</h1>
# <hr style="height: 2pt;background-color: green">
# Condensing a longer document into a short concise document without losing the core information
# <br>
# Based on input, it can be a sinlge document or multi-document summary
# <br>Based on the Purpose: Like some documents are generic or some from one domain (like summarising covid-19 dataset is domain)
# <br>Query Based: User asks questions.
# <h6>Extractive (just retains main sentences) and Abstractive (writing the summary in own words)</h6>
# 
# 
# <It's assumed you are familiar with supervised and unsupervised learning>
# <hr style="height: 2pt;background-color: red">
# Starting with Code (Explained with comments)

# <h4>Text summariation by frequency of words </h4>

# In[23]:


#Importing the Libraries
#NLTK-natural language toolkit for natural language processing
#CORPUS- Collection of Documents, eg Wall Street Journal CORPUS
#using stop-words CORPUS, stop-words are words like of, are, is etc, 
#which occur more frequently and have no semantic meaning
#We need to tokenize the words because we need to compute the frequency of each word
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize


# In[41]:


#import documents
f = open(('./trial_covid_dataset.txt'),"r")
text = f.read()
f.close()


# In[44]:


#So, we have stored the document's text into text variable
#Preprocessing the data : Very Important to avoid overfit or underfit

#Step-1 We tokenize each sentence

sent_tokens = nltk.sent_tokenize(text)
word_tokens = nltk.word_tokenize(text)

#Step-2 We convert to lower case
word_tokens_lower = [word.lower() for word in word_tokens]

#Step-3 remove stopwords
stopWords = list(set(stopwords.words('english'))) #getting all stopwords of English and storing in StopWords
word_tokens_refined = [word for word in word_tokens_lower if word not in stopWords]


# In[62]:


FreqTable = {} #defining a dictionary
for word in word_tokens_refined:
    if word in FreqTable:
        FreqTable[word]+=1
    else:
        FreqTable[word]=1

##This is here major part of summary comes to play
sentence_value = {}
for sentence in sent_tokens:
    sentence_value[sentence]=0
    for word,freq in FreqTable.items():
        if word in sentence.lower():
            sentence_value[sentence]+=freq
#How it works on the basis of frequency can be visualised in the console


# In[63]:


#For inding the score of each sentence

#Finding the average
sum = 0
for sentence in sentence_value:
    sum = sum + sentence_value[sentence]
average = sum/len(sentence_value)


# In[65]:


#We'll be using it to generate the summary
summary = ''
for sentence in sent_tokens:
    if sentence_value[sentence]>average:
        summary=summary+sentence


# In[66]:


print(summary)


# <h1>Voila! Your first Text Summarisation is Ready

# In[ ]:




