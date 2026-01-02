# 🧠 BasicRAG: Akıllı Doküman Asistanı (Term Project)

> **"Dokümanlarınızı sadece okumayın, onlarla matematiksel bir derinlikte konuşun."**

BasicRAG, Google'ın **Gemini 1.5 Flash** modelini ve **LangChain** kütüphanesini kullanarak, PDF ve metin belgelerinizden anlamlı bilgiler çıkaran bir **Retrieval-Augmented Generation (RAG)** sistemidir.
Öxellikle bu proje Cacio e Pepe'nin faz evreleri hakkındaki makale üzerine kurulmuştur.
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
5.  **Generation:** Gemini, bu parçaları kullanarak size en doğru yanıtı verir.



---

## 🛠️ Kurulum

### 1. Repoyu Klonlayın
```bash
git clone [https://github.com/mel-ektron/basicrag-term-project.git](https://github.com/mel-ektron/basicrag-term-project.git)
cd basicrag-term-project

basicrag-term-project/
├── 🐍 main.py             # Başlatıcı dosya
├── 🐍 rag_engine.py       # RAG 
├── 📂 makale.pdf          # makale
├── 📄 .env                # API Key 
├── 📄 requirements.txt    # Gerekli paketler
└── 📄 README.md           # Proje dökümantasyonu
