Simple crypto profit/loss calculator
---------

Uses tdax API to get crypto currency current values and calculate the profit loss based on your coins.

To add your coins, create a .csv file in the `data` folder (to be mounted as volume to the docker container) using this format:
YYYY-mm-dd COIN_QTY COIN_PURCHASE_PRICE PURCHASE_TOTAL_COST

Then name the file "xxx_thb.csv" with `xxx` being the curreny.
Currently are hard-coded only 4 types of coins:
- ADA
- DOGE
- BTC
- THB

I will update to determine dynamically the currencies.