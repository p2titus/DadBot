# bot that will absolutely destroy your friends in telegram chats
import re
import telepot
from telepot.loop import MessageLoop
import time


def msg_responder(msg):
    x = msg['text']
    res = say_hi(x)
    if res is not None:
        chat_id = msg['chat']['id']
        bot.sendMessage(chat_id, res)
        print('gotem')


def greet(xs: str) -> str:
    return "hi "+xs+", i'm dad"


def say_hi(msg: str):
    cap1 = r"i'm "
    cap2 = r"im "
    xs = re.split(cap1, msg)
    ys = re.split(cap2, msg)
    if len(xs) > 1:
        print(xs)
        return greet(xs[1])
    elif len(ys) > 1:
        print(ys)
        return greet(ys[1])
    else:
        return None


token = 'REPLACE WITH OWN TOKEN'
bot = telepot.Bot(token)

MessageLoop(bot, msg_responder).run_as_thread()
print('listening')

while True:
    time.sleep(10)
