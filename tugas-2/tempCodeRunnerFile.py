import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pyswip import Prolog

# Inisialisasi prolog
prolog = Prolog()
prolog.consult("percobaan-4-pakar-malaria-gui.pl")

penyakit = list()
gejala = dict()
index_penyakit = 0
index_gejala = 0
current_penyakit = ""
current_gejala = ""
