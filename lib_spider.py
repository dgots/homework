#!/usr/bin/env python
# coding: utf-8

# # 图书馆爬虫

# In[1]:


import requests
import re


# # 准备数据

# In[2]:


search_url = "https://findcumt.libsp.com/find/unify/search"
headers={
"Host": "findcumt.libsp.com",
"Connection": "keep-alive",
"Content-Length": '510',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
'groupCode': '200069',
'sec-ch-ua-mobile': '?0',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
'Content-Type': 'application/json;charset=UTF-8',
'Accept': 'application/json, text/plain, */*',
'mappingPath': "",
'x-lang': 'CHI',
'sec-ch-ua-platform': "Windows",
'Origin': 'https://findcumt.libsp.com',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://findcumt.libsp.com/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Cookie': 'SameSite=None',
        }


# # 获取DATA

# In[3]:


search = input("输入关键字")


# In[4]:


data1 ='{"docCode":[null],"searchFieldContent":"'
data2 = '","searchField":"keyWord","matchMode":"2","resourceType":[],"subject":[],"discode1":[],"publisher":[],"libCode":[],"locationId":[],"eCollectionIds":[],"curLocationId":[],"campusId":[],"kindNo":[],"collectionName":[],"author":[],"langCode":[],"countryCode":[],"publishBegin":null,"publishEnd":null,"coreInclude":[],"ddType":[],"verifyStatus":[],"group":[],"sortField":"relevance","sortClause":"asc","page":'
page = 1
data3 = ',"rows":10,"onlyOnShelf":null,"searchItems":null,"keyWord":[]}'
data4 = data1+search+data2


# In[5]:


def getdata(page):
    return data4+str(page)+data3


# # POST请求

# In[6]:


book_list=[]
def addbooks(books):
    book_list.extend(books)


# In[7]:


for page in range(1,99999):
    data=getdata(page)
    books = requests.post(search_url,data=data,headers=headers)
    if len(books.text)<5000:
        break
    books = books.text
    finding=re.findall('"title":"(.*?)"',books,re.S)
    addbooks(finding)


# # 输出

# In[8]:


book_num = len(book_list)


# In[9]:


print("爬取完成")
print("共爬取",page-1,"页")
print("总计",book_num,"本资料")
for i in range(book_num):
    print(i+1,book_list[i])


# In[ ]:




