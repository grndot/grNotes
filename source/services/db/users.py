from typing import Tuple
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from source.models.database import Users


async def delUserByTelegramID(
        session: AsyncSession,
        telegram_id: int) -> None:
    stmt = delete(Users).where(
            Users.TelegramID == telegram_id)
    await session.execute(stmt)
    await session.commit()


async def getIDbyTelegramID(
        session: AsyncSession,
        telegram_id: int) -> int:
    stmt = select(Users.ID).where(
            Users.TelegramID == telegram_id)
    result = await session.execute(stmt)
    answer: Tuple[int] = result.first()
    return answer[0]


async def getIDbyRecoveryKey(
        session: AsyncSession,
        recovery_key: str) -> int:
    stmt = select(Users.ID).where(
            Users.RecoveryKey == recovery_key)
    result = await session.execute(stmt)
    answer: Tuple[int] = result.first()
    return answer[0]


async def getRecoveryKeyByTelegramID(
        session: AsyncSession,
        telegram_id: int) -> str:
    stmt = select(Users.RecoveryKey).where(
            Users.TelegramID == telegram_id)
    result = await session.execute(stmt)
    answer: Tuple[str] = result.first()
    return answer[0]


async def checkUserExists(
        session: AsyncSession,
        telegram_id: int) -> bool:
    stmt = select(Users.TelegramID).where(
            Users.TelegramID == telegram_id)
    result = await session.execute(stmt)
    if result.first() is None:
        return False
    else:
        return True


async def checkRecoveryKey(
        session: AsyncSession, 
        key: str) -> bool:
    stmt = select(
            Users.TelegramID,
            Users.RecoveryKey).where(
                    Users.RecoveryKey == key)
    result = await session.execute(stmt)
    status = result.first()
    if status is None:
        return False
    else: 
        return True


async def insertNewUser(
        session: AsyncSession, 
        telegram_id: int, 
        language_id: int,
        recovery_key: str):
    stmt = insert(Users).values(
            TelegramID=telegram_id,
            LanguageID=language_id,
            RecoveryKey=recovery_key)
    result = await session.execute(stmt)
    await session.commit()
    return result.scalars()


async def updateUserTelegramId(
        session: AsyncSession,
        recovery_key: str,
        telegram_id: int) -> None:
    stmt = update(Users).where(
            Users.RecoveryKey == recovery_key).values(
                    {Users.TelegramID: telegram_id})    
    await session.execute(stmt)
    await session.commit()


async def updateUserRecoveryKey(
        session: AsyncSession,
        recovery_key: str,
        new_recovery_key: str) -> None:
    stmt = update(Users).where(
            Users.RecoveryKey == recovery_key).values(
                    {Users.RecoveryKey: new_recovery_key})
    await session.execute(stmt)
    await session.commit()
