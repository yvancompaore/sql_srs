import streamlit as st
import pandas as pd
import duckdb

st.write("""
#SQL SRS 
Spaced Repetion System SQL practice
""")


option = st.selectbox(
    "Que Voulez vous reviser?",
    ("Joins", "GroupBy","Windows Function"),
    index=None,
    placeholder="Selectionner un theme ..." ,
)

st.write("Votre Selection",option)

data = {"a": [1, 2, 3], "b": [3, 5, 6]}
df = pd.DataFrame(data)

tab1,tab2,tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1: 
     input_text = st.text_area(label="Entrer votre valeur")
     st.write(input_text)
     st.write(df)
     query = input_text
     d = duckdb.query(query).df()
     st.write(d)





