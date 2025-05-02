% GEJALA PENYAKIT MALARIA
% DATABASE
:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

% PERTANYAAN
pertanyaan(nyeri_otot) :- write("Apakah Anda merasa nyeri otot?").
pertanyaan(muntah) :- write("Apakah Anda muntah-muntah?").
pertanyaan(kejang) :- write("Apakah Anda mengalami kejang-kejang?").
pertanyaan(menggigil) :- write("Apakah Anda sering menggigil?").
pertanyaan(tidak_enak_badan) :- write("Apakah Anda merasa tidak enak badan?").
pertanyaan(keringat_dingin) :- write("Apakah Anda mengalami keringat dingin?").
pertanyaan(sakit_kepala) :- write("Apakah Anda sering sakit kepala?").
pertanyaan(mimisan) :- write("Apakah Anda sering mimisan?").
pertanyaan(mual) :- write("Apakah Anda merasa mual?").
pertanyaan(demam) :- write("Apakah Anda demam?").

% DIAGNOSA GEJALA
diagnosa(G) :-
    pertanyaan(G),
    writeln(" (y/t)"),
    read(Jawaban),
    Jawaban == y,
    assertz(gejala_pos(G)).
diagnosa(G) :-
    assertz(gejala_neg(G)),
    fail.

% CEK GEJALA
gejala(G) :- gejala_pos(G), !.
gejala(G) :- gejala_neg(G), !, fail.
gejala(G) :- diagnosa(G).

% PENYAKIT
penyakit(tertiana) :-
    gejala(nyeri_otot),
    gejala(muntah),
    gejala(kejang),
    terdeteksi("Malaria Tertiana").

penyakit(quartana) :-
    gejala(nyeri_otot),
    gejala(menggigil),
    gejala(tidak_enak_badan),
    terdeteksi("Malaria Quartana").

penyakit(tropika) :-
    gejala(keringat_dingin),
    gejala(sakit_kepala),
    gejala(mimisan),
    gejala(mual),
    terdeteksi("Malaria Tropika").

penyakit(pernisiosa) :-
    gejala(menggigil),
    gejala(tidak_enak_badan),
    gejala(demam),
    gejala(mimisan),
    gejala(mual),
    terdeteksi("Malaria Pernisiosa").

penyakit(_) :-
    writeln("Tidak terdeteksi penyakit.").

% TERDETEKSI
terdeteksi(P) :-
    write("Anda terdeteksi penyakit "),
    writeln(P).

% CLEAR DATABASE
clear_db :-
    retractall(gejala_pos(_)),
    retractall(gejala_neg(_)).

% MAIN LOOP
main :-
    write('\33\[2J'), % Clear window
    writeln("DIAGNOSA PENYAKIT MALARIA"),
    penyakit(_),
    clear_db,
    writeln("INGIN MENGULANG? (y/t)"),
    read(Jawaban), !,
    Jawaban == y,
    main.
