from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from source.models.database import Languages


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
