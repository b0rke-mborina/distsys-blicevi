def predmeti(firstDict, secondDict):
	assert isinstance(firstDict, str) and isinstance(secondDict, str), "Error"
	assert all(True if isinstance(v, list) else False for k,v in firstDict) and all(True if isinstance(v, list) else False for k,v in secondDict), "Error"
	return {listaPredmeta.index(item):item[::-1] for item in listaPredmeta}

print(predmeti(["Stol", "Stolica", "Krevet", "Fotelja"]))