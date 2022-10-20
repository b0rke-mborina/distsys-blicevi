def predmeti(listaPredmeta):
    assert isinstance(listaPredmeta, list) and all([isinstance(item, str) for item in listaPredmeta])
    return {k:v[::-1] for k,v in enumerate(listaPredmeta)}


print(predmeti(["Stol", "Stolica", "Krevet", "Fotelja"]))
