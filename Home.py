import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)


with col1:
    st.image("images/pradnya_photo.jpg", width=200)

with col2:
    st.title("Pradnya Dolthade")
    content= """
        Hi, I am Pradnya, software engineer at Capgemini. I graduated in 2021 from bharati vidyapeeth college of 
    engineering for women, Pune. I am interested to work in Python development and data science.  
    """
    st.info(content)

content2 = """
Below you can find the projects i have built in Python :)

"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[source code]({row['url']})")



