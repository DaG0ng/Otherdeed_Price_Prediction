import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import functools
import plotly.graph_objects as go
from plotly.subplots import make_subplots

chart = functools.partial(st.plotly_chart, use_container_width=True)

st.set_page_config(layout='wide')

st.title('Market Analytics')

# st.write('Explore the market trends here and try to seize the opportunities!')

# st.write('')
# st.write('')

row0_1, row0_space1= st.columns(
    (1, 3)
)

with row0_1:
    period = st.selectbox(
        'Select the length of period you want to explore',
        (
            'Last 3 days',
            'Last 7 days',
            'Last 30 days',
        ),
    )

row1_1, row1_space1, row1_2, row1_space1 = st.columns(
    (1, 0.1, 1, 0.1)
)

with row1_1:
    st.subheader("Volume and Price")
    df = pd.DataFrame({
        'Date': ['Nov 6', 'Nov 7', 'Nov 8', 'Nov 9', 'Nov 10', 'Nov 11', 'Nov 12'],
        'Price': [2.5752, 2.2616, 2.0926, 2.5147, 2.7904, 1.7714, 2.074],
        'Volume': [126, 217, 336, 347, 365, 462, 165]
    })
    if (period == 'Last 3 days'):
        df = df.tail(3)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['Price'],
            name='Average Price',
            mode='lines'
        ),
        secondary_y=True
    )
    fig.add_trace(
        go.Bar(
            x=df['Date'],
            y=df['Volume'],
            name='Volume'
        ),
        secondary_y=False
    )
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="Volume", secondary_y=False)
    fig.update_yaxes(title_text="Average Price", secondary_y=True, gridcolor='grey')
    chart(fig)

with row1_2:
    st.subheader("Floor and Ceiling Price")
    df = pd.DataFrame({
        'Date': ['Nov 6', 'Nov 7', 'Nov 8', 'Nov 9', 'Nov 10', 'Nov 11', 'Nov 12'],
        'Floor Price': [0.932, 0.977, 1.101, 0.989, 0.963, 0.973, 0.966],
        'Ceiling Price': [15.792, 50.000, 32.181, 19.292, 23.101, 28.232, 17.777]
    })
    if (period == 'Last 3 days'):
        df = df.tail(3)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['Floor Price'],
            name='Floor Price',
            mode='lines'
        ),
        secondary_y=True
    )
    fig.add_trace(
        go.Scatter(
            x=df['Date'],
            y=df['Ceiling Price'],
            name='Ceiling Price',
            mode='lines'
        ),
        secondary_y=False
    )
    fig.update_xaxes(title_text="Date")
    fig.update_yaxes(title_text="Celing Price", secondary_y=False, showgrid=False, range=[0,55])
    fig.update_yaxes(title_text="Floor Price", secondary_y=True, showgrid=False, range=[0,5])
    chart(fig)

st.subheader("Rencent Sales")
dfTrade=pd.read_csv("recent_sales.csv")
if period == 'Last 3 days':
    date_range = ["2022-11-07","2022-11-09"]
else:
    date_range = ["2022-11-03","2022-11-09"]
fig = px.scatter(dfTrade, x="Trade Time", y="Price in USD",hover_name="token_ids",range_x=date_range,range_y=["1800","3000"])
chart(fig)

st.subheader("Latest Predicted Price of Otherdeeds in USD")
prediction_df=pd.read_csv("df_final.csv")
fig = px.line(prediction_df, x="token_ids", y='price', markers=True,range_x=["0","100000"],range_y=[0,800000],
             labels={
                     "token_ids": "# of Otherdeed",
                     "price": "USD Dollars"})
chart(fig)




