import streamlit as st

st.title("chai taste poll")

col1,col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://www.sharmispassions.com/wp-content/uploads/2019/07/cutting-chai4.jpg",width=100)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://www.loveandotherspices.com/wp-content/uploads/2025/01/masala-chai-tea-2.jpg",width=100)
    vote2 = st.button("Vote Adrak Chai") 

if vote1:
    st.success("Thanks for masala chai")

elif vote2:
    st.success("Thanks for Adark chai")        
         

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose Your Chai",["Masala","Kesar","Adrak"])
st.write(f"Welcome {name} and your {tea} chai is getting ready") 


with st.expander("Show Chai Making Instructions "):
    st.write("""
        1. Boli water
        2. add milk
        3. serve hot     

""")
    
st.markdown("### Welcome to Chai App ")
st.markdown('> BlockQuote')    