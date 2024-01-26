from langchain_community.document_loaders import PyPDFLoader

# PDF LOADER
def docLoader(docList):
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
    docs = []
    
    for loader in loaders:
        docs.append(loader.load())

    print(f"docs: {docs}")
    return docs
