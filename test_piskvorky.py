from ai import tah_pocitace
from piskvorky1 import vyhodnot
from tool import tah

def test_vyhodnot_xxx():
    vysledne_pole = '---xxx--------------'
    assert vyhodnot(vysledne_pole, 'x', 'o') == 'vyhra hrace'

def test_vyhodnot_ooo():
    vysledne_pole_ooo = '-------ooo----------'
    assert vyhodnot(vysledne_pole_ooo, 'x', 'o') == 'vyhra počítače'

def test_vyhodnot_vykricnik():
    vysledne_pole_vykricnik = 'xoxoxoxoxoxoxoxoxoxo'
    assert vyhodnot(vysledne_pole_vykricnik, 'x', 'o') == '!'

def test_tah():
    pole_test_tah = '-' * 20
    assert tah(pole_test_tah, 0, 'x') == 'x-------------------'

def test_tah_podruhe():
    pole_test_tah = '-' * 20
    assert tah(pole_test_tah, 0, 'o') == 'o-------------------'









#def test_delka_hraciho_pole():
    #pole = ai.PC_pole
    #assert len(pole) == 19
