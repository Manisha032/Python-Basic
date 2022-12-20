import streamlit as st
from random import choice

st.title('Name generator')

fnames= ['Alex', 'Bob','Charlie','David','Eve','Frank','George',
         'Hannah','Ivan','Jenny','Karl']



lnames = ['Anderson','Baker','Clark','Davis', 'Evans', 'Foster',
          'Garcis','Harris','Ivanov']

btn= st.button("Generate name")
if btn:
    fn = choice(fnames)
    ln= choice(lnames)
    fullname = f"{fn} {ln}"
    st.success(fullname)
    
    #streamlit run ui/app1.py