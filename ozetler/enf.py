T('enf', "ATS/IDSA 2019 TKP, Surviving Sepsis 2021, IDSA 2021 C. difficile, IDSA 2024 dirençli Gram negatif, DSÖ ve Sağlık Bakanlığı TB rehberi, DHHS HIV kılavuzu, ESCMID")

S("Toplum kökenli pnömoni", ["pnömoni","tkp","curb-65","makrolid","florokinolon","atipik","legionella","seftriakson"], """
- CURB-65: konfüzyon, üre >7 mmol/L (BUN >19 mg/dL), solunum ≥30, KB <90/≤60, yaş ≥65. 0-1 ayaktan, 2 yatış, ≥3 ağır.
- Ayaktan, komorbiditesiz: amoksisilin veya doksisiklin (makrolid yalnız direnç <%25'te).
- Ayaktan, komorbiditeli: amoksisilin-klavulanat/sefalosporin + makrolid veya doksisiklin; ya da solunum florokinolonu.
- Yatan, ağır olmayan: beta laktam + makrolid veya solunum florokinolonu.
- Ağır: beta laktam + makrolid (veya florokinolon). Önceden MRSA/Pseudomonas izolasyonu varsa kapsama eklenir.
- Ağır TKP'de hidrokortizon mortaliteyi azaltabilir (CAPE COD); influenzada steroid verilmez.
- Süre: klinik stabilite sağlandıysa en az 5 gün.
| Etken | İpucu |
| Legionella | Hiponatremi, ishal, KC enzimleri, idrar antijeni |
| Mikoplazma | Genç, soğuk aglütinin, büllöz miringit |
| S. aureus | İnfluenza sonrası, kavite |
| Klebsiella | Alkolizm, frenk üzümü jölesi balgam |
""")

S("Sepsis", ["sepsis","septik şok","sofa","qsofa","laktat","norepinefrin","vazopressin","hidrokortizon"], """
- Sepsis-3: enfeksiyon + SOFA'da ≥2 puan artış. Septik şok: MAP ≥65 için vazopressör gerekmesi + laktat >2 mmol/L (yeterli sıvıya rağmen).
- qSOFA tek başına tarama aracı olarak önerilmez.
- Şokta antibiyotik ilk 1 saat içinde; şok yoksa ve sepsis olası ise 3 saat içinde.
- Sıvı: ilk 3 saatte ≥30 mL/kg kristaloid (dengeli solüsyon tercih).
- İlk vazopressör norepinefrin; doz arttıkça vazopressin eklenir; kardiyak disfonksiyonda dobutamin.
- Süren vazopressör ihtiyacında hidrokortizon 200 mg/gün.
- Laktat izlemi ve kapiller dolum yanıtı resüsitasyona rehberlik eder.
! Kaynak kontrolü (abse drenajı, enfekte kateter çekilmesi) pratik olarak en kısa sürede yapılır.
""")

S("Tüberküloz", ["tüberküloz","tbc","latent","igra","ppd","izoniazid","rifampisin","pirazinamid","etambutol","mdr","bpalm"], """
- Latent TB tanısı: IGRA veya PPD; aktif hastalık dışlanır (akciğer grafisi).
- Latent tedavi seçenekleri: 3HP (12 hafta haftalık izoniazid + rifapentin), 4R (4 ay rifampisin), 3HR, 6-9 ay izoniazid.
- Anti-TNF öncesi tarama zorunlu; latent tedavi başladıktan ≥1 ay sonra biyolojik başlanabilir.
- Aktif TB: 2 ay HRZE + 4 ay HR. SSS ve kemik tutulumunda süre uzar (9-12 ay); TB menenjit ve perikarditte steroid.
| İlaç | Önemli yan etki |
| İzoniazid | Hepatit, periferik nöropati (B6 profilaksisi), ilaç ilişkili lupus |
| Rifampisin | Hepatit, turuncu sekresyon, güçlü enzim indükleyici (OKS, varfarin, HIV ilaçları) |
| Pirazinamid | Hepatotoksisite (en sık), hiperürisemi, artralji |
| Etambutol | Optik nörit (kırmızı-yeşil renk körlüğü) |
- İlaca dirençli TB: BPaLM (bedakilin, pretomanid, linezolid, moksifloksasin) 6 ay.
! Hepatotoksisitede (ALT >3 × ÜSN + semptom veya >5 × ÜSN) tüm ilaçlar kesilir, düzelince tek tek eklenir.
""")

S("HIV", ["hiv","antiretroviral","cd4","fırsatçı","pcp","pnömosistis","toksoplazma","iris","prep","viral yük"], """
- Tanı: 4. kuşak antijen/antikor testi; pozitifse ayırt edici test ve HIV RNA.
- Tanı konan herkese mümkün olan en kısa sürede ART (CD4'ten bağımsız). İlk tedavi: integraz inhibitörü temelli; bictegravir/TAF/FTC veya dolutegravir + TAF/TDF + FTC/3TC; seçilmiş hastada dolutegravir + lamivudin.
- Kriptokok ve TB menenjitinde ART birkaç hafta ertelenir (IRIS ve mortalite riski).
| CD4 eşiği | Profilaksi |
| <200 /µL | PCP: TMP-SMX |
| <100 /µL + Toxo IgG (+) | Toksoplazma: TMP-SMX |
| <50 /µL | MAC: ART başlanıyorsa rutin önerilmez |
- PCP: subakut nefes darlığı, LDH yüksek, bilateral buzlu cam; PaO2 <70 ise steroid eklenir.
- IRIS: ART başlandıktan sonra haftalar içinde fırsatçı enfeksiyonun alevlenmesi; çoğunlukla ART sürdürülür.
- PrEP: TDF/FTC günlük, kabotegravir 2 ayda bir IM, lenakapavir 6 ayda bir SC.
! Saptanamayan viral yük = bulaştırmaz (B=B).
""")

S("Menenjit ve ensefalit", ["menenjit","ensefalit","lomber ponksiyon","bos","deksametazon","listeria","hsv","asiklovir","meningokok"], """
- Ampirik tedavi: 18-50 yaş seftriakson + vankomisin; >50 yaş, gebe, alkolik, immünsüprese → + ampisilin (Listeria).
- Deksametazon antibiyotikten hemen önce veya birlikte (pnömokokta mortaliteyi azaltır); 4 gün.
- LP öncesi BT: immünsüpresyon, SSS hastalığı öyküsü, yeni nöbet, papil ödemi, bilinç bozukluğu, fokal nörolojik bulgu. BT bekleniyorsa antibiyotik geciktirilmez.
| BOS | Hücre | Glukoz | Protein |
| Bakteriyel | PMNL, binler | Düşük (<%40 serum) | Yüksek |
| Viral | Lenfosit, <500 | Normal | Normal/hafif yüksek |
| TB | Lenfosit | Düşük | Çok yüksek |
| Kriptokok | Lenfosit | Düşük | Yüksek; açılış basıncı yüksek |
- HSV ensefaliti: ateş, davranış değişikliği, temporal lob tutulumu; şüphede hemen IV asiklovir; BOS HSV PCR.
- Meningokok temaslılarına profilaksi: siprofloksasin tek doz, rifampisin veya seftriakson.
""")

S("Hastane enfeksiyonları ve direnç", ["clostridioides","difficile","fidaksomisin","vankomisin","mrsa","bakteriyemi","esbl","karbapenem","kpc","seftazidim-avibaktam","sefiderokol","kateter"], """
- C. difficile: ilk atakta fidaksomisin (tercih) veya oral vankomisin 10 gün. Fulminan: oral/rektal vankomisin + IV metronidazol. Tekrarlayan: fidaksomisin; çoklu tekrarda fekal mikrobiyota nakli.
- S. aureus bakteriyemisi: her zaman ciddiye alınır; kontrol kan kültürü, ekokardiyografi (çoğunda TEE), kateter çekilir. Komplike olmayan en az 14 gün IV.
- MSSA: sefazolin veya antistafilokokal penisilin (vankomisinden üstün). MRSA: vankomisin veya daptomisin (pnömonide daptomisin kullanılmaz).
| Direnç | Tedavi |
| ESBL | Karbapenem (ciddi enfeksiyonda pip-tazo değil) |
| KPC tipi karbapenemaz | Seftazidim-avibaktam, meropenem-vaborbaktam, imipenem-relebaktam |
| OXA-48 | Seftazidim-avibaktam |
| Metallo-beta laktamaz (NDM) | Seftazidim-avibaktam + aztreonam veya sefiderokol |
| DTR P. aeruginosa | Seftolozan-tazobaktam, seftazidim-avibaktam |
| Karbapenem dirençli Acinetobacter | Sulbaktam-durlobaktam temelli kombinasyon |
- Kandidemi: ekinokandin; tüm kateterler çekilir, göz dibi muayenesi, ilk negatif kültürden sonra 14 gün.
""")

S("Zoonozlar ve bölgesel enfeksiyonlar", ["bruselloz","brusella","kırım-kongo","kkka","kene","tularemi","şarbon","eskar","hayvancılık","leptospiroz","kist hidatik","ekinokok","q ateşi","sıtma","amip","ameb"], """
| Hastalık | İpucu | Tedavi |
| Bruselloz | Çiğ süt/peynir, dalgalı ateş, terleme, sakroiliit, spondilit | Doksisiklin + rifampisin 6 hafta veya doksisiklin + streptomisin/gentamisin; spondilitte ≥3 ay |
| KKKA | Kene, ateş, kanama, trombositopeni, lökopeni, AST/LDH/CK yüksek | Destek tedavi; ribavirinin yararı tartışmalı; temas izolasyonu |
| Tularemi | Kaynak su (Türkiye'de orofaringeal form), servikal LAP | Gentamisin/streptomisin; hafifte siprofloksasin veya doksisiklin |
| Leptospiroz | Su/kemirgen, konjunktival sufüzyon, Weil (sarılık + AKİ) | Penisilin, seftriakson veya doksisiklin |
| Kist hidatik | Karaciğer/akciğer kisti, anafilaksi riski | Albendazol + PAIR veya cerrahi |
| Şarbon | Siyah ağrısız eskar, ödem | Siprofloksasin veya doksisiklin |
- Amipli karaciğer apsesi: endemik bölgeye seyahat, sağ üst kadran ağrısı, ateş, tek büyük apse; metronidazol, ardından luminal ajan (paromomisin).
- Sıtma: endemik bölgeden dönüşte ateş → kalın ve ince yayma; ağır P. falciparum'da IV artesunat.
! KKKA'da sağlık çalışanı bulaşı kan ve vücut sıvılarıyla olur; iğne batmasında ribavirin profilaksisi düşünülebilir.
""")

S("Erişkin aşılama", ["aşı","pnömokok","zona","herpes zoster","rsv","influenza","tetanoz","hepatit b aşısı","pcv20"], """
- Pnömokok: ≥65 yaş veya risk grubunda PCV20 ya da PCV21 tek doz (veya PCV15 + PPSV23).
- Zona: rekombinant zoster aşısı (2 doz), ≥50 yaş ve ≥18-19 yaş immünsüprese.
- RSV: ≥75 yaş tümüne; 50/60-74 yaş risk grubunda tek doz.
- İnfluenza: yıllık; ≥65 yaşta yüksek doz veya adjuvanlı aşı tercih.
- Tetanoz-difteri: 10 yılda bir; gebelikte her gebelikte Tdap.
- Hepatit B: risk grubu ve 19-59 yaş; diyaliz hastalarında yüksek doz.
- Canlı aşılar (MMR, suçiçeği, sarı humma) immünsüprese ve gebelerde kontrendike.
! Splenektomi öncesi (en az 2 hafta önce) pnömokok, meningokok (ACWY ve B) ve Hib aşıları.
""")
