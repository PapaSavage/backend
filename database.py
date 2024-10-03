from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import asyncio

DATABASE_URL = "mysql+aiomysql://p684612_course:MidNightHero123@p684612.mysql.ihc.ru/p684612_course"


class workwithbd:
    def __init__(self) -> None:
        self.engine = create_async_engine(DATABASE_URL, echo=True, future=True)

        self.async_session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

        self.Base = declarative_base()
        
        

    async def check_connection(self):
        try:
            async with self.async_session() as session:
                result = await session.execute(text("SELECT 1"))
                print("Подключение к базе данных успешно!")
        except SQLAlchemyError as e:
            print(f"Ошибка подключения к базе данных: {e}")
            
    async def get_reviews(self):
        async with self.async_session() as session:
            stmt = text(
                "SELECT * FROM reviews;"
            )
            result = await session.execute(stmt, {"age_threshold": 30})
            rows = result.all()
            await session.commit()
            return rows
