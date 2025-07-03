# 🌍 Afet Uyarı ve Müdahale Bilgi Asistanı

Bu proje, **BTK Akademi Hackathon 2025** kapsamında geliştirilmiştir. Amaç; Türkiye'deki şehirlerin afet risklerine göre vatandaşlara **önleyici bilgi ve müdahale önerileri sunan bir yapay zeka destekli bilgi asistanı** oluşturmaktır.

Uygulama, kullanıcının seçtiği şehre göre olası afet türlerini belirler ve **Gemini 2.5 Flash** modeli aracılığıyla sade, anlaşılır, maddeler halinde öneriler üretir.

---

## 🚀 Özellikler

- ✅ Şehir bazlı afet risk analiz sistemi (örnek JSON veri tabanı ile)
- 🤖 Google Gemini API ile öneri üretimi (yapay zeka tabanlı)
- 💬 Markdown çıktısını HTML’ye çevirme desteği
- 🔁 Form gönderiminde loading (spinner) animasyonu
- 🧠 Flask framework ile hızlı prototipleme
- 📁 Temiz ve modüler proje yapısı

---

## 🔧 Kullanılan Teknolojiler

| Katman | Teknoloji |
|--------|-----------|
| Backend | Python 3.10+ |
| Framework | Flask |
| AI | Google Gemini (gemini-2.5-flash) |
| Arayüz | HTML, CSS, Vanilla JS |
| Veri | Yerel JSON dosyası (şehir-risk eşlemesi) |
| Güvenlik | .env ile gizli API anahtarı yönetimi |

---

## ⚙️ Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/HyperWorth/afet_yard-m_ai.git
cd afet_yard-m_ai
````

2. Ortamı oluşturun ve bağımlılıkları yükleyin:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. `.env` dosyasını oluşturun:

```
GEMINI_API_KEY=senin_gemini_api_anahtarin
```

4. Uygulamayı çalıştırın:

```bash
flask run
```

5. Tarayıcıda aç: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📸 Ekran Görüntüsü
 
https://github.com/user-attachments/assets/91634d52-5bd7-4dd8-b767-3d5f926ba508


---

## 💡 Geliştirilecek Özellikler

* [ ] Gerçek afet risk verileri ile entegrasyon (AFAD, MTA vb.)
* [ ] Kullanıcının konumuna göre şehir seçimi (geo-location)
* [ ] Harita destekli görsel seçim arayüzü
* [ ] JSON yerine veritabanı kullanımı (SQLite veya PostgreSQL)
* [ ] Çok dilli destek (TR/EN)
* [ ] PDF çıktı veya e-posta ile gönderim

---

## 📁 Proje Yapısı


```
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── gemini_api.py
│   ├── risk_data.json
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
├── run.py
├── .env
├── requirements.txt
├── README.md
```

---

## 📄 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasını inceleyin.

---

## 👤 Geliştirici

* Ad Soyad: \[HyperWorth]
* GitHub: [[github.com/kullanici-adi](https://github.com/HyperWorth)


---

