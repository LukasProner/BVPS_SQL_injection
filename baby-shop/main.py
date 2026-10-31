import logging
from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

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


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    conn = get_db()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "products": products})


@app.get("/vulnerable/search", response_class=HTMLResponse)
def vuln_search(request: Request, q: str = ""):
    conn = get_db()
    sql = "SELECT * FROM products WHERE name LIKE '%" + q + "%'"
    log.info("[VULNERABLE] search SQL: %s", sql)
    try:
        rows = conn.execute(sql).fetchall()
    except Exception as e:
        log.error("[VULNERABLE] search ERROR: %s", e)
        rows = []
    conn.close()
    return templates.TemplateResponse("search.html", {
        "request": request,
        "mode": "vulnerable",
        "rows": rows,
        "q": q,
    })


@app.get("/vulnerable/login", response_class=HTMLResponse)
def vuln_login_form(request: Request):
    return templates.TemplateResponse("login.html", {
        "request": request, "mode": "vulnerable",
        "user": None, "sql": None, "error": None,
    })


@app.post("/vulnerable/login", response_class=HTMLResponse)
def vuln_login(request: Request, username: str = Form(...), password: str = Form(...)):
    conn = get_db()
    sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    log.info("[VULNERABLE] login SQL: %s", sql)
    try:
        user = conn.execute(sql).fetchone()
    except Exception as e:
        log.error("[VULNERABLE] login ERROR: %s", e)
        user = None
    conn.close()
    return templates.TemplateResponse("login.html", {
        "request": request,
        "mode": "vulnerable",
        "user": user,
    })


@app.get("/secure/search", response_class=HTMLResponse)
def sec_search(request: Request, q: str = ""):
    conn = get_db()
    sql = "SELECT * FROM products WHERE name LIKE ?"
    log.info("[SECURE] search SQL: %s  [param: '%%%s%%']", sql, q)
    rows = conn.execute(sql, (f"%{q}%",)).fetchall()
    conn.close()
    return templates.TemplateResponse("search.html", {
        "request": request,
        "mode": "secure",
        "rows": rows,
        "q": q,
    })


@app.get("/secure/login", response_class=HTMLResponse)
def sec_login_form(request: Request):
    return templates.TemplateResponse("login.html", {
        "request": request, "mode": "secure",
        "user": None, "sql": None, "error": None,
    })


@app.post("/secure/login", response_class=HTMLResponse)
def sec_login(request: Request, username: str = Form(...), password: str = Form(...)):
    conn = get_db()
    sql = "SELECT * FROM users WHERE username = ? AND password = ?"
    log.info("[SECURE] login SQL: %s  [params: ('%s', '***')]", sql, username)
    user = conn.execute(sql, (username, password)).fetchone()
    conn.close()
    return templates.TemplateResponse("login.html", {
        "request": request,
        "mode": "secure",
        "user": user,
    })
