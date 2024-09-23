import os 
from dotenv import load_dotenv
from models import Base

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from databases import Database
from .models import Base


# DB Engine & DB
DATABASE_URL = "sqlite+aiosqlite://.fitness_tracker.db"
engine = create_async_engine(DATABASE_URL, echo=True)

database = Database(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all())

async def get_db():
    yield engine

async def get_async_session():
    async_session = sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession
    )
    
    async with async_session() as session:
        yield session
        