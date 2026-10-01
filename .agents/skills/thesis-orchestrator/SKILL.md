---
name: thesis-orchestrator
description: >-
  Master orchestrator skill for the autonomous thesis preparation pipeline.
  Coordinates AI Studio analysis, Google Scholar literature search, NotebookLM
  in-depth summarization, and Antigravity Thesis Proposal Form generation.
---

# Thesis Orchestrator (Ana Orkestratör)

Bu yetenek, Emel Aydoğdu'nun yüksek lisans tez çalışması için tasarlanan 4 aşamalı otonom boru hattının (pipeline) ana yönetim merkezidir.

## Temel Görevler

1. **İş Akışı Kontrolü:** 4 aşamayı sırasıyla tetikler ve aşama geçiş şartlarını denetler. Her aşama sonunda kullanıcı kontrolü ve ONAYI alır.
2. **Hafıza Yönetimi:** `memory/` dizinindeki veritabanlarını (`user_profile.json`, `candidate_topics.json`, `active_project.json`, `scholar_database.json`, `state_tracker.json`) güncel tutar.
3. **Rol ve Kısıt Uyumu:** `01_role_and_boundaries.md` ve `02_academic_standards.md` kurallarının her aşamada titizlikle uygulanmasını sağlar.

## Aşama Tetikleme Protokolü

### 1. Aşama: AI Studio Analizörü
- **Yetenek:** `ai-studio-analyst`
- Seçilen tez konusunu alır (`AI-01`, `ELT-01` vb.).
- Konuya ait problem durumunu, 3-4 alt araştırma sorusunu, 2-3 alt temayı ve Scholar arama sorgularını üretip `memory/active_project.json`'a yazar.

### 2. Aşama: Scholar Taraması
- **Yetenek:** `scholar-searcher`
- Üretilen sorgularla Google Scholar üzerinde arama yapar (`google-scholar` CLI veya MCP).
- Her tema için en az 10 adet (toplam 30 makale) tespit edip `memory/scholar_database.json`'a işler.

### 3. Aşama: Derinlemesine Özetleme ve Literatür Raporu
- **Yetenek:** `notebooklm-synthesizer`
- 30 makalenin tamamı için 300-500 kelime bandında, akıcı akademik İngilizce düzyazı, alt başlıksız ve madde işaretsiz, doğrudan temel bulgularla biten genişletilmiş literatür raporu üretir (`outputs/Genisletilmis_Literatur_Ozetleri_<konu_kodu>.docx`).

### 4. Aşama: Sentez ve Tez Öneri Formu
- **Yetenek:** `proposal-writer`
- 5-15 sayfa uzunluğunda, Akdeniz Üniversitesi / TÜBİTAK standartlarına uygun 5 ana bölümden oluşan resmi Tez Öneri Formunu oluşturur:
  1. 1. Introduction (1-3 sayfaya daraltılmış literatür, akıcı araştırma soruları ve özgün değer; tek ana başlık).
  2. 2. Methodology (Eğitim bilimleri bakış açısı, 400-500 anket + 15-16 gözlem, dikkat kontrolleri, kişi-merkezli Makine Öğrenmesi / LPA yöntemlerinin sözel-ikna edici anlatımı; harici kişi ismi içermez).
  3. 3. Project Management, Work Package and Risk Management (Gantt çizelgesi, B planları, araştırma olanakları).
  4. 4. Broader Impact and Dissemination (Gerçekçi akademik yayın ve bildiri hedefleri, pedagojik rehber ve toplumsal katkı).
  5. 5. References (APA 6 formatında doğrudan liste).
- Çıktılar: `outputs/Tez_Oneri_Formu_<konu_kodu>.md` ve `.docx`.
