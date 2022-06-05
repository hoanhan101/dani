from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

jtemplates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return jtemplates.TemplateResponse("index.html", {"request": request})


@app.get("/projects/{name}", response_class=HTMLResponse)
def projects(request: Request, name: str):
    pretty_name = name
    if name == "timesheetx":
        pretty_name = "TimeSheetX"

    return jtemplates.TemplateResponse(
        f"projects_{name}.html", {"request": request, "name": pretty_name}
    )
