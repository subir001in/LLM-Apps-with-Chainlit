from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.vectorstores import chroma

# 1 - PDF LOADER
def doc_Loader(docList):
    """
    Load PDF using pypdf into array of documents, where each document contains the page content and metadata with page number.
    
    ------------------------------
    Parameters:
        docList : Document List
    ------------------------------

    Returns back the pages as a list.

    """

    #docList = ['D:\\SUBIR\\LEARNING\\GenAI\\ChatBot\\chainlit-chatbot-interface\\LLM-Apps-with-Chainlit\\MSA.docx', 'D:\\SUBIR\\LEARNING\\GenAI\\ChatBot\\chainlit-chatbot-interface\\LLM-Apps-with-Chainlit\\MSA.pdf']

    loaders = [PyPDFLoader(doc) for doc in docList]
    pages = []
    
    for loader in loaders:
        pages.append(loader.load())

    #print(f"docs: {pages[0]}")
    #print(len(pages))

    return pages[0]


# 2 - SPLIT DOCUMENT
# Reference: https://python.langchain.com/docs/modules/data_connection/document_transformers/

def doc_Split(pages):
    """
    Split the documents into smaller chunks.
    
    ------------------------------
    Parameters:
        pages : Pages of the Document
    ------------------------------

    Returns back page splits of Document Pages in Document format.
    Document(page_content='', metadata={'source': 'D:\\SUBIR\\LEARNING\\GenAI\\ChatBot\\chainlit-chatbot-interface\\LLM-Apps-with-Chainlit\\src\\Documents\\MSA.pdf', 'page': 0})

    """

    r_splitter= RecursiveCharacterTextSplitter(
        chunk_size= 50,
        chunk_overlap= 5,
        
        separators=[". "]
        #separators= [". ","[1-12]","[.|((?<=\\n)|(?<=\\r))]"]
        #separators= ["\n\n","\n","."," ",""]
    )

    pageSplits= r_splitter.split_documents(pages)


    #print(f"PageSplits =  {pageSplits}")
    print(f"Length of Pages: {len(pages)}")
    print(f"Length of PageSplits: {len(pageSplits)}")

    return pageSplits


# 3 - EMBEDDINGS and VectorStores
# Reference: 

def doc_embeddings_vectorstores(pageSplits):
    """
    Create the embeddings for the documents splits and stores them into vectorstores. 
    
    ------------------------------
    Parameters:
        docList : Document
    ------------------------------

    Returns back pages as list of Document Objects.
    Document(page_content='', metadata={'source': 'D:\\SUBIR\\LEARNING\\GenAI\\ChatBot\\chainlit-chatbot-interface\\LLM-Apps-with-Chainlit\\src\\Documents\\MSA.pdf', 'page': 0})

    """

    # Get the embeddings
    print(f"pageSplits = {pageSplits}")
    embedding = OpenAIEmbeddings()
    pageSplitEmbeddings = [embedding.embed_documents(split.page_content) for split in pageSplits]
    print(f"pageSplitEmbeddings = {pageSplitEmbeddings}")
    

