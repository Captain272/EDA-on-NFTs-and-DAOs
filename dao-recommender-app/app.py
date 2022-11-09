import streamlit as st
from config import config
import pickle
from gensim.utils import simple_preprocess
import pandas as pd

def preprocessor(x):
    return " ".join(simple_preprocess(x))


st.title("Datapack")

blockchain = st.multiselect("Select your favourite blockchain",config.blockchains)
# print(blockchain)
st.write("#### Select your Interests:(If any)")

music = st.multiselect("Select your favourite music",config.music)
sports = st.multiselect("Select your favourite sport",config.sports)
travel = st.multiselect("Select your favourite travel",config.travel)
finance = st.multiselect("Select your favourite financial services",config.finance)
books = st.multiselect("Select your favourite book genres",config.books)

music = [ele.replace(" ", "_").lower() for ele in music]
sports = [ele.replace(" ", "_").lower() for ele in sports]
travel = [ele.replace(" ", "_").lower() for ele in travel]
finance = [ele.replace(" ", "_").lower() for ele in finance]
books = [ele.replace(" ", "_").lower() for ele in books]



content = " ".join(blockchain)+ " " + " ".join(music) + " " + " ".join(sports) + " " + " ".join(travel) + " " + " ".join(finance) + " " + " ".join(books)

if len(music): 
    content+= " " + "music "
if len(sports): 
    content+= " " + "sports "
if len(travel): 
    content+= " " + "travel "
if len(finance):
     content+= " " + "finance "
if len(books): 
    content+= " " + "books"


dao_data = pd.read_csv("dao_cleaned_data.csv", usecols=['Dao_title', 'categories','blockchain', 'followers'])

# st.write(content)
if st.button("Set"):
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    knn = pickle.load(open("knn.pkl", "rb"))

    _, idx = knn.kneighbors(vectorizer.transform([content]))

    df = dao_data.iloc[idx[0]].reset_index(drop=True)
    st.write(df)