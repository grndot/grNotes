from asyncio import run
from sqlalchemy import select

from source.models.database import Users


async def selectTelegramIdAndRecoveryCode(session, key):
    stmt = select(
            Users.TelegramID,
            Users.RecoveryKey).where(
                    Users.RecoveryKey == key)
    result = await session.execute(stmt)
    print(result.all())
    return result.all()
