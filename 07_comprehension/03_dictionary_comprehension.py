tea_prices_naira = {
  "Masal Chai" : 150,
  "Ginger Chai" : 200,
  "Mint Chai" : 250,
  "Elachi Chai" : 300,
  "Lemon Chai" : 350
}

tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_naira.items()}
print(tea_prices_usd)