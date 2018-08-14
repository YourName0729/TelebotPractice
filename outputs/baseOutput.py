from pprint import pprint

import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove

class BaseOutput():
    bot = None

    def send_text(self, user, text):
        reply_markup = ReplyKeyboardRemove()
        self.bot.sendMessage(user, text, reply_markup=reply_markup,
                        disable_web_page_preview=True)

    @staticmethod
    def info(message):
        pprint(message)