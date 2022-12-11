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
        print("DEBUG!!!\nGET_USER_LOCALE\n\n")
        user: Optional[types.User] = types.User.get_current()
        locale: Optional[Locale] = user.locale if user else None
        print(f"DEBUG!!!\n{self.locales=}\n\n")
        if locale and locale.language in self.locales:
            print("DEBUG!!!\nIF CONDITION\n\n")
            *_, data = args
            session = data['session']
            print("DEBUG!!!\nGOT SESSION\n\n")
            language = await getI18NameByID(
                    session=session,
                    language_id=await getLanguageIDByTelegramID(
                        session=session,
                        telegram_id=user.id))
            print("DEBUG!!!\nDID LANGUAGE FUNCS\n\n")
            return language
        return self.default


get_text = LanguageMiddleware(
        domain=load_config().i18n.i18n_domain,
        path=load_config().i18n.locales_dir).gettext
