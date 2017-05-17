

price = [ 5,10,8]

n=0
buys = [ ]

for i, t in enumerate(price) :
   currBuy = { "tbuy" : i , "buy" : t, "profit" : None, "tsell" : None, "sell" : None}
   for prev in buys :
      currentProfit = t - prev["buy"]
      if(prev["profit"] is None or prev["profit"] < currentProfit) :
         prev["profit"] = currentProfit
         prev["tsell"]  = i
         prev["sell"] = t
      n = n+1
   buys.append(currBuy)

for i in buys :
   print(i)
print(n)



