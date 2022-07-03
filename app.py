import streamlit as st
import pickle
import pandas as pd
import numpy as np


pipe = pickle.load(open('phymodel.pkl','rb'))
st.title('Physics Based Temp Predictor')


depth = st.number_input('depth')
lat = st.number_input('lat')
lon = st.number_input('lon')



# 'pH(CaCl2)':[pH(CaCl2)],'pH(H2O)':[pH(H2O)],
if st.button('Predict Clay'):
      input=pd.DataFrame({'depth':[depth],'lat':[lat],'Silt':[lon]})
      result = pipe.predict(input)
      st.success('THE Clay FOR GIVEN DATA WILL BE {}'.format(result))
# st.header(result)