#from src.llm import client # get the OPENAI_API_KEY

import os
import sys

from dotenv import load_dotenv,find_dotenv

from src.helper import doc_Loader,doc_Split,doc_embeddings_vectorstores

from openai import OpenAI
OpenAI.api_key = os.environ.get('OPENAI_API_KEY')
print(f"OPENAI_API_KEY : {OpenAI.api_key}")

path = sys.path.append('../..')

docPathList =  [os.path.abspath(f'src\Documents\{a}') for a in os.listdir("src\Documents")]
#print(f"docPathList: {docPathList}")

# 1- Load the Document
pages = doc_Loader(docPathList)
print(f"Pages = {pages}")
#print(len(pages))

# 2- Split the Document
pageSplits = doc_Split(pages)

for split in pageSplits:
    #df.add(split.page_content,split.metadata)
    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    print(split.page_content)
    #print(split.metadata)

# 3- Vectorstores and Embeddings
doc_embeddings_vectorstores(pageSplits)
    
