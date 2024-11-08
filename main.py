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
    "http://papasavage.xyz.testihc.ru/",
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
    reviews = [
        {
            "photo_path": "img/potapov.jpg",
            "author_name": "Potapov Artem",
            "description": "Я был впечатлен уровнем профессионализма и вниманием к деталям, которые демонстрирует этот специалист. Работа была выполнена с высокой точностью и в срок. Особенно порадовало то, что все технические требования были соблюдены без исключения. Коммуникация была прозрачной и эффективной, что значительно упрощало процесс сотрудничества. Я высоко оцениваю качество работы и рекомендую этого специалиста всем, кто ищет надежного партнера в своей области.",
        },
        {
            "photo_path": "img/suslov.jpg",
            "author_name": "Suslov Pavel",
            "description": "Сотрудничество с этим специалистом было действительно удовлетворительным. Он показал глубокое понимание наших потребностей и бренда, что отразилось в высоком качестве работы. Процесс был хорошо организован, и я получал регулярные обновления о ходе работы. Этот специалист был очень отзывчив и готов решать любые вопросы, которые у меня возникали. Я особенно ценю творческий подход и способность адаптировать работу к нашей целевой аудитории. Рекомендую этого специалиста всем, кто нуждается в профессиональных услугах.",
        },
        {
            "photo_path": "img/domrachev.jpg",
            "author_name": "Domrachev Artem",
            "description": "Этот специалист продемонстрировал исключительный уровень экспертизы в своей области. Работа была выполнена быстро и качественно, с учетом всех нюансов и особенностей нашего проекта. Я был впечатлен вниманием к деталям и готовностью этого специалиста идти на компромисс, чтобы обеспечить максимальное удовлетворение наших потребностей. Коммуникация была открытой и конструктивной, что сделало процесс сотрудничества очень комфортным. Я рекомендую этого специалиста всем, кто ищет надежного и профессионального партнера.",
        },
    ]

    return {"results": reviews}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
