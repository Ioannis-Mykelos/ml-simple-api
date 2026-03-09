"""
This is a simple server that uses a dictionary to store the products and the warehouse catalog.
"""

from typing import TypedDict

from fastapi import FastAPI, HTTPException


class ProductInfo(TypedDict):
    units: str
    qty: int


catalog: dict[str, ProductInfo] = {
    "tomatoes": {
        "units": "boxes",
        "qty": 1000,
    },
    "wine": {
        "units": "bottles",
        "qty": 500,
    },
}

app = FastAPI(title="New Jersey API Server")


@app.get("/warehouse/{product}")
async def load_truck(product: str, order_qty: int):
    """
    Deduct ordered product quantity from the catalog, updating the inventory.

    Args:
        product: The product to deduct the quantity from.
        order_qty: The quantity of the product to deduct.
    """
    available: int = catalog[product]["qty"]

    if order_qty > available:
        raise HTTPException(
            status_code=400,
            detail=f"Sorry, only {available} units are available, please try again…",
        )

    catalog[product]["qty"] -= order_qty

    return {
        "product": product,
        "order_qty": order_qty,
        "units": catalog[product]["units"],
        "remaining_qty": catalog[product]["qty"],
    }
