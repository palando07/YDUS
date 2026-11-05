T('onko', "ESMO ve NCCN kılavuzları, ASCO/IDSA febril nötropeni, ASCO immün ilişkili yan etki kılavuzu, USPSTF 2021 akciğer taraması")

S("Onkolojik aciller", ["tümör lizis","febril nötropeni","mascc","spinal kord bası","vena kava","hiperkalsemi","malignite hiperkalsemisi","hiperviskozite","lökostaz"], """
- Tümör lizis sendromu: hiperürisemi, hiperkalemi, hiperfosfatemi, hipokalsemi ± AKİ. Önlem: bol sıvı; orta riskte allopürinol, yüksek riskte rasburikaz (G6PD eksikliğinde kontrendike).
- Febril nötropeni: MNS <500/µL (veya <500'e düşmesi beklenen) + ateş ≥38,3 °C tek ölçüm veya ≥38 °C 1 saat. İlk 1 saat içinde antipsödomonal beta laktam (sefepim, piperasilin-tazobaktam, meropenem).
- Vankomisin eklenecek durumlar: hemodinamik instabilite, kateter enfeksiyonu, deri-yumuşak doku enfeksiyonu, pnömoni, MRSA kolonizasyonu, ağır mukozit.
- MASCC ≥21 düşük risk → seçilmiş hastada oral amoksisilin-klavulanat + siprofloksasin ile ayaktan.
- Malign spinal kord basısı: sırt ağrısı + nörolojik bulgu; acil tüm omurga MR, yüksek doz deksametazon, RT ve/veya dekompresif cerrahi.
- Malignite hiperkalsemisi: en sık PTHrP (skuamöz hücreli kanserler); tedavi SF + zoledronat/denosumab.
! SVK sendromunda stridor veya bilinç bozukluğu yoksa tedaviden önce doku tanısı alınır; stridorda önce stent.
""")

S("Akciğer kanseri", ["akciğer kanseri","egfr","alk","osimertinib","pd-l1","pembrolizumab","küçük hücreli","yassı hücreli","adenokarsinom","düşük doz bt","paraneoplastik"], """
- Tarama (USPSTF 2021): 50-80 yaş, ≥20 paket-yıl, aktif içici veya son 15 yılda bırakmış → yıllık düşük doz BT.
| KHDAK sürücü mutasyonu | Tedavi |
| EGFR | Osimertinib (adjuvan ADAURA; ileri evrede ± kemoterapi veya amivantamab-lazertinib) |
| ALK | Alektinib, lorlatinib, brigatinib |
| ROS1 | Krizotinib, entrektinib, repotrektinib |
| KRAS G12C | Sotorasib, adagrasib (ikinci basamak) |
| BRAF V600E | Dabrafenib + trametinib |
- Sürücü mutasyon yoksa: PD-L1 ≥%50 → pembrolizumab tek başına (veya kemoimmünoterapi); <%50 → kemoterapi + immünoterapi.
- Rezektabl evre II-III: perioperatif kemoimmünoterapi.
- KHAK: sınırlı evre kemoradyoterapi (platin-etoposid) ve ardından durvalumab; yaygın evre platin-etoposid + atezolizumab/durvalumab. Profilaktik kraniyal ışınlama yerine MR izlemi seçenek.
| Paraneoplastik | Tümör |
| SIADH, ektopik ACTH, Lambert-Eaton | Küçük hücreli |
| PTHrP hiperkalsemisi | Yassı hücreli |
| Hipertrofik osteoartropati | Adenokarsinom |
! Pancoast tümörü: omuz ağrısı, Horner sendromu, el kaslarında atrofi.
""")

S("Meme kanseri", ["meme kanseri","her2","trastuzumab","pertuzumab","üçlü negatif","cdk4/6","tamoksifen","aromataz","brca","t-dxd"], """
| Alt tip | Temel tedavi |
| HR+ HER2− | Endokrin tedavi 5-10 yıl; yüksek riskte adjuvan abemasiklib veya ribosiklib |
| HER2+ | Kemoterapi + trastuzumab ± pertuzumab; rezidüde T-DM1 |
| Üçlü negatif | Neoadjuvan kemoterapi + pembrolizumab; rezidüde kapesitabin, gBRCA'da olaparib |
- Metastatik HR+ HER2−: aromataz inhibitörü + CDK4/6 inhibitörü; kemoterapi yalnız visseral krizde.
- HER2 düşük metastatik hastalıkta trastuzumab derukstekan (interstisyel akciğer hastalığı yapabilir).
- Tamoksifen: endometriyum kanseri ve VTE riski; premenopozda tercih. Aromataz inhibitörü: kemik kaybı, artralji; postmenopozda.
- Trastuzumab kardiyotoksisitesi geri dönüşümlüdür; 3 ayda bir EF izlenir.
- BRCA1 taşıyıcısı: 35-40 yaşta salpingo-ooferektomi; meme MR taraması 25 yaşından itibaren.
""")

S("GİS kanserleri", ["kolorektal","kolon kanseri","rektum","folfox","msi","dmmr","mide kanseri","pankreas kanseri","folfirinoks","hcc","hepatoselüler","gist","cea"], """
- Kolon kanseri evre III: adjuvan FOLFOX veya CAPOX (düşük riskte CAPOX 3 ay yeterli).
- Evre II: yüksek risk özelliklerinde (T4, <12 lenf düğümü, perforasyon) adjuvan; dMMR/MSI-H evre II'de 5-FU tek başına yarar sağlamaz.
- Metastatik dMMR/MSI-H: ilk basamak pembrolizumab veya nivolumab + ipilimumab.
- Metastatik RAS/BRAF yabanıl, sol yerleşimli: kemoterapi + anti-EGFR (setuksimab, panitumumab). BRAF V600E: enkorafenib + setuksimab.
- dMMR lokal ileri rektum kanseri: dostarlimab ile yüksek tam klinik yanıt; cerrahiden kaçınılabilir.
- Mide: HER2+ → trastuzumab; klaudin 18.2+ → zolbetuksimab; PD-L1 CPS yüksekse nivolumab/pembrolizumab. Perioperatif FLOT.
- Pankreas: rezektabl → cerrahi + adjuvan mFOLFIRINOKS; metastatikte FOLFIRINOKS veya gemsitabin + nab-paklitaksel; gBRCA'da olaparib idame.
- HCC ileri evre: atezolizumab + bevasizumab veya durvalumab + tremelimumab.
- GIST: KIT/PDGFRA; imatinib. PDGFRA D842V imatinibe dirençli (avapritinib).
! Kolon kanserinde ameliyat sonrası CEA yükselmesi nüksü düşündürür; CEA tarama testi değildir.
""")

S("Ürogenital kanserler", ["prostat","psa","androjen","abirateron","enzalutamid","böbrek hücreli","rcc","testis","germ hücreli","mesane kanseri"], """
- Metastatik hormona duyarlı prostat kanseri: ADT + androjen reseptör yolu inhibitörü (abirateron, enzalutamid, apalutamid, darolutamid) ± dosetaksel.
- Kastrasyona dirençli: AR yolu inhibitörü, dosetaksel, kabazitaksel; HRR/BRCA mutasyonunda PARP inhibitörü; PSMA (+) hastada lutesyum-177 PSMA.
- Renal hücreli kanser ileri evre: immünoterapi kombinasyonları (pembrolizumab + aksitinib veya lenvatinib; nivolumab + kabozantinib veya ipilimumab). Paraneoplastik: polisitemi, hiperkalsemi, Stauffer sendromu.
- Testis tümörü: AFP yüksekse seminom değildir (nonseminom). β-hCG her ikisinde de olabilir. Tedavi orşiektomi + risk grubuna göre BEP. Biyopsi skrotal yoldan yapılmaz.
- Kas invaziv mesane kanseri: neoadjuvan sisplatinli kemoterapi + sistektomi; metastatikte enfortumab vedotin + pembrolizumab.
""")

S("Tümör belirteçleri", ["tümör belirteci","ca-125","ca 19-9","afp","beta-hcg","kalsitonin","kromogranin","ldh"], """
| Belirteç | Ana kullanım | Yanıltıcı yükselme |
| CEA | Kolorektal kanser izlemi | Sigara, İBH, karaciğer hastalığı |
| CA 19-9 | Pankreas, safra yolu | Kolestaz, kolanjit; Lewis antijen (−) kişilerde salgılanmaz |
| CA-125 | Over kanseri izlemi | Endometriyoz, gebelik, asit, menstrüasyon |
| AFP | HCC, nonseminom | Gebelik, hepatit, siroz |
| β-hCG | Germ hücreli tümör, koryokarsinom | Gebelik |
| Kalsitonin | Medüller tiroid kanseri | KBH, PPI |
| Kromogranin A | Nöroendokrin tümör | PPI, atrofik gastrit, KBH |
! Tümör belirteçleri (PSA hariç tartışmalı) tarama amacıyla kullanılmaz; tanı ve yanıt izleminde yardımcıdır.
""")

S("İmmünoterapi ve kemoterapi toksisiteleri", ["immünoterapi","immün ilişkili","kontrol noktası","nivolumab","ipilimumab","kolit","pnömonit","hipofizit","miyokardit","antrasiklin","doksorubisin","sisplatin","bleomisin","siklofosfamid","metotreksat","irinotekan","5-fu"], """
| İmmün ilişkili yan etki | Not |
| Kolit | Grade ≥2'de steroid; dirençte infliksimab veya vedolizumab |
| Pnömonit | Steroid; dirençte infliksimab, MMF |
| Hepatit | Steroid; dirençte MMF (infliksimab değil) |
| Hipofizit | En sık ipilimumab; yerine koyma tedavisi |
| Tiroidit | En sık anti-PD-1; çoğu kalıcı hipotiroidi |
| Tip 1 diyabet | DKA ile başlayabilir; insülin |
| Miyokardit | Nadir ama mortal; yüksek doz steroid, tedavi kalıcı kesilir |
- Endokrin yan etkilerde hormon yerine konarak immünoterapiye çoğunlukla devam edilebilir.
| Kemoterapi | Toksisite | Önlem/antidot |
| Antrasiklin | Doza bağımlı KMP | Kümülatif doz sınırı, deksrazoksan |
| Bleomisin | Pulmoner fibrozis | Yüksek FiO2'den kaçın |
| Sisplatin | Nefrotoksisite, ototoksisite, hipomagnezemi | Hidrasyon, Mg |
| Siklofosfamid/ifosfamid | Hemorajik sistit | Mesna |
| Metotreksat | Mukozit, miyelosupresyon, AKİ | Lökovorin, glukarpidaz |
| 5-FU/kapesitabin | DPD eksikliğinde ağır toksisite, koroner vazospazm | Uridin triasetat, DPYD testi |
| İrinotekan | İshal (UGT1A1*28) | Loperamid |
| Vinkristin | Periferik nöropati | Doz azaltma |
""")
