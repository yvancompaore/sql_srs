import streamlit as st
import pandas as pd
import duckdb
import io

st.write("""
#SQL SRS 
Spaced Repetion System SQL practice
""")

csv = '''
beverage, price
orangejuice,2.5
Expresso, 2
Tea, 3
'''
beverages = pd.read_csv(io.StringIO(csv))

csv2 = '''
food_item, food_price
cookie juice, 2.5
chocolatine, 2
muffin, 3
'''
food_items = pd.read_csv(io.StringIO(csv2))

answer = '''
SELECT * FROM beverages
CROSS JOIN food_items
'''
solution = duckdb.sql(answer).df()

with st.sidebar :
     option = st.selectbox(
        "Que Voulez vous reviser?",
        ("Joins", "GroupBy","Windows Function"),
        index=None,
        placeholder="Selectionner un theme ..." ,
     )
     st.write('Votre Selection : ', option)



data = {"a": [1, 2, 3], "b": [3, 5, 6]}
df = pd.DataFrame(data)

st.header("entrer votre code")
query = st.text_area(label="Entrer votre valeur")

if query :
    result  = duckdb.query(query).df()
    st.write(result)

tab2,tab3 = st.tabs(["Table","Solution"])

with tab2 :
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution)

with tab3:
    st.write(answer)





