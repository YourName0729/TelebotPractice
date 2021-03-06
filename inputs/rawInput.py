
import time
import json
from pprint import pprint

import telepot

from outputs.baseOutput import BaseOutput

from inputs.textInput import TextInput
from inputs.inlineKeyboardInput import InlineKeyboardInput
from exceptions.myInputTypeError import InputTypeError

class RawInput():

    @staticmethod
    def recieve(message):
        # pprint(message)
        # content_type, chat_type, chat_id = telepot.glance(message)
        content_type = telepot.glance(message)[0]
        
        try:
            if content_type == 'text':
                TextInput.recieve(message)
            # if someday we have to detect other content_type
            # just add elif here
            else:
                raise InputTypeError('an unknow or invalid input type', content_type)
        except InputTypeError as e:
            print('InputTypeError : ', end = '')
            print(e.args[0])
            print("which is a {0}".format(e.args[1]))
            pprint(message)
        except Exception as e:
            print(e.args)
        except :
            print('unknow error occurred')
    
    @staticmethod
    def on_callback_query(message):
        # pprint(message)
        # query_id, from_id, query_data = telepot.glance(message, flavor='callback_query')
        InlineKeyboardInput.recieve(message)

        