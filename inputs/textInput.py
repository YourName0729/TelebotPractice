
import time
import json
from pprint import pprint

import telepot

from outputs.baseOutput import BaseOutput
from inputs.baseInput import BaseInput

class TextInput(BaseInput):

    @staticmethod
    def recieve(message):
        chat_type = message['chat']['type']
        chat_id = message['from']['id']
        name = message['from']['first_name'] + message['from']['last_name']
        text = message['text']

        output = BaseOutput()

        if chat_type != 'private':
            output.send_text(chat_id, 'no no no private only!')
            return

        # show info
        print('get message (msg: {0}, id: {1}) from chat {2} by (name: {3}, id: {4})'.format(
            text, message['message_id'], chat_id, name, message['from']['id']))
        
        # do_something when input text : below here 
        # example :
        output.send_text(chat_id, 'get plain message {0}'.format(text))
        output.create_buttons(chat_id, 'show buttons', [['b1'], ['b2'], ['b3']])
        output.create_inline_buttons(chat_id, 'show illine buttons', ['ib1', 'ib2', 'ib3'])
        output.create_inline_buttons(chat_id, 'show inline buttons2', [['00', '01'], ['10', '11']])
        