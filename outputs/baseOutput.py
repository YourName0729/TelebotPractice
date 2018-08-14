from pprint import pprint

import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove 
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

class BaseOutput():
    bot = None

    def send_text(self, user, text):
        reply_markup = ReplyKeyboardRemove()
        self.bot.sendMessage(user, text, reply_markup=reply_markup,
                        disable_web_page_preview=True)

    def create_buttons(self, user, text, buttons):
        markup = ReplyKeyboardMarkup(
            keyboard = buttons, resize_keyboard = True)
        self.bot.sendMessage(user, text, reply_markup = markup, 
            disable_web_page_preview = True)

    def create_inline_buttons(self, user, text, buttons):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Press 1', callback_data='press 1')],
                   [InlineKeyboardButton(text='Press 2', callback_data='press 2')]
               ])
        self.bot.sendMessage(user, 'Use inline keyboard', reply_markup = keyboard)

    @staticmethod
    def info(message):
        pprint(message)