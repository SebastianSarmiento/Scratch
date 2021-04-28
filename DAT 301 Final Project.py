#!/usr/bin/env python
# coding: utf-8

# In[252]:


# !pip install bs4
# !pip install requests
# !pip install pandas
#!pip install wordcloud


import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from wordcloud import WordCloud, STOPWORDS
import sys
import os
import numpy as np
from PIL import Image



# In[160]:


url = "https://wikileaks.org/clinton-emails/?q=%28favor+%26+confidential%29+%7C+%28favor+%26+classified%29&mfrom=&mto=&title=&notitle=&date_from=&date_to=&nofrom=&noto=&count=200&sort=0&page=1&#searchresult"
url1 = 'https://wikileaks.org/clinton-emails/emailid/'

r = requests.get(url)

soup = bs(r.content, 'html.parser')


# In[161]:


table = soup.find("table",  class_='table table-striped search-result')
tab_rows = table.find_all('tr')


# In[163]:


l = []
for tr in tab_rows:
    td = tr.find_all('td')
    row = tr.get_text().strip() 
    l.append(row)


# In[228]:


df = pd.DataFrame(l)
df[['DocID', 'Date', 'Subject', 'From', 'To']] = df[0].str.split('\n', expand=True)
df = df.iloc[1:,1:]
#df.set_index('DocID')
df.describe()
#df.isnull().sum()


# In[246]:


li = []
for i in df.iloc[1:5,0]:
    one = url1 + i
    one1 = requests.get(one)
    two = bs(one1.content, 'html.parser')
    three = two.find(id='uniquer')
    four = three.get_text().strip()
    li.append(four)


# In[ ]:





# In[255]:



currdir = 'C:/Users/sebas/OneDrive/Documents/ASU/DAT301'

 
 
def create_wordcloud(four):
    mask = np.array(Image.open(path.join(currdir, "cloud.png")))
     
    stopwords = set(STOPWORDS)
 
    wc = WordCloud(background_color="white",
                    max_words=200, 
                    mask=mask,
                    stopwords=stopwords)
     
    wc.generate(text)
    wc.to_file(path.join(currdir, "output.png"))
 
 
if __name__ == "__main__":
    query = sys.argv[1]
    text = four
     
    create_wordcloud(text)

