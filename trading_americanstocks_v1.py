def compute_stock(): #calculates score and trend for a specific stock using several indicators (OBV, ADX, Aroon Up, Aroon Down, RSI)
    stock_score = 0
    stock_trend = 0
    wt1 = 0.6 #weight for adx in stock_trend
    wt2 = 0.15 #weight for aroon_up in stock_trend
    wt3 = 0.15 #weight for aroon_down in stock_trend
    ws1 = 0.2 #weight for volume in stock_score
    ws2 = 0.15 #weight for aroon_up in stock_score
    ws3 = 0.15 #weight for aroon_down in stock_score
    ws4 = 0.5 #weight for rsi in stock_score
    
    #Variables input
    obv = eval(input('Enter 1 if OBV is up or 0 if OBV is down : '))
    adx = eval(input('Enter ADX : '))
    aroon_up = eval(input('Enter Aroon Up : '))
    aroon_down = eval(input('Enter Aroon Down : '))
    rsi = eval(input('Enter RSI : '))

    #Computing stock_trend
    y1 = adx/100
    y2 = aroon_up/100
    y3 = aroon_down/100
    stock_trend = wt1 * y1 + wt2 * y2 + wt3 * y3 

    #Computing stock_score
    if obv == 1 :
        x1 = 1
    if obv == 0 :
        x1 = -1
    x2 = -((aroon_up - 50)/50)
    x3 = (aroon_down - 50)/50
    x4 = (rsi - 50)/50
    stock_score = ws1 * x1 + ws2 * x2 + ws3 * x3 + ws4 * x4
    list = [stock_score , stock_trend]
    return list

def compute_trade(score,trend): #calculates trading index using stock's score and trend
    w1 = 0.8 #weight for score
    w2 = 0.2 #weight for trend
    trade = w1 * score + w2 * trend
    return trade


def main():
    result = compute_stock()
    print('Score = ', result[0])
    print('Trend = ', result[1])

main()