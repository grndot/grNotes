from sqlalchemy import insert, select

from source.models.database import Users


async def checkUserExists(
        session,
        telegram_id):
    stmt = select(Users.TelegramID).where(
            Users.TelegramID == telegram_id)
    result = await session.execute(stmt)
    print(result.all())
    return True if result.all() else False


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
            LanguageID=language_id,
            RecoveryKey=recovery_key)
    result = await session.execute(stmt)
    await session.commit()
    return result.scalars()



