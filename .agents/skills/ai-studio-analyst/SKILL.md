---
name: ai-studio-analyst
description: >-
  Stage 1 skill: Analyzes the chosen thesis topic based on AI Studio context,
  generates 3-4 specific research questions, 2-3 sub-themes, and precision
  academic search queries for Google Scholar.
---

# AI Studio Analyst (Aşama 1 Yeteneği)

Bu yetenek, seçilen tez konusunu sahadaki kısıtlılıklar (A2 hazırlık, 300-400 anket, max 5-10 dk ders içi mikro-uygulama) ve akademik beklentiler (Binnur Hoca & İbrahim Hoca) çerçevesinde yapılandırır.

## Yapılacak İşlemler

1. **Konu Seçimi ve Yükleme:**
   - `memory/candidate_topics.json` dosyasından seçilen konunun detaylarını çeker.
2. **Araştırma Soruları ve Hipotezlerin Üretilmesi:**
   - 1 ana araştırma sorusu ve 3-4 alt araştırma sorusu formüle eder.
3. **Alt Temaların Belirlenmesi:**
   - Konuyla ilgili literatür taramasının yapılacağı 2-3 temel alt temayı (başlığı) saptar.
4. **Hassas Arama Sorguları (Keywords):**
   - Google Scholar'da taranmak üzere uluslararası akademik terminolojiye (ELT / Applied Linguistics) uygun İngilizce sorgular üretir (yıl aralıkları ve yazar isimleriyle birlikte).
5. **Kayıt:**
   - Tüm bu çıktıları `memory/active_project.json` dosyasına kaydeder ve State Tracker'ı günceller.
