import logging
from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database import get_db, init_db

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("babyshosp")

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR.parent / "pics"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.on_event("startup")
def startup():
    init_db()


@app.get("/",response_class=HTMLResponse)
def home(req:Request):
    conn=get_db()
    p=conn.execute("SELECT * FROM prod").fetchall()
    conn.close()
    return templates.TemplateResponse("index.html",{"request":req,"products":p})


@app.get("/vulnerable/search",response_class=HTMLResponse)
def vuln_search(req:Request,q:str = ""):
    conn=get_db()
    sql="SELECT * FROM prod WHERE name LIKE '%" + q + "%'"
    # log.info("[VULNERABLE] search SQL: %s", sql)
    try:
        rows =conn.execute(sql).fetchall()
    except Exception as e:
        # log.error("vul err: %s",e)
        rows = []
    conn.close()
    return templates.TemplateResponse("search.html",{
        "request":req,
        "mode":"vulnerable",
        "rows":rows,
        "q": q,
    })


@app.get("/vulnerable/login",response_class=HTMLResponse)
def vuln_login_form(req: Request):
    return templates.TemplateResponse("login.html",{
        "request":req, "mode":"vulnerable", "user":None,
    })


@app.post("/vulnerable/login", response_class=HTMLResponse)
def vuln_login(r: Request, name: str = Form(...), passw: str = Form(...)):
    conn = get_db()
    sql = f"SELECT * FROM users WHERE username = '{name}' AND password = '{passw}'"
    # log.info("VUL login SQL: %s", sql)
    try:
        user = conn.execute(sql).fetchone()
    except Exception as e:
        log.error("vulnerable login ERROR:%s",e)
        user=None
    conn.close()
    return templates.TemplateResponse("login.html",{
        "request":r,
        "mode":"vulnerable",
        "user":user,
    })


@app.get("/secure/search",response_class=HTMLResponse)
def sec_search(r:Request,q:str=""):
    conn=get_db()
    sql = "SELECT * FROM prod WHERE name LIKE ?"
    # log.info("[SECURE] search SQL: %s  [param:'%%%s%%']", sql, q)
    selection=conn.execute(sql,(f"%{q}%",)).fetchall()
    conn.close()
    return templates.TemplateResponse("search.html", {
        "request":r,
        "mode":"secure",
        "rows":selection,
        "q":q,
    })


@app.get("/secure/login",response_class=HTMLResponse)
def sec_login_form(req: Request):
    return templates.TemplateResponse("login.html", {
        "request":req, "mode":"secure","user": None,
    })


@app.post("/secure/login", response_class=HTMLResponse)
def sec_login(req: Request, name: str = Form(...), passw: str = Form(...)):
    conn = get_db()
    sql="SELECT * FROM users WHERE username = ? AND password = ?"
    # log.info("[SECURE] login SQL: %s  [params: ('%s', '***')]",sql,name)
    user=conn.execute(sql,(name, passw)).fetchone()
    conn.close()
    return templates.TemplateResponse("login.html",{
        "request":req,
        "mode":"secure",
        "user":user,
    })
