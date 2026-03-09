# Simple_API_Example
A minimal example demonstrating how to build a simple API featuring a **server** and **client** using **FastAPI**, in the context of delivering goods from New Jersey to New York.

## Overview 📚

This repository contains a small FastAPI-based server that simulates a simple delivery endpoint—sending goods from New Jersey to New York - and a client script to interact with it.

It is intended as a hands-on demonstration of building and consuming RESTful APIs using FastAPI.

## Installation and Set Up ⚙️

1. Clone this repository on your local system, and navigate to project folder:
```
git clone https://github.com/Ioannis-Mykelos/ml-simple-api.git
cd /ml-simple-api
```

> [!NOTE]
> This project uses the `uv` Python package manager for dependency management.
> Follow the instructions from the [official documentation](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer) if you want to run the app locally without Docker.

2. Create a virtual environment with `uv` and install dependencies (uv + WSL example):
```
uv init
uv add pre-commit fastapi requests jinja2 python-multipart uvicorn
uv lock
uv sync
```

To activate your `.venv` environment (created by `uv sync`):
- Windows use `.venv\Scripts\activate`
- Linux `source .venv/bin/activate`

3. In one instance of WSL terminal, run the server with:
```
uvicorn nj_server:app --reload
```

4. Your server will now be available on port 8000 in your browser.
To interact with your API's backend Navigate to:
```
localhost:8000/docs
```

<img width="600" alt="FastAPI Swagger UI Backend Screenshot" src="https://github.com/user-attachments/assets/bad37e97-96c9-4fdb-83e9-9a3e5cbc7b1f"/>

Or navigate directly to an endpoint like:
```
http://127.0.0.1:8000/warehouse/tomatoes?order_qty=30
```

<img width="600" alt="FastAPI Raw Endpoint Screenshot" src="https://github.com/user-attachments/assets/25bde797-5465-4fc5-b414-f084b5e9eb43"/>

5. While the server is running, you can use my custom client to interact with the server more conveniently.
Open an additional instance of WSL (open another WSL terminal next to the existing one), activate environment, navigate to project folder, and run the client with:

```
- Windows use `.venv\Scripts\activate`
- Linux `source .venv/bin/activate`
cd ml-simple-api
uvicorn ny_client:app --reload --port 8001
```

6. Your client will now be available on port 8001 in your browser.
To interact with your client and server, navigate to:
```
localhost:8001
```
<img width="600" alt="Custom Client Screenshot - Order Products" src="https://github.com/user-attachments/assets/b9c19b23-4c3d-4697-a0cf-eb56a9603bac"/>
<br>
<img width="600" alt="Custom Client Screenshot - Shipping Confirmation" src="https://github.com/user-attachments/assets/33385e35-047d-48f6-a1e5-03bd7eb15251"/>

7. Once you understand how the simple implemintation works, I highly recomend to check out `nj_advanced_server.py` to see a more professional approach (using pydantic).

## Dependencies 💻
- **FastAPI** — for building the API.
- **Uvicorn** — ASGI server to run the app.
- HTTP client libraries used in `ny_client.py`:
    - requests
    - jinja2
    - python-multipart
    - pydantic (automatically installed with fastapi)


