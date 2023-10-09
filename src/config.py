from os import environ
from dotenv import load_dotenv

load_dotenv()


configs = {"OPENAI_API_KEY": environ["OPENAI_API_KEY"]}
