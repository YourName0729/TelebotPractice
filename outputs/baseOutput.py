import time
from pprint import pprint

import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove 
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

class BaseOutput():
    bot = None
    sent = None

    def send_text(self, user, text):
        reply_markup = ReplyKeyboardRemove()
        return self.bot.sendMessage(user, text, reply_markup=reply_markup,
                         disable_web_page_preview=True)
        # BaseOutput.sent = self.bot.sendMessage(user, text, reply_markup=reply_markup,
        #                 disable_web_page_preview=True)

    def create_buttons(self, user, text, buttons):
        markup = ReplyKeyboardMarkup(
            keyboard = buttons, resize_keyboard = True)
        self.bot.sendMessage(user, text, reply_markup = markup, 
            disable_web_page_preview = True)

    def create_inline_buttons(self, user, text, buttons):
        keyboard = None
        if isinstance(buttons[0], str):
            keyboard = [[InlineKeyboardButton(text = x, callback_data = x)] for x in buttons]
        elif isinstance(buttons[0], list):
            keyboard = [[InlineKeyboardButton(text = y, callback_data = y) for y in x] for x in buttons]

        markup = InlineKeyboardMarkup(inline_keyboard = keyboard)
        self.bot.sendMessage(user, text, reply_markup = markup)

    def edit_message(self, chat_id, msg_id, text):
        # todo: somehow error occurred
        # self.bot.editMessageText((chat_id, msg_id), text)
        pass

    def answer_query(self, query_id, text):
        self.bot.answerCallbackQuery(query_id, text)

    @staticmethod
    def info(message):
        pprint(message)