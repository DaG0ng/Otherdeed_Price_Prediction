import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(layout='wide')

st.title('Search Your Interested Otherdeed')

token_id = st.text_input('Input the token ID of your interested Otherdeed here', placeholder='Search Otherdeeds...')


if len(token_id)>0 and not token_id.lstrip('-').isnumeric():
    st.write('Sorry, please input a positive number between [1, 100000]')
elif len(token_id)>0 and (int(token_id)<0 or int(token_id)>100000):
    st.write('Sorry, this token ID does not exist')
elif len(token_id) > 0:
    st.write('')
    st.write('')
    row1_1, row1_space1, row1_2, row1_space1, row1_3 = st.columns(
        (0.8, 0.1, 0.5, 0.1, 1)
    )
    with row1_1:
        deed_image = Image.open('images/1.jpg')
        st.image(deed_image)
    with row1_2:
        st.write('')
        st.header('# ' + token_id)
        st.write('')
        st.write('')
        st.metric(
            "Current Price",
            f"${2300.69}"
        )
        st.metric(
            "Predicted Next Trade Price",
            f"${2500.69}",
            f"{200.00}"
        )
        st.write('')
        st.markdown('***Warn**: Please take the predicted price as a reference only, don\'t rely on it completely.*')
    with row1_3:
        st.write('')
        st.subheader('Features')
        st.markdown('+  ARTIFACT: ' + '***' + 'No' + '***' + '\n' +
                    '+  CATEGORY: ' + '***' + 'Decay' + '***' + '\n' +
                    '+  ENVIRONMENT: ' + '***' + 'Ruins' + '***' + '\n' +
                    '+  ENVIRONMENT TIER: ' + '***' + '1' + '***' + '\n' +
                    '+  KODA: ' + '***' +  'No' + '***' + '\n' +
                    '+  SEDIMENT: ' + '***' + 'Cosmic Dream' + '***' + '\n' +
                    '+  SEDIMENT TIER: ' + '***' + '2' + '***' + '\n' +
                    '+  NORTHERN RESOURCE: ' + '***' + 'None' + '***' + '\n' +
                    '+  NORTHERN RESOURCE TIER: ' + '***' + 'N/A' + '***' + '\n' +
                    '+  SOUTHERN RESOURCE: ' + '***' + 'None' + '***' + '\n' +
                    '+  SOUTHERN RESOURCE TIER: ' + '***' + 'N/A' + '***' + '\n' +
                    '+  EASTERN RESOURCE: ' + '***' + 'None' + '***' + '\n' +
                    '+  EASTERN RESOURCE TIER: ' + '***' + 'N/A' + '***' + '\n' +
                    '+  WESTERN RESOURCE: ' + '***' + 'None' + '***' + '\n' +
                    '+  WESTERN RESOURCE TIER: ' + '***' + 'N/A' + '***')


