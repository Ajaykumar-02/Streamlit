import streamlit as st

st.title('hello chai app')
st.subheader('Brewed with stremilt')
st.text("welcome to your first interactive app")
st.write("choose your fav. chai")

chai = st.selectbox("your fav chai:",["masala chai","Lemon chai","adrak chai"])
st.write(f"Your choose {chai}.Excellent chai")

st.success("Your chai has been brewed")