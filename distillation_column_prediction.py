import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open('distillation_tower.png')

st.image(image)

st.write("""****""")

st.title('Vapour Pressure Prediction')
st.subheader('Using: [CatBoost Regression] (https://catboost.ai/)')
st.subheader('CSV file from: [OpenMV.net Datasets] (https://openmv.net/)')
st.text('For learning purpose')
st.text('@bryson_je')

st.write("""****""")

st.subheader('The Objective:')
st.text('Find process settings to get high quality pressure')
st.text('based on used dataset and selected algorithm')

st.write("""****""")

st.subheader('Analysing Dataset:')
st.text('Find process settings to get high quality pressure')
st.text('based on used dataset and selected algorithm')
