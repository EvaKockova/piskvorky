from tool import tah
from ai import tah_pocitace


def vyhodnot(pole, symbol_hrace, symbol_pocitace):
    if symbol_hrace * 3 in pole:
        return 'vyhra hrace'
    elif symbol_pocitace * 3 in pole:
        return 'vyhra počítače'
    elif '-' not in pole:
        return '!'
    else:
        return '-'

def tah_hrace(konkretni_pole, symbol_hrace, delka_retezce):
    delka_retezce = len(konkretni_pole)
    konkretni_tah = int(input('Hráči, na kterém poli chceš hrát?'))

    while konkretni_tah > delka_retezce: #and konkretni_tah < 0:
        print('Zadej číslo v rozsahu 1 -', delka_retezce, '.')
        konkretni_tah = int(input('Hráči, na kterém poli chceš hrát?'))

    while konkretni_pole[konkretni_tah] != '-':
        print('Obsazeno')
        konkretni_tah = int(input('Hráči, na kterém poli chceš hrát?'))

    return tah(konkretni_pole, konkretni_tah, symbol_hrace)


def piskvorky1d(delka_retezce):
    piskvorky_pole = '-' * delka_retezce
    "Funkce vytvoří řetězec s herním polem a střídá tah hráče a tah počítače."
    symbol_hrace = input('Hráči, vyber si symbol. Zadej x nebo o, prosím.')
    while symbol_hrace != 'x' or 'o':
        if symbol_hrace == 'x':
            symbol_pocitace = 'o'
            break
        elif symbol_hrace == 'o':
            symbol_pocitace = 'x'
            break
        else:
            symbol_hrace = input('Hráči, vyber si symbol. Zadej x nebo o, prosím.')

    while True:
        prvni_tah = tah_hrace(piskvorky_pole, symbol_hrace, delka_retezce)
        print(prvni_tah)
        vyhodnoceni = vyhodnot(prvni_tah, symbol_hrace, symbol_pocitace)
        print(vyhodnoceni)
        if vyhodnoceni == 'vyhra hrace':
            return 'Gratuluji k výhře!'
            break
        elif vyhodnoceni == '!':
            return 'Remíza.'
            break
        elif vyhodnoceni == 'vyhra pocitace':
            return 'Bohužel, prohrál jsi.'
            break

        druhy_tah_PC = tah_pocitace(prvni_tah, symbol_pocitace, symbol_hrace, delka_retezce)
        print(druhy_tah_PC)
        vyhodnoceni = vyhodnot(druhy_tah_PC, symbol_hrace, symbol_pocitace)
        print(vyhodnoceni)
        if vyhodnoceni == 'vyhra hrace':
            return 'Gratuluji k výhře!'
            break
        elif vyhodnoceni == '!':
            return 'Remíza.'
            break
        elif vyhodnoceni == 'vyhra pocitace':
            return 'Bohužel, prohrál jsi.'
            break

        piskvorky_pole = druhy_tah_PC

    return 'Gratuluji ke skvělé hře!'
