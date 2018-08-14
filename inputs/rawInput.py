# 原生套件
import time
import json
from pprint import pprint

from outputs.baseOutput import BaseOutput
from outputs.happyOutput import HappyOutput

from inputs.textInput import TextInput
from exceptions.myInputTypeError import InputTypeError

class RawInput():

    @staticmethod
    def recieve(message):
        content_type = RawInput.get_state(message, 'content_type')
        try:
            if content_type == 'text':
                TextInput.recieve(message)
            else:
                raise InputTypeError('an unknow or invalid input type', content_type)
        except InputTypeError as e:
            print('InputTypeError : ', end = '')
            print(e.args[0])
            print("which is a {0}".format(e.args[1]))
        except:
            print('unknow error occurred')
    
    @staticmethod
    def get_state(message, request):
        if message.get(request):
            return message[request]
        if request == 'content_type':
            for x in message.keys():
                if x not in ['chat', 'date', 'from', 'message_id']:
                    return x

        