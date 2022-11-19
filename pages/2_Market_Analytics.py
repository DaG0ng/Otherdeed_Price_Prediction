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
        df = df.iloc[:3]
    # font = {'family':'Helvetica','weight':'normal','size':13}
    # fig = plt.figure()
    # ax2 = fig.add_subplot(111)
    # ax2.bar(df['Date'], df['Volume'], label='Volume', color='goldenrod')
    # ax2.legend(prop = {'family':'Helvatica','size':8}, loc='upper left')
    # ax2.set_ylim([100,500])
    # ax2.set_ylabel(u'Volume',font)
    # ax1 = ax2.twinx()
    # ax1.plot(df['Date'], df['Price'], label='Average Price')
    # ax1.set_ylim([1,3])
    # ax1.legend(prop = {'family':'Helvatica','size':8})
    # ax1.set_ylabel(u'Average Price',font)
    # plt.xlabel(u'Date',font)
    # plt.grid(True)
    # plt.tight_layout()
    # # plt.show()
    # st.pyplot(fig)
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
        df = df.iloc[:3]
    # font = {'family':'Helvetica','weight':'normal','size':13}
    # fig = plt.figure()
    # ax2 = fig.add_subplot(111)
    # ax2.plot(df['Date'], df['Floor Price'], label='Floor Price')
    # ax2.legend(prop = {'family':'Helvatica','size':8}, loc='upper left')
    # ax2.set_ylim([0.9,1.5])
    # ax2.set_ylabel(u'Floor Price',font)
    # ax1 = ax2.twinx()
    # ax1.plot(df['Date'], df['Ceiling Price'], label='Ceiling Price', color='goldenrod')
    # ax1.set_ylim([5,50])
    # ax1.legend(prop = {'family':'Helvatica','size':8})
    # ax1.set_ylabel(u'Ceiling Price',font)
    # plt.xlabel(u'Date',font)
    # plt.grid(True)
    # plt.tight_layout()
    # # plt.show()
    # st.pyplot(fig)
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

dfTrade=pd.read_csv("recent_sales.csv")
fig = px.scatter(dfTrade, x="Trade Time", y="Price in USD",hover_name="token_ids",range_x=["2022-11-01","2022-11-09"],range_y=["1800","3000"],
                title="Recent Sales"
                )
chart(fig)

prediction_df=pd.read_csv("df_final.csv")
fig = px.line(prediction_df, x="token_ids", y='price', markers=True,range_x=["500","550"],range_y=[10000,50000],title="Otherdeed Prediction Value in USD",
             labels={
                     "token_ids": "# of Otherdeed",
                     "price": "USD Dollars"})
chart(fig)




