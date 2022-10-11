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


async def checkRecoveryCode(
        session, 
        key):
    stmt = select(
            Users.TelegramID,
            Users.RecoveryKey).where(
                    Users.RecoveryKey == key)
    result = await session.execute(stmt)
    status = result.first()
    print(status)
    if status is None:
        return False
    else: 
        return True


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


async def updateUserTelegramId(
        session,
        recovery_key: str,
        telegram_id: int):
    stmt = update(Users).where(
            Users.RecoveryKey == recovery_key).values(
                    {Users.TelegramID: telegram_id})    
    await session.execute(stmt)
    await session.commit()


async def updateUserRecoveryKey(
        session,
        recovery_key: str,
        new_recovery_key: str):
    stmt = update(Users).where(
            Users.RecoveryKey == recovery_key).values(
                    {Users.RecoveryKey: new_recovery_key})
    await session.execute(stmt)
    await session.commit()
