from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+asyncpg://bet:password@db:5432/bet_db"

engine = AsyncEngine(create_engine(DATABASE_URL, echo=True, future=True))
Base = declarative_base()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
