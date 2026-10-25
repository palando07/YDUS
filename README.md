# YDUS Çalışma Defteri

İç hastalıkları yan dal (YDUS) sınavına hazırlanan iki kişi için soru odaklı çalışma uygulaması.

Canlı sürüm: https://claude.ai/artifact/GwBgZBfDxwwAmM7FjWkqV9 (claude.ai hesabıyla açılır, ilerleme orada saklanır)

## Neler var

- 11 dahiliye konusunda açıklamalı soru bankası; her sorunun açıklaması ve tek cümlelik "sınav incisi" var
- Çalışma modu (anında açıklama) ve süreli deneme sınavı modu
- Yanlış yapılan soruların otomatik eklendiği aralıklı tekrar kartları
- Profil bazında ilerleme, konu bazında başarı karşılaştırması ve çalışma planı
- Kendi sorunu tek tek ya da kopyala-yapıştırla toplu ekleme

Hazır sorular YDUS'ta sık sorulan konu ve kavramlar esas alınarak yazılmış özgün sorulardır; birebir çıkmış soru değildir. Güncel kılavuzlarla teyit ederek kullanın.

## Klasör yapısı

| Yol | İçerik |
| --- | --- |
| `sorular/bolum1.py` … `bolum4.py` | Soru bankasının kaynağı. Her soru bir `Q(konu, tür, kök, şıklar, doğru_indeks, açıklama, inci)` çağrısı |
| `sorular/bank.json` | Derlenmiş soru bankası |
| `app/sablon.html` | Uygulamanın kaynağı; `__BANK__` yerine soru bankası konur |
| `app/index.html` | Yayınlanan, tek dosyalık uygulama |
| `araclar/derle.py` | Bankayı derleyip `app/index.html`'i oluşturur |

Konu kodları: `kardiyo`, `gastro`, `nefro`, `sivi`, `endo`, `hemato`, `onko`, `romato`, `gogus`, `enf`, `geri`.
Soru türleri: `sik` (sık sorulan tema), `olasi` (olası soru / güncel kılavuz).

## Soru eklemek

1. İlgili `sorular/bolum*.py` dosyasına, konunun bulunduğu yere yeni bir `Q(...)` ekleyin. Doğru cevap indeksi 0'dan başlar (A=0, E=4).
2. `python3 araclar/derle.py` çalıştırın.
3. `app/index.html` canlı sürüme yeniden yayınlanır.

Soru kimlikleri (`kardiyo-01` gibi) konu içindeki sıraya göre verilir ve çözülen soruların kaydı bu kimliklere bağlıdır. Yeni soruları konunun sonuna ekleyin; mevcut soruların sırasını değiştirmeyin.
