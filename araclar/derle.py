"""Soru bankasını derler ve uygulamayı oluşturur.

sorular/bolum*.py -> sorular/bank.json -> app/index.html (app/sablon.html içindeki __BANK__ yerine)
Çalıştırma: python3 araclar/derle.py
"""
import collections, glob, json, os, random, re

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = []

def Q(t, g, s, o, a, e, p):
    B.append(dict(t=t, g=g, s=s, o=o, a=a, e=e, p=p))

for yol in sorted(glob.glob(os.path.join(KOK, 'sorular', 'bolum*.py'))):
    kod = open(yol, encoding='utf-8').read()
    kod = kod.replace('B = []\n', '').replace(
        'def Q(t, g, s, o, a, e, p):\n    B.append(dict(t=t, g=g, s=s, o=o, a=a, e=e, p=p))\n', '')
    exec(kod, {'Q': Q})

sayac = collections.Counter()
for q in B:
    if q['s'].startswith('Plevral efüzyonun eksüda'):
        q['o'][4] = 'Hiçbiri; hepsi Light kriteridir'
    assert len(q['o']) == 5 and 0 <= q['a'] < 5, q['s']
    sayac[q['t']] += 1
    q['id'] = f"{q['t']}-{sayac[q['t']]:02d}"

# Doğru şıkların A-E arasında dengeli dağılması için sabit tohumla karıştır.
# Sayısal sıralı şıklar ve "Hiçbiri" içeren sorular karıştırılmaz.
rng = random.Random(2027)
for q in B:
    if all(re.match(r'^[<\d]', o) for o in q['o']) or q['o'][4].startswith('Hiçbiri'):
        continue
    sira = list(range(5))
    rng.shuffle(sira)
    q['o'] = [q['o'][i] for i in sira]
    q['a'] = sira.index(q['a'])

banka = json.dumps(B, ensure_ascii=False, separators=(',', ':'))
open(os.path.join(KOK, 'sorular', 'bank.json'), 'w', encoding='utf-8').write(banka)
sablon = open(os.path.join(KOK, 'app', 'sablon.html'), encoding='utf-8').read()
open(os.path.join(KOK, 'app', 'index.html'), 'w', encoding='utf-8').write(
    sablon.replace('__BANK__', banka.replace('</', '<\\/')))
print(len(B), 'soru:', dict(sayac))
