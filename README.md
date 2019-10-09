# EA Trading
Open Source Trading System using Technical Indicators

EA Trading will be divided in several projects representing different trading strategies. The goal is to develop multiple strategies and test them in a live environment in order to develop a complete and accurate unique trading system compiling the different strategies studied.

## Project 1

The aim of this project is to build a simple trading system using technical five indicators which will be tested on a live platform. 

### How does it work?

The system uses five technical indicators and for a given stock, will return two results:

- A score, normalized between -1 and 1, representing the strength of the stock. The closer to 1, the better the investment. 
- A trend, normalized between 0 and 1, representing the accuracy of the previous score. The closer to 1, the more accurate the score.
Therefore, when searching for the best stocks to buy, you want to look for a score close to 1 but also a trend close to 1.


### Used indicators

This system uses five technical indicators chosen according to their use and their compatibility. The choice is certainly not optimal but this is the first version of the system and the indicators choice will evolve in the future. 
The following indicators were used: 

- Average Directional Index (ADX): The ADX is a momentum indicator and helps indicators determine trend strength. The ADX identifies a strong strength when the ADX is above 25 and a weak trend when the ADX is below 20. The ADX is only used in computing the trend as it does not provide relevant information regarding the score.
- On Balance Volume (OBV): OBV is a technical trading momentum indicator that uses volume flow to predict changes in stock price. According to some traders, the volume is the key force behind markets and OBV can project when major moves in the market would occur based on volume changes 
