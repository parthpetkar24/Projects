from fastapi import FastAPI,Request,Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR=os.path.join(BASE_DIR,"templates")
STATIC_DIR=os.path.join(BASE_DIR,"static")

app=FastAPI()

app.mount("/static",StaticFiles(directory=STATIC_DIR),name="static")

templates=Jinja2Templates(directory=TEMPLATES_DIR)

@app.get("/")
async def index(request:Request):
    return templates.TemplateResponse(name="index.html",request=request)