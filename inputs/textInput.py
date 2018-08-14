# 原生套件
import time
import json
from pprint import pprint

from outputs.baseOutput import BaseOutput
from outputs.happyOutput import HappyOutput
from inputs.baseInput import BaseInput

class TextInput(BaseInput):

    @staticmethod
    def recieve(message):
        chat_type = message['chat']['type']
        chat_id = message['from']['id']
        name = message['from']['first_name'] + message['from']['last_name']
        text = message['text']

        output = HappyOutput()

        if chat_type != 'private':
            output.send_text(chat_id, 'no no no private only!')
            return

        # pprint(message)
        output.send_text(chat_id, name + " said " + text)