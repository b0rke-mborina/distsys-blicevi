def predmeti(firstDict, secondDict):
	assert isinstance(firstDict, str) and isinstance(secondDict, str), "Error"
	assert all(True if isinstance(v, list) else False for k,v in firstDict) and all(True if isinstance(v, list) else False for k,v in secondDict), "Error"
	assert "valute" and "cijena" in firstDict.keys(), "Error"
	return []

print(predmeti(["Stol", "Stolica", "Krevet", "Fotelja"]))