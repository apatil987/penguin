import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import SessionState
state = SessionState.get(searches=[])
st.title('NFL Player Stats Explorer')
st.sidebar.header('Player Name')
def print_data(name):
  name = name.lower()
  names = name.split()
  df = pd.read_html('https://www.nfl.com/players/'+ names[0] + '-'+ names[1] + '/stats/career')
  st.write(df[0])

name = st.sidebar.text_input('Player Name', 'Tom Brady')
if(not(name.title() in state.searches)):
  state.searches.append(name.title())

st.sidebar.markdown("""**Recent Searches: **""")
prev = state.searches[0]
for x in state.searches[1:]:
  prev = prev+', '+ x
searches = st.sidebar.write(prev)
st.write('Showing stats for '+ name.title())
print_data(name)
if st.sidebar.button('Clear Recents'):
  state.searches=[name.title()]