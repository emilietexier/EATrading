# EA Trading
Open Source Trading System using Technical Indicators

EA Trading will be divided in several projects representing different trading strategies. The goal is to develop multiple strategies and test them in a live environment in order to develop a complete and accurate unique trading system compiling the different strategies studied.

## Project 1

The aim of this first project is to build a simple trading system using technical five indicators which will be tested on a live platform. 

### How does it work?

The system uses five technical indicators and for a given stock, will return two results:

- A score, normalized between -1 and 1, representing the strength of the stock. The closer to 1, the better the investment. 
- A trend, normalized between 0 and 1, representing the accuracy of the previous score. The closer to 1, the more accurate the score.
Therefore, when searching for the best stocks to buy, you want to look for a score close to 1 but also a trend close to 1.


### Choice of technical indicators

This system uses five technical indicators chosen according to their use and their compatibility. The choice is certainly not optimal but this is the first version of the system and the indicators choice will evolve in the future. 
The following indicators were used: 

- Average Directional Index (ADX): The ADX is a momentum indicator and helps indicators determine trend strength. The ADX identifies a strong strength when the ADX is above 25 and a weak trend when the ADX is below 20. The ADX is only used in computing the trend as it does not provide relevant information regarding the score.
- On Balance Volume (OBV): OBV is a technical trading momentum indicator that uses volume flow to predict changes in stock price. According to some traders, the volume is the key force behind markets and OBV can project when major moves in the market would occur based on volume changes. OBV is used to compute the stock's score.
- Relative Strength Index (RSI): The RSI is a momentum indicator that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of a stock or other asset. The RSI is used to compute the stock's score.
- Aroon Up & Aroon Down: The Aroon indicator is a technical indicator that is used to identify trend changes in the price of an asset, as well as the strength of that trend. In essence, the indicator measures the time between highs and the time between lows over a period of time. The indicator consists of the 'Aroon Up' line, which measures the strength of the uptrend, and the 'Aroon Down' line, which measures the strength of the downtrend. The Aroon indicators are used to compute both trend and score. 

### Computing 

After the choice of indicators, it was necessary to allocate a specific weight to each indicator for computing both stock's score and trend. This choice was made based on research work but can most likely be optimized. 

- #### Score
The score is computed using 4 indicators: OBV (*x1*), Aroon Up (*x2*), Aroon Down (*x3*) and RSI (*x4*). 

Each *xi* is assigned a specific value calculated using the indicator's value. 
- if OBV is down, then *x1 = -1*, otherwise, *x1 = 1*
- *x2 = -((aroon_up - 50)/50)*
- *x3 = (aroon_down - 50)/50*
- *x4 = (rsi - 50)/50*

Each *xi* is associated with its weight *wsi* representing the weight of the indicator when computing the score.
- *ws1 = 0.2*
- *ws2 = 0.15*
- *ws3 = 0.15*
- *ws4 = 0.5*

Thus, ***score = x1 * ws1 + x2 * ws2 + x3 * ws3 + x4 * ws4***

- #### Trend 
The trend is computed using 3 indicators: ADX (*y1*), Aroon Up (*y2*) and Aroon Down (*y3*).

Each *yi* is assigned a specific value calculated using the indicator's value.
- *y1 = adx/100*
- *y2 = aroon_up/100*
- *y3 = aroon_down/100*

Each *yi* is associated with its weight *wti* representing the weight of the indicator when computing the trend.
- *wt1 = 0.6*
- *wt2 = 0.15*
- *wt3 = 0.15*

Thus, ***trend = y1 * wt1 + y2 * wt2 + y3 * wt3***

### Conclusion 

This section will be filled with the results once the testing period is over.

