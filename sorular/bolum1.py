B = []
def Q(t, g, s, o, a, e, p):
    B.append(dict(t=t, g=g, s=s, o=o, a=a, e=e, p=p))

# ---------------- KARDİYOLOJİ ----------------
Q('kardiyo','sik',
 "22 yaşında erkek hasta egzersizle gelen senkop nedeniyle başvuruyor. Sol sternal kenarda sistolik ejeksiyon üfürümü duyuluyor. Ekokardiyografide asimetrik septal hipertrofi saptanıyor. Aşağıdaki manevralardan hangisi üfürümün şiddetini artırır?",
 ["Çömelme","Valsalva manevrası","Pasif bacak kaldırma","El sıkma (handgrip)","Fenilefrin infüzyonu"],1,
 "Hipertrofik kardiyomiyopatide sol ventrikül çıkış yolu obstrüksiyonu, ventrikül hacmi küçüldükçe artar. Valsalva ve ayağa kalkma venöz dönüşü (ön yükü) azaltarak obstrüksiyonu ve üfürümü artırır. Çömelme ve bacak kaldırma ön yükü, el sıkma ve fenilefrin ard yükü artırarak üfürümü azaltır.",
 "HKMP ve MVP üfürümü ön yükü azaltan her şeyle (Valsalva, ayağa kalkma, nitrat) artar; aort darlığı üfürümü ise azalır.")
Q('kardiyo','sik',
 "Ejeksiyon fraksiyonu %30 olan, optimal tedavi altındaki semptomatik kalp yetersizliği hastasında aşağıdaki ilaçlardan hangisinin mortaliteyi azalttığı gösterilmemiştir?",
 ["Sakubitril-valsartan","Bisoprolol","Spironolakton","Dapagliflozin","Digoksin"],4,
 "HFrEF'te mortalite faydası gösterilmiş dört temel ilaç grubu ARNİ (veya ACEi/ARB), kanıtlanmış beta bloker (bisoprolol, karvedilol, metoprolol süksinat, nebivolol), MRA ve SGLT2 inhibitörüdür. DIG çalışmasında digoksin mortaliteyi değiştirmemiş, yalnızca kalp yetersizliğine bağlı hastaneye yatışları azaltmıştır.",
 "HFrEF'in 'dört sütunu': ARNİ/ACEi, beta bloker, MRA, SGLT2i. Digoksin ve diüretikler semptom tedavisidir.")
Q('kardiyo','sik',
 "68 yaşında, hipertansiyonu dışında hastalığı olmayan kadın hastada nonvalvüler atriyal fibrilasyon saptanıyor. CHA2DS2-VASc skoru kaçtır?",
 ["1","2","3","4","5"],2,
 "Puanlama: yaş 65-74 = 1, kadın cinsiyet = 1, hipertansiyon = 1; toplam 3. Kadında skor ≥3 (erkekte ≥2) olduğunda oral antikoagülan önerilir. Nonvalvüler AF'de DOAK'lar varfarine tercih edilir.",
 "CHA2DS2-VASc: KKY, HT, Yaş ≥75 (2), DM, İnme/TİA (2), Vasküler hastalık, Yaş 65-74, Kadın cinsiyet.")
Q('kardiyo','sik',
 "İnferior duvar miyokard infarktüsü ile gelen hastada TA 80/50 mmHg, juguler venöz dolgunluk var ve akciğerler oskültasyonda temiz. Sağ prekordiyal derivasyonlarda V4R'de ST elevasyonu saptanıyor. İlk yapılması gereken hangisidir?",
 ["IV nitrogliserin","IV furosemid","IV sıvı yüklemesi","IV morfin","IV metoprolol"],2,
 "Tablo sağ ventrikül infarktüsüdür (hipotansiyon, JVD, temiz akciğer üçlüsü). Sağ ventrikül ön yüke bağımlı olduğundan ilk adım dikkatli IV sıvı yüklemesidir. Nitrat, diüretik ve morfin ön yükü azaltarak derin hipotansiyona yol açar; beta bloker kardiyojenik şoku ağırlaştırır.",
 "İnferior MI + hipotansiyon gördüğünde önce V4R çek; sağ ventrikül tutulumu varsa nitrat ve diüretik verme.")
Q('kardiyo','sik',
 "Ciddi aort darlığı olan hastalarda aşağıdaki semptomlardan hangisinin ortaya çıkması tedavi edilmezse en kısa ortalama sağ kalımla ilişkilidir?",
 ["Angina pektoris","Senkop","Kalp yetersizliği (eforla dispne)","Çarpıntı","Baş dönmesi"],2,
 "Klasik verilere göre semptom başladıktan sonra ortalama sağ kalım angina için yaklaşık 5 yıl, senkop için 3 yıl, kalp yetersizliği için 2 yıldır. Semptomatik ciddi aort darlığı cerrahi veya transkateter kapak replasmanı (TAVI) endikasyonudur.",
 "Aort darlığı semptomları 'ASK' sırasıyla kötüleşir: Angina 5, Senkop 3, Kalp yetersizliği 2 yıl.")
Q('kardiyo','sik',
 "35 yaşında erkek hastanın ateşli bir hastalık sırasında çekilen EKG'sinde V1-V2'de sağ dal bloğu görünümü ile birlikte 'coved' tipte (kubbe şeklinde) ST elevasyonu saptanıyor. Kardeşi 40 yaşında uykuda ani ölmüş. Ani kardiyak ölümü önlemede en etkili yaklaşım hangisidir?",
 ["Amiodaron","Beta bloker","İmplante edilebilir kardiyoverter defibrilatör (ICD)","Flekainid","Digoksin"],2,
 "Tip 1 Brugada paterni ve ani ölüm aile öyküsü ile Brugada sendromu düşünülür (çoğunlukla SCN5A mutasyonu). Ani ölümü önleyen tek kanıtlanmış tedavi ICD'dir. Flekainid gibi sodyum kanal blokerleri paterni ortaya çıkarır ve kontrendikedir; ateş de tetikleyicidir ve agresif düşürülmelidir. Kinidin elektriksel fırtınada yardımcı olabilir.",
 "Brugada: ateş ve sodyum kanal blokerleri (flekainid, prokainamid) paterni açığa çıkarır; tedavi ICD.")
Q('kardiyo','olasi',
 "Diyastolik disfonksiyon ve sağ kalp yetersizliği bulguları olan hastada konstriktif perikardit ile restriktif kardiyomiyopati ayırıcı tanısında aşağıdakilerden hangisi konstriktif perikardit lehinedir?",
 ["Belirgin yüksek BNP düzeyi","Solunumla belirgin ventriküler etkileşim (septal sıçrama)","Ventrikül duvar kalınlığında artış","Doku Doppler ile düşük mitral anüler e' hızları","Pulmoner arter sistolik basıncının 60 mmHg üzerinde olması"],1,
 "Konstriksiyonda sertleşmiş perikard nedeniyle ventriküller birbirine bağımlı çalışır; solunumla belirgin ventriküler etkileşim ve septal sıçrama görülür. Miyokard sağlam olduğundan e' hızları normal veya yüksektir, BNP görece düşüktür. Restriktif KMP'de ise miyokard tutulumu nedeniyle e' düşük, BNP yüksek, pulmoner hipertansiyon daha belirgindir.",
 "Konstriksiyonda miyokard sağlamdır: e' normal, BNP görece düşük. Restriksiyonda e' düşük, BNP yüksek.")
Q('kardiyo','sik',
 "Tip B aort diseksiyonu saptanan ve TA 190/110 mmHg, nabız 105/dk olan hastada ilk seçilmesi gereken antihipertansif tedavi hangisidir?",
 ["IV hidralazin","IV beta bloker (esmolol veya labetalol)","Sublingual nifedipin","IV furosemid","Oral kaptopril"],1,
 "Aort diseksiyonunda amaç duvar stresini (dP/dt) azaltmaktır. Önce IV beta bloker ile nabız 60/dk civarına indirilir, ardından gerekirse vazodilatör eklenir. Hedef sistolik basınç hızla 100-120 mmHg'dir. Beta blokaj olmadan verilen hidralazin gibi vazodilatörler refleks taşikardiyle diseksiyonu ilerletebilir; sublingual nifedipin kontrolsüz düşüş nedeniyle kullanılmaz.",
 "Diseksiyonda sıra: önce beta bloker (nabız ~60), sonra vazodilatör; hedef SKB 100-120.")
Q('kardiyo','olasi',
 "Bir yıl önce akut koroner sendrom geçirmiş hastada ESC kılavuzlarına göre LDL kolesterol hedefi hangisidir?",
 ["<116 mg/dL","<100 mg/dL","<70 mg/dL","<55 mg/dL ve bazal değerden en az %50 azalma","<30 mg/dL"],3,
 "Aterosklerotik kardiyovasküler hastalığı olan çok yüksek riskli hastalarda hedef LDL <55 mg/dL ve bazal değere göre ≥%50 azalmadır. Maksimal tolere edilen statinle hedefe ulaşılamazsa ezetimib, ardından PCSK9 inhibitörü eklenir. İki yıl içinde tekrarlayan vasküler olay yaşayanlarda <40 mg/dL hedeflenebilir.",
 "Risk kategorisine göre LDL hedefleri: çok yüksek <55, yüksek <70, orta <100, düşük <116 mg/dL.")
Q('kardiyo','sik',
 "Aşağıdaki ilaçlardan hangisinin QT aralığını uzatma etkisi yoktur?",
 ["Azitromisin","Haloperidol","Ondansetron","Metadon","Amlodipin"],4,
 "Makrolidler, antipsikotikler (haloperidol), ondansetron, metadon, sınıf IA ve III antiaritmikler, florokinolonlar QT'yi uzatır. Dihidropiridin kalsiyum kanal blokeri amlodipinin anlamlı QT etkisi yoktur. Uzun QT'de torsades de pointes gelişirse ilk tedavi IV magnezyum sülfattır.",
 "Torsades de pointes: IV magnezyum; hemodinamik bozuksa defibrilasyon.")
Q('kardiyo','sik',
 "Wolff-Parkinson-White sendromu bilinen hastada geniş QRS'li, düzensiz, hızlı (220/dk) taşikardi saptanıyor; hasta hemodinamik olarak stabil. Tedavide tercih edilmesi gereken ilaç hangisidir?",
 ["Verapamil","Digoksin","Adenozin","Prokainamid","Metoprolol"],3,
 "Preeksitasyonlu atriyal fibrilasyonda AV nodu bloke eden ilaçlar (verapamil, diltiazem, digoksin, adenozin, beta bloker) uyarıların aksesuar yoldan geçişini kolaylaştırarak ventrikül fibrilasyonuna yol açabilir. Stabil hastada aksesuar yolu yavaşlatan prokainamid (veya ibutilid) tercih edilir; instabil hastada senkronize kardiyoversiyon yapılır. Kalıcı tedavi kateter ablasyonudur.",
 "WPW + AF'de AV nod blokerleri kontrendike: 'ABCD' (Adenozin, Beta bloker, Ca kanal blokeri, Digoksin) verilmez.")
Q('kardiyo','olasi',
 "İdiyopatik pulmoner arteriyel hipertansiyon tanısı alan hastada sağ kalp kateterizasyonu sırasında yapılan akut vazoreaktivite testi pozitif bulunuyor. Bu hastada ilk tercih edilecek tedavi hangisidir?",
 ["Bosentan","Yüksek doz kalsiyum kanal blokeri","Sildenafil","IV epoprostenol","Riosiguat"],1,
 "Vazoreaktivite testi pozitif olan (ortalama PAB'ın ≥10 mmHg düşerek ≤40 mmHg'ye inmesi, kalp debisinin korunması) idiyopatik, kalıtsal veya ilaca bağlı PAH hastalarında yüksek doz KKB (nifedipin, diltiazem, amlodipin) ilk tedavidir. Bu hastaların yaklaşık %10'u bu gruptadır. Testi negatif olanlarda endotelin reseptör antagonisti, PDE-5 inhibitörü veya prostasiklin yolağı ilaçları kullanılır.",
 "PAH'ta yalnızca vazoreaktivite testi pozitif hastalara KKB verilir; negatiflerde KKB zararlıdır.")

# ---------------- GASTROENTEROLOJİ ----------------
Q('gastro','sik',
 "Uzun süreli gastroözofageal reflü öyküsü olan hastada yapılan endoskopide distal özofagusta somon renkli mukoza izleniyor ve biyopside goblet hücreli intestinal metaplazi saptanıyor. Bu durum en çok hangi tümör için risk oluşturur?",
 ["Skuamöz hücreli karsinom","Adenokarsinom","Gastrointestinal stromal tümör","MALT lenfoma","Nöroendokrin tümör"],1,
 "Barrett özofagusu, skuamöz epitelin goblet hücreli intestinal kolumnar epitelle yer değiştirmesidir ve özofagus adenokarsinomunun öncül lezyonudur. Displazi yoksa izlem endoskopisi segment uzunluğuna göre 3-5 yılda bir yapılır; yüksek dereceli displazide endoskopik eradikasyon (rezeksiyon ve radyofrekans ablasyon) uygulanır. Skuamöz hücreli karsinom ise sigara, alkol ve akalazya ile ilişkilidir.",
 "Barrett → adenokarsinom (distal); sigara/alkol/akalazya → skuamöz (orta).")
Q('gastro','sik',
 "H. pylori eradikasyon tedavisinin başarısını değerlendirmek için aşağıdakilerden hangisi en uygundur?",
 ["Tedavi bitiminden 1 hafta sonra serolojik antikor testi","Tedavi bitiminden en az 4 hafta sonra, PPI 2 hafta kesilerek üre nefes testi","Tedavi devam ederken dışkı antijen testi","Tedavi bitiminden hemen sonra hızlı üreaz testi","Tedavi bitiminden 6 ay sonra serolojik test"],1,
 "Eradikasyon kontrolü için üre nefes testi veya monoklonal dışkı antijen testi kullanılır. Yalancı negatifliği önlemek için antibiyotik/bizmut tedavisinden en az 4 hafta sonra ve PPI 2 hafta kesildikten sonra yapılmalıdır. Antikorlar eradikasyondan sonra aylarca pozitif kalabildiğinden seroloji kontrol için uygun değildir.",
 "Seroloji yalnızca ilk tanıda kullanılır, eradikasyon kontrolünde asla.")
Q('gastro','sik',
 "Hem katı hem sıvı gıdalara karşı disfaji, regürjitasyon ve kilo kaybı olan hastada baryumlu grafide distal özofagusta 'kuş gagası' görünümü saptanıyor. Kesin tanı için altın standart test hangisidir?",
 ["Üst GİS endoskopisi","Yüksek çözünürlüklü özofagus manometrisi","24 saatlik pH monitorizasyonu","Toraks BT","Endoskopik ultrasonografi"],1,
 "Akalazyada alt özofagus sfinkteri gevşeyemez ve gövde peristaltizmi kaybolur; kesin tanı yüksek çözünürlüklü manometri ile konur (Chicago sınıflaması). Endoskopi psödoakalazyayı (özellikle kardiya tümörü) dışlamak için mutlaka yapılmalıdır. Tedavide pnömatik dilatasyon, laparoskopik Heller miyotomi veya POEM kullanılır; Tip II en iyi yanıt veren alt tiptir.",
 "Yaşlı, hızlı kilo kaybı ve kısa öyküde akalazya tablosu: psödoakalazyayı (kardiya kanseri) düşün.")
Q('gastro','sik',
 "Kronik ishal ve demir eksikliği anemisi olan hastada çölyak hastalığından şüpheleniliyor. Doku transglutaminaz IgA negatif bulunuyor, total serum IgA düzeyi belirgin düşük. Bir sonraki en uygun adım hangisidir?",
 ["Çölyak hastalığı dışlanmıştır","Doku transglutaminaz IgG veya deamide gliadin peptid IgG bakılması","Glutensiz diyete başlanması","Antiendomisyum IgA bakılması","Gluten yüklemesi ardından tTG-IgA tekrarı"],1,
 "Çölyak hastalarında selektif IgA eksikliği genel popülasyondan sık görülür ve IgA tabanlı testler yalancı negatif sonuç verir. Bu durumda IgG tabanlı testler (tTG-IgG, DGP-IgG) kullanılır ve tanı duodenum biyopsisi ile doğrulanır. Testler mutlaka gluten içeren diyet altında yapılmalıdır; diyete başlamak tanıyı maskeler.",
 "Çölyak testi isterken total IgA'yı da iste; HLA-DQ2/DQ8 negatifliği çölyakı pratikte dışlar.")
Q('gastro','sik',
 "Aşağıdaki bulgulardan hangisi Crohn hastalığından çok ülseratif koliti düşündürür?",
 ["Perianal fistül","Kaldırım taşı görünümü","Rektumdan başlayıp proksimale devamlı yayılan tutulum","Biyopside nonkazeifiye granülom","Terminal ileit"],2,
 "Ülseratif kolit her zaman rektumu tutar ve proksimale doğru kesintisiz, mukozal tutulum yapar. Crohn ağızdan anüse herhangi bir yeri, atlamalı (skip) ve transmural tutar; fistül, striktür, kaldırım taşı görünümü, granülom ve terminal ileit Crohn lehinedir. Sigara ÜK'de koruyucu, Crohn'da ise kötüleştiricidir. Primer sklerozan kolanjit ÜK ile daha sık birliktedir.",
 "Sigara: ÜK'yi korur, Crohn'u kötüleştirir. PSC: daha çok ÜK.")
Q('gastro','sik',
 "Safra taşına bağlı akut pankreatit tanısıyla izlenen hastada ateş, sarılık ve sağ üst kadran ağrısı gelişiyor; total bilirubin 6 mg/dL. Acil ERCP endikasyonu açısından en belirleyici bulgu hangisidir?",
 ["Serum amilazın normalin 3 katından yüksek olması","Eşlik eden akut kolanjit","BT'de peripankreatik sıvı","Hiperkalsemi","CRP'nin 150 mg/L üzerinde olması"],1,
 "Biliyer pankreatitte acil (24 saat içinde) ERCP endikasyonu eşlik eden kolanjittir; persistan koledok obstrüksiyonunda da (72 saat içinde) yapılır. Kolanjitsiz biliyer pankreatitte rutin erken ERCP önerilmez. Hafif biliyer pankreatitte aynı yatışta kolesistektomi nüksü önler. Sıvı tedavisinde laktatlı Ringer ile ölçülü (agresif olmayan) hidrasyon önerilir.",
 "Biliyer pankreatit + kolanjit = 24 saat içinde ERCP. Hafif biliyer pankreatit = aynı yatışta kolesistektomi.")
Q('gastro','sik',
 "Hepatit B serolojisi şu şekilde sonuçlanıyor: HBsAg negatif, anti-HBs pozitif, anti-HBc IgG pozitif, HBV DNA negatif. Bu tablo neyi gösterir?",
 ["Aşıyla kazanılmış bağışıklık","Akut hepatit B","Kronik hepatit B","Geçirilmiş ve iyileşmiş enfeksiyon (doğal bağışıklık)","Pencere dönemi"],3,
 "Anti-HBc yalnızca doğal enfeksiyonla oluşur; anti-HBs ile birlikte pozitifliği geçirilmiş ve iyileşmiş enfeksiyonu gösterir. Yalnızca anti-HBs pozitifliği aşı yanıtıdır. Pencere döneminde HBsAg ve anti-HBs negatif, anti-HBc IgM pozitiftir. Anti-HBc pozitif hastalara rituksimab gibi güçlü immünsüpresif tedavi verilecekse reaktivasyon riski nedeniyle profilaksi (entekavir/tenofovir) gerekir.",
 "Rituksimab öncesi HBsAg ve anti-HBc bak: anti-HBc tek başına pozitif olsa bile profilaksi gerekir.")
Q('gastro','sik',
 "19 yaşında kadın hasta sarılık ve bilinç bulanıklığıyla getiriliyor. Coombs negatif hemolitik anemi, INR 3,1, AST/ALT 380/120 U/L, ALP belirgin düşük saptanıyor. En olası tanı hangisidir?",
 ["Herediter hemokromatoz","Wilson hastalığı","Otoimmün hepatit","Alfa-1 antitripsin eksikliği","Budd-Chiari sendromu"],1,
 "Genç hastada Coombs negatif hemoliz, akut karaciğer yetmezliği, AST/ALT oranının yüksekliği ve düşük ALP fulminan Wilson hastalığı için tipiktir. ALP/total bilirubin oranının <4 olması ve AST/ALT >2,2 tanıyı destekler. Kayser-Fleischer halkası, düşük seruloplazmin ve yüksek 24 saatlik idrar bakırı görülür. Fulminan tabloda tek kesin tedavi karaciğer naklidir; kronik formda penisilamin veya trientin, idamede çinko kullanılır.",
 "Wilson: ATP7B (kr 13), otozomal resesif; fulminan formda ALP orantısız düşük.")
Q('gastro','sik',
 "Sirozlu hastada parasentezde asit sıvısında PMNL 480/mm³ saptanıyor. Sefotaksim tedavisine ek olarak hepatorenal sendrom gelişimini ve mortaliteyi azaltan tedavi hangisidir?",
 ["Furosemid","IV albumin (1. gün 1,5 g/kg, 3. gün 1 g/kg)","Terlipressin","Propranolol","Laktuloz"],1,
 "Spontan bakteriyel peritonitte (PMNL ≥250/mm³) üçüncü kuşak sefalosporine ek IV albumin verilmesi böbrek yetmezliği gelişimini ve mortaliteyi anlamlı azaltır. SBP geçiren hastalara sekonder profilaksi (norfloksasin veya siprofloksasin) verilir. Nonselektif beta blokerler dirençli asit ve hipotansiyonda dikkatle kullanılmalıdır.",
 "SBP: tanı PMNL ≥250; tedavi sefotaksim + albumin (1,5 g/kg ve 1 g/kg).")
Q('gastro','sik',
 "Sirozlu hastada asit, kreatinin yükselmesi (0,9'dan 2,4 mg/dL'ye), idrar sodyumu <10 mEq/L saptanıyor. Diüretikler kesilip 2 gün albumin verilmesine rağmen böbrek fonksiyonları düzelmiyor, idrar sedimenti normal. En uygun tedavi hangisidir?",
 ["Yüksek doz furosemid","Terlipressin + albumin","Nonselektif beta bloker","IV kontrast ile BT","Siprofloksasin"],1,
 "Tablo hepatorenal sendrom-akut böbrek hasarıdır (HRS-AKI). Hipovolemi diüretik kesilmesi ve albumin ile dışlandıktan sonra tedavi vazokonstriktör (terlipressin; yoksa norepinefrin) ile albumin kombinasyonudur. Kesin tedavi karaciğer naklidir. Nefrotoksik ajanlar ve kontrast madde kaçınılmalıdır.",
 "HRS tanısından önce: diüretik kes, 48 saat albumin ver; yanıt yoksa terlipressin + albumin.")
Q('gastro','sik',
 "48 yaşında kadın hastada kaşıntı ve yorgunluk mevcut. ALP 3 kat yüksek, GGT yüksek, antimitokondriyal antikor (AMA) pozitif, görüntülemede safra yolları normal. İlk basamak tedavi hangisidir?",
 ["Prednizolon","Ursodeoksikolik asit","Azatiyoprin","Obetikolik asit","Kolestiramin tek başına"],1,
 "Tablo primer biliyer kolanjittir (PBC). İlk basamak tedavi ursodeoksikolik asittir (13-15 mg/kg/gün); hastalık progresyonunu yavaşlatır ve sağ kalımı uzatır. UDCA'ya yetersiz yanıtta obetikolik asit veya fibratlar eklenir. Kaşıntı semptomatik olarak kolestiraminle tedavi edilebilir ama hastalığı değiştirmez. PBC'de osteoporoz ve yağda eriyen vitamin eksikliği taranmalıdır.",
 "PBC: orta yaş kadın + ALP yüksek + AMA (+) → UDCA. PSC: genç erkek + ÜK + MRCP'de boncuk dizisi.")
Q('gastro','sik',
 "Sirozlu hastada özofagus varis kanaması gelişiyor. Aşağıdakilerden hangisinin akut dönemde mortaliteyi azalttığı gösterilmiştir?",
 ["PPI infüzyonu","Profilaktik antibiyotik (seftriakson)","Traneksamik asit","INR'yi düzeltmek için taze donmuş plazma","Hemoglobini 10 g/dL üzerinde tutacak şekilde transfüzyon"],1,
 "Sirozlu hastada GİS kanamada profilaktik antibiyotik (ilerlemiş sirozda IV seftriakson 1 g/gün, 7 gün) enfeksiyonları, yeniden kanamayı ve mortaliteyi azaltır. Tedavinin diğer bileşenleri vazoaktif ilaç (terlipressin, oktreotid), 12 saat içinde endoskopik band ligasyonu ve kısıtlayıcı transfüzyondur (hedef Hb 7-8 g/dL). Liberal transfüzyon portal basıncı artırarak yeniden kanamayı artırır.",
 "Varis kanamasında 'üçlü': vazoaktif ilaç + antibiyotik + 12 saatte band ligasyonu; Hb hedefi 7-8.")

# ---------------- NEFROLOJİ ----------------
Q('nefro','sik',
 "Akut böbrek hasarı gelişen ve diüretik kullanmayan hastada aşağıdaki idrar bulgularından hangisi prerenal azotemiyi destekler?",
 ["Fraksiyone sodyum atılımı (FENa) >%2","İdrar sodyumu >40 mEq/L","FENa <%1","İdrar sedimentinde çamur kahvesi granüler silendirler","İdrar osmolalitesi <350 mOsm/kg"],2,
 "Prerenal durumda tübüller sağlamdır ve sodyumu avidite ile geri emer: FENa <%1, idrar Na <20 mEq/L, idrar osmolalitesi >500 mOsm/kg, BUN/kreatinin >20. Akut tübüler nekrozda FENa >%2, çamur kahvesi granüler silendirler ve izostenüri görülür. Diüretik kullanan hastada FENa güvenilmez; fraksiyone üre atılımının <%35 olması prerenal lehinedir.",
 "Diüretik kullanıyorsa FENa yerine FEüre bak: <%35 prerenal.")
Q('nefro','sik',
 "Hodgkin lenfoma tanılı hastada gelişen nefrotik sendromda en olası glomerüler patoloji hangisidir?",
 ["Membranöz nefropati","Minimal değişiklik hastalığı","Fokal segmental glomerüloskleroz","Membranoproliferatif glomerülonefrit","IgA nefropatisi"],1,
 "Hodgkin lenfoma klasik olarak minimal değişiklik hastalığı ile ilişkilidir; NSAİİ kullanımı da erişkinde MDH nedenidir. Işık mikroskobu normaldir, elektron mikroskopide podosit ayak çıkıntılarında yaygın silinme görülür ve steroide yanıt iyidir. Solid tümörler (akciğer, kolon, meme) ise daha çok membranöz nefropati ile ilişkilidir.",
 "Hodgkin → minimal değişiklik; solid tümör → membranöz nefropati.")
Q('nefro','sik',
 "Erişkin nefrotik sendromlu hastada böbrek biyopsisinde glomerül bazal membranında subepitelyal immün kompleks birikimi ('spike' görünümü) saptanıyor. Primer formda en sık saptanan otoantikor hangisidir?",
 ["Anti-GBM antikoru","Anti-fosfolipaz A2 reseptör (PLA2R) antikoru","ANCA","Anti-dsDNA","Antistreptolizin O"],1,
 "Primer membranöz nefropatinin yaklaşık %70-80'inde anti-PLA2R antikoru pozitiftir; antikor düzeyi hastalık aktivitesi ve tedavi yanıtıyla koreledir. Sekonder nedenler (HBV, SLE sınıf V, solid tümörler, ilaçlar) araştırılmalıdır. Membranöz nefropati renal ven trombozu riskinin en yüksek olduğu nefrotik sendrom nedenidir.",
 "Membranöz: anti-PLA2R; nefrotik sendromlar içinde renal ven trombozu riski en yüksek.")
Q('nefro','sik',
 "24 yaşında erkek hastada üst solunum yolu enfeksiyonunun 2. gününde makroskopik hematüri gelişiyor. Serum kompleman düzeyleri normal. En olası tanı hangisidir?",
 ["Poststreptokokal glomerülonefrit","IgA nefropatisi","Lupus nefriti","Membranoproliferatif glomerülonefrit","Kriyoglobulinemik glomerülonefrit"],1,
 "IgA nefropatisi dünyada en sık primer glomerülonefrittir; mukozal enfeksiyonla eşzamanlı (sinfarenjitik, 1-3 gün içinde) makroskopik hematüri ve normal kompleman tipiktir. Poststreptokokal GN'de hematüri enfeksiyondan 1-3 hafta sonra başlar ve C3 düşüktür. Biyopside mezangiyal IgA birikimi görülür.",
 "Hematüri enfeksiyonla eş zamanlı → IgA; 2-3 hafta sonra + düşük C3 → PSGN.")
Q('nefro','sik',
 "Hemoptizi ve hızlı ilerleyen glomerülonefrit tablosuyla başvuran hastanın böbrek biyopsisinde glomerül bazal membranı boyunca lineer IgG birikimi saptanıyor. Tedavinin temel bileşeni hangisidir?",
 ["Yalnızca ACE inhibitörü","Plazmaferez + yüksek doz steroid + siklofosfamid","Yalnızca hidroksiklorokin","Rituksimab monoterapisi","Hemodiyaliz ve gözlem"],1,
 "Lineer IgG birikimi anti-GBM hastalığının (pulmoner tutulum varsa Goodpasture sendromu) tanı koydurucu bulgusudur. Dolaşımdaki antikorların uzaklaştırılması için acil plazmaferez, yeni antikor yapımını baskılamak için steroid ve siklofosfamid verilir. Granüler birikim immün kompleks GN'yi, birikim olmaması (pauci-immün) ANCA vasküliti düşündürür.",
 "İmmünofloresan: lineer = anti-GBM, granüler = immün kompleks, birikim yok = pauci-immün (ANCA).")
Q('nefro','sik',
 "Kronik böbrek hastalığına bağlı anemide eritropoez uyarıcı ajan tedavisi sırasında hedeflenen hemoglobin aralığı hangisidir?",
 ["8-9 g/dL","10-11,5 g/dL","12-13 g/dL","13-15 g/dL","15 g/dL üzeri"],1,
 "ESA tedavisinde hemoglobin 10-11,5 g/dL aralığında tutulur; 13 g/dL üzerine çıkılması inme, tromboz ve kardiyovasküler olay riskini artırır (TREAT, CHOIR çalışmaları). ESA başlamadan önce demir eksikliği düzeltilmelidir (ferritin >100-200 ng/mL, transferrin satürasyonu >%20). ESA yanıtsızlığında en sık neden demir eksikliğidir.",
 "KBH aneminde önce demir; ESA ile Hb 13'ü aşma.")
Q('nefro','olasi',
 "Kronik böbrek hastalığı-mineral kemik bozukluğu sürecinde, GFR azalmaya başladığında ilk ortaya çıkan laboratuvar değişikliği hangisidir?",
 ["Hiperfosfatemi","FGF-23 düzeyinde artış","Hipokalsemi","Kalsitriol düzeyinde artış","PTH düzeyinde düşüş"],1,
 "GFR azaldıkça fosfat atılımını sürdürmek için kemikten FGF-23 salınımı artar; bu en erken değişikliktir. FGF-23 1-alfa hidroksilazı baskılayarak kalsitriolü düşürür, bu da PTH artışına yol açar. Hiperfosfatemi ve hipokalsemi genellikle ileri evrelerde ortaya çıkar.",
 "KBH-MKB sırası: FGF-23 ↑ → kalsitriol ↓ → PTH ↑ → ileri evrede fosfor ↑.")
Q('nefro','sik',
 "Sjögren sendromlu hastada hipokalemi, normal anyon açıklı metabolik asidoz ve idrar pH'sının 6,5 olduğu saptanıyor. Böbrek ultrasonunda nefrokalsinozis var. En olası tanı hangisidir?",
 ["Tip 1 (distal) renal tübüler asidoz","Tip 2 (proksimal) renal tübüler asidoz","Tip 4 renal tübüler asidoz","Laktik asidoz","Diyabetik ketoasidoz"],0,
 "Distal RTA'da toplayıcı kanallar H+ salgılayamaz; asidoza rağmen idrar pH'sı >5,5 kalır. Hipokalemi, hiperkalsiüri, nefrokalsinozis ve kalsiyum fosfat taşları tipiktir. Sjögren, SLE ve amfoterisin B başlıca nedenlerdir. Proksimal RTA'da (Fanconi) bikarbonat geri emilimi bozuktur ve asidoz derinleşince idrar pH'sı <5,5'e iner; tip 4 RTA hiperkalemiktir (hipoaldosteronizm).",
 "RTA ayrımı: Tip 1 idrar pH >5,5 + taş; Tip 2 Fanconi, idrar pH değişken; Tip 4 hiperkalemi.")
Q('nefro','olasi',
 "Otozomal dominant polikistik böbrek hastalığı olan, hızlı ilerleme riski taşıyan 38 yaşında hastada hastalık progresyonunu yavaşlattığı gösterilmiş ilaç hangisidir?",
 ["Tolvaptan","Siklofosfamid","Prednizolon","Allopurinol","Sevelamer"],0,
 "Vazopressin V2 reseptör antagonisti tolvaptan kist büyümesini ve eGFR kaybını yavaşlatır (TEMPO, REPRISE çalışmaları); hepatotoksisite nedeniyle karaciğer enzimleri izlenmelidir. ADPKD'de en sık genetik neden PKD1 (kromozom 16) mutasyonudur. İntrakraniyal anevrizma, karaciğer kistleri ve mitral kapak prolapsusu eşlik edebilir.",
 "ADPKD'de aile öyküsünde subaraknoid kanama varsa MR anjiyografi ile anevrizma taraması yapılır.")
Q('nefro','sik',
 "Akut böbrek hasarı olan hastada aşağıdakilerden hangisi tek başına acil diyaliz endikasyonu değildir?",
 ["Üremik perikardit","Medikal tedaviye dirençli hiperkalemi","Diüretiğe yanıtsız akciğer ödemi","Üremik ensefalopati","Serum kreatininin 4 mg/dL olması"],4,
 "Acil diyaliz endikasyonları 'AEIOU' ile hatırlanır: dirençli Asidoz, Elektrolit (dirençli hiperkalemi), Intoksikasyon (diyalizle uzaklaştırılabilen; lityum, metanol, etilen glikol, salisilat), Overload (dirençli sıvı yüklenmesi) ve Üremi komplikasyonları (perikardit, ensefalopati, kanama). Tek başına kreatinin veya BUN değeri endikasyon değildir.",
 "Diyaliz endikasyonu: AEIOU. Sayılar değil, komplikasyonlar karar verdirir.")
