def tah(tah_pole, cislo_policka, symbol):

    "Vrátí herní pole s daným symbolem umístěným na danou pozici."

    return tah_pole[:cislo_policka] + symbol + tah_pole[cislo_policka + 1:]
