
import time
import json
from pprint import pprint

import telepot

from outputs.baseOutput import BaseOutput
from outputs.happyOutput import HappyOutput
from inputs.baseInput import BaseInput

class InlineKeyboardInput(BaseInput):

    @staticmethod
    def recieve(message):
        # pprint(message)
        query_id, from_id, query_data = telepot.glance(message, flavor='callback_query')
        name = message['from']['first_name'] + message['from']['last_name']


        output = BaseOutput()
        output.answer_query(query_id, 'got yayayaya')
        output.send_text(from_id, name + ' click ' + query_data)