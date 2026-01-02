import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# .env yükle
load_dotenv()

st.title("Cacio e Pepe Chef! ")

# 1. PDF Yükle ve Böl
@st.cache_resource
def load_pdf():
    loader = PyPDFLoader("2501.00536v3.pdf")
    data = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(data)

    # Hepsini tek string yap
    return "\n\n".join(doc.page_content for doc in docs)

context = load_pdf()

# 2. LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    max_tokens=500
)

# 3. Prompt
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following context to answer the question. "
    "If you don't know the answer, say that you don't know. "
    "Use three sentences maximum.\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{question}")
    ]
)

chain = prompt | llm | StrOutputParser()

# 4. UI
query = st.chat_input("Sorunuzu yazın:")

if query:
    with st.spinner("Cevap hazırlanıyor..."):
        response = chain.invoke(
            {
                "context": context,
                "question": query
            }
        )

    st.write("**AI:**")
    st.write(response)
