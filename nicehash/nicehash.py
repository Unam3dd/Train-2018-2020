import urllib.request,json,threading, locale

addr='1GFy862aHtKtGafoKYh7ARBEaxkT9FLzTn';
currency='GBP';

stats = 'https://api.nicehash.com/api?method=stats.provider.ex&addr='+addr
price = 'http://api.coindesk.com/v1/bpi/currentprice/'+currency+'.json'

reqStats = urllib.request.Request(stats)

stop_event = threading.Event()

##parsing currency
locale.setlocale( locale.LC_ALL, '' )
reqPrice = urllib.request.Request(price)
rPrice = urllib.request.urlopen(reqPrice).read()
priceCurrency=float(json.loads(rPrice)['bpi'][currency]['rate_float'])
print("\n\nUsing Currency: BTC/{0} = {1:,.2f}".format(currency,priceCurrency))
print("=======================================\n")

##parsing response
rStats = urllib.request.urlopen(reqStats).read()
cont = json.loads(rStats.decode('utf-8'))
counter = 0
balance = 0
totalWorkers = 0
profitability = 0

##parsing json
for item in cont['result']['current']:
	counter += 1
	balance+=float(item['data'][1])
	
	print("Algo: ({0}) {1}".format(item['algo'],item['name']))
	
	
	worker = 'https://api.nicehash.com/api?method=stats.provider.workers&addr='+addr+'&algo='+str(item['algo'])
	reqWorkers = urllib.request.Request(worker)
	rWorker = urllib.request.urlopen(reqWorkers).read()
	totalWorkers += len(json.loads(rWorker)['result']['workers'])
	print("Workers: {0}".format(len(json.loads(rWorker)['result']['workers'])))
	if (len(item['data'][0])>=1):
		print("Accepted Speed: {0} {1}/s".format(item['data'][0]['a'],item['suffix']))
		print("Profitability: {0} BTC/day or {1:,.2f} {2}/day".format(float(item['profitability'])*float(item['data'][0]['a']),float(item['profitability'])*float(item['data'][0]['a'])*priceCurrency, currency))
	else:
		print("Accepted Speed: 0 {0}/s".format(item['suffix']))
		print("Profitability: 0 BTC/day or 0.00 {0}/day".format(currency))
	
	
	if (len(json.loads(rWorker)['result']['workers'])>=1):
		profitability+=float(float(item['profitability'])*float(item['data'][0]['a']))
	print("Balance: {0} BTC or {1:,.2f} {2}".format(item['data'][1],float(item['data'][1])*priceCurrency, currency))
	print("---------------------------------------------------")

print("===================================================")
print("Total Algo: ", counter)
print("Total Workers: {0}".format(totalWorkers))
print("Total Profitability: {0} BTC/day or {1:,.2f} {2}".format(profitability, float(profitability)*priceCurrency, currency))
print("Total Balance: ", balance, "BTC")

