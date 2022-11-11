import pickle
import re
from pathlib import Path
from unittest.case import doModuleCleanups
from scipy.spatial import distance
import pandas as pd
__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

df=pd.read_csv(f"{BASE_DIR}/nft_mod.csv")   
df2=pd.read_csv(f"{BASE_DIR}/nftmusic_blockbeats_solana.csv")  
with open(f"{BASE_DIR}/savemodel.pkl", "rb") as f:
    model = pickle.load(f)

cluster_map = pd.DataFrame()
cluster_map['data_index'] = df.index.values
cluster_map['cluster'] = model.labels_

def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    if model:
        return "dodo"
    else:
        return "fuck"  
def ct():
    if df.empty:
        return "dodo"
    else:
        return df['Track'][0] 
def query():
    
#     l.append(df['image_url'].mode()[0])
#     l.append(df['transfer_activity'].mode()[0])
   
    
    
    # tk=list(set(df2['Track'].values))
    # for i in range(len(tk)):
    #     print(i,tk[i])
    # tk_in=int(input("Track"))
    
    
    # mc=list(set(df2['Music'].values))
    # for i in range(len(mc)):
    #     print(i,mc[i])
    # mc_in=int(input("Music"))
    
    # tm=list(set(df['time'].values))
    # for i in range(len(tm)):
    #     print(i,tm[i],"Sec")
    # tm_in=int(input("Enter preferable Duration of the audio"))
    
    # l.append(tk_in)
    # l.append(mc_in)
    # l.append(tm_in)
    # print("The input vector is:",l)
    l=[2,3,7,152]
    print(l)
    k=make_mat(df,[l])
    return k

def get_points(p):
    k=cluster_map.loc[cluster_map['cluster']==p]
    print("get points called")
    return k['data_index']


def make_mat(df,x):
    print("make function called")
    cluster=model.predict(x)

    points=get_points(cluster[0])
    
    tk=df['Track'].values
    
    mc=df['Music'].values
    print('mc',mc)
    tm=df['time'].values
    print('tm',tm)
    cp=df.iloc[points]
    print('cp1')
    cp=cp.fillna(df.mean())
    print('cp2','tp',cp,tm)
    song_names=cp['name'].values
    print('song names',song_names)
    p=[]
    
    k=set(df.iloc[points]['name'])

    j=[]
    for i in k:
       j.append(i[:-5]) 
    j=list(set(j))
    
    
    
    
    count=0
    for i in cp[cp.drop(columns=['name']).columns].values:
        
        p.append([distance.euclidean(x[0],i),count])
        
        count+=1
    p.sort()
    
    for i in range(5):
        print(song_names[p[i][1]],tk[p[i][1]],mc[p[i][1]],tm[p[i][1]])
    l_top=[]
    for i in j:
        ll=0
        k=0
#         print(i,song_names[p[k][1]])
#         k+=1
        
        while(ll!=5):
            if i in song_names[p[k][1]]:
                
                l_top.append(song_names[p[k][1]])
                ll+=1
            k+=1
             
    return l_top   
            
           
    # pred = model.predict([text])
    # return classes[pred[0]]