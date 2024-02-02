from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

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
        docList : Document
    ------------------------------

    Returns back pages as list of Document Objects.
    Document(page_content='', metadata={'source': 'D:\\SUBIR\\LEARNING\\GenAI\\ChatBot\\chainlit-chatbot-interface\\LLM-Apps-with-Chainlit\\src\\Documents\\MSA.pdf', 'page': 0})

    """

    r_splitter= RecursiveCharacterTextSplitter(
        chunk_size= 50,
        chunk_overlap= 5,
        
        separators=[". "]
        #separators= [". ","[1-12]","[.|((?<=\\n)|(?<=\\r))]"]
        #separators= ["\n\n","\n","."," ",""]
    )

    docSplits= r_splitter.split_documents(pages)


    print(f"DocSplits =  {docSplits}")
    print(f"Length of Pages: {len(pages)}")
    print(f"Length of DocSplits: {len(docSplits)}")

    return docSplits
