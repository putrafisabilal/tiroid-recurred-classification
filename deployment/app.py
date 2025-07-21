import streamlit as st
import eda,prediction,home

st.set_page_config(page_title = "PEMERIKSAAN KAMBUH DARI PASIEN PASCA OPERASI TIROID",
                   layout='centered',
                   initial_sidebar_state='expanded')

with st.sidebar:
    st.write('# Navigation')
    navigation = st.radio('Page', ['Home', 'EDA', 'Predict Reccured'])

if navigation == 'EDA':
    eda.eda()
elif navigation == 'Home':
    home.home()
else:
    prediction.run()