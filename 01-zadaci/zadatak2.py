def conversion(firstDict, secondDict):
	assert isinstance(firstDict, dict) and isinstance(secondDict, dict)
	assert all([isinstance(i, list) for _,i in firstDict.items()]) and all([isinstance(i, list) for _,i in secondDict.items()])
	assert (firstDict.get("valute") and firstDict.get("cijena")) and (secondDict.get("valute") and secondDict.get("cijena"))
	return [(a, b) for a,d,b,c in zip(firstDict["cijena"], secondDict["cijena"], firstDict["valute"], secondDict["valute"]) if (a==d) and (b==c)]

print(conversion(
	{"valute":["GBP","USD","CZK","Error"], "cijena":[8.5,7.7,0.3,10.3]},
	{"valute":["EUR","USD","CZK","Error"], "cijena":[7.5,7.7,0.3,5.5]}
))
