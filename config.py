import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config(object):
    VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")
    PAGE_ACCESS_TOKEN = os.environ.get("PAGE_ACCESS_TOKEN")
