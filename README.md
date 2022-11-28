DSCI-560 Data Science Professional Practicum: Fall 2022

**PROJECT PROPOSAL** 

**Estimate the Next Trade Price for Otherdeeds in Otherside**

### [Enter the website from here.](https://dag0ng-block-chain-database--home-vm3dm9.streamlit.app/About)> 

**Team: Datavengers**

Na Ni, Da Gong, Wenhao Zhang, Tianran Qiu 

*{nani, dagong, wzhang01, tianranq}@usc.edu* 

**ABSTRACT** 

Otherdeeds are dynamic NFTs that were built as a collection and presenting static pieces of lands, and they contain all of the game elements such as a set of resources and some include a Koda, and it can evolve depending on what users do in the game. Now it’s been released and traded throughout NFT ecosystem (Thomas, 2022). According to data from NFT aggregator CryptoSlam, it has generated more than $1 billion in all-time sales volume. Otherdeed is the key to claiming land in the Otherside. Otherside has become the largest expansion of the Bored Ape NFT universe (Minter, 2022). We will leverage several machine learning models such as Recurrent Neural Network, Decision Tree, and Linear Regression that ingest historical sales data and properties of Otherdeeds to generate reliable pricings.

***Keywords:** Otherdeed Price Prediction, NNET, Decision Tree, Linear Regression, Data Mining* 

**I. Business Cases** 

Datavengers, a tech consulting team, aims to provide technology investment strategies by estimating the price of Otherdeeds for our clients, to help maximize their profits through our model.

**II. Problem Statement** 

- A platform where all kinds of Otherdeeds can be retrieved by setting different properties using a filter so that traders can find their interested Otherdeeds fast and conveniently. 
- The proposed website will combine various visualization techniques like a straightforward dashboard and charts of historical transaction records to help users monitor the market status and price trend.
- The system can predict the next trade price of an Otherdeed based on its properties and transaction history, which will assist traders make proper decisions and help maximize their profits.
- The prediction model that combines multiple machine learning algorithms can comprehensively take into account various factors that affect the price of an Otherdeed, and help traders avoid making improper judgments on the price due to information asymmetry or ill-consideration. 
- Clients can make more thoughtful decisions based on price prediction and reduce the risk of loss, which is significantly important in a risky NFT market.

**III. Goal Statement**

- Implementing machine learning algorithms (RNN and regression algorithms) to predict the next trade price for Otherdeeds.
- Using features such as historical sales prices, environmental tier, sediment tier, category, environment, sentiment, resources, artifact, and Koda to train the model and improve model accuracy.

**IV. Project Scope** 

**A. In Scope:** 

This project is divided into four steps in order to build a price estimator for the next trade for Otherdeeds.

- Firstly, collecting and cleaning data from OpenSea with data mining techniques.
- Secondly, building a dataset for Otherdeeds containing features such as historical prices, location, sediment, and so on.
- Thirdly, creating and training models to predict the price of the next trade of Otherdeeds using ML algorithms.
- Lastly, evaluating the price estimator model.

**B. Out of Scope:** 

- Robust market for NFT tradings.
- Implementation of the price estimator involves high velocity, real-time, and marked data.

**V. Data Collection & Data Exploration** 

- Sales Data of Otherdeeds can be easily acquired through the NFT market like OpenSea API and DappRadar API. We can obtain data like properties and historical sales prices of an Otherdeed using data mining techniques. Hence, we can study the trend of its market price and make predictions of price based on these data.
- The total market of Otherdeeds is huge and each transfer or sale action is listed clearly due to one of the greatest features of NFTs: transparency.

**Top 10 NFT sales in May 2022**

**Line Chart: Otherdeeds June 2022 Monthly Sales**

**VI. Authorization**
**
`	`Da Gong, Wenhao Zhang, and Tianran Qiu authorized Na Ni to submit this proposal.

**VII. Team Details**

|**Name**|**Email Address**|
| :-: | :-: |
|Na Ni|nani@usc.edu|
|Da Gong|dagong@usc.edu|
|Tianran Qiu|tianranq@usc.edu|
|Wenhao Zhang|wzhang01@usc.edu|
**VIII. Project Timeline**

|**Key Milestone**|**Target Date**|
| :-: | :-: |
|Project Design|September 2, 2022|
|Data Mining and Data Collecting|Septermber 3, 2022|
|Feature Selection and Model Building|Septermber 15, 2022|
|Model Analysis and Evaluation|October 15, 2022|
|Model Improve|November 1, 2022|
|Presentation and Project Report|Novermber 15, 2022|
**IX. References**

1. Minter, R., Price, U. by G., writer, R. M. A. a, Minter, R., & writer, A. a. (2022, August 1). *Otherdeed NFT collection becomes quickest to surpass $1 billion in all-time sales*. BeInCrypto. Retrieved September 2, 2022, from <https://beincrypto.com/otherdeed-nft-collection-quickest-surpass-1-billion-sales>
1. Yordanova, H. (2022, May 9). *Bored Ape Otherside Land takes over the charts – top 10 NFT sales*. DappRadar Blog RSS. Retrieved September 2, 2022, from <https://dappradar.com/blog/bored-ape-otherside-land-takes-over-the-charts-top-10-nft-sales> 
1. Thomas, L. ((2022, May 9))“Otherside: Everything to Know about the New BAYC NFT Project.” *Nft Now*, Retrieved September 2, 2022, from <https://nftnow.com/guides/otherside-everything-you-need-to-know/>.
