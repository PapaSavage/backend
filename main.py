from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import asyncio

# from database import *
from database import *
import uvicorn

app = FastAPI()
conn = workwithbd()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8888",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class review_item(BaseModel):
    review_id: Optional[int] = None
    author_name: Optional[str] = None
    description: Optional[str] = None
    photo_path: Optional[str] = None

    class Config:
        from_attributes = True


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/reviews")
async def read_item():
    results = await conn.get_reviews()
    reviews = [
        {
            "photo_path": "img/mainphoto.png",
            "author_name": "Falaleev Danil",
            "description": "Мы были впечатлены качеством и скоростью работы на...",
        },
        {
            "photo_path": "img/mainphoto.png",
            "author_name": "Falaleev Danil",
            "description": "Мы были впечатлены качеством и скоростью работы на...",
        },
        {
            "photo_path": "img/mainphoto.png",
            "author_name": "Falaleev Danil",
            "description": "Мы были впечатлены качеством и скоростью работы на...",
        },
    ]

    return {"results": reviews}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
