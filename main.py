from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

jtemplates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def tmp_index(request: Request):
    return jtemplates.TemplateResponse("501.html", {"request": request})


@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    return jtemplates.TemplateResponse("index.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
def index(request: Request):
    return jtemplates.TemplateResponse("about.html", {"request": request})


@app.get("/otherside", response_class=HTMLResponse)
def index(request: Request):
    return jtemplates.TemplateResponse("otherside.html", {"request": request})


@app.get("/projects/{name}", response_class=HTMLResponse)
def projects(request: Request, name: str):
    return jtemplates.TemplateResponse(f"projects_{name}.html", {"request": request})
