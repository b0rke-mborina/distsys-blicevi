def predmeti(listaProizvoda):
	assert isinstance(listaProizvoda, list) and all(isinstance(item, dict) for item in listaProizvoda), "Error"
	return {dictValue["kategorija"] for dictinary in listaProizvoda for dictKey,dictValue in dictinary.items()}

print(predmeti([
	{"naziv": "Burek", "kategorija": "pite", "ocjena": 1},
	{"naziv": "Ramsteak", "kategorija": "steak", "ocjena": 9},
	{"naziv": "Ribeye", "kategorija": "steak", "ocjena": 4},
	{"naziv": "Sirnica", "kategorija": "pite", "ocjena": 5},
]))
