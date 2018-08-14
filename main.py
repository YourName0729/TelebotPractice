
import time
import json
from pprint import pprint

import telepot
from telepot.loop import MessageLoop

from outputs.baseOutput import BaseOutput
from inputs.rawInput import RawInput

def main():
    BOT_TOKEN = None
    with open('./config.json', 'r') as f:
        BOT_TOKEN = json.load(f)['BOT_TOKEN']
        f.close()

    bot = telepot.Bot(BOT_TOKEN)
    BaseOutput.bot = bot
    MessageLoop(bot, {'chat': RawInput.recieve,
                      'callback_query': RawInput.on_callback_query}).run_as_thread()
    print("Bot start!")

    tmp_input = input()
    while tmp_input != 'exit':
        tmp_input = input()


main()