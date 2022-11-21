import aiosqlite
import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/filterJoke")
async def filterJoke(request):
	try:
		json_data = await request.json()
		print(json_data)
		print(json_data.get("type"))
		jsonResponse = web.json_response({
			"data": {
				"joke": {
					"setup": "What do you give a sick lemon?",
					"punchline": "Lemonaid."
				}
			}
		}, status = 200)
		tasks = []
		async with aiohttp.ClientSession() as session:
			tasks.append(asyncio.create_task(session.get("http://127.0.0.1:8083/filterUser", json = jsonResponse)))
			results = await asyncio.gather(*tasks)
			results = [await x.json() for x in results]
		return web.json_response(results, status = 200)
	except Exception as e:
		return web.json_response({"status": "failed", "message": str(e)}, status = 400)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8082)
