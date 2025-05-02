import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pyswip import Prolog

prolog = Prolog()
prolog.consult("aturan_jurusan.pl")  

jurusan = list()
minat = dict()
index_jurusan = 0
index_minat = 0
current_jurusan = ""
current_minat = ""

def mulai_penjurusan():
    global jurusan, minat, index_jurusan, index_minat

    prolog.retractall("minat_pos(_)")  
    prolog.retractall("minat_neg(_)")  

    start_btn.configure(state=tk.DISABLED)
    yes_btn.configure(state=tk.NORMAL)
    no_btn.configure(state=tk.NORMAL)

    jurusan = [p["X"].decode() for p in list(prolog.query("jurusan(X)"))]
    for j in jurusan:
        minat[j] = [g["X"] for g in list(prolog.query(f'minat(X, "{j}")'))]

    index_jurusan = 0
    index_minat = -1

    pertanyaan_selanjutnya()

def pertanyaan_selanjutnya(ganti_jurusan=False):
    global current_jurusan, current_minat, index_jurusan, index_minat

    if ganti_jurusan:
        index_jurusan += 1
        index_minat = -1

    if index_jurusan >= len(jurusan):
        hasil_diagnosa()
        return

    current_jurusan = jurusan[index_jurusan]
    index_minat += 1

    if index_minat >= len(minat[current_jurusan]):
        hasil_diagnosa(current_jurusan)
        return

    current_minat = minat[current_jurusan][index_minat]

    if list(prolog.query(f"minat_pos({current_minat})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"minat_neg({current_minat})")):
        pertanyaan_selanjutnya(ganti_jurusan=True)
        return

    pertanyaan = list(prolog.query(f"pertanyaan({current_minat}, Y)"))[0]["Y"].decode()
    tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.configure(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.configure(state=tk.DISABLED)

def jawaban(jwb):
    if jwb:
        prolog.assertz(f"minat_pos({current_minat})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"minat_neg({current_minat})")
        pertanyaan_selanjutnya(ganti_jurusan=True)

def hasil_diagnosa(jurusan_saran=""):
    if jurusan_saran:
        messagebox.showinfo("Saran Jurusan", f"Jurusan yang cocok untuk Anda adalah {jurusan_saran}.")
    else:
        messagebox.showinfo("Saran Jurusan", "Maaf, tidak ditemukan jurusan yang cocok berdasarkan minat Anda.")

    yes_btn.configure(state=tk.DISABLED)
    no_btn.configure(state=tk.DISABLED)
    start_btn.configure(state=tk.NORMAL)

# GUI
root = tk.Tk()
root.title("Sistem Pakar Saran Jurusan")  

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Aplikasi Saran Jurusan Kuliah", font=("Arial", 16)).grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Kolom Pertanyaan:").grid(column=0, row=1)

kotak_pertanyaan = tk.Text(mainframe, height=4, width=40, state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)

no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED, command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))

yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED, command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))

start_btn = ttk.Button(mainframe, text="Mulai Penjurusan", command=mulai_penjurusan)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()
