from dataclasses import dataclass
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from source.models.database import Languages


async def getAllLanguageData(
        session: AsyncSession) -> tuple:
    
    @dataclass
    class Language:
        ID: int
        HumanName: str
        LocaleName: str

    stmt = select(Languages)
    result = await session.execute(stmt)
    arrow = result.all()
    responce = tuple(
            Language(
                ID=lang[0],
                HumanName=lang[1],
                LocaleName=lang[2]) for lang in arrow)
    return responce


async def getI18NameByID(
        session: AsyncSession,
        language_id: int) -> str:
    stmt = select(Languages.I18Name).where(
            Languages.ID == language_id)
    result = await session.execute(stmt)
    return result.first()[0]


async def getLanguageNameByID(
        session: AsyncSession,
        language_id: int) -> str:
    stmt = select(Languages.Name).where(
            Languages.ID == language_id)
    result = await session.execute(stmt)
    return result.first()[0]
