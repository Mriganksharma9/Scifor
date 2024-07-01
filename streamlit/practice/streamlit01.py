import streamlit as st
st.title('Hello this is my streamlit app')
st.slider('x',0,10)
st.button("Reset", type="primary")
if st.button('Hello'):
    st.write('Hello there')
else :
    st.write('Good bye')

from PIL import Image


# Open the image file
img = Image.open("mountains.jpg")

# Display the image in Streamlit
st.image(
    img,
    caption="Image of mountains",
    width=800
)



