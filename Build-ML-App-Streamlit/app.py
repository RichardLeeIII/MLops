import streamlit as st
#powershell command, streamlit run app.py
st.title("Streamlit Demo RichardLeeIII")

st.header("Heading of Streamlit")

st.subheader("subheading")

st.text("This is an Example")

st.success("Success")
st.warning("warining")
st.info("information")
st.error("Error")

#st.checkbox("Select/Unselect")

if st.checkbox("Select/Unselect"):
    st.text("User selected the checkbox")
else:
    st.text("User has not selected the checkbox")

state = st.radio("What is your favorite color?",("Red","Green","Yellow"))

if state == 'Green':
    st.success("Thats my favorite color as well")

occpation = st.selectbox("whatdoyoudo",["student","clogger"])

st.text(f"selected option is {occpation}")

if st.button("Example Button"):
    st.error("You Clicked it")

st.sidebar.header("Heading of sidebar")
st.sidebar.text("Created by Murthy")