from llama_index.core import StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI

def setup_query_engine():
    # Initialize the storage context with default persistence directory
    storage_context = StorageContext.from_defaults(persist_dir="./stores")

    # Load the index from the specified storage context
    index = load_index_from_storage(storage_context)

    # Initialize the LLM with the desired model
    llm = OpenAI(model="gpt-3.5-turbo")
    
    # Create a query engine using the index and LLM
    query_engine = index.as_query_engine(llm=llm)

    return query_engine

def query_response(query_engine, user_query):
    system_prompt = f"""
    Your job is to provide accurate and relevant information to the user. 
    You are USIM AI assistant and you have access to data related to USIM.
    USIM is a university which in full name is Universiti Sains Islam Malaysia.
    You can provide information about the university, its courses, faculties, and other relevant information.
    Provide only accurate and relevant information to the user, if you do not have the information, please inform the user.
    """
    full_query = f"{system_prompt}\n\n{user_query}"
    
    # Execute the query using the query engine
    result = query_engine.query(full_query)
    return result
