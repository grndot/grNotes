from typing import Any, Optional, Tuple
from aiogram import types

from aiogram.contrib.middlewares.i18n import (
        I18nMiddleware, 
        Locale)
from source.config import load_config

from source.services.db.langugaes import getI18NameByID
from source.services.db.users import getLanguageIDByTelegramID


class LanguageMiddleware(I18nMiddleware):
    
    async def get_user_locale(
            self, 
            action: str, 
            args: Tuple[Any]) -> Optional[str]:

        *_, data = args
        session = data["session"]
        user: Optional[types.User] = types.User.get_current()
        locale: Optional[Locale] = user.locale
        db_language_id: Optional[int] = await getLanguageIDByTelegramID(
                session=session,
                telegram_id=user.id
                )
        if db_language_id:
            db_I18Name: str = await getI18NameByID(
                session=session,
                language_id=db_language_id)
            return db_I18Name
        return self.default


_ = LanguageMiddleware(
        domain=load_config().i18n.i18n_domain,
        path=load_config().i18n.locales_dir)
