import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove

from outputs.baseOutput import BaseOutput

class HappyOutput(BaseOutput):

    def send_text(self, user, text):
        self.bot.sendMessage(user, "happy~")
        reply_markup = ReplyKeyboardRemove()
        self.bot.sendMessage(user, text, reply_markup=reply_markup,
                        disable_web_page_preview=True)
