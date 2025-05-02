% SISTEM PAKAR MANAJEMEN JURUSAN

% DATABASE
:- dynamic minat_pos/1.
:- dynamic minat_neg/1.

% FAKTA & ATURAN
jurusan("Teknik Informatika").
jurusan("Teknik Mesin").
jurusan("Psikologi").
jurusan("Sastra Inggris").

minat(logika_matematika, "Teknik Informatika").
minat(komputer, "Teknik Informatika").
minat(pemrograman, "Teknik Informatika").

minat(fisika, "Teknik Mesin").
minat(mekanik, "Teknik Mesin").
minat(desain_teknik, "Teknik Mesin").

minat(berempati, "Psikologi").
minat(komunikasi, "Psikologi").
minat(observasi_perilaku, "Psikologi").

minat(bahasa_inggris, "Sastra Inggris").
minat(menulis, "Sastra Inggris").
minat(analisis_sastra, "Sastra Inggris").

pertanyaan(logika_matematika, Y) :-
    Y = "Apakah Anda suka logika atau matematika?".

pertanyaan(komputer, Y) :-
    Y = "Apakah Anda tertarik dengan komputer?".

pertanyaan(pemrograman, Y) :-
    Y = "Apakah Anda suka pemrograman?".

pertanyaan(fisika, Y) :-
    Y = "Apakah Anda menyukai pelajaran fisika?".

pertanyaan(mekanik, Y) :-
    Y = "Apakah Anda tertarik dengan mesin dan mekanik?".

pertanyaan(desain_teknik, Y) :-
    Y = "Apakah Anda suka mendesain sesuatu yang bersifat teknis?".

pertanyaan(berempati, Y) :-
    Y = "Apakah Anda merasa mudah berempati pada orang lain?".

pertanyaan(komunikasi, Y) :-
    Y = "Apakah Anda suka berkomunikasi dan mendengarkan orang lain?".

pertanyaan(observasi_perilaku, Y) :-
    Y = "Apakah Anda suka mengamati perilaku orang lain?".

pertanyaan(bahasa_inggris, Y) :-
    Y = "Apakah Anda suka belajar bahasa Inggris?".

pertanyaan(menulis, Y) :-
    Y = "Apakah Anda suka menulis karya seperti cerita atau artikel?".

pertanyaan(analisis_sastra, Y) :-
    Y = "Apakah Anda suka menganalisis karya sastra?".

