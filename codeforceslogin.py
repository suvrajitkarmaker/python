#!/usr/bin/env python
# coding: utf-8

# In[39]:


import requests
import bs4


# In[40]:


login_data={
    'action': 'enter',
    'handleOrEmail': '',#username
    'password': '',#password
}


# In[104]:


with requests.Session() as s:
    url="http://codeforces.com/enter?back=%2F"
    r=s.get(url)
    soup=BeautifulSoup(r.content,'html5lib')
    login_data['csrf_token']=soup.find('input',attrs={'name': 'csrf_token'})['value']
    r=s.post(url, data=login_data)
    r=s.get("http://codeforces.com/problemset/standings?friendsEnabled=on")
    soup=bs4.BeautifulSoup(r.text,'html.parser')
    soup=soup.select('#pageContent > div.datatable')

    print(soup)
       
    #print(type(string))
    #result = value.find('Suvrajit') 
    #print ("Substring 'for ' found at index:", result ) 


# In[ ]:




