---
trigger: always_on
---

# 4 Aşamalı Otonom İş Akışı ve Pipeline Kuralları

Bu belge, Antigravity orkestrasyonunda yürütülen 4 aşamalı tez hazırlama sisteminin çalışma ve geçiş kurallarını belirler.

---

## 1. Boru Hattı (Pipeline) Aşamaları

```
[Aşama 1: AI Studio] ➔ [Aşama 2: Google Scholar] ➔ [Aşama 3: NotebookLM] ➔ [Aşama 4: Antigravity]
(Konu, Sorular, Tema)    (Tarama, Abstract, BibTeX)    (300-500k Akıcı Özet)    (Tez Öneri Formu & Docx)
```

---

## 2. Aşama Geçiş Kuralları (Gates)

### Aşama 1: Konu Analizi ve Anahtar Kelime Üretimi
- **Girdi:** 8 aday konudan seçilen bir konu (veya kullanıcının girdiği yeni bir konu).
- **İşlem:** Araştırma soruları belirlenir, 2-3 alt tema çıkarılır, Google Scholar için spesifik İngilizce arama sorguları/anahtar kelimeleri türetilir.
- **Çıktı & Kayıt:** `memory/active_project.json` dosyası güncellenir.
- **Geçiş Şartı:** En az 3 araştırma sorusu, 2 alt tema ve en az 4 hassas arama sorgusu üretilip kaydedilmiş olmalıdır.

### Aşama 2: Literatür Taraması (Google Scholar)
- **Girdi:** `memory/active_project.json` içindeki arama sorguları.
- **İşlem:** `search_google_scholar` MCP aracı veya CLI ile aramalar yapılır. Her tema için en az 10 yüksek nitelikli (Q1/Q2/Q3 veya yüksek atıflı) makale seçilir.
- **Geçiş Şartı:** Veritabanına her tema için 10 adet olmak üzere toplam 30 adet doğrudan konuyla ilişkili makale eklenmiş ve üniversite ağı üzerinden temin edilebilen PDF'ler `papers/` klasörüne indirilmiş olmalıdır.

### Aşama 3: Derinlemesine Analiz ve Özetleme (NotebookLM)
- **Girdi:** `memory/scholar_database.json` içindeki makale verileri.
- **İşlem:** Her makale için `02_academic_standards.md` kurallarına uygun, 300-500 kelimelik, alt başlıksız ve madde işaretsiz, doğrudan temel bulgularla sonlanan akıcı akademik İngilizce metinler üretilir.
- **Çıktı & Kayıt:** `outputs/Genisletilmis_Literatur_Ozetleri_<konu_kodu>.docx` dosyası oluşturulur.
- **Geçiş Şartı:** 30 makalenin tamamı için 300-500 kelime bandında doğrulanmış özetler oluşturulmuş ve kullanıcı onayı alınmış olmalıdır.

### Aşama 4: Sentez ve Tez Öneri Formu Raporlama (Antigravity)
- **Girdi:** `memory/summaries/` içindeki özetler, genişletilmiş literatür raporu ve `memory/active_project.json`.
- **İşlem:** Akdeniz Üniversitesi / TÜBİTAK standartlarında 5-15 sayfa uzunluğunda, 5 ana bölümden oluşan kapsamlı Tez Öneri Formu hazırlanır:
  1. 1. Introduction (1-3 sayfaya daraltılmış entegre literatür, araştırma boşluğu, akıcı araştırma soruları ve özgün değer; tek ana başlık altında).
  2. 2. Methodology (Eğitim bilimleri bakış açısı, yöntem gerekçesi ve atıflar, 400-500 anket + 15-16 gözlem örneklemi, dikkat kontrollü araçlar, kişi-merkezli makine öğrenmesi / LPA analizlerinin sözel-ikna edici anlatımı; harici kişi ismi içermez).
  3. 3. Project Management, Work Package and Risk Management (Gantt zaman çizelgesi, veri toplama ve izin risklerine karşı B planları, araştırma olanakları).
  4. 4. Broader Impact and Dissemination (Gerçekçi akademik yayın ve bildiri hedefleri, pedagojik rehber ve toplumsal katkı).
  5. 5. References (APA 6 formatında doğrudan liste).
- **Çıktı & Kayıt:** 
  - `outputs/Tez_Oneri_Formu_<konu_kodu>.md`
  - `outputs/Tez_Oneri_Formu_<konu_kodu>.docx` (Word formatı)
- **Geçiş Şartı:** Formun tüm akademik bölümleri eksiksiz doldurulmuş, APA 6 referansları kontrol edilmiş ve çıktı dosyaları yazılmış olmalıdır.

---

## 3. Hafıza ve Durum Yönetimi (Memory & State Tracker)
- Her aşama başlangıcında ve bitiminde `memory/state_tracker.json` güncellenir.
- Sistem kesintiye uğrasa dahi, kullanıcı bir sonraki komutta kaldığı aşamadan itibaren devam edebilir.
- Her aşama sonunda kullanıcıdan kontrol ve ONAY talep edilir.
