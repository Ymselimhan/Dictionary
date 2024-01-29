import tkinter as tk
from tkinter import messagebox
import json

# Sözlük verileri (kelime: {"anlam": anlam, "cumle_tr": cümle_tr, "cumle_en": cümle_en})
sozluk = {}

def kelime_ara(event=None):
    kelime = entry_kelime.get().lower()
    veri = sozluk.get(kelime, {"anlam": "Kelime bulunamadı.", "cumle_tr": "", "cumle_en": ""})
    messagebox.showinfo("Sözlük", f"{kelime.capitalize()}: {veri['anlam']}\nCümle (TR): {veri['cumle_tr']}\nCümle (EN): {veri['cumle_en']}")
    guncelle_liste(kelime)

def kelime_ekle():
    kelime = entry_kelime_ekle.get().lower()
    anlam = entry_anlam_ekle.get()
    cumle_tr = entry_cumle_tr_ekle.get()
    cumle_en = entry_cumle_en_ekle.get()
    sozluk[kelime] = {"anlam": anlam, "cumle_tr": cumle_tr, "cumle_en": cumle_en}
    kaydet()
    guncelle_liste(kelime)

def kaydet():
    with open("sozluk.json", "w") as dosya:
        json.dump(sozluk, dosya)
    messagebox.showinfo("Başarılı", "Sözlük kaydedildi!")

def yukle():
    try:
        with open("sozluk.json", "r") as dosya:
            return json.load(dosya)
    except FileNotFoundError:
        return {}

def guncelle_liste(bulunan_kelime=None):
    liste.delete(0, tk.END)  # Mevcut liste elemanlarını temizle
    for kelime in sorted(sozluk.keys()):
        veri = sozluk[kelime]
        liste.insert(tk.END, f"{kelime.capitalize()}: {veri['anlam']}")
    label_liste["text"] = "Kelimeler"

    if bulunan_kelime:
        label_bulunan_var.set(f"Bulunan Kelime: {bulunan_kelime.capitalize()}")
    else:
        label_bulunan_var.set("Bulunan Kelime: ")

# Tkinter penceresi oluştur
pencere = tk.Tk()
pencere.title("İngilizce-Türkçe Sözlük Uygulaması")

# Verileri yükle
sozluk = yukle()

# Arayüz elemanları
label_baslik = tk.Label(pencere, text="İngilizce-Türkçe Sözlük", font=("Helvetica", 16))
label_baslik.pack(pady=10)

# Kelime Ara
label_giris = tk.Label(pencere, text="Kelime:")
label_giris.pack()

entry_kelime = tk.Entry(pencere, width=50)
entry_kelime.pack(pady=5)

button_ara = tk.Button(pencere, text="Ara", command=kelime_ara)
button_ara.pack(pady=10)

# Kelime Ekle
label_ekle = tk.Label(pencere, text="Yeni Kelime:")
label_ekle.pack()

entry_kelime_ekle = tk.Entry(pencere, width=50)
entry_kelime_ekle.pack(pady=5)

label_anlam_ekle = tk.Label(pencere, text="Anlam:")
label_anlam_ekle.pack()

entry_anlam_ekle = tk.Entry(pencere, width=50)
entry_anlam_ekle.pack(pady=5)

label_cumle_tr_ekle = tk.Label(pencere, text="Cümle (TR):")
label_cumle_tr_ekle.pack()

entry_cumle_tr_ekle = tk.Entry(pencere, width=50)
entry_cumle_tr_ekle.pack(pady=5)

label_cumle_en_ekle = tk.Label(pencere, text="Cümle (EN):")
label_cumle_en_ekle.pack()

entry_cumle_en_ekle = tk.Entry(pencere, width=50)
entry_cumle_en_ekle.pack(pady=5)

button_ekle = tk.Button(pencere, text="Kelime Ekle", command=kelime_ekle)
button_ekle.pack(pady=10)

# Bulunan Kelime Etiketi
label_bulunan_var = tk.StringVar()
label_bulunan = tk.Label(pencere, textvariable=label_bulunan_var)
label_bulunan.pack(pady=10)

# Kelimelerin Listesi
label_liste = tk.Label(pencere, text="Kelimeler")
label_liste.pack()

liste = tk.Listbox(pencere, selectmode=tk.SINGLE, height=10, width=80)
liste.pack(pady=10)
guncelle_liste()

# Tkinter penceresini kapatma olayını yakala
pencere.protocol("WM_DELETE_WINDOW", kaydet)

# Ara butonuna Enter tuşuyla da tepki verme
entry_kelime.bind("<Return>", kelime_ara)

# Tkinter penceresini başlat
pencere.mainloop()
