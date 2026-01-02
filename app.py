import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

primaryColor = "#F63366"
backgroundColor = "#D0C60FCE"
secondaryBackgroundColor = "#8C8CF0"
textColor = "#262730"
font = "sans serif"

import streamlit as st

# Önceki ayarların (Kreme arka plan ve Pizza ikonu)
st.set_page_config(page_title="Pizza Bot", page_icon="🍕")

# --- AÇILIŞ MESAJI MANTIĞI ---

# 1. Eğer hafızada mesaj listesi yoksa oluştur
if "messages" not in st.session_state:
    st.session_state.messages = []
    
    # 2. Listeyi oluştururken İLK mesajı biz ekliyoruz (Açılış Mesajı)
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hi there! "
    })

# --- MESAJLARI GÖSTERME ---

# 3. Geçmişteki tüm mesajları (açılış mesajı dahil) ekrana yazdır
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- KULLANICI GİRDİSİ ---
# .env yükle
load_dotenv()

st.title("This is the Chef! 🍕 ")

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
    model="gemini-2.0-flash",
    temperature=0.3,
    max_tokens=500
)

# 3. Prompt
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "You are an italian chef"
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
query = st.chat_input("Lets talk about the sauce")

if query:
    with st.spinner("Thinking about it..."):
        response = chain.invoke(
            {
                "context": context,
                "question": query
            }
        )

    st.write("**AI:**")
    st.write(response)
