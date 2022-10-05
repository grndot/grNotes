from sqlalchemy import insert, select, update

from source.models.database import Users


async def checkUserExists(
        session,
        telegram_id):
    stmt = select(Users.TelegramID).where(
            Users.TelegramID == telegram_id)
    result = await session.execute(stmt)
    if result.first() is None:
        print(f"User {telegram_id} is login")
        return False
    else:
        print(f"User {telegram_id} is sing up")
        return True


async def selectRecoveryCode(
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


async def updateUser(
        session,
        telegram_id,
        recovery_key,
        new_recovery_key):
    stmt = update(Users).values(
            Users.TelegramID == telegram_id,
            Users.RecoveryKey == new_recovery_key).where(
            Users.RecoveryKey == recovery_key)
    result = await session.execute(stmt)
    await session.commit()
    return result.scalars()
