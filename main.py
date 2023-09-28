# This is a sample Python script.

import streamlit as st
import langChain_helper

st.title("Resturant Name Genertor")

cuisine = st.sidebar.selectbox("Pick a cuisin",
                               ("Sri Lankan", "Indian", "Mexican", "Italian", "American", "Australian", "Canadian"))

if cuisine:
    response = langChain_helper.generate_resturant_name_and_items(cuisine)
    st.header(response['resturant_name'].strip())
    menu_items = response['menu_items'].strip().split(',')
    st.write("Menu Items")
    for item in menu_items:
        st.write("-",item)
