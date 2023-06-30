from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, FileResponse 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json


app = FastAPI()

# templates = Jinja2Templates(directory='templates')


# @app.get('/')
# def root(request : Request):
#   return templates.TemplateResponse('index.html',{'request': request})

app.mount('/',StaticFiles(directory="templates"),name="static")
