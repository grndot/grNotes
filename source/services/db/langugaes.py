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
        I18Name: str

    stmt = select(
            Languages.ID, 
            Languages.Name,
            Languages.I18Name)
    result = await session.execute(stmt)
    arrow = result.all()
    response = tuple(
            Language(
                ID=lang[0],
                HumanName=lang[1],
                I18Name=lang[2]) for lang in arrow)
    return response


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
