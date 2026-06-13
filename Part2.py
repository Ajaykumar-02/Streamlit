import streamlit as st

st.title("APP CHAI")

if st.button("MAKE CHAI"):
    st.success("Your cahi is being brewed")

add_masala = st.checkbox("Add Masala") 

if add_masala:
    st.write("Masala added to your chai")

tea_type = st.radio("Pick your chai base",["milk","Water","Almond Mlik"])
st.write(f"Selcted base {tea_type}")

Flav = st.selectbox("Chosse flav: ",["Adrak","Kesar","Tulsi"])
st.write(f"Slected flav {Flav}")

sugar = st.slider("sugar level ",0,5,2)
st.write(f"Sugar level {sugar}")

cups = st.number_input("How many Cups",min_value=1,max_value=10,step=1)
st.write(f"Cups  {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"{name} your chai on the way")

dob = st.date_input("Select your dob")
st.write(f"Your Date of birth is {dob}  ")    