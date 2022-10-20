def proizvodi(listaProizvoda):
	assert isinstance(listaProizvoda, list) and all([isinstance(item, dict) for item in listaProizvoda])
	kategorije = {v for dictionary in listaProizvoda for k,v in dictionary.items() if k=="kategorija"}
	return {kategorija:sum([proizvod["ocjena"] for proizvod in listaProizvoda if proizvod["kategorija"] == kategorija]) for dictionary in listaProizvoda for _,kategorija in dictionary.items() if kategorija in kategorije}

print(proizvodi([
	{"naziv": "Burek", "kategorija": "pite", "ocjena": 1},
	{"naziv": "Ramsteak", "kategorija": "steak", "ocjena": 9},
	{"naziv": "Ribeye", "kategorija": "steak", "ocjena": 4},
	{"naziv": "Sirnica", "kategorija": "pite", "ocjena": 5},
]))
