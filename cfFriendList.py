import requests
from bs4 import BeautifulSoup


# In[40]:


login_data={
    'action': 'enter',
    'handleOrEmail': 'Suvrajit',#username
    'password': 'ma.baba.suvrajit',#password
}
# In[104]:


with requests.Session() as s:
    url="http://codeforces.com/enter?back=%2F"
    r=s.get(url)
    soup=BeautifulSoup(r.content,'html.parser')
    login_data['csrf_token']=soup.find('input',attrs={'name': 'csrf_token'})['value']
    r=s.post(url, data=login_data)
    r=s.get("http://codeforces.com/problemset/standings?friendsEnabled=on")
    soup=BeautifulSoup(r.text,'html.parser')
    #soup=soup.select('div:nth-child(11) div.content-with-sidebar:nth-child(2) div.datatable:nth-child(6) div:nth-child(6) > table:nth-child(3)')

    #soup = soup.select_one('div:nth-child(11) div.content-with-sidebar:nth-child(2) div.datatable:nth-child(6) div:nth-child(6) > table:nth-child(3)')
    soup = soup.find_all("table")[1]

    # print(soup)
    list = list(soup.find_all('tr')[1])

    print("...............")
    print(list[7])
    # for child in list:
    #     #print(len(child.find_all("td")))
    #
    #     if hasattr(child, 'a'):
    #         name = child.a
    #         solve = child.find_all("td")
    #         if hasattr(name, 'text'):
    #             print(name.text)
    #             print(solve)
