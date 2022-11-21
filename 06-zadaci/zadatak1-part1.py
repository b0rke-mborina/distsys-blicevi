import aiosqlite
import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/getJokes")
async def getJokes(request):
	try:
		responsesJoke, responsesUser = [], []
		for i in range(6):
			tasksJoke, tasksUser = [], []
			async with aiohttp.ClientSession() as session:
				for i in range(10):
					tasksJoke.append(asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke")))
					tasksUser.append(asyncio.create_task(session.get("https://randomuser.me/api/")))
				resultsJoke = await asyncio.gather(*tasksJoke)
				resultsUser = await asyncio.gather(*tasksUser)
				print(resultsUser)
				resultsJoke = [await x.json() for x in resultsJoke]
				resultsUser = [await x.json() for x in resultsUser]
				print("RESPONSES JOKE:", resultsJoke)
				responsesJoke += resultsJoke
				print("RESPONSES USER:", resultsUser)
				responsesUser += resultsUser
			await asyncio.sleep(4)
		
		tasksSecond, tasksThird = [], []
		async with aiohttp.ClientSession() as session:
			for i in range(len(responsesUser)):
				tasksSecond.append(asyncio.create_task(session.get("http://127.0.0.1:8081/filterUser", json = responsesUser[i])))
			statusUserResults = await asyncio.gather(*tasksSecond)
			statusUserResults = [await x.json() for x in statusUserResults]
		
		async with aiohttp.ClientSession() as session:
			for i in range(len(responsesJoke)):
				tasksThird.append(asyncio.create_task(session.get("http://127.0.0.1:8082/filterJoke", json = responsesJoke[i])))
			statusJokeResults = await asyncio.gather(*tasksThird)
			statusJokeResults = [await x.json() for x in statusJokeResults]
		print("RESULTS JOKE:\n", statusJokeResults)
		print("RESULTS USER:\n", statusUserResults)
		return web.json_response({"jokeResults": statusJokeResults, "UserResults": statusUserResults}, status = 200)
	except Exception as e:
		return web.json_response({"status": "failed", "message": str(e)}, status = 400)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8080)
