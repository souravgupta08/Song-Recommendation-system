#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import numpy as np 
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import nltk
import chardet
from nltk.stem.porter import PorterStemmer 
from sklearn.feature_extraction.text import CountVectorizer

class preprocess:
    @staticmethod
    def print_encoding(file_path):
        with open(file_path, 'rb') as file:
            result = chardet.detect(file.read())
        return result['encoding']
    
    @staticmethod
    def convert(text):
        text=text.replace(" ","")
        text=list(text.split(","))
        return text
    
    @staticmethod
    def convert2(text):
        li=[]
        l=text[0:3]
        li.append(l)
        return li
    
    
    @staticmethod
    def stem(text):
        ps=PorterStemmer()
        y=[]
        for i in text.split():
            y.append(ps.stem(i))
        return " ".join(y)
    @staticmethod
    def recommend(df,similarity,song_name):
        index = df[df['Song-Name'] == song_name].index[0]
        distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
        for i in distances[1:6]:
            print(df.iloc[i[0]]['Song-Name'])
    

