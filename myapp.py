from scipy.sparse import data
import streamlit as st
import locale
from prediction import *
from PIL import Image
import plotly.express as px


image = Image.open('spotifypredictor.png')
st.image(image)

st.title(""" Welcome to the Spotify predictor """)
st.write("""  An artist or a producer can try this app to get a prediction of the amount of streams his song will get or to get a prediction of how high the song will be in the charts compared to the existing songs on Spotify.""")
st.write("""This app uses a prediction algtorithm based on a data set of spotify songs.
        To make a valid prediction we need a little bit information about the song:\n
        - Artist's number of followers on Spotify
        - Tempo of the song
        - Duration of the song in ms""")

st.header("Criterias")
st.write("Please give an input to all of the following:\n  ")
st.write("(The less information provided the less precise the prediction will be. So please try to answer all of the fields!)")

#inputs
name_song = st.text_input('Name of the song:',)
followers = st.number_input("Artist's number of followers: (ex. 4953667)",step=1, value=4953667, min_value = 0, max_value=100000000)
tempo = st.number_input('Tempo of the song: (ex. 142)',step=1, value=142, min_value = 0, max_value = 200)
duration = st.number_input('Duration of the song in ms: (ex. 155453)',step=1, value=155453, min_value = 0)

#    data class
app = SpotifyApp('spotify_dataset.csv')
predict_options = ['Streams', 'Highest Charting Position']
predict = st.selectbox('Select what to predict.',predict_options)
if st.button('Predict'):
    with st.spinner("Training ongoing"):
        if predict == 'Streams':
                streams = app.predict_streams(followers,tempo,duration)
                streams = app.predict_streams(followers,tempo,duration)
                st.header(f'Following our predicition algorithm we estimated that {name_song} will reach {round(streams[0])} streams!')
        else:
                highest_charting = app.predict_highest_charting_position(followers,tempo,duration)
                st.header(f'Following our predicition algorithm we estimated that {name_song} will reach {round(highest_charting[0])} as the highest charting position!')
#plot
df = app.data #get csv file
st.header ('Scatter Plot') #title
st.write('To get a better understanding of the prediction we have provided a scatterplot of the data set.  ')
st.write('The X  value can be changed using the selectboxes at the top of the plot.')
st.write('We have also provided a local regression line to help us see the relationship between the axes. ')
x_options = ['Artist Followers','Duration (ms)','Tempo'] #selectbox options
x_axis = st.selectbox('Select X-as', x_options)
y_axis = predict
fig = px.scatter(df, 
        x=x_axis,
        y=y_axis,
        hover_name=y_axis,
        title=f'{y_axis} compared to {x_axis}',
        color = "Tempo",
        trendline="lowess")
#creating a scatter plot 
if y_axis == 'Highest Charting Position': fig['layout']['yaxis']['autorange'] = "reversed"
st.plotly_chart(fig)

