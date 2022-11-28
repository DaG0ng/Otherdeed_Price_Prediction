import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

@st.cache
def get_otherdeeds_dataset():
  nft_df_1 = pd.read_csv("preprocessed_dataset/ntf_df1.csv")
  nft_df_2 = pd.read_csv("preprocessed_dataset/ntf_df2.csv")
  nft_df_3 = pd.read_csv("preprocessed_dataset/ntf_df3.csv")
  nft_df_4 = pd.read_csv("preprocessed_dataset/ntf_df4.csv")
  nft_df_5 = pd.read_csv("preprocessed_dataset/ntf_df5.csv")
  nft_df = pd.concat([nft_df_1, nft_df_2, nft_df_3, nft_df_4, nft_df_5])
  return nft_df

@st.cache
def get_trades_dataset():
  trades_dataset = pd.read_csv('preprocessed_dataset/new_trade_df.csv')
  return trades_dataset

@st.cache
def get_image(address):
    image = Image.open(address)
    return image

st.set_page_config(layout='wide')

row0_1, row0_spacer1, row0_2, row0_spacer2 = st.columns(
    (2, 0.2, 1, 0.1)
)
row0_1.title('Otherdeeds Price Prediction')

with row0_2:
    st.write("")
    st.subheader("A Streamlit web app created by [Datavengers](https://github.com/DaG0ng/Otherdeed_Price_Prediction)")

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
  otherdeeds_dataset = get_otherdeeds_dataset()
  st.dataframe(data=otherdeeds_dataset)
see_dataset2 = st.expander('You can click here to view the raw trades dataset')
with see_dataset2:
  trades_dataset = get_trades_dataset()
  st.dataframe(data = trades_dataset)

st.subheader('🔥Hot Otherdeeds🔥')
with st.container():
  deed1, deed2, deed3, deed4, deed5, deed6 = st.columns(6)
  with deed1:
    image = get_image('images/1.jpg')
    st.image(image)
  with deed2:
    image = get_image('images/2.jpg')
    st.image(image)
  with deed3:
    image = get_image('images/3.jpg')
    st.image(image)
  with deed4:
    image = get_image('images/4.jpg')
    st.image(image)
  with deed5:
    image = get_image('images/5.jpg')
    st.image(image)
  with deed6:
    image = get_image('images/6.jpg')
    st.image(image)
