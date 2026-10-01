---
name: notebooklm-synthesizer
description: >-
  Stage 3 skill: Leverages Gemini Notebook (NotebookLM) CLI and MCP to create notebooks,
  ingest sources, and generate structured 500-600 word in-depth academic literature summaries.
---

# NotebookLM Synthesizer (Aşama 3 Yeteneği)

Bu yetenek, Google Scholar tarafından toplanan makale verilerini NotebookLM'e aktararak her biri için 500-600 kelimelik derinlemesine akademik özetler üretir.

## Kullanılan Araçlar
- `nlm` CLI araçları (`nlm notebook create`, `nlm source add`, `nlm query`, `nlm report`).
- `gemini-notebook-mcp` MCP araçları (`notebook_create`, `source_add`, `notebook_query`).

## 500-600 Kelimelik Özetleme Formatı
Her makale için aşağıdaki 6 bölüm eksiksiz üretilir:
1. **Künye ve Kuramsal Arka Plan (~75 kelime):** APA 7 künye ve temel alınan teori.
2. **Araştırmanın Amacı ve Araştırma Soruları (~75 kelime):** Çözülmek istenen problem ve sorular.
3. **Metodoloji ve Örneklem (~100 kelime):** Katılımcılar, veri toplama araçları, ölçekler.
4. **Veri Analiz Yöntemleri (~75 kelime):** İstatistiksel veya nitel analiz süreçleri.
5. **Temel Bulgular ve Sonuçlar (~150 kelime):** İstatistiksel bulgular, doğrulanmış hipotezler.
6. **Emel Hoca'nın Tez Çalışmasına Katkısı ve Araştırma Boşluğu (Research Gap) (~75-100 kelime):** Bizim teze sağladığı zemin ve dolduracağımız literatür boşluğu.

## Çıktı Dosyaları
- Her makale özeti `memory/summaries/ozet_<bib_id>.md` olarak kaydedilir.
