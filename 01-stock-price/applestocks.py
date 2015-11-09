def get_max_profit(stock_prices_yesterday):
	if sorted(stock_prices_yesterday, reverse=True) == stock_prices_yesterday:
		return 0
	candidates = {}
	lowestprice = {}
	for outeridx, outerprice in enumerate(stock_prices_yesterday):
		if not lowestprice:
			lowestprice = {'idx':outeridx, 'price':outerprice}
		highestprice = {}
		for inneridx, innerprice in enumerate(stock_prices_yesterday[outeridx+1:]):
			if not highestprice:
				if innerprice > outerprice:
					highestprice = {'idx':outeridx+1+inneridx, 'price':innerprice}
			else:
				if innerprice > highestprice['price']:
					highestprice = {'idx':outeridx+1+inneridx, 'price':innerprice}
		if not candidates:
			candidates = {
							'highpos': highestprice['idx'], 'highval': highestprice['price'],
							'lowpos': lowestprice['idx'], 'lowval': lowestprice['price'],
							'diff': highestprice['price']-lowestprice['price']
			}
		if highestprice and lowestprice and candidates:
			if (highestprice['price']-lowestprice['price']) > candidates['diff']:
				candidates = {
								'highpos': highestprice['idx'], 'highval': highestprice['price'],
								'lowpos': lowestprice['idx'], 'lowval': lowestprice['price'],
								'diff': highestprice['price']-lowestprice['price']
				}
		lowestprice = {}
		highestprice = {}
	#print '{diff} (buying for ${lowval} and selling for ${highval})'.format(
	#	diff=str(candidates['diff']), 
	#	lowval=str(candidates['lowval']), 
	#	highval=str(candidates['highval']))
	return candidates['diff']


stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

max_profit = get_max_profit(stock_prices_yesterday)
print max_profit
# returns 6 (buying for $5 and selling for $11)
stock_prices_yesterday = [10, 9, 8, 7, 6, 5]

max_profit = get_max_profit(stock_prices_yesterday)
print max_profit
