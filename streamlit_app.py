import streamlit as st
import clips 
import logging

st.subheader("User Input")
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}!")

fruit = st.selectbox("Choose a fruit", ["Apple", "Banana", "Orange"])
st.write(f"You chose: {fruit}")



# Setup working environment
logging.basicConfig(level=15,format='%(message)s')
    
env = clips.Environment()
router = clips.LoggingRouter()
env.add_router(router)

env.build("""(defrule room
                (cold)
             =>
             (printout t "Best plant is ivy!" crlf))""")

# Display rules
# env.eval("(list-defrules)")  
# env.eval("(ppdefrule room)")
st.write(env.eval("(list-defrules)"))