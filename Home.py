import streamlit as st
import numpy as np
import pandas as pd
import time
import requests as req
from PIL import Image
from io import BytesIO

st.set_page_config(layout='wide')

row0_1, row0_spacer1, row0_2, row0_spacer2 = st.columns(
    (2, 0.2, 1, 0.1)
)
row0_1.title('Otherdeeds Price Prediction')

with row0_2:
    st.write("")
    st.subheader("A Streamlit web app created by [Datavengers](https://github.com/DaG0ng/Otherdeed_Price_Prediction)")

# header_image = Image.open('images/page_header.png')
# st.image(header_image, width=1550)

st.markdown('Hey there, welcome to Datavengers\' Otherdeeds Price Prediction App👏. This app aims to provide technology investment strategies by estimating the next trade price of Otherdeeds for our clients through our models, to help maximize their profits since the market of NFT is turbulent.')

st.subheader('App Introduction')
st.markdown('+  **Home**: This is where you are now!' + '\n' +
            '+  **Market Analytics**: On this page you can see the recent market trends of Otherdeeds.' + '\n' +
            '+  **Feature Exploration**: Check how rare are the features of an Othderdeed.' + '\n' +
            '+  **Search Otherdeeds**: Search for your interested Otherdeed and see our predicted price.' + '\n' + 
            '+  **About**: Learn more about the members of Datavengers.')

st.subheader('Datasets We Use')
st.markdown('With the help of OpenSea API, we successfully collected two raw datasets. The first one is the **Otherdeeds dataset**, which contains 99,939 records of all possible 100,000 Otherdeeds. The raw Otherdeeds dataset has some necessary attributes like token id and properties of the Otherdeed. The second dataset is the **trades dataset**, which contains all the records of Otherdeed transactions occurred on the OpeanSea platform from May 1st to now. It also has some valuable attributes like token id and price of the transaction.')
see_dataset1 = st.expander('You can click here to view the raw Otherdeeds dataset')
with see_dataset1:
  otherdeeds_dataset = pd.read_csv('preprocessed_dataset/ntf_df1.csv')
  otherdeeds_dataset = pd.DataFrame(otherdeeds_dataset)
  st.dataframe(data=otherdeeds_dataset)
see_dataset2 = st.expander('You can click here to view the raw trades dataset')
with see_dataset2:
  trades_dataset = pd.read_csv('preprocessed_dataset/new_trade_df.csv')
  st.dataframe(data = trades_dataset)

# st.text_input('Input your interested Otherdeeds here', placeholder='Search Otherdeeds...')

st.subheader('🔥Hot Otherdeeds🔥')
with st.container():
  deed1, deed2, deed3, deed4, deed5, deed6 = st.columns(6)
  with deed1:
    # response = req.get('https://assets.otherside.xyz/otherdeeds/98de818747a85008c5b88b7125763067d9106ebc295296ee5a3c3f31e3527d29.jpg')
    # image = Image.open(BytesIO(response.content))
    image = Image.open('images/1.jpg')
    st.image(image)
  with deed2:
    # response = req.get('https://assets.otherside.xyz/otherdeeds/871079decce602d36188f532fe6623a15d8c6817ecd3bcd9b0c3a2933bb51c3b.jpg')
    # image = Image.open(BytesIO(response.content))
    image = Image.open('images/2.jpg')
    st.image(image)
  with deed3:
    # response = req.get('https://assets.otherside.xyz/otherdeeds/96ad825867364361055d7a967e46f30298e8a05ae6c3556d63847f2b8ef6bb96.jpg')
    # image = Image.open(BytesIO(response.content))
    image = Image.open('images/3.jpg')
    st.image(image)
  with deed4:
    # response = req.get('https://assets.otherside.xyz/otherdeeds/54abf723d8b4a7a885753fd4345b8d182f590ab150f7c9778d0a320b27b134bd.jpg')
    # image = Image.open(BytesIO(response.content))
    image = Image.open('images/4.jpg')
    st.image(image)
  with deed5:
    # response = req.get('https://assets.otherside.xyz/otherdeeds/88e0c462929c07b4cc3bdfec785a1d980e664b12cccf5c69981b3d230e3242a8.jpg')
    # image = Image.open(BytesIO(response.content))
    image = Image.open('images/5.jpg')
    st.image(image)
  with deed6:
    # response = req.get('https://assets.otherside.xyz/otherdeeds/94ea6488aca918ce15a4d8549bc9eae475647a14ae7f7688cb587e0469162c99.jpg')
    # image = Image.open(BytesIO(response.content))
    image = Image.open('images/6.jpg')
    st.image(image)
