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
        keyboard = [[InlineKeyboardButton(text = x, callback_data = x)] for x in buttons]
        # print(keyboard)
        # for x in buttons:
        #     inline_keyboard.append(InlineKeyboardButton(text = x, callback_data = x))

        markup = InlineKeyboardMarkup(inline_keyboard = keyboard)
        self.bot.sendMessage(user, text, reply_markup = markup)
        
        # keyboard = InlineKeyboardMarkup(inline_keyboard=[
        #            [InlineKeyboardButton(text='Press 1', callback_data='press 1')],
        #            [InlineKeyboardButton(text='Press 2', callback_data='press 2')]
        #        ])
        # self.bot.sendMessage(user, 'Use inline keyboard', reply_markup = keyboard)

    def answer_query(self, query_id, text):
        self.bot.answerCallbackQuery(query_id, text='Got it')

    @staticmethod
    def info(message):
        pprint(message)