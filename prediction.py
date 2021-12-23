import pandas as pd
import numpy as np
import seaborn as sns
import os, sys
import matplotlib.pyplot as plt
sns.set(color_codes=True)
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#import GUI

"""
SpotifyApp class:
constructor input: filepath
cleans code
multiple prediction functions
"""
class SpotifyApp:
    
    #Load dataset into SpotifyApp and clean it
    def __init__(self, file_path) -> None:
        # load data set
        self.file = pd.read_csv(file_path)
        # clean data set
        self.data = self.file.loc[:,['Index','Highest Charting Position','Streams','Artist Followers','Genre','Tempo','Duration (ms)' ]]
        self.data.loc[:,"Streams"] = self.data["Streams"].str.replace(',','').astype(np.float64)
        self.data.loc[:,"Artist Followers"] = pd.to_numeric(self.data["Artist Followers"],errors = 'coerce')
        self.data.loc[:,"Tempo"] = pd.to_numeric(self.data["Tempo"],errors = 'coerce')
        self.data.loc[:,"Duration (ms)"] = pd.to_numeric(self.data["Duration (ms)"],errors = 'coerce')
        #drop Null/NaN/NaT Values
        self.data = self.data.dropna()

    def __repr__(self) -> str:
        return str(self.data.describe())
    
    def predict_streams(self, followers, tempo, duration):
        #create train and test set
        train = self.data.drop(['Streams','Highest Charting Position','Index', 'Genre'], axis=1)
        test = self.data.loc[:,'Streams']
        x_train, x_test, y_train, y_test = train_test_split(train, test, test_size=0.3,random_state=2)

        #create regression model
        regr = LinearRegression()
        
        #train regression model
        regr.fit(x_train,y_train)

        #predict total streams
        pred = regr.predict(x_test)
        
        #check accuracy
        acc = regr.score(x_test, y_test)
        print(acc)
        
        #predict stream from input
        input = [[followers, tempo, duration]]
        streams = regr.predict(input)
        return streams

    def predict_highest_charting_position(self, followers, tempo, duration):
        #create train and test set
        train = self.data.drop(['Streams','Highest Charting Position','Index', 'Genre'], axis=1)
        test = self.data.loc[:,'Highest Charting Position']
        x_train, x_test, y_train, y_test = train_test_split(train, test, test_size=0.3,random_state=2)

        #create regression model
        regr = LinearRegression()
        
        #train regression model
        regr.fit(x_train,y_train)

        #predict total streams
        pred = regr.predict(x_test)
        
        #check accuracy
        acc = regr.score(x_test, y_test)
        print(acc)
        
        #predict stream from input
        input = [[followers, tempo, duration]]
        prediction = regr.predict(input)
        return prediction    
