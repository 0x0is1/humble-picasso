from picasso_bot import *
import os
from utils import wsv

auth_token = os.environ.get('BOT_TOKEN')
wsv.wsv()
bot.run(auth_token)
