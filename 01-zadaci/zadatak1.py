def predmeti(listaPredmeta):
	assert all(isinstance(item, str) for item in listaPredmeta), "Error"
	return {listaPredmeta.index(item):item[::-1] for item in listaPredmeta}

print(predmeti(["Stol", "Stolica", "Krevet", "Fotelja"]))