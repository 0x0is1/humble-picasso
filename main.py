from picasso_bot import *
import os
from utils import wsv

auth_token = os.environ.get('EXPERIMENTAL_BOT_TOKEN')
wsv.wsv()
bot.run(auth_token)
