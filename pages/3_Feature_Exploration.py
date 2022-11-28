import streamlit as st
import numpy as np
import pandas as pd
import functools
import plotly.graph_objects as go
from plotly.subplots import make_subplots

@st.cache
def get_processed_df():
    data = pd.read_csv("preprocessed_dataset/new_trade_df.csv")
    trades_df = pd.DataFrame(data)
    nft_df_1 = pd.read_csv("preprocessed_dataset/ntf_df1.csv")
    nft_df_2 = pd.read_csv("preprocessed_dataset/ntf_df2.csv")
    nft_df_3 = pd.read_csv("preprocessed_dataset/ntf_df3.csv")
    nft_df_4 = pd.read_csv("preprocessed_dataset/ntf_df4.csv")
    nft_df_5 = pd.read_csv("preprocessed_dataset/ntf_df5.csv")
    nft_df = pd.concat([nft_df_1, nft_df_2, nft_df_3, nft_df_4, nft_df_5])
    nft_df=nft_df.rename(columns={"token_id":"token_ids"})
    trades_df = trades_df[["token_ids","block_timestamp","price_usd"]]
    nft_df = nft_df[['token_ids', 'Artifact', 'Category',
        'Eastern Resource', 'Eastern Resource Tier', 'Environment',
        'Environment Tier', 'Koda', 'Northern Resource',
        'Northern Resource Tier', 'Obelisk Piece', 'Plot', 'Sediment',
        'Sediment Tier', 'Southern Resource', 'Southern Resource Tier',
        'Western Resource', 'Western Resource Tier']]
    temp = []
    for i in nft_df['Koda']:
        if (np.isnan(i)):
            temp.append('n')
        else:
            temp.append('y')
    nft_df['Koda'] = temp
    df = nft_df.merge(trades_df, on='token_ids', how='left')
    df = df.dropna(subset=["price_usd"])
    df = df.groupby("token_ids").first()
    return df

@st.cache
def get_feature_df(df):
    mean_values = df.groupby(feature)['price_usd'].mean().sort_values()
    mean_values = mean_values.to_frame()
    counts = df.groupby(feature)[feature].count().sort_values(ascending=True)
    counts = counts.to_frame()
    counts.insert(counts.shape[1], 'price_usd', 0)
    for index, row in counts.iterrows():
        counts.loc[index, 'price_usd'] = mean_values.loc[index, 'price_usd']
    final_df = counts.rename(columns={feature:"count","price_usd":"average_price"})
    return final_df

chart = functools.partial(st.plotly_chart, use_container_width=True)

st.set_page_config(layout='wide')

st.title('Feature Exploration')

row0_1, row0_space1= st.columns(
    (1, 3)
)

with row0_1:
    feature = st.selectbox(
        'Select the feature you want to explore',
        (
            'Artifact',
            'Category',
            'Environment',
            'Environment Tier',
            'Koda',
            'Sediment',
            'Sediment Tier',
            'Northern Resource',
            'Northern Resource Tier',
            'Southern Resource',
            'Southern Resource Tier',
            'Eastern Resource',
            'Eastern Resource Tier',
            'Western Resource',
            'Western Resource Tier',
        ),
    )

df = get_processed_df()
final_df = get_feature_df(df)

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(
    go.Scatter(
        x=final_df.index,
        y=final_df['average_price'],
        name='Average Price',
        mode='lines'
    ),
    secondary_y=True
)
fig.add_trace(
    go.Bar(
        x=final_df.index,
        y=final_df['count'],
        name='Count'
    ),
    secondary_y=False
)
fig.update_yaxes(title_text="Count", showgrid=False, secondary_y=False)
fig.update_yaxes(title_text="Average Price", secondary_y=True, showgrid=False)
chart(fig)