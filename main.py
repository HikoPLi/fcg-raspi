import json
import re
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FCG API", docs_url="/api", redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["GET", "POST", "PUT", "DELETE"], 
    allow_headers=["Content-Type"], 
)

@app.get("/")
async def scare_off_creeps(
):
    html_content = """
    <html>
        <head>
            <title>Hello???</title>
        </head>
        <body>
            <h1>WHY ARE YOU HERE SON??</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/getData")
def getData():
    with open("result.json", 'r') as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)