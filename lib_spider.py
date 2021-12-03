#!/usr/bin/env python
# coding: utf-8

# # 图书馆爬虫

# In[1]:


import requests
import re


# # 准备数据

# In[2]:


search_url = "https://findcumt.libsp.com/find/unify/search"
extend_url="https://findcumt.libsp.com/find/unify/getPItemAndOnShelfCountAndDuxiuImageUrl"
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


# ##### 主要数据储存

# In[3]:


title_list=[]
isbn_list=[]
recordId_list=[]
def addfindings(list1,list2):
    list1.extend(list2)


# ##### 拓展数据储存

# In[4]:


imgUrl_list=[]
onShelfCount_list=[]


# # 获取DATA

# ##### 主要搜索DATA

# In[5]:


search = input("输入关键字")


# In[6]:


data1 ='{"docCode":[null],"searchFieldContent":"'
data2 = '","searchField":"keyWord","matchMode":"2","resourceType":[],"subject":[],"discode1":[],"publisher":[],"libCode":[],"locationId":[],"eCollectionIds":[],"curLocationId":[],"campusId":[],"kindNo":[],"collectionName":[],"author":[],"langCode":[],"countryCode":[],"publishBegin":null,"publishEnd":null,"coreInclude":[],"ddType":[],"verifyStatus":[],"group":[],"sortField":"relevance","sortClause":"asc","page":'
page = 1
data3 = ',"rows":10,"onlyOnShelf":null,"searchItems":null,"keyWord":[]}'
data4 = data1+search+data2


# In[7]:


def getdata(page):
    data = data4+str(page)+data3
    data = data.encode("utf-8")
    return data


# ##### 拓展搜索DATA

# In[8]:


edata1=r'{"title":"'
edata2 = r'","isbn":"'
edata3 = r'","recordId":'
edata4 = r'}'


# In[9]:


def getedata(title_list,isbn_list,recordId_list):
    for i in range(len(title_list)):
        title = title_list[i]
        isbn = isbn_list[i]
        recordId = recordId_list[2*i]
        edata = edata1+title+edata2+isbn+edata3+recordId+edata4
        edata = edata.encode()
        print(i)
        yield edata
getedatas = getedata(title_list,isbn_list,recordId_list)


# # POST请求

# #### 获取基本数据

# In[10]:


for page in range(1,99999):
    data=getdata(page)
    data_to_find = requests.post(search_url,data=data,headers=headers)
    if len(data_to_find.text)<5000:
        break
    data_to_find = data_to_find.text
    title_findings=re.findall('"title":"(.*?),',data_to_find,re.S)
    isbn_findings=re.findall('isbn":(.*?),',data_to_find,re.S)
    recordId_findings = re.findall('recordId":(.*?),"',data_to_find,re.S)
    addfindings(title_list,title_findings)
    addfindings(isbn_list,isbn_findings)
    addfindings(recordId_list,recordId_findings)
    #print(title_findings)


# In[11]:


for i in range(len(title_list)):
    title_list[i] = title_list[i][:-1]


# In[12]:


for i in range(len(isbn_list)):
    if isbn_list[i] == 'null':
        isbn_list[i] = ""
    else:
        isbn_list[i] = isbn_list[i][1:-1]


# ##### 获取其他数据

# In[13]:


for i in range(len(title_list)):
    edata = next(getedatas)
    #print(edata)
    edata_to_find = requests.post(extend_url,data=edata,headers=headers)
    edata_to_find = edata_to_find.text
    imgUrl = re.findall('ImageUrl":"(.*?)"',edata_to_find,re.S)
    onShelfCount = re.findall('onShelfCount":(.*?),"',edata_to_find,re.S)
    addfindings(imgUrl_list,imgUrl)
    addfindings(onShelfCount_list,onShelfCount)
    


# # 输出

# In[14]:


book_num = len(title_list)


# In[15]:


print("爬取完成")
print("总计",book_num,"本资料")
for i in range(book_num):
    print(i+1,title_list[i],"可借数量",onShelfCount_list[i])


# # TEST

# # 1339
# ###### Programming PyTorch for deep learning = PyTorch深度学习编程  \"影印版\".

# In[ ]:




