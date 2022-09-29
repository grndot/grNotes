from sqlalchemy import insert, select

from source.models.database import Users


async def selectTelegramIdAndRecoveryCode(
        session, 
        key):
    stmt = select(
            Users.TelegramID,
            Users.RecoveryKey).where(
                    Users.RecoveryKey == key)
    result = await session.execute(stmt)
    print(result.all())
    return result.all()


async def insertNewUser(
        session, 
        telegram_id, 
        language_id,
        recovery_key):
    stmt = insert(Users).values(
            TelegramID=telegram_id,
            Language=language_id,
            RecoveryKey=recovery_key)
    result = await session.execute(stmt)
    return result.scalars()
