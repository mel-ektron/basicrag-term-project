# 🧠 BasicRAG: Akıllı Doküman Asistanı (Term Project)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-🦜️🔗-green?style=for-the-badge)
![Google Gemini](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-orange?style=for-the-badge&logo=google)

> **"Dokümanlarınızı sadece okumayın, onlarla matematiksel bir derinlikte konuşun."**

BasicRAG, Google'ın **Gemini 1.5 Flash** modelini ve **LangChain** kütüphanesini kullanarak, PDF ve metin belgelerinizden anlamlı bilgiler çıkaran bir **Retrieval-Augmented Generation (RAG)** sistemidir.

---

## 🚀 Öne Çıkan Özellikler

* **⚡ Gemini 1.5 Flash Entegrasyonu:** Düşük gecikme süresi ve yüksek doğrulukla metin üretimi.
* **📚 Gelişmiş Doküman İşleme:** PDF dosyalarını parçalara ayırıp (chunking) vektör uzayına taşıma.
* **🔍 Semantik Arama:** Sorularınıza sadece anahtar kelimeyle değil, cümlenin anlamıyla cevap bulur.
* **🧠 Hafıza Desteği:** Konuşmanın geçmişini hatırlar ve takip sorularına cevap verebilir.

---

## 🏗️ Çalışma Mantığı

Sistem temel olarak şu adımları izler:

1.  **Ingestion:** PDF/Text dokümanları okunur.
2.  **Splitting:** Uzun metinler küçük, anlamlı parçalara bölünür.
3.  **Embedding:** Her parça, Google'ın embedding modelleri ile vektörlere (sayısal dizilere) dönüştürülür.
4.  **Retrieval:** Sorunuzla en alakalı metin parçaları vektör veritabanından çağrılır.
5.  **Generation:** Gemini (ya da OpenAI), bu parçaları kullanarak size en doğru yanıtı verir.



---

## 🛠️ Kurulum - Repoyu Klonlayın
```bash
git clone [https://github.com/mel-ektron/basicrag-term-project.git](https://github.com/mel-ektron/basicrag-term-project.git)
cd basicrag-term-project

## Proje Akışı
basicrag-term-project/
├── 🐍 main.py             # Başlatıcı dosya
  ├── 🐍 rag_engine.py       # RAG 
    ──── gemini_basic_rag.ipnyb
     ──── openai_basic_rag.ipynb
├── 📂 data/               # PDF ve dökümanların saklandığı klasör
├── 📄 .env                # API Key (Gizli tutulmalıdır)
├── 📄 requirements.txt    # Gerekli paketler
└── 📄 README.md           # Proje dökümantasyonu