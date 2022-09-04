from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()

from influx import router as influx_router
app.include_router( influx_router )


app.mount("", StaticFiles(directory="client/public", html=True), name="client")
app.mount("/build", StaticFiles(directory="client/public/build"), name="build")

@app.get("/")
async def client(): return RedirectResponse(url="client")
