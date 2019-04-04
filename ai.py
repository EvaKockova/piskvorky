from tool import tah
from random import randrange

def tah_pocitace(PC_pole, symbol_pocitace, symbol_hrace, delka_retezce):
    "Vrátí herní pole se zaznamenaným tahem počítače."
    PPV = symbol_pocitace + symbol_pocitace + '-'
    PVP = symbol_pocitace + '-' + symbol_pocitace
    VPP = '-' + symbol_pocitace + symbol_pocitace
    HHV = symbol_hrace + symbol_hrace + '-'
    HVH = symbol_hrace + '-' + symbol_hrace
    VHH = '-' + symbol_hrace + symbol_hrace
    HV = symbol_hrace + '-'
    VH = '-' + symbol_hrace
    PV = symbol_pocitace + '-'
    VP = '-' + symbol_pocitace

    if PPV in PC_pole:
        index_PPV = PC_pole.find(PPV)
        PC_tah = index_PPV + 2
    elif PVP in PC_pole:
        index_PVP = PC_pole.find(PVP)
        PC_tah = index_PVP + 1
    elif VPP in PC_pole:
        index_VPP = PC_pole.find(VPP)
        PC_tah = index_VPP

    elif HHV in PC_pole:
        index_HHV = PC_pole.find(HHV)
        PC_tah = index_HHV + 2
    elif HVH in PC_pole:
        index_HVH = PC_pole.find(HVH)
        PC_tah = index_HVH + 1
    elif VHH in PC_pole:
        index_VHH = PC_pole.find(VHH)
        PC_tah = index_VHH


    elif PV in PC_pole:
        index_PV = PC_pole.find(PV)
        PC_tah = index_PV + 1
    elif VP in PC_pole:
        index_VP = PC_pole.find(VP)
        PC_tah = index_VP
    elif HV in PC_pole:
        index_HV = PC_pole.find(HV)
        PC_tah = index_HV + 1
    elif VH in PC_pole:
        index_VH = PC_pole.find(VH)
        PC_tah = index_VH

    else:
        PC_tah = randrange(0, delka_retezce)
        while PC_pole[PC_tah] != '-':
            PC_tah = randrange(0, delka_retezce)

    return tah(PC_pole, PC_tah, symbol_pocitace)
