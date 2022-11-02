#imports

import pandas as pd
from bs4 import BeautifulSoup
import requests

with open('myfile_total.txt','r') as file: #path to be changed
    url_file = file.readlines()
    
#list of urls
for i in url_file:
    urls = i.split(' ')
    
#initializing dictionary
dao_dict={}
dao_dict['Dao_title']=[]
dao_dict['categories']=[]
dao_dict['about']=[]
dao_dict['simdaos']=[]
dao_dict['sim-text']=[]
dao_dict['chain']=[]


for url in urls:
    resp = requests.get(url).content
    soup = BeautifulSoup(resp,'html')
    
    #extracting dao title
    dao_dict['Dao_title'].append(soup.title.text)
    
    #extracting 'about' of dao
    k=[]
    for i in soup.findAll('div',{'class':"markdown text-gray-600"}):
        k.append(i.text)
    about=""
    about=' '.join(k)
    dao_dict['about'].append(about)
    
    #similar daos
    sim_daos = []
    for sim_dao in soup.findAll('div',{'class':'pt-2 pb-1'}):
        sim_daos.append(sim_dao.text)
        
    dao_dict['simdaos'].append(list(set(sim_daos)))
    
    #similar daos 'about'
    similar_div=set(soup.findAll('div',{'class':"relative overflow-hidden"}))
    similar_paragraph=[]
    for div in similar_div:
        link=div.find('a').get('href')
        temp=requests.get("https://www.daohq.co"+str(link)).content
        similar_dao_soup=BeautifulSoup(temp,"html")
        similar_text=[]
        for sim_text in similar_dao_soup.findAll('div',{'class':"markdown text-gray-600"}):
            similar_text.append(sim_text.text)
        similar_paragraph.append(similar_text)
    dao_dict['sim-text'].append(similar_paragraph)
        

    
    #chain and followers
    chain=[]
    for i in soup.findAll('p',{'class':'text-md text-black'}):
        chain.append(i.text)
    dao_dict['chain'].append(chain) 
    
    #categories of the dao
    categories_list=[]
    dao_categories_div=soup.find('div',{'class':'mt-4 flex items-center space-x-2 text-sm'})
    dao_categories=dao_categories_div.findAll('div')
    for cat in dao_categories[1:]:
        categories_list.append(cat.text)
    dao_dict['categories'].append(categories_list)    
    
#dict to dataframe
df = pd.DataFrame(dao_dict)

#dataframe to csv
df.to_csv('DAOs_DATA.csv')
