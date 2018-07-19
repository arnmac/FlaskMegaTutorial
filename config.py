import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '5j2X0!jf82#@m'
