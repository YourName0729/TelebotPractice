
import time
import json
from pprint import pprint

import telepot

from outputs.baseOutput import BaseOutput
from inputs.baseInput import BaseInput

class InlineKeyboardInput(BaseInput):

    @staticmethod
    def recieve(message):
        query_id, from_id, query_data = telepot.glance(message, flavor='callback_query')
        name = message['from']['first_name'] + message['from']['last_name']


        output = BaseOutput()

        print('inline button {0} clicked id: {1} by (name: {2}, id: {3})'.format(
            query_data, query_id, name, message['from']['id']))

        # do_something when input text : below here 
        # example :
        output.answer_query(query_id, 'answer query')
        output.send_text(from_id, name + ' click ' + query_data)