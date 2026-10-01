# Otonom Tez Öneri Formu ve Literatür Boru Hattı (Master Prompt)

Bu sistem; **Antigravity**, **Google AI Studio**, **Google Scholar** ve **NotebookLM** araçlarını birbirine bağlayarak, İngiliz Dili Eğitimi (ELT) alanında yüksek lisans tez konusu için otonom literatür taraması yapan, 500-600 kelimelik derinlemesine makale özetleri çıkaran ve akademik formatta nihai **Tez Öneri Formu (Word/Markdown)** üreten entegre bir yapay zeka boru hattıdır.

---

## 1. Paydaşlar, Rol ve Sınırlar (`.agents/rules/01_role_and_boundaries.md`)

* **Araştırmacı:** Öğr. Gör. Emel Aydoğdu (Akdeniz Üniversitesi Yabancı Diller Yüksekokulu).
* **Öğrenci Profili:** A2 seviyesi üniversite hazırlık öğrencileri (Haftalık 12 saat ders yükü).
* **Örneklem:** Okul genelinde Google Forms ile ulaşılabilecek 300 - 400 hazırlık öğrencisi.
* **Ders İçi Sınır:** Katı müfredat nedeniyle ders içinde en fazla **5-10 dakikalık mikro-etkinlik** yapılabilir (uzun ders içi deneysel uygulama yapılamaz).
* **Tez Danışmanı:** Binnur Hoca (Sağlam kuramsal zemin, hazır/geçerli ölçekler, kusursuz jüri savunması beklentisi).
* **Teknik ve İleri Veri Analizi:** Prof. Dr. İbrahim Aydoğdu (İnşaat Mühendisliği; Makine Öğrenmesi, Kümeleme - LPA, Yapısal Eşitlik Modeli - SEM, Ağ Analizi).

---

## 2. Sistem Mimarisi ve 4 Aşamalı İş Akışı

```
                     ┌──────────────────────────────────────────────┐
                     │          ANTIGRAVITY (Orkestratör)           │
                     │          Master Prompt & State Machine       │
                     └──────────────────────┬───────────────────────┘
                                            │
       ┌──────────────────┬─────────────────┴─────────────────┬──────────────────┐
       ▼                  ▼                                   ▼                  ▼
┌──────────────┐   ┌──────────────┐                   ┌──────────────┐   ┌──────────────┐
│   AŞAMA 1    │   │   AŞAMA 2    │                   │   AŞAMA 3    │   │   AŞAMA 4    │
│  AI Studio   │   │Google Scholar│                   │  NotebookLM  │   │ Antigravity  │
├──────────────┤   ├──────────────┤                   ├──────────────┤   ├──────────────┤
│• Konu Seçimi │   │• Otonom      │                   │• nlm CLI/MCP │   │• Literatür   │
│• Araştırma   │   │  Makale      │                   │• 500-600     │   │  Sentezi     │
│  Soruları    │   │  Taraması    │                   │  Kelime Derin│   │• Tez Öneri   │
│• 2-3 Alt Tema│   │• Q1/Q2 Seçimi│                   │  Özetler     │   │  Formu       │
│• Arama       │   │• Abstract ve │                   │  (6 Bölümlü) │   │• Word (.docx)│
│  Sorguları   │   │  BibTeX      │                   │              │   │  & Markdown  │
└──────────────┘   └──────────────┘                   └──────────────┘   └──────────────┘
```

---

## 3. Hazır Aday Tez Konuları (`memory/candidate_topics.json`)

Google AI Studio ön hazırlık sohbetinden çıkarılan ve tüm saha kısıtlarınıza uyan 8 konu:

### A. Yapay Zeka Odaklı Konular (Teknik ve Yenilikçi)
1. **[AI-01] ML ile Başarı Tahmini:** Hazırlık öğrencilerinin YZ kullanım alışkanlıkları ve özerklikleri üzerinden başarılarının makine öğrenmesiyle tahmin edilmesi (Ders içi yük: 0 dk).
2. **[AI-02] Teknoloji Kabul Modeli (TAM) ve AI:** A2 öğrencilerinin üretken yapay zeka araçlarını kabul düzeyleri ve dil öğrenme stratejileri (SEM analizi, Ders içi yük: 0 dk).
3. **[AI-03] Prompt Engineering ve Öğrenci Etkileşimi:** Öğrencilerin yapay zeka ile diyalog ve istemlerinin taksonomik analizi (Kendi sınıfında 5-10 dk mikro-aktivite).

### B. Ana Akım ELT Konuları (Pozitif Psikoloji & Çağdaş Yaklaşımlar)
4. **[ELT-01] Pozitif Psikoloji (Dil Keyfi ve Huzur):** Yabancı Dil Keyfi (FLE) ve Huzuru (FLPM) düzeylerinin Latent Profile Analysis ile incelenmesi (Dewaele akımı).
5. **[ELT-02] Siber Kaytarma (Cyberloafing) ve Öz-Düzenleme:** Derste telefonla ilgilenme davranışlarının dil öğrenme stratejileriyle ilişkisi.
6. **[ELT-03] Mikro-Oyunlaştırma ve Kelime Öğrenimi:** Dersin son 5 dakikasında puan/rozet/yarışma unsurlarının kelime motivasyonuna etkisi.
7. **[ELT-04] İletişim Kurmaya İsteklilik (WTC) ve Dijital Okuryazarlık:** WTC teorisinin dijital beceriler ve SEM yol analiziyle modellenmesi.
8. **[ELT-05] Akademik Yılmazlık ve Ters Yüz Sınıf (Flipped Learning):** Pes etmeme (resilience) becerisinin ters yüz öğrenmeye hazırbulunuşlukla ilişkisi.

---

## 4. Sistemi Çalıştırma Komutları (Master Prompt)

Sistemi başlatmak için bu sohbette aşağıdaki komutlardan birini vermeniz yeterlidir:

### Seçenek 1: Konu Seçerek Tam Otonom Başlatma
> **"Seçtiğim konu: [AI-01]. Boru hattını başlat."**  
*(Veya listedeki herhangi bir konu: `AI-02`, `AI-03`, `ELT-01`, `ELT-02`, `ELT-03`, `ELT-04`, `ELT-05`)*

Bu komutu verdiğinizde sistem:
1. `memory/active_project.json` dosyasına konuyu işler, araştırma sorularını ve Scholar anahtar kelimelerini üretir.
2. Google Scholar üzerinden otomatik olarak makaleleri tarar ve `memory/scholar_database.json`'a kaydeder.
3. NotebookLM'e aktararak her makale için 500-600 kelimelik yapılandırılmış özetler üretir (`memory/summaries/`).
4. Literatürü sentezleyip resmi Tez Öneri Formunu (`outputs/Tez_Oneri_Formu.md` ve `.docx`) oluşturur.

### Seçenek 2: Aşama Aşama Onaylı İlerleme
> **"Seçtiğim konu: [ELT-01]. Sadece 1. Aşamayı çalıştır ve bana araştırma soruları ile alt temaları sun."**
