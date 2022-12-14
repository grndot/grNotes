from typing import Optional
from aiogram import types

from aiogram.contrib.middlewares.i18n import I18nMiddleware, Locale 
from source.config import load_config

from source.services.db.langugaes import getI18NameByID
from source.services.db.users import getLanguageIDByTelegramID


class LanguageMiddleware(I18nMiddleware):

    async def get_user_locale(
            self,
            action,
            args):
        
        user: Optional[types.User] = types.User.get_current()
        locale: Optional[Locale] = user.locale if user else None
        self.reload()
        
        if locale and locale.language in self.locales:
            *_, data = args
            session = data['session']
            language = await getI18NameByID(
                    session=session,
                    language_id=await getLanguageIDByTelegramID(
                        session=session,
                        telegram_id=user.id))
            return language
        return self.default


get_text = LanguageMiddleware(
        domain=load_config().i18n.i18n_domain,
        path=load_config().i18n.locales_dir).gettext
