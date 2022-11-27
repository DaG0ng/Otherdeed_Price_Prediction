import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import functools
import plotly.graph_objects as go
from plotly.subplots import make_subplots

@st.cache
def get_stats_df():
    stats_df = pd.read_csv('stats_by_date.csv')
    return stats_df

chart = functools.partial(st.plotly_chart, use_container_width=True)

st.set_page_config(layout='wide')

st.title('Market Analytics')

row0_1, row0_space1= st.columns(
    (1, 3)
)

stats_df = get_stats_df()

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

if period == 'Last 3 days':
    stats_df = stats_df.tail(3)
elif period == 'Last 7 days':
    stats_df = stats_df.tail(7)
else:
    stats_df = stats_df.tail(30)

with row1_1:
    st.subheader("Volume and Price")
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(
            x=stats_df['block_timestamp'],
            y=stats_df['average_trade_price'],
            name='Average Price',
            mode='lines'
        ),
        secondary_y=True
    )
    fig.add_trace(
        go.Bar(
            x=stats_df['block_timestamp'],
            y=stats_df['trade_times'],
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
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Scatter(
            x=stats_df['block_timestamp'],
            y=stats_df['min_trade_price'],
            name='Floor Price',
            mode='lines'
        ),
        secondary_y=True
    )
    fig.add_trace(
        go.Scatter(
            x=stats_df['block_timestamp'],
            y=stats_df['max_trade_price'],
            name='Ceiling Price',
            mode='lines'
        ),
        secondary_y=False
    )
    fig.update_xaxes(title_text="Date")
    if period == 'Last 30 days':
        fig.update_yaxes(title_text="Celing Price", secondary_y=False, showgrid=False, range=["0", "50000"])
    else:
        fig.update_yaxes(title_text="Celing Price", secondary_y=False, showgrid=False, range=["0", "20000"])
    fig.update_yaxes(title_text="Floor Price", secondary_y=True, showgrid=False, range=["0", "10000"])
    chart(fig)

st.subheader("Rencent Sales")
dfTrade=pd.read_csv("recent_sales.csv")
if period == 'Last 3 days':
    date_range = ["2022-11-25","2022-11-27"]
elif period == 'Last 7 days':
    date_range = ["2022-11-21","2022-11-27"]
else:
    date_range = ["2022-10-28","2022-11-27"]
fig = px.scatter(dfTrade, x="Trade Time", y="Price in USD",hover_name="token_ids",range_x=date_range,range_y=["1800","3000"])
chart(fig)

st.subheader("Latest Predicted Price of Otherdeeds in USD")
prediction_df=pd.read_csv("df_price_prediction.csv")
fig = px.line(prediction_df, x="token_ids", y='price', markers=True,range_x=["500","550"],range_y=[0,100000],
             labels={
                     "token_ids": "# of Otherdeed",
                     "price": "USD Dollars"})
chart(fig)




