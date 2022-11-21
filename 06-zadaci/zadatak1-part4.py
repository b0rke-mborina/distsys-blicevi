import aiosqlite
import aiohttp
import asyncio
from aiohttp import web

tempJokes = []
tempUser = []

routes = web.RouteTableDef()

@routes.get("/storeData")
async def get_fact(request):
	try:
		json_data = await request.json()
		print(json_data)
		print(json_data.get("type"))
		noOfRows = 0
		if next(iter(json_data["data"])) == "user" or next(iter(json_data["data"])) == "joke":
			tempJokes.append(json_data)
			if next(iter(json_data["data"])) == "user":
				if len(tempJokes) > 0:
					async with aiosqlite.connect("05-zadaci/blic2.db") as db:
						await db.execute("INSERT INTO users (name, city, username) VALUES (?, ?, ?)",
							(json_data["data"]["user"]["name"], json_data["data"]["joke"]["city"], json_data["data"]["joke"]["username"]))
						await db.execute("INSERT INTO jokes (setup, punchline) VALUES (?, ?)",
							(json_data["data"]["joke"]["setup"], json_data["data"]["joke"]["punchline"]))
						await db.commit()
						assert db.rowcount > 0
						noOfRows = db.rowcount
					tempJokes.clear()
					tempUser.clear()
			return web.json_response({"status": "OK", "data": { "numberOfRowsInTable": noOfRows } }, status = 200)
		else:
			return web.json_response({"status": "Failed", "message": "Joke not present"}, status = 400)
	except Exception as e:
		return web.json_response({"status": "failed", "message": str(e)}, status = 400)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8083)
