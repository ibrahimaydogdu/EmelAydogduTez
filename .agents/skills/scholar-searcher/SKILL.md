---
name: scholar-searcher
description: >-
  Stage 2 skill: Performs autonomous academic literature search on Google Scholar,
  extracts articles, metadata, citations, and abstracts, storing them in scholar_database.json.
---

# Scholar Searcher (Aşama 2 Yeteneği)

Bu yetenek, Aşama 1'de belirlenen temalar ve arama sorguları doğrultusunda Google Scholar üzerinden otonom veri toplama işlemini yürütür.

## Kullanılan Araçlar
- `search_google_scholar` MCP aracı veya `google-scholar search` CLI aracı.
- Web search / DOI / arXiv / ResearchGate çözücüleri.

## İş Akışı

1. **Sorguları Alma:**
   - `memory/active_project.json` içerisindeki `search_queries` listesini okur.
2. **Otonom Tarama:**
   - Her bir sorgu için Scholar taraması yapar (`num_results: 5`).
   - Öncelikli olarak SSCI / Scopus Q1 ve Q2 dergilerde yayımlanmış makaleleri ve yüksek atıflı çalışmaları tespit eder.
3. **Veri Çıkarma:**
   - Başlık, yazarlar, yayın yılı, dergi adı, özet (abstract), alıntı sayısı, makale linki (`pub_url`) ve BibTeX kaydını toplar.
4. **Veritabanına Kayıt:**
   - Verileri tekilleştirerek `memory/scholar_database.json` dosyasına yazar.
   - Her alt tema için en az 3-4 kilit makale seçilmesini temin eder.
