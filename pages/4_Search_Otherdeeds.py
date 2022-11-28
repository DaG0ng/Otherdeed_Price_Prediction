import streamlit as st
import numpy as np
import pandas as pd
import requests as req
import json
from io import BytesIO
from PIL import Image

@st.cache
def get_otherdeeds_dataset():
    df = pd.read_csv("with_images.csv")
    df = df.groupby("token_ids").first()
    return df

@st.cache
def get_predicted_dataset():
    prediction_df=pd.read_csv("df_price_prediction.csv")
    prediction_df = prediction_df.groupby("token_ids").first()
    return prediction_df

@st.cache
def get_image(image_url):
    response = req.get(image_url)
    image = Image.open(BytesIO(response.content))
    return image


st.set_page_config(layout='wide')

st.title('Search Your Interested Otherdeed')

token_id = st.text_input('Input the token ID of your interested Otherdeed here', placeholder='Search Otherdeeds...')

otherdeeds_df = get_otherdeeds_dataset()
prediction_df = get_predicted_dataset()

if len(token_id)>0 and not token_id.lstrip('-').isnumeric():
    st.write('Sorry, please input a positive number between [1, 100000]')
elif len(token_id)>0 and (int(token_id)<0 or int(token_id)>100000):
    st.write('Sorry, this token ID does not exist')
elif len(token_id) > 0:
    st.write('')
    st.write('')
    features = otherdeeds_df.loc[int(token_id)]
    price = prediction_df.loc[int(token_id)]
    row1_1, row1_space1, row1_2, row1_space1, row1_3 = st.columns(
        (0.8, 0.1, 0.5, 0.1, 1)
    )
    with row1_1: 
        image_url = features['image']
        image = get_image(image_url)
        st.image(image)
    with row1_2:
        st.write('')
        st.header('# ' + token_id)
        st.write('')
        st.write('')
        st.metric(
            "Current Price",
            f"${round(features['price_usd'], 2)}"
        )
        st.metric(
            "Predicted Next Trade Price",
            f"${round(price['price'], 2)}",
            f"{round(price['price'] - features['price_usd'], 2)}"
        )
        st.write('')
        st.markdown('***Warn**: Please take the predicted price as a reference only, don\'t rely on it completely.*')
    with row1_3:
        st.write('')
        st.subheader('Features')
        st.markdown('+  ARTIFACT: ' + '***' + str(features['Artifact']) + '***' + '\n' +
                    '+  CATEGORY: ' + '***' + str(features['Category']) + '***' + '\n' +
                    '+  ENVIRONMENT: ' + '***' + str(features['Environment']) + '***' + '\n' +
                    '+  ENVIRONMENT TIER: ' + '***' + str(features['Environment Tier']) + '***' + '\n' +
                    '+  KODA: ' + '***' +  str(features['Koda']) + '***' + '\n' +
                    '+  SEDIMENT: ' + '***' + str(features['Sediment']) + '***' + '\n' +
                    '+  SEDIMENT TIER: ' + '***' + str(features['Sediment Tier']) + '***' + '\n' +
                    '+  NORTHERN RESOURCE: ' + '***' + str(features['Northern Resource']) + '***' + '\n' +
                    '+  NORTHERN RESOURCE TIER: ' + '***' + str(features['Northern Resource Tier']) + '***' + '\n' +
                    '+  SOUTHERN RESOURCE: ' + '***' + str(features['Southern Resource']) + '***' + '\n' +
                    '+  SOUTHERN RESOURCE TIER: ' + '***' + str(features['Southern Resource Tier']) + '***' + '\n' +
                    '+  EASTERN RESOURCE: ' + '***' + str(features['Eastern Resource']) + '***' + '\n' +
                    '+  EASTERN RESOURCE TIER: ' + '***' + str(features['Eastern Resource Tier']) + '***' + '\n' +
                    '+  WESTERN RESOURCE: ' + '***' + str(features['Western Resource']) + '***' + '\n' +
                    '+  WESTERN RESOURCE TIER: ' + '***' + str(features['Western Resource Tier']) + '***')


