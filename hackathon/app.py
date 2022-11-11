# FeedBack
# ---------------------------------------------------------------------------------------------
# Use a feedback system to know how accurate are the recommended results with respeat to web2.
# ---------------------------------------------------------------------------------------------

from flask import Flask,render_template,redirect,request,url_for
import json
import collections
from web3 import Web3
import pandas as pd
import requests
import random
import os

import pickle
from gensim.utils import simple_preprocess
import pandas as pd



def preprocessor(x):
    return " ".join(simple_preprocess(x))

dao_data = pd.read_csv("dao_cleaned_data.csv", usecols=['Dao_title', 'categories','blockchain', 'followers','img','link'])


user_data=[]


def profile_read():
    if "Profile.data" in os.listdir():
        with open("Profile.data","r") as f:
            userdata=f.read()
        vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
        knn = pickle.load(open("knn.pkl", "rb"))
        _, idx = knn.kneighbors(vectorizer.transform([userdata]),25)
        df_pred = dao_data.iloc[idx[0]].reset_index(drop=True)
        df_pred=df_pred.to_dict('index')
        preds=[]
        for i in df_pred.keys():
            preds.append(df_pred[i])
        # print(df_pred)
        return preds
    else:
        return []

# print(profile_read())

preds=[]
top_preds=[]

stuff=[]
df=pd.read_csv('dao_cleaned_data.csv')
data=df.to_dict('index')

for i in data.keys():
    stuff.append(data[i])

app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def hello():
    preds=profile_read()
    # preds=[]
    # print(preds)
    global data
    global user_data

    # Dao_title,categories,about,blockchain,followers,categories,about,blockchain,followers

    if len(preds)!=0:
        return render_template('index.html',data=stuff,preds_len=len(preds),preds=preds)
    else:
        return render_template('index.html',data=stuff,preds_len=len(preds),preds=preds)
        # print(stuff,preds,len(stuff),len(preds))

app.run(host='0.0.0.0', port=5000,debug=True)
