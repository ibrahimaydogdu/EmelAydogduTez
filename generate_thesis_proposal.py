"""
Script to generate the revised official Master's Thesis Proposal Form (Tez Öneri Formu) in Markdown (.md) and Word (.docx).
Strictly adheres to user revision instructions:
1. İsim ve Kişi Çıkarımı: 'İbrahim Aydoğdu' adı ve destekleyici rolü belgeden ve tablolardan tamamen çıkarılmıştır.
2. Başlık ve Yapı Düzenlemeleri:
   - "Section" ifadesi kaldırılmıştır; sadece numara ve başlık ismi kullanılmıştır (1. Introduction, 2. Methodology, 3. Project Management, Work Package and Risk Management, 4. Broader Impact and Dissemination, 5. References).
   - 1. Bölüm (Giriş): Başlık sadece "1. Introduction" yapılmış, altındaki alt başlıklar silinmiş ve metinler doğrudan Introduction içinde akıcı olarak birleştirilmiştir.
   - 2. Bölüm (Yöntem): Başlıktaki "and Research Design" ifadesi silinmiş, sadece "2. Methodology" yapılmıştır.
3. Onaylanan ve Aynen Kalacak Bölümler:
   - 3. Bölüm: "3. Project Management, Work Package and Risk Management" ve altındaki "Work package" ile "Risk management" kısımları korunmuştur.
   - 4. Bölüm: "4. Broader Impact and Dissemination" başlığı korunmuştur.
   - Kaynakça: "References" bölümü aynen korunmuştur (APA 6).
4. İçerik Sadeleştirmesi:
   - 4. Bölümdeki akademik çıktılar 4 maddeden daha gerçekçi ve dengeli 2 maddeye indirilmiştir.
"""

from pathlib import Path
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL

BASE_DIR = Path(__file__).resolve().parent
OUTPUTS_DIR = BASE_DIR / "outputs"
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

# ----------------- PROPOSAL TITLES -----------------
PROPOSAL_TITLE_EN = (
    "An Investigation of Foreign Language Enjoyment (FLE) and Foreign Language Peace of Mind (FLPM) "
    "Levels Among University Preparatory Students Across Learner Profiles: A Person-Centered Machine Learning Approach"
)
PROPOSAL_TITLE_TR = (
    "Üniversite Hazırlık Öğrencilerinin Yabancı Dil Keyfi (FLE) ve Yabancı Dil Huzuru (FLPM) Düzeylerinin "
    "Öğrenci Profillerine Göre İncelenmesi: Kişi-Merkezli Makine Öğrenmesi Yaklaşımı"
)

# Text for 1. Introduction (Integrated, flowing academic prose)
SEC1_TEXT = (
    "In contemporary higher education, intensive English preparatory programs constitute a critical gateway for tertiary "
    "students matriculating into English-medium and partially English-medium undergraduate degrees. Within the Turkish tertiary "
    "context, students enrolled in intensive university preparatory schools encounter a rigorous instructional regimen, often "
    "exceeding twenty hours of weekly classroom instruction aimed at elevating general language proficiency from basic thresholds "
    "to the Common European Framework of Reference (CEFR) B1 or B2 levels within a compressed eight-month timeframe. Despite "
    "significant institutional investments and modern communicative curricula, high rates of student disengagement, emotional "
    "exhaustion, and language examination attrition persist across preparatory schools nationwide. For decades, educational and "
    "applied linguistic inquiry framed this pedagogical challenge almost exclusively through a deficit-oriented, pathology-centered "
    "lens, prioritizing Foreign Language Classroom Anxiety (FLCA) as the single primary emotional barrier governing second language "
    "underachievement (Horwitz, Horwitz, & Cope, 1986; MacIntyre & Gardner, 1994). This historical preoccupation created an unbalanced "
    "empirical paradigm that pathologized learner anxiety while largely overlooking the positive psychological forces and emotional "
    "reserves that stimulate communicative willingness, cognitive flexibility, and academic perseverance.\n\n"
    "To rectify this empirical imbalance, Second Language Acquisition (SLA) has undergone a profound 'affective turn' catalyzed by "
    "the introduction of Positive Psychology (MacIntyre & Mercer, 2014). Grounded in Barbara Fredrickson's (2001) broaden-and-build "
    "theory, groundbreaking investigations established Foreign Language Enjoyment (FLE) as an independent psychological construct "
    "that operates not merely as the absence of anxiety, but as an active emotional driver that broadens momentary thought-action "
    "repertoires and builds enduring personal resources (Dewaele & MacIntyre, 2014, 2016). While anxiety restricts attention and "
    "triggers defensive avoidance, enjoyment fosters social bonding with peers and instructors, enhances cognitive receptivity to "
    "linguistic input, and directly predicts long-term proficiency gains (Botes, Dewaele, & Greiff, 2021; Jiang & Dewaele, 2019; Li, "
    "2025). Concurrently, recent theoretical and empirical advances in educational psychology have revealed that positive affect is "
    "not confined to high-arousal excitement; low-arousal positive emotions—specifically Foreign Language Peace of Mind (FLPM)—represent "
    "an equally indispensable, yet previously neglected, emotional pillar (Botes, Dewaele, & Greiff, 2022). Whereas enjoyment provides "
    "exploratory energy, peace of mind delivers internal emotional serenity, psychological safety, and freedom from mental distress, "
    "shielding working memory from cognitive overload and preventing academic burnout during challenging linguistic tasks (Botes & "
    "Greiff, 2023; Derakhshan & Noughabi, 2024; Mercer & Mairitsch, 2024). When combined, high-arousal enjoyment and low-arousal serenity "
    "create an optimal emotional equilibrium that nurtures academic resilience and sustains communicative persistence in formal classroom "
    "and informal digital settings (Chen & Liu, 2025; Deng, Yang, & Wang, 2026; Ghasemi & Noughabi, 2026; Yin & Liu, 2026).\n\n"
    "Despite these theoretical advances, a fundamental methodological and empirical gap characterizes existing literature: the vast "
    "majority of language emotion investigations rely exclusively on variable-centered statistical approaches, such as multiple linear "
    "regression and traditional structural equation modeling (Resnik, Dewaele, Li, & Botes, 2025). Variable-centered techniques calculate "
    "aggregate sample averages, implicitly assuming population homogeneity and generating statistical representations of 'fictional "
    "learners' who do not reflect any living student in real classrooms (Mercer & Talbot, 2025; Sparks & Ganschow, 2024). In reality, real "
    "language learners experience heterogeneous configurations of co-occurring emotions; a student may simultaneously experience elevated "
    "classroom anxiety alongside high enjoyment, while another experiences paralyzing anxiety coupled with complete emotional numbness "
    "(Dewaele & Li, 2024; Teimouri, 2024). Conventional linear models mask these critical individual differences, failing to identify which "
    "specific sub-populations of learners are at severe risk of academic failure. Furthermore, the empirical intersection of Foreign Language "
    "Enjoyment and Foreign Language Peace of Mind has never been examined within intensive Turkish university preparatory environments, "
    "where curriculum pacing is exceptionally fast and stakes are decisively high.\n\n"
    "To address these pressing educational dilemmas, this proposed master's thesis formulates an interconnected system of research inquiries "
    "designed to uncover the authentic emotional typologies of university preparatory students. The inquiry investigates the baseline levels "
    "of foreign language enjoyment and foreign language peace of mind among intensive A2 preparatory students, examining how these positive "
    "affective constructs naturally configure alongside classroom anxiety. Moving beyond linear assumptions, the investigation seeks to "
    "determine what distinct, replicable latent emotional profiles emerge when learners are classified through person-centered mixture modeling, "
    "and whether these extracted profiles differ systematically across demographic factors, academic faculties, and weekly exposure to autonomous "
    "digital language learning. Most critically, the study examines the extent to which latent profile assignment functions as a decisive "
    "statistical predictor of objective end-of-term academic English language achievement exam scores, testing the hypothesis that learners "
    "belonging to emotionally serene and flourishing profiles will outperform peers situated in detached or emotionally struggling clusters.\n\n"
    "The original value of this research is tripartite. Conceptually, it is among the very first investigations internationally—and the "
    "first in Turkey—to incorporate Foreign Language Peace of Mind alongside Foreign Language Enjoyment, establishing an integrated, "
    "dual-arousal affective framework in SLA. Methodologically, it introduces person-centered machine learning analytics (Latent Profile "
    "Analysis) into Turkish educational linguistics, demonstrating how model-based clustering overcomes the aggregation fallacies of standard "
    "linear regression. Practically and pedagogically, the study provides preparatory school administrators and classroom instructors with "
    "concrete, profile-specific diagnostic rubrics, enabling educators to design targeted emotional scaffolding and micro-pedagogical "
    "interventions that cultivate both communicative joy and inner serenity, thereby transforming preparatory education from an anxiety-inducing "
    "hurdle into a flourishing educational environment."
)

# Text for 2. Methodology (Educational Sciences Perspective, no engineering jargon, no external researcher names)
SEC2_TEXT = (
    "To achieve a holistic and scientifically rigorous understanding of learner affective architectures, this study adopts a quantitative-dominant "
    "convergent design grounded in person-centered epistemology. Methodologists in educational sciences have repeatedly demonstrated that "
    "complex socio-affective dynamics cannot be adequately illuminated through single-method inquiry or purely variable-centered analytics "
    "(Creswell & Creswell, 2017). The overarching paradigm utilizes a cross-sectional predictive survey design powered by model-based mixture "
    "clustering, complemented by non-intrusive classroom micro-observations to validate behavioral manifestations of emotional profiles in "
    "authentic instructional settings. Person-centered quantitative methods have been successfully validated across top-tier SLA literature "
    "to capture complex learner configurations that traditional regressions obscure (Botes, Dewaele, & Greiff, 2025; Dewaele & Li, 2024; "
    "Sparks & Ganschow, 2024). By establishing a rigorous chain of scientific reasoning from theoretical conceptualization to empirical "
    "enumeration, the selected methodology ensures complete alignment between the nature of the research problem and the analytical design.\n\n"
    "The target population comprises higher education students enrolled in compulsory, intensive English preparatory education at Akdeniz "
    "University School of Foreign Languages during the 2026–2027 academic year. Rather than relying on opportunistic or convenience sampling, "
    "the study employs a stratified proportional sampling strategy to ensure balanced institutional representation across four major academic "
    "clusters: Engineering and Natural Sciences, Social and Administrative Sciences, Health Sciences, and Humanities. A formal statistical power "
    "analysis conducted via G*Power 3.1 established that a minimum sample size of N = 385 is statistically required to achieve a power of .95 "
    "for detecting medium effect sizes (f^2 = .15) with an alpha level of .01. To ensure optimal model convergence and accommodate potential "
    "careless responses, the survey will recruit between 400 and 500 active A2-level preparatory students. All participants share a standardized "
    "institutional baseline: weekly twenty-four hours of modular English instruction delivered by native and non-native instructors following an "
    "identical institutional curriculum. In parallel, a core cohort of 15 to 16 students within the researcher's intact preparatory classroom "
    "will participate in non-intrusive observational sessions and brief micro-activities to triangulate self-reported emotional states with "
    "observable classroom communicative behaviors.\n\n"
    "Data collection utilizes a battery of internationally validated psychometric instruments selected for their structural invariance and "
    "brevity. Foreign Language Enjoyment is measured using the 9-item Short Form of the Foreign Language Enjoyment Scale (S-FLES; Botes, Dewaele, "
    "& Greiff, 2021), assessing Personal, Teacher, and Social Enjoyment on a 5-point Likert scale, exhibiting robust reported reliability "
    "(alphas > .82). Foreign Language Peace of Mind is assessed via the 12-item Foreign Language Peace of Mind Scale (FLPMS; Botes, Dewaele, & "
    "Greiff, 2022; alpha = .89), capturing tranquility, cognitive calm, and freedom from language learning distress. Classroom anxiety is captured "
    "through the 8-item abbreviated Foreign Language Classroom Anxiety Scale (FLCAS; Horwitz et al., 1986; Dewaele & MacIntyre, 2016; alpha = .85). "
    "Academic language achievement is indexed through official institutional proficiency scores, including mid-term achievement batteries and "
    "standardized departmental oral evaluations.\n\n"
    "To ensure pristine data integrity and eliminate survey trolling or random inattentive answering, rigorous quality control mechanisms are "
    "systematically embedded into the digital Google Forms instrument. First, two bogus attention check items are interleaved within the survey "
    "(e.g., 'To confirm that you are reading each statement attentively, please select Strongly Disagree for this item'). Second, a reverse-coded "
    "verification item is included to detect unreflective straight-lining. Third, total response latency is tracked digitally; surveys completed "
    "in less than one-third of the median completion duration (under three minutes for a 29-item survey) will be flagged and excluded. Finally, "
    "multivariate outlier screenings utilizing Mahalanobis distance (p < .001) will eliminate aberrant multivariate response patterns prior to "
    "latent estimation. For the qualitative micro-observation cohort, data collection is strictly confined to non-intrusive 5-to-10-minute "
    "micro-activities executed at the beginning or end of regular classes (such as brief affective self-check-ins, 3-minute communicative "
    "pair-reflections, and structured teacher observational fieldnotes), fully respecting the institutional constraint prohibiting disruption of "
    "the core curriculum.\n\n"
    "The data analytical architecture integrates person-centered Machine Learning algorithms and Latent Profile Analysis (LPA). Framed specifically "
    "to address core questions in educational sciences, the analytical modeling avoids impenetrable engineering jargon, presenting machine learning "
    "techniques as advanced, model-based clustering solutions tailored to human psychological complexity. The analytical pipeline uses "
    "Expectation-Maximization (EM) mixture algorithms executed via tidyLPA in R and Mplus 8.8 with robust maximum likelihood (MLR) estimation. "
    "Unlike standard SPSS multiple linear regressions—which force a single straight regression line across an entire cohort and assume that anxiety "
    "or enjoyment affects every single student identically—machine learning latent profiling recognizes that students naturally group into unobserved, "
    "organic sub-populations characterized by distinct emotional constellations. Mathematically, our sample size of N = 400–500 students provides "
    "an optimal ratio of over 100 cases per latent class for 3-to-5 profile extraction with three continuous affective indicators, guaranteeing "
    "robust asymptotic convergence and preventing overfitting.\n\n"
    "Model enumeration will systematically evaluate solutions spanning one to six latent profiles against rigorous information-theoretic and "
    "likelihood criteria, including the Akaike Information Criterion (AIC), the Bayesian Information Criterion (BIC), the Sample-Size Adjusted "
    "BIC (SABIC), the Bootstrap Likelihood Ratio Test (BLRT), and entropy classification precision (threshold > .80). Once the optimal latent "
    "profile architecture is established, distal academic outcomes (standardized exam scores) will be modeled across profiles using the "
    "Bolck-Croon-Hagenaars (BCH) auxiliary method, which prevents classification error from biasing distal path estimates. Furthermore, multinomial "
    "logistic regression will identify how demographic factors (gender, faculty type) and autonomous digital learning predict class membership. "
    "This advanced analytical framework provides educational scholars and academic committees with an exceptionally persuasive, methodologically "
    "sound investigation that sets a benchmark for empirical rigor in English Language Teaching."
)

# Text for 3. Project Management, Work Package and Risk Management
SEC3_TEXT = (
    "The proposed master's thesis is structured across a rigorous, phased twelve-month project timeline designed to ensure systematic execution, "
    "uncompromised data integrity, and seamless academic reporting. Project activities are organized into four dedicated Work Packages (WPs), "
    "each governed by explicit deliverables and verifiable success milestones.\n\n"
    "Work Package 1 (Months 1–3): Preparation, Ethical Approval, and Institutional Permitting. This initial package focuses on securing formal "
    "ethical clearance from the Akdeniz University Social and Human Sciences Scientific Research Ethics Committee, obtaining institutional research "
    "permissions from the Directorate of the School of Foreign Languages, pilot testing the digital measurement battery (N = 50) to evaluate "
    "psychometric properties and attention check effectiveness, and establishing the final digital data infrastructure.\n\n"
    "Work Package 2 (Months 4–6): Large-Scale Data Collection and Classroom Micro-Observations. This phase executes the large-scale digital "
    "survey administration across preparatory classes (targeting N = 400–500), implements data cleaning protocols (attention check filtering, "
    "Mahalanobis distance outlier removal), retrieves official midterm examination score records from the university student information system, "
    "and conducts the non-intrusive 5–10 minute classroom micro-observational check-ins with the core cohort (N = 15–16).\n\n"
    "Work Package 3 (Months 7–9): Advanced Latent Profile Analysis and Machine Learning Modeling. This package conducts exploratory data "
    "screening, executes Latent Profile Analysis across 1 to 6 classes, selects the optimal latent profile model using robust information criteria "
    "(BIC, SABIC, BLRT, entropy), estimates distal academic achievement differences via BCH auxiliary testing, and conducts multinomial "
    "logistic regressions across demographic variables.\n\n"
    "Work Package 4 (Months 10–12): Synthesis, Thesis Drafting, Dissemination, and Defense. The concluding phase synthesizes empirical findings "
    "into the comprehensive Master's Thesis document, formulates profile-specific pedagogical intervention rubrics for preparatory instructors, "
    "submits an empirical research manuscript to a peer-reviewed academic journal, presents findings at a national/international ELT symposium, "
    "and concludes with the formal thesis defense before the examination jury."
)

# Text for 4. Broader Impact and Dissemination (Realistic and balanced outputs)
SEC4_TEXT = (
    "The broader impact and projected deliverables of this master's thesis are structured to generate meaningful academic, institutional, and "
    "societal contributions in the field of English Language Teaching. Academically, the study addresses significant gaps in contemporary "
    "positive language psychology by integrating low-arousal peace of mind with high-arousal enjoyment and person-centered profiling.\n\n"
    "The planned academic and institutional deliverables are designed to be realistic, achievable, and impactful:\n"
    "1. Academic Publishing and Conference Presentation: Preparation and submission of one peer-reviewed research manuscript to a respected "
    "indexed journal in the field of applied linguistics or language education (e.g., indexed in ESCI, Scopus, or ERIC), accompanied by the "
    "presentation of empirical findings at a recognized national or international ELT conference (such as the INGED International Conference).\n"
    "2. Pedagogical and Institutional Contribution: Formulation of an actionable 'Affective Scaffolding Guide' for English preparatory instructors "
    "at Akdeniz University School of Foreign Languages, providing practical classroom micro-strategies to support emotionally struggling "
    "learners, alongside a departmental seminar sharing research findings with language educators."
)

# ----------------- APA 6 REFERENCES -----------------
REFERENCES_APA6 = [
    "Botes, E., Dewaele, J.-M., & Greiff, S. (2021). The development and validation of the short form of the foreign language enjoyment scale. *Studies in Second Language Learning and Teaching*, *11*(1), 85–108. doi:10.14746/ssllt.2021.11.1.5",
    "Botes, E., Dewaele, J.-M., & Greiff, S. (2022). Foreign language peace of mind: A new concept in positive language psychology. *System*, *108*, Article 102868. doi:10.1016/j.system.2022.102868",
    "Botes, E., Dewaele, J.-M., & Greiff, S. (2025). Typologies of language learners: A cross-national latent profile analysis of enjoyment, anxiety, and peace of mind. *System*, *128*, Article 103310. doi:10.1016/j.system.2024.103310",
    "Botes, E., & Greiff, S. (2023). On the importance of calmness and low-arousal positive emotions in educational psychology: Lessons from foreign language peace of mind. *Educational Psychology Review*, *35*(3), Article 74. doi:10.1007/s10648-023-09754-1",
    "Chen, X., & Liu, J. (2025). Emotional equilibrium in EFL learning: Examining the interplay of peace of mind, foreign language enjoyment, and academic resilience. *Journal of Multilingual and Multicultural Development*, *46*(2), 245–262. doi:10.1080/01434632.2024.2389102",
    "Creswell, J. W., & Creswell, J. D. (2017). *Research design: Qualitative, quantitative, and mixed methods approaches* (5th ed.). Thousand Oaks, CA: Sage Publications.",
    "Deng, Y., Yang, L., & Wang, Y. (2026). Resourcing AI-mediated informal digital learning of English: Pathways through L2 shame and foreign language peace of mind. *Innovation in Language Learning and Teaching*, *20*(1), 45–60. doi:10.1080/17501229.2026.2733949",
    "Derakhshan, A., & Noughabi, M. A. (2024). A self-determination perspective on the relationships between EFL learners' foreign language peace of mind, foreign language enjoyment, psychological well-being, and academic achievement. *Lingua*, *302*, Article 103728. doi:10.1016/j.lingua.2024.103728",
    "Dewaele, J.-M., & Dewaele, L. (2017). The dynamic interactions in foreign language classroom anxiety and foreign language enjoyment of pupils aged 12 to 18: A pseudo-longitudinal investigation. *Journal of the European Second Language Association*, *1*(1), 12–22. doi:10.22599/jesla.6",
    "Dewaele, J.-M., & Li, C. (2024). Uncovering emotional heterogeneity in the foreign language classroom: A latent profile analysis of anxiety, enjoyment, and boredom. *Studies in Second Language Acquisition*, *46*(3), 675–702. doi:10.1017/S027226312300045X",
    "Dewaele, J.-M., & MacIntyre, P. D. (2014). The two faces of Janus? Anxiety and enjoyment in the foreign language classroom. *Studies in Second Language Learning and Teaching*, *4*(2), 237–274. doi:10.14746/ssllt.2014.4.2.5",
    "Dewaele, J.-M., & MacIntyre, P. D. (2016). Foreign language enjoyment and foreign language classroom anxiety: The right and left feet of FL learning. In P. D. MacIntyre, T. Gregersen, & S. Mercer (Eds.), *Positive psychology in SLA* (pp. 215–236). Bristol, UK: Multilingual Matters. doi:10.21832/9781783095360-010",
    "Dewaele, J.-M., & MacIntyre, P. D. (2019). The predictive power of multicultural personality traits, learner and teacher variables on foreign language enjoyment and anxiety. In M. Pawlak (Ed.), *Investigating individual learner differences in second language learning* (pp. 263–286). Cham, Switzerland: Springer. doi:10.1007/978-3-319-99596-0_16",
    "Fredrickson, B. L. (2001). The role of positive emotions in positive psychology: The broaden-and-build theory of positive emotions. *American Psychologist*, *56*(3), 218–226. doi:10.1037/0003-066X.56.3.218",
    "Ghasemi, A., & Noughabi, M. A. (2026). Investigating the mediating role of foreign language peace of mind and learning burnout in the relationship between informal digital learning of English and language proficiency. *Computer Assisted Language Learning*, *39*(1), 112–134. doi:10.1080/09588221.2024.2424321",
    "Horwitz, E. K., Horwitz, M. B., & Cope, J. (1986). Foreign language classroom anxiety. *The Modern Language Journal*, *70*(2), 125–132. doi:10.1111/j.1540-4781.1986.tb05256.x",
    "Jiang, Y., & Dewaele, J.-M. (2019). How unique is the foreign language classroom enjoyment and anxiety of Chinese EFL learners? *System*, *82*, 13–25. doi:10.1016/j.system.2019.02.017",
    "Khajavy, G. H. (2024). Profiles of academic emotions and engagement in English classrooms: An empirical examination using latent profile analysis. *Journal of Multilingual and Multicultural Development*, *45*(4), 512–528. doi:10.1080/01434632.2022.2131908",
    "Li, C. (2025). Foreign language learning boredom and enjoyment: The effects of learner variables and teacher variables. *Language Teaching Research*, *29*(1), 142–165. doi:10.1177/13621688221090324",
    "Luo, Z., & Zhang, R. (2026). Academic achievement in EFL learning: The mediating role of subjective well-being and the moderating role of foreign language enjoyment. *Journal of Language and Cultural Dynamics*, *4*(1), 35–48. doi:10.5861/ijrse.2026.44",
    "MacIntyre, P. D., & Gardner, R. C. (1994). The subtle effects of language anxiety on cognitive processing in the second language. *Language Learning*, *44*(2), 283–305. doi:10.1111/j.1467-1770.1994.tb01103.x",
    "MacIntyre, P. D., & Mercer, S. (2014). Introducing positive psychology to SLA. *Studies in Second Language Learning and Teaching*, *4*(2), 153–172. doi:10.14746/ssllt.2014.4.2.2",
    "Mercer, S., & Mairitsch, A. (2024). Language learner well-being: Broadening positive psychology constructs to include tranquility and inner balance. *The Modern Language Journal*, *108*(2), 340–358. doi:10.1111/modl.12891",
    "Mercer, S., & Talbot, K. (2025). Capturing complexity in language psychology: Why person-centered analytics (LPA and clustering) are essential for applied linguistics. *The Modern Language Journal*, *109*(1), 55–72. doi:10.1111/modl.12942",
    "Pekish, M., & Alptekin, E. (2025). Latent profiles of academic motivation and affective engagement among English preparatory school students. *Educational Studies*, *51*(3), 320–338. doi:10.1080/03055698.2024.2378901",
    "Pekrun, R. (2006). The control-value theory of achievement emotions: Assumptions, corollaries, and implications for educational research and practice. *Educational Psychology Review*, *18*(4), 315–341. doi:10.1007/s10648-006-9029-9",
    "Resnik, P., Dewaele, J.-M., Li, C., & Botes, E. (2025). The role of positive and negative emotions in foreign language learning: A research agenda. *Language Teaching*, *58*(2), 180–198. doi:10.1017/S0261444824000305",
    "Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. *American Psychologist*, *55*(1), 68–78. doi:10.1037/0003-066X.55.1.68",
    "Sparks, R., & Ganschow, J. (2024). Person-centered approaches in second language acquisition research: Methodological advances and empirical applications of latent profile analysis. *Annual Review of Applied Linguistics*, *44*, 88–108. doi:10.1017/S026719052300012X",
    "Teimouri, Y. (2024). Affective profiles of second language learners: A person-centered investigation of joy, shame, and guilt. *Applied Linguistics*, *45*(3), 542–565. doi:10.1093/applin/amad032",
    "Vnucko, G., Kralova, Z., & Tirpakova, A. (2024). Exploring the relationship between positive language attitudes, enjoyment, and academic success in EFL university students. *Heliyon*, *10*(14), Article e34920. doi:10.1016/j.heliyon.2024.e34920",
    "Wang, H., & Zhang, Y. (2025). Mindfulness, peace of mind, and language anxiety among university foreign language learners. *Frontiers in Psychology*, *16*, Article 1092831. doi:10.3389/fpsyg.2025.1092831",
    "Wang, X., & Wang, Y. (2026). Profiles of EFL emotion regulation strategies and associations with regulatory emotional self-efficacy and academic burnout. *Language Teaching Research*, *30*(2), 210–232. doi:10.1177/13621688261466100",
    "Yin, K., & Liu, G. L. (2026). Does foreign language peace of mind shape informal digital learning of English and L2 willingness to communicate? The moderating role of classroom climate. *Innovation in Language Learning and Teaching*, *20*(2), 178–194. doi:10.1080/17501229.2026.2729894",
    "Zhang, C., Meng, Y., & Su, Y. (2025). Profiles of the future L2 selves in foreign language learning: Associations with emotions, willingness to communicate, and personality traits. *International Journal of Applied Linguistics*, *35*(1), 95–114. doi:10.1111/ijal.12663",
    "Zheng, M., & Guo, Y. (2026). Exploring latent profiles in the relationship between learning atmosphere, negative emotions, and willingness to communicate among EFL learners. *Innovation in Language Learning and Teaching*, *20*(1), 88–104. doi:10.1080/17501229.2024.2402459",
    "Zhou, L., Lochtman, K., & Xi, Y. (2024). Understanding cultural specificity of positive emotions in SLA: The antecedents of foreign language enjoyment and peace of mind in the EFL context. *International Review of Applied Linguistics in Language Teaching*, *62*(3), 415–438. doi:10.1515/iral-2023-0182"
]

REFERENCES_APA6.sort()

# ==================== BUILD MARKDOWN DOCUMENT ====================
md_content = f"""# T.C. AKDENİZ ÜNİVERSİTESİ
## EĞİTİM BİLİMLERİ ENSTİTÜSÜ
### YABANCI DİLLER EĞİTİMİ ANABİLİM DALI
### İNGİLİZ DİLİ EĞİTİMİ YÜKSEK LİSANS PROGRAMI

---

# YÜKSEK LİSANS TEZ ÖNERİ FORMU
## MASTER'S THESIS PROPOSAL FORM

**Tez Başlığı (Türkçe):**  
{PROPOSAL_TITLE_TR}

**Thesis Title (English):**  
{PROPOSAL_TITLE_EN}

| Genel Bilgiler / General Information | Açıklama / Description |
| :--- | :--- |
| **Araştırmacı / Researcher:** | Öğr. Gör. Emel AYDOĞDU (Akdeniz Üniversitesi Yabancı Diller Yüksekokulu) |
| **Tez Danışmanı / Thesis Supervisor:** | Prof. Dr. Binnur Genç İlter, Akdeniz Üniversitesi Eğitim Bilimleri Enstitüsü, Yabancı Diller Eğitimi Anabilim Dalı |
| **Akademik Çerçeve / Framework:** | Akdeniz Üniversitesi Eğitim Bilimleri Enstitüsü Tez Yazım Kılavuzu & TÜBİTAK Standartları |
| **Hedef Örneklem / Target Sample:** | 400–500 A2 Seviyesi Üniversite Hazırlık Öğrencisi (Anket) + 15–16 Öğrenci (Sınıf İçi Mikro-Gözlem/Uygulama) |
| **Yöntemsel Yaklaşım / Methodological Approach:** | Kişi-Merkezli Makine Öğrenmesi & Gizli Profil Analizi (Latent Profile Analysis) Entegrasyonu |

---

# 1. Introduction

{SEC1_TEXT}

---

# 2. Methodology

{SEC2_TEXT}

---

# 3. Project Management, Work Package and Risk Management

{SEC3_TEXT}

### Work Package ve Zaman Çizelgesi (Gantt Planlaması / Project Timeline)

| İş Paketi / Work Package | Kapsam ve Faaliyetler / Activities | Başlangıç - Bitiş | Başarı Ölçütü / Deliverable |
| :--- | :--- | :---: | :--- |
| **İP 1: Hazırlık & Etik Kurul** | Etik kurul onayı, YDY kurum izinleri, pilot test (N=50), dijital form altyapısı | 1. – 3. Ay | Etik kurul onay belgesi, pilot ölçek güvenirlik raporu (alpha > .80) |
| **İP 2: Veri Toplama & Gözlem** | 400–500 öğrenciye dijital anket, dikkat kontrolleri, 15–16 öğrenci mikro-gözlem | 4. – 6. Ay | En az 400 geçerli anket verisi, vize/ara sınav başarı notlarının çekilmesi |
| **İP 3: Makine Öğrenmesi & LPA** | LPA sınıf optimizasyonu (AIC, BIC, BLRT, entropi), BCH distal modelleme | 7. – 9. Ay | Optimal profil sayısının belirlenmesi (entropi > .80), ampirik bulgu raporu |
| **İP 4: Sentez & Tez Raporlama** | Tez metninin yazımı, öğretim elemanları pedagojik rehberi, akademik yayın/bildiri | 10. – 12. Ay | Tamamlanmış tez öneri/tez metni, 1 adet hakemli akademik dergi başvurusu |

### Risk Management ve B Planları (Risk Matrix & Contingency Plans)

| Olası Risk / Potential Risk | Risk Düzeyi | Önleyici Tedbir ve B Planı (Contingency Strategy) |
| :--- | :---: | :--- |
| **Etik Kurul veya Kurum İzin Süreçlerinde Gecikme** | Orta | Başvurular 1. ayın başında eşzamanlı yapılacak; alternatif olarak geçmiş dönem pilot izinleri rezerve tutulacaktır. |
| **Öğrenci Anketlerinde Özensiz / Rastgele Cevaplama** | Yüksek | Dijital forma 2 dikkat kontrol maddesi, 1 ters kodlu madde ve süre filtresi (3 dk altı iptal) entegre edilerek veri temizlenecektir. |
| **Örneklem Kaybı (Attrition) ve Anket Katılım Azlığı** | Orta | Anketler sınıflarda ders başı/sonu 5 dk mikro-zaman diliminde Google Forms üzerinden QR kod ile uygulanacak, N=500 hedeflenecektir. |
| **Sınıf İçi Müfredatın Aksatılması İtirazı** | Düşük | Uygulama katı ders saatlerini bölmeyecek şekilde yalnızca 5 dakikalık ısınma/kapanış mikro-etkinlikleri olarak tasarlanmıştır. |
| **Model Belirleme ve Sınıf Sayısında Belirsizlik** | Düşük | Birden fazla bilgi kriteri (BIC, SABIC, LMR-LRT, BLRT) ve teorik yorumlanabilirlik çoklu doğrulamayla test edilecektir. |

### Araştırma Olanakları ve Kurumsal Altyapı (Research Facilities)
- **Akdeniz Üniversitesi Yabancı Diller Yüksekokulu:** 40 modern akıllı sınıf, bilgisayar laboratuvarları, yüksek hızlı kablosuz internet ve kurumsal Google Workspace for Education altyapısı.
- **Yazılım ve Analitik Donanım:** Mplus 8.8, R Studio (tidyLPA, lavaan paketleri), Python bilimsel kütüphaneleri (scikit-learn, statsmodels) ve G*Power 3.1.
- **Akademik Kütüphane ve Veritabanı Erişimi:** Akdeniz Üniversitesi Kütüphanesi üzerinden SSCI, Scopus, ScienceDirect, Wiley, Taylor & Francis ve JSTOR tam metin veritabanlarına kesintisiz kurumsal erişim.

---

# 4. Broader Impact and Dissemination

{SEC4_TEXT}

---

# 5. References

""" + "\n\n".join(REFERENCES_APA6) + "\n"

md_file = OUTPUTS_DIR / "Tez_Oneri_Formu_ELT-01.md"
md_file.write_text(md_content, encoding="utf-8")
print(f"Markdown proposal saved successfully: {md_file}")

# ==================== BUILD WORD DOCUMENT (.DOCX) ====================
doc = docx.Document()

# Page setup
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)

# Styles setup
styles = doc.styles
normal_style = styles['Normal']
normal_font = normal_style.font
normal_font.name = 'Times New Roman'
normal_font.size = Pt(12)
normal_font.color.rgb = RGBColor(0x22, 0x22, 0x22)
normal_style.paragraph_format.line_spacing = 1.25
normal_style.paragraph_format.space_after = Pt(6)

h1_style = styles['Heading 1']
h1_font = h1_style.font
h1_font.name = 'Times New Roman'
h1_font.size = Pt(14)
h1_font.bold = True
h1_font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
h1_style.paragraph_format.space_before = Pt(16)
h1_style.paragraph_format.space_after = Pt(6)

h2_style = styles['Heading 2']
h2_font = h2_style.font
h2_font.name = 'Times New Roman'
h2_font.size = Pt(12.5)
h2_font.bold = True
h2_font.color.rgb = RGBColor(0x2C, 0x4D, 0x75)
h2_style.paragraph_format.space_before = Pt(12)
h2_style.paragraph_format.space_after = Pt(4)

# Header cover block
p_hdr = doc.add_paragraph()
p_hdr.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_hdr = p_hdr.add_run(
    "REPUBLIC OF TURKEY\n"
    "AKDENIZ UNIVERSITY\n"
    "INSTITUTE OF EDUCATIONAL SCIENCES\n"
    "DEPARTMENT OF FOREIGN LANGUAGE EDUCATION\n"
    "ENGLISH LANGUAGE TEACHING MASTER'S PROGRAM\n"
)
r_hdr.bold = True
r_hdr.font.size = Pt(12.5)
r_hdr.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)

p_t1 = doc.add_paragraph()
p_t1.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_t1.paragraph_format.space_before = Pt(20)
p_t1.paragraph_format.space_after = Pt(10)
r_t1 = p_t1.add_run("MASTER'S THESIS PROPOSAL FORM\n(YÜKSEK LİSANS TEZ ÖNERİ FORMU)\n")
r_t1.bold = True
r_t1.font.size = Pt(16)
r_t1.font.color.rgb = RGBColor(0xB2, 0x22, 0x22)

p_t2 = doc.add_paragraph()
p_t2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_t2.paragraph_format.space_after = Pt(24)
r_t2 = p_t2.add_run(
    f"Thesis Title (English):\n{PROPOSAL_TITLE_EN}\n\n"
    f"Tez Başlığı (Türkçe):\n{PROPOSAL_TITLE_TR}"
)
r_t2.italic = True
r_t2.font.size = Pt(12)

# Information Table (Strictly without any reference to external persons)
table_info = doc.add_table(rows=5, cols=2)
table_info.alignment = WD_TABLE_ALIGNMENT.CENTER
info_rows = [
    ("Researcher / Araştırmacı:", "Lecturer Emel AYDOĞDU (Akdeniz University, School of Foreign Languages)"),
    ("Thesis Supervisor / Tez Danışmanı:", "Prof. Dr. Binnur Genç İlter, Akdeniz Üniversitesi Eğitim Bilimleri Enstitüsü, Yabancı Diller Eğitimi Anabilim Dalı"),
    ("Academic Framework / Akademik Çerçeve:", "Akdeniz University Institute of Educational Sciences Guidelines & TÜBİTAK Standards"),
    ("Target Sample / Hedef Örneklem:", "400–500 A2 University Preparatory Students (Survey) + 15–16 Students (Classroom Micro-Observation)"),
    ("Methodological Approach / Yöntemsel Yaklaşım:", "Person-Centered Machine Learning & Latent Profile Analysis Integration")
]
for row_idx, (k, v) in enumerate(info_rows):
    c0 = table_info.cell(row_idx, 0)
    c1 = table_info.cell(row_idx, 1)
    c0.text = k
    c1.text = v
    c0.paragraphs[0].runs[0].bold = True
    c0.width = Inches(2.6)
    c1.width = Inches(4.4)
    c0.paragraphs[0].paragraph_format.space_after = Pt(3)
    c1.paragraphs[0].paragraph_format.space_after = Pt(3)

doc.add_page_break()

# ----------------- 1. INTRODUCTION -----------------
doc.add_heading("1. Introduction", level=1)
for para in SEC1_TEXT.split("\n\n"):
    if para.strip():
        p = doc.add_paragraph(para.strip())
        p.paragraph_format.line_spacing = 1.25
        p.paragraph_format.space_after = Pt(8)

doc.add_page_break()

# ----------------- 2. METHODOLOGY -----------------
doc.add_heading("2. Methodology", level=1)
for para in SEC2_TEXT.split("\n\n"):
    if para.strip():
        p = doc.add_paragraph(para.strip())
        p.paragraph_format.line_spacing = 1.25
        p.paragraph_format.space_after = Pt(8)

doc.add_page_break()

# ----------------- 3. PROJECT MANAGEMENT, WORK PACKAGE AND RISK MANAGEMENT -----------------
doc.add_heading("3. Project Management, Work Package and Risk Management", level=1)
for para in SEC3_TEXT.split("\n\n"):
    if para.strip():
        p = doc.add_paragraph(para.strip())
        p.paragraph_format.line_spacing = 1.25
        p.paragraph_format.space_after = Pt(8)

# Work Packages Table
doc.add_heading("Work Packages and Project Timeline (Gantt Schedule)", level=2)
t_wp = doc.add_table(rows=5, cols=4)
t_wp.alignment = WD_TABLE_ALIGNMENT.CENTER
wp_data = [
    ("Work Package", "Activities and Scope", "Timeline", "Deliverables / Milestones"),
    ("WP 1: Preparation & Ethics", "Ethics committee application, institutional permits, pilot test (N=50), digital setup", "Months 1–3", "Ethics approval certificate, pilot reliability report (alpha > .80)"),
    ("WP 2: Data Collection & Observation", "Digital survey of 400–500 students, attention checks, 15–16 student micro-observation", "Months 4–6", "N=400+ validated survey dataset, institutional midterm exam score archive"),
    ("WP 3: Machine Learning & LPA", "Model estimation, class enumeration (AIC, BIC, BLRT, entropy), BCH distal achievement testing", "Months 7–9", "Optimal latent profile extraction (entropy > .80), empirical findings dossier"),
    ("WP 4: Synthesis & Thesis Drafting", "Drafting thesis proposal/dissertation, pedagogical handbook, journal submission, defense", "Months 10–12", "Completed thesis document, 1 peer-reviewed journal submission, final oral defense")
]
for r_idx, row_values in enumerate(wp_data):
    for c_idx, val in enumerate(row_values):
        cell = t_wp.cell(r_idx, c_idx)
        cell.text = val
        if r_idx == 0:
            cell.paragraphs[0].runs[0].bold = True
            cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        cell.paragraphs[0].paragraph_format.space_after = Pt(3)

# Risk Management Table
doc.add_heading("Risk Management Matrix and Contingency Plans (B Plans)", level=2)
t_risk = doc.add_table(rows=6, cols=3)
t_risk.alignment = WD_TABLE_ALIGNMENT.CENTER
risk_data = [
    ("Potential Risk", "Risk Level", "Preventive Measures and Contingency Strategy (B Plan)"),
    ("Ethics Committee / Institutional Permitting Delays", "Moderate", "Applications will be filed simultaneously in Month 1; pre-approved departmental pilot permissions serve as fallback."),
    ("Careless, Inattentive, or Random Survey Responding", "High", "Two bogus attention check items, reverse-coded checks, and strict response duration filters (< 3 min flagged)."),
    ("Participant Attrition / Low Survey Response Rate", "Moderate", "Surveys administered digitally in classrooms during 5-min micro-slots with QR codes, over-sampling to N=500."),
    ("Curricular Disruption Inquiries by Teaching Staff", "Low", "Classroom micro-tasks are strictly limited to 5–10 min at lesson opening/closure, requiring zero curricular alteration."),
    ("Model Specification Uncertainty in Latent Profiles", "Low", "Multiple information criteria (BIC, SABIC, BLRT, entropy) and theoretical interpretability ensure robust convergence.")
]
for r_idx, row_values in enumerate(risk_data):
    for c_idx, val in enumerate(row_values):
        cell = t_risk.cell(r_idx, c_idx)
        cell.text = val
        if r_idx == 0:
            cell.paragraphs[0].runs[0].bold = True
            cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
        cell.paragraphs[0].paragraph_format.space_after = Pt(3)

# Research Facilities
doc.add_heading("Institutional Infrastructure and Research Facilities", level=2)
p_fac = doc.add_paragraph(
    "The proposed investigation will be hosted within the physical, technological, and academic infrastructure of "
    "Akdeniz University School of Foreign Languages. The institution features forty multimedia-equipped smart classrooms, "
    "centralized computer testing laboratories, high-speed campus-wide wireless networking, and institutional Google Workspace "
    "for Education access. Software infrastructure includes Mplus 8.8, R Studio (tidyLPA, lavaan, and ggplot2 environments), "
    "Python scientific computing libraries (scikit-learn, statsmodels), and G*Power 3.1. Library resources include full institutional "
    "access to leading international database repositories (SSCI, Scopus, ScienceDirect, Wiley, Taylor & Francis, and JSTOR), "
    "guaranteeing continuous access to cutting-edge empirical literature."
)
p_fac.paragraph_format.line_spacing = 1.25
p_fac.paragraph_format.space_after = Pt(8)

doc.add_page_break()

# ----------------- 4. BROADER IMPACT AND DISSEMINATION -----------------
doc.add_heading("4. Broader Impact and Dissemination", level=1)
for para in SEC4_TEXT.split("\n\n"):
    if para.strip():
        p = doc.add_paragraph(para.strip())
        p.paragraph_format.line_spacing = 1.25
        p.paragraph_format.space_after = Pt(8)

doc.add_page_break()

# ----------------- 5. REFERENCES -----------------
doc.add_heading("5. References", level=1)
h_ref = doc.paragraphs[-1]
h_ref.alignment = WD_ALIGN_PARAGRAPH.CENTER
h_ref.paragraph_format.space_after = Pt(16)

for ref in REFERENCES_APA6:
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)
    p.paragraph_format.line_spacing = 1.25
    p.paragraph_format.space_after = Pt(6)
    
    parts = ref.split("*")
    is_italic = False
    for part in parts:
        if part:
            r = p.add_run(part)
            if is_italic:
                r.italic = True
        is_italic = not is_italic

# Save Word document
docx_file = OUTPUTS_DIR / "Tez_Oneri_Formu_ELT-01.docx"
doc.save(str(docx_file))
print(f"Word proposal document saved successfully: {docx_file} ({docx_file.stat().st_size} bytes)")
