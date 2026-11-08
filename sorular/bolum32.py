# ---------------- PAKET 4: TIBBİ ONKOLOJİ (1/2) ----------------
Q('onko','sik',
 "USPSTF 2024 önerisine göre ortalama riskli kadınlarda tarama mamografisinin başlama yaşı ve sıklığı hangisidir?",
 ["30 yaşından itibaren yıllık","40-74 yaş arasında 2 yılda bir","50-69 yaş arasında 3 yılda bir","45 yaşından itibaren 5 yılda bir","Yalnızca aile öyküsü varsa"],1,
 "USPSTF 2024 güncellemesiyle ortalama riskli kadınlarda tarama mamografisi 40 yaşında başlatılır ve 74 yaşına kadar 2 yılda bir yapılır (önceki öneri 50 yaştı). 75 yaş üstü için kanıt yetersizdir. BRCA taşıyıcıları, göğüs duvarına 30 yaş öncesi radyoterapi öyküsü olanlar (örn. Hodgkin lenfoma) ve yaşam boyu riski >%20 olan kadınlarda yıllık MR ve mamografi ile daha erken tarama önerilir. Yoğun meme dokusunda ek görüntülemenin yararı konusunda kanıt yetersizdir.",
 "USPSTF 2024: mamografi 40-74 yaş, 2 yılda bir; yüksek riskte yıllık MR + mamografi.")
Q('onko','olasi',
 "Hodgkin lenfoma nedeniyle 18 yaşında mantle alan radyoterapisi alan 30 yaşındaki kadın için meme kanseri taraması önerisi hangisidir?",
 ["50 yaşında mamografiyle başlanır","Radyoterapiden 8 yıl sonra veya 25 yaşından itibaren (hangisi geç ise) yıllık meme MR'ı + mamografi","Tarama gerekmez","Yalnızca kendi kendine muayene","Profilaktik mastektomi zorunlu"],1,
 "10-30 yaş arasında göğüs duvarına radyoterapi alan kadınlarda meme kanseri riski BRCA taşıyıcılarına yakındır. Bu hastalarda tarama, radyoterapiden 8 yıl sonra veya 25 yaşında (hangisi daha geç ise) yıllık meme MR'ı ve 30 yaşından itibaren yıllık mamografiyle başlatılır. Mantle RT sonrası diğer geç etkiler arasında hipotiroidi, koroner arter ve kapak hastalığı, akciğer kanseri ve tiroid kanseri vardır; bu hastalar uzun süre izlenmelidir.",
 "Göğse RT (10-30 yaş) → RT'den 8 yıl sonra veya 25 yaşında yıllık meme MR + mamografi.")
Q('onko','sik',
 "Gebeliğin 20. haftasında HER2 pozitif, hormon reseptörü pozitif meme kanseri tanısı alan hastada gebelik sürerken kaçınılması gereken tedavi hangisidir?",
 ["Mastektomi","Antrasiklin temelli kemoterapi","Trastuzumab ve tamoksifen","Sentinel lenf nodu biyopsisi (teknesyum ile)","Antiemetik olarak ondansetron"],2,
 "Gebelikte meme kanserinde cerrahi her trimesterde yapılabilir; antrasiklin ve siklofosfamid içeren kemoterapi ilk trimesterden sonra güvenle verilebilir. Trastuzumab oligohidramniyoza yol açtığından, tamoksifen ise teratojenik olduğundan gebelikte kontrendikedir; doğumdan sonraya ertelenir. Radyoterapi de doğum sonrasına bırakılır. Kemoterapinin son dozu ile doğum arasında nötropeni riski nedeniyle yaklaşık 3 hafta bırakılır.",
 "Gebelikte meme ca: cerrahi + (2. trimesterden sonra) antrasiklin; trastuzumab, tamoksifen ve RT doğum sonrası.")
Q('onko','olasi',
 "Meme kanseri tanısı alan 58 yaşında erkek hastada genetik açıdan yapılması gereken yaklaşım hangisidir?",
 ["Genetik test gerekmez","Germline genetik test (özellikle BRCA2)","Yalnızca karyotip","Yalnızca CHEK2 testi ailede kanser varsa","Yalnızca tümör HER2 testi"],1,
 "Erkek meme kanseri olan tüm hastalara aile öyküsünden bağımsız olarak germline genetik test önerilir; en sık ilişkili gen BRCA2'dir (yaşam boyu risk yaklaşık %7). BRCA2 taşıyıcısı erkeklerde ayrıca prostat ve pankreas kanseri riski artmıştır. Erkek meme kanserlerinin büyük çoğunluğu hormon reseptörü pozitiftir ve adjuvan endokrin tedavide tamoksifen tercih edilir. Klinefelter sendromu da risk faktörüdür.",
 "Erkek meme kanseri → herkese germline test (BRCA2); adjuvanda tamoksifen.")
Q('onko','sik',
 "HER2-düşük (IHC 1+) metastatik meme kanserinde etkinliği gösterilmiş antikor-ilaç konjugatı ve önemli yan etkisi hangisidir?",
 ["Trastuzumab emtansin; kardiyomiyopati","Trastuzumab derukstekan; interstisyel akciğer hastalığı/pnömonit","Sasituzumab govitekan; hiperkalsemi","Bevasizumab; hipertansiyon","Pertuzumab; hepatit"],1,
 "DESTINY-Breast04 çalışmasıyla trastuzumab derukstekan (T-DXd), HER2-düşük (IHC 1+ veya 2+/ISH negatif) metastatik meme kanserinde kemoterapiye göre sağkalımı uzatmıştır; bu yeni bir 'HER2-düşük' kategorisini ortaya çıkarmıştır. En önemli yan etkisi interstisyel akciğer hastalığı/pnömonittir; yeni öksürük veya nefes darlığında ilaç ara verilir, BT çekilir ve gerekirse steroid başlanır, grade ≥2 olgularda kalıcı kesilir. Bulantı ve nötropeni de sıktır.",
 "HER2-düşük metastatik meme → T-DXd; en önemli yan etki ILD/pnömonit.")
Q('onko','olasi',
 "Hormon reseptörü pozitif metastatik meme kanseri nedeniyle letrozol + ribosiklib başlanacak hastada ribosiklibe özgü olarak izlenmesi gereken parametre hangisidir?",
 ["Serum amilaz","EKG'de QTc ve karaciğer enzimleri","Göz içi basıncı","İdrar proteini","Kalsitonin"],1,
 "CDK4/6 inhibitörlerinin hepsi nötropeni yapar (özellikle palbosiklib ve ribosiklib); ancak febril nötropeni nadirdir. Ribosiklib QTc uzaması ve hepatotoksisite yapabildiğinden başlangıçta ve ilk aylarda EKG ve karaciğer testleri izlenir; QT uzatan ilaçlarla birlikte dikkatli kullanılır. Abemasiklib ise belirgin ishal yapar ve daha az nötropeniye yol açar; yüksek riskli, nod pozitif erken meme kanserinde adjuvan kullanımı onaylıdır.",
 "CDK4/6i: nötropeni; ribosiklib → QTc + karaciğer; abemasiklib → ishal.")
Q('onko','sik',
 "PIK3CA mutasyonlu hormon reseptörü pozitif metastatik meme kanserinde alpelisib tedavisinin en sık ve önemli yan etkisi hangisidir?",
 ["Hipoglisemi","Hiperglisemi","Hiperkalemi","Bradikardi","Hipotiroidi"],1,
 "Alpelisib (PI3Kα inhibitörü) fulvestrant ile birlikte PIK3CA mutasyonlu HR (+)/HER2 (−) ileri meme kanserinde kullanılır. İnsülin sinyal yolu inhibisyonuna bağlı hiperglisemi en sık ve en önemli yan etkidir; başlamadan önce açlık glukozu ve HbA1c değerlendirilir, glukoz yakından izlenir ve gerekirse metformin başlanır. Döküntü ve ishal de sıktır. Benzer etki kapivasertib (AKT inhibitörü) ve inavolisib ile de görülür.",
 "Alpelisib (PIK3CA) → hiperglisemi (metformin), döküntü, ishal.")
Q('onko','olasi',
 "55-69 yaş arası ortalama riskli erkeklerde PSA ile prostat kanseri taraması için USPSTF önerisi hangisidir?",
 ["Herkese yıllık PSA zorunludur","Bireysel karar; olası yarar ve zararlar (aşırı tanı, tedavi yan etkileri) hastayla tartışılarak paylaşılan kararla","Hiçbir yaşta önerilmez","40 yaşında başlanır","Yalnızca rektal muayene yeterlidir"],1,
 "USPSTF 55-69 yaş arası erkeklerde PSA taramasının, mortaliteye küçük bir yararı olabileceğini ancak aşırı tanı ve tedaviye bağlı inkontinans ve erektil disfonksiyon gibi zararlar içerdiğini belirterek paylaşılan karar verme önerir (derece C). 70 yaş üstünde tarama önerilmez (derece D). Siyahi ırk, aile öyküsü ve BRCA2 taşıyıcılığı gibi yüksek risk durumlarında daha erken başlangıç (40-45 yaş) tartışılır. Düşük riskli tümörlerde aktif izlem tercih edilir.",
 "PSA taraması 55-69 yaş: paylaşılan karar; ≥70 önerilmez; yüksek riskte (BRCA2, siyahi, aile) daha erken.")
Q('onko','sik',
 "Düşük riskli (PSA <10, Gleason 3+3 / grade grubu 1, T1c) lokalize prostat kanseri olan 64 yaşında erkek için tercih edilen yaklaşım hangisidir?",
 ["Radikal prostatektomi zorunlu","Aktif izlem (PSA, muayene, MR ve gerektiğinde tekrar biyopsi)","Androjen deprivasyon tedavisi","Dosetaksel kemoterapisi","Abirateron"],1,
 "Düşük riskli prostat kanserinde kanser spesifik mortalite çok düşüktür; ProtecT çalışmasında 15 yıllık izlemde aktif izlem, cerrahi ve radyoterapi arasında prostat kanseri mortalitesi açısından anlamlı fark görülmemiştir. Bu nedenle tercih edilen yaklaşım aktif izlemdir; progresyon bulgusunda küratif tedaviye geçilir. Cerrahi ve radyoterapi üriner, bağırsak ve cinsel yan etkilere yol açar. ADT lokalize düşük riskli hastalıkta endike değildir.",
 "Düşük riskli lokalize prostat ca → aktif izlem; progresyonda küratif tedavi.")
Q('onko','olasi',
 "Metastatik kastrasyona dirençli prostat kanserinde abirateron başlanan hastaya neden düşük doz prednizon da verilir?",
 ["Bulantıyı önlemek için","CYP17 inhibisyonuyla artan ACTH'ye bağlı mineralokortikoid fazlalığını (HT, hipokalemi, ödem) önlemek için","Kemik ağrısını azaltmak için","Hepatotoksisiteyi önlemek için","Tümöre doğrudan etkisi için"],1,
 "Abirateron CYP17A1 inhibitörüdür ve androjen sentezini adrenal bez, testis ve tümörde engeller; kortizol sentezi de azaldığı için ACTH artar ve mineralokortikoid öncüllerinin birikmesiyle hipertansiyon, hipokalemi ve sıvı tutulumu gelişir. Düşük doz prednizon ACTH'yi baskılayarak bu etkileri önler. Hepatotoksisite nedeniyle karaciğer testleri izlenmelidir. Enzalutamid ise androjen reseptör antagonistidir; nöbet eşiğini düşürür ve yorgunluk yapar.",
 "Abirateron + prednizon (mineralokortikoid fazlalığını önler); karaciğer testlerini izle. Enzalutamid → nöbet riski.")
Q('onko','sik',
 "Uzun süreli androjen deprivasyon tedavisi (ADT) alan prostat kanseri hastasında izlenmesi ve önlenmesi gereken yan etkiler hangileridir?",
 ["Yalnızca jinekomasti","Osteoporoz ve kırık, metabolik sendrom/diyabet, kardiyovasküler risk, sıcak basmaları ve kas kaybı","Hiperkalsemi","Polisitemi","Hipertiroidi"],1,
 "ADT ile testosteronun kastrasyon düzeyine inmesi kemik mineral yoğunluğu kaybı ve kırık riskinde artış, insülin direnci, diyabet, dislipidemi, kilo artışı, sarkopeni, anemi, sıcak basmaları, libido kaybı ve bilişsel etkiler yapar. Başlangıçta DXA, kalsiyum ve D vitamini desteği önerilir; kırık riski yüksekse bifosfonat veya denosumab verilir. Kardiyovasküler risk faktörleri düzenli izlenmelidir. GnRH agonisti başlarken ilk haftalarda 'flare' (alevlenme) etkisini önlemek için antiandrojen eklenir; antagonistlerde (degareliks, relugoliks) flare yoktur.",
 "ADT: osteoporoz (DXA, Ca/D, gerekirse bifosfonat/denosumab), metabolik ve KV risk; agonistte flare → antiandrojen.")
Q('onko','olasi',
 "PSMA-PET pozitif, androjen reseptör yolu inhibitörü ve taksan kemoterapisi sonrası ilerleyen metastatik kastrasyona dirençli prostat kanserinde sağkalımı uzattığı gösterilen tedavi hangisidir?",
 ["Lutesyum-177 PSMA-617","İyot-131","Radyum-223 yalnızca visseral metastazda","İnterferon","Tamoksifen"],0,
 "VISION çalışmasında Lutesyum-177 PSMA-617 radyoligand tedavisi, PSMA pozitif mCRPC'de standart tedaviye eklendiğinde genel sağkalımı ve radyografik progresyonsuz sağkalımı uzatmıştır. En sık yan etkiler kuru ağız, yorgunluk ve kemik iliği baskılanmasıdır. Radyum-223 ise yalnızca semptomatik kemik metastazı olan, visseral metastazı olmayan hastalarda kullanılır. BRCA ve diğer homolog rekombinasyon gen mutasyonlu hastalarda PARP inhibitörleri (olaparib) de seçenektir.",
 "PSMA (+) mCRPC (ARPI + taksan sonrası) → Lu-177 PSMA-617; kemik metastazında Ra-223; BRCA → olaparib.")
Q('onko','olasi',
 "HLA-A*02:01 pozitif, karaciğer metastazlı ve rezeke edilemeyen uveal melanom hastasında genel sağkalımı uzattığı gösterilen tedavi hangisidir?",
 ["Dakarbazin","Tebentafusp","Dabrafenib + trametinib","Tamoksifen","İmatinib"],1,
 "Uveal melanom kutanöz melanomdan farklı biyolojiye sahiptir: BRAF mutasyonu nadirdir, GNAQ/GNA11 mutasyonları sıktır ve metastazlar en sık karaciğere olur; immün kontrol noktası inhibitörlerine yanıt düşüktür. Tebentafusp, gp100'ü tanıyan TCR ile anti-CD3 içeren bispesifik bir füzyon proteinidir ve yalnızca HLA-A*02:01 pozitif hastalarda etkilidir; faz 3 çalışmada genel sağkalımı uzatmıştır. Sitokin salınım sendromu ve deri reaksiyonları sık yan etkileridir. Karaciğere yönelik tedaviler (perkütan hepatik perfüzyon) diğer seçeneklerdir.",
 "Metastatik uveal melanom + HLA-A*02:01 → tebentafusp; BRAF nadir, ICI yanıtı düşük.")
Q('onko','olasi',
 "Kas invaziv mesane kanseri (T2N0M0) olan ve sisplatin almaya uygun 62 yaşında hastada standart küratif tedavi hangisidir?",
 ["Yalnızca TUR ve BCG","Neoadjuvan sisplatin temelli kemoterapi + radikal sistektomi","Yalnızca radikal sistektomi","Yalnızca immünoterapi","Palyatif radyoterapi"],1,
 "Kas invaziv mesane kanserinde sisplatine uygun hastalarda neoadjuvan sisplatin temelli kemoterapi (dd-MVAC veya gemsitabin-sisplatin) sonrası radikal sistektomi ve pelvik lenf nodu diseksiyonu standarttır; neoadjuvan tedavi sağkalımı yaklaşık %5-8 artırır. Mesane koruyucu seçenek olarak maksimal TUR sonrası eşzamanlı kemoradyoterapi (üçlü yaklaşım) seçilmiş hastalarda uygundur. Yeni çalışmalar perioperatif durvalumab eklenmesiyle sağkalım yararı göstermiştir (NIAGARA). BCG yalnızca kas invaziv olmayan hastalıkta kullanılır.",
 "Kas invaziv mesane ca: neoadjuvan sisplatin KT → radikal sistektomi; alternatif üçlü mesane koruma.")
Q('onko','sik',
 "Lokal ileri veya metastatik ürotelyal karsinomda birinci basamakta platin temelli kemoterapiye göre sağkalımı belirgin uzatan kombinasyon hangisidir?",
 ["Enfortumab vedotin + pembrolizumab","İpilimumab + nivolumab","Bevasizumab + paklitaksel","Sunitinib","Mitomisin C"],0,
 "EV-302 çalışmasında Nektin-4 hedefli antikor-ilaç konjugatı enfortumab vedotin ile pembrolizumab kombinasyonu, ileri ürotelyal karsinomda birinci basamakta platin temelli kemoterapiye göre genel sağkalımı yaklaşık iki katına çıkarmış ve yeni standart olmuştur. Enfortumab vedotinin önemli yan etkileri periferik nöropati, deri reaksiyonları (Stevens-Johnson dahil), hiperglisemi ve göz bulgularıdır. FGFR3 değişikliği olan hastalarda erdafitinib seçenektir.",
 "İleri ürotelyal karsinom 1. basamak → enfortumab vedotin + pembrolizumab (EV-302).")
Q('onko','olasi',
 "Berrak hücreli renal hücreli karsinom nedeniyle nefrektomi yapılan ve yüksek nüks riski taşıyan (pT3, grade 4) hastada sağkalım yararı gösterilmiş adjuvan tedavi hangisidir?",
 ["Sunitinib 5 yıl","Pembrolizumab 1 yıl","İnterlökin-2","Sitotoksik kemoterapi","Radyoterapi"],1,
 "KEYNOTE-564 çalışmasında nefrektomi sonrası yüksek nüks riskli berrak hücreli RHK hastalarında 1 yıl adjuvan pembrolizumab hastalıksız sağkalımı ve genel sağkalımı uzatmıştır. Sunitinib adjuvan tedavide genel sağkalım yararı göstermemiş ve yan etkileri belirgindir. RHK kemoterapiye ve radyoterapiye göreceli olarak dirençlidir. İmmün ilişkili yan etkiler (tiroidit, hepatit, kolit) açısından izlem gereklidir.",
 "Yüksek riskli berrak hücreli RHK nefrektomi sonrası → 1 yıl adjuvan pembrolizumab.")
Q('onko','sik',
 "Sınırlı evre küçük hücreli akciğer kanserinde eşzamanlı kemoradyoterapi sonrası progresyon olmayan hastada sağkalımı uzattığı gösterilen konsolidasyon tedavisi hangisidir?",
 ["Osimertinib","Durvalumab","Bevasizumab","Lorlatinib","Gefitinib"],1,
 "ADRIATIC çalışmasında sınırlı evre KHAK'ta platin-etoposid ile eşzamanlı kemoradyoterapi sonrası progresyon olmayan hastalarda 2 yıla kadar konsolidasyon durvalumab genel sağkalımı ve progresyonsuz sağkalımı uzatmıştır. Tam yanıt alınan hastalarda profilaktik kraniyal ışınlama veya düzenli beyin MR izlemi seçenekleri tartışılır. Yaygın evrede ise platin-etoposide atezolizumab veya durvalumab eklenir. EGFR ve ALK inhibitörlerinin KHAK'ta yeri yoktur.",
 "Sınırlı evre KHAK: eşzamanlı KRT → konsolidasyon durvalumab (ADRIATIC); PCI veya MR izlemi.")
Q('onko','olasi',
 "Rezektabl evre II-IIIA küçük hücre dışı akciğer kanserinde (EGFR/ALK negatif) neoadjuvan dönemde sağkalım ve patolojik tam yanıt oranını artırdığı gösterilen yaklaşım hangisidir?",
 ["Yalnızca cerrahi","Platin temelli kemoterapi + nivolumab (kemoimmünoterapi), ardından cerrahi","Yalnızca radyoterapi","Osimertinib","Yalnızca bevasizumab"],1,
 "CheckMate 816 çalışmasında rezektabl KHDAK'ta neoadjuvan nivolumab + platin temelli kemoterapi, yalnızca kemoterapiye göre olaysız sağkalımı ve patolojik tam yanıt oranını belirgin şekilde artırmıştır. Perioperatif (neoadjuvan + adjuvan) pembrolizumab (KEYNOTE-671) ve durvalumab (AEGEAN) da etkili bulunmuştur. EGFR veya ALK pozitif hastalarda immünoterapi yararı sınırlıdır; bu nedenle tedavi öncesi moleküler test yapılmalıdır. EGFR pozitif rezeke hastalarda adjuvan osimertinib (ADAURA), ALK pozitiflerde adjuvan alektinib (ALINA) kullanılır.",
 "Rezektabl KHDAK (EGFR/ALK −) → neoadjuvan kemoimmünoterapi; EGFR (+) → adjuvan osimertinib.")
Q('onko','sik',
 "KRAS G12C mutasyonu olan ve önceki tedaviyle ilerleyen metastatik KHDAK'ta kullanılabilen hedefe yönelik ajan hangisidir?",
 ["Osimertinib","Sotorasib veya adagrasib","Krizotinib","Trastuzumab","Larotrektinib"],1,
 "KRAS G12C mutasyonu özellikle sigara içen adenokarsinom hastalarında görülür. Sotorasib ve adagrasib KRAS G12C'yi kovalent olarak bağlayan inhibitörlerdir ve önceki sistemik tedavi sonrası ilerleyen hastalarda onaylıdır; hepatotoksisite ve ishal başlıca yan etkilerdir. Diğer hedeflenebilir değişiklikler: EGFR (osimertinib), ALK (alektinib, lorlatinib), ROS1 (entrektinib, repotrektinib), BRAF V600E (dabrafenib + trametinib), MET ekzon 14 atlama (kapmatinib, tepotinib), RET (selperkatinib), NTRK (larotrektinib) ve HER2 (trastuzumab derukstekan).",
 "KRAS G12C KHDAK → sotorasib/adagrasib; tüm adenokarsinomlarda geniş moleküler panel.")
Q('onko','olasi',
 "ALK pozitif metastatik KHDAK nedeniyle lorlatinib kullanan hastada tedavi sırasında özellikle izlenmesi gereken yan etki hangisidir?",
 ["Hipoglisemi","Hiperlipidemi (kolesterol/trigliserid artışı) ve bilişsel/duygudurum değişiklikleri","Hiperkalsemi","Hipotiroidi tek başına","Pulmoner fibrozis"],1,
 "Lorlatinib üçüncü kuşak ALK inhibitörüdür ve santral sinir sistemi metastazlarında çok etkilidir (CROWN çalışması). En sık yan etkisi hiperkolesterolemi ve hipertrigliseridemidir; çoğu hastada statin gerekir. Bilişsel bozulma, duygudurum değişiklikleri, konuşma bozuklukları, periferik nöropati, ödem ve kilo artışı da görülür. Alektinib ise miyalji/CK yüksekliği, bradikardi ve anemi yapabilir.",
 "Lorlatinib (ALK): hiperlipidemi (statin) + SSS yan etkileri; beyin metastazında çok etkili.")
