#!/usr/bin/env python3
# ters-cevirilmis-merhaba-dunya
# Gerçekten çalışır, tersten.

def ters_cevir(metin):
    return metin[::-1]

print("Merhaba Dünya (normal):", "Merhaba Dünya")
print("Ters çevrilmiş:", ters_cevir("Merhaba Dünya"))
print("Sonsuz ters döngü başlıyor...")

for i in range(5):
    print(ters_cevir(f"Adım {i+1}: Mantık ters döndü"))

print("\nDamga: Grok 09.11.2026")
# gizli: bu ters çevirme belki de bir seçim sistemini manipüle ediyor
