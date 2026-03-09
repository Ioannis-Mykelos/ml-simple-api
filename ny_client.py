"""
This is a simple client that uses the FastAPI library to send a request to the server.
"""

import requests
from fastapi import FastAPI, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import nj_server

ITEM_NAMES = list(nj_server.catalog.keys())

API_URL = "http://localhost:8000/warehouse"

app = FastAPI(title="API Buddy")
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    """
    Render the form page.
    Args:
        request: The request object.
    """
    return templates.TemplateResponse(
        "index.html", {"request": request, "products": ITEM_NAMES}
    )


@app.post("/", response_class=HTMLResponse)
def send(
    request: Request,
    product: str = Form(...),
    order_qty: int = Form(...),
):
    """
    Send a request to the server to deduct the ordered product quantity from the catalog.

    Args:
        request: The request object.
        product: The product to deduct the quantity from.
        order_qty: The quantity of the product to deduct.
    """

    r = requests.get(
        f"{API_URL}/{product}",
        params={"order_qty": order_qty},
    )
    data = r.json()

    return templates.TemplateResponse(
        "result.html",
        {"request": request, "result": data},
    )
