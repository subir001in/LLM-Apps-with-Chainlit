#from src.llm import client # get the OPENAI_API_KEY

import os
import sys
from dotenv import load_dotenv,find_dotenv

from src.helper import docLoader

from openai import OpenAI
OpenAI.api_key = os.environ.get('OPENAI_API_KEY')
print(f"OPENAI_API_KEY : {OpenAI.api_key}")

path = sys.path.append('../..')

docPathList =  [os.path.abspath(f'src\Documents\{a}') for a in os.listdir("src\Documents")]
print(f"docPathList: {docPathList}")

# Load the Document
docs = docLoader(docPathList)
print(len(docs))

