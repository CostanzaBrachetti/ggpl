from pyplasm import*
from math import*

def ggpl_My_Stair_Type(dx,dy,dz):
    piano = PROD([PROD([QUOTE([0.2]),QUOTE([dy])]),QUOTE([dz])])
    pedata = (0.15*dy)/dz
    numeroScalini = dy/pedata
    scalino = PROD([PROD([QUOTE([dx]),QUOTE([pedata])]),QUOTE([0.10])])
    scala = STRUCT([scalino])
    altezza = 0.15 
    profondita = 0
    while altezza<dz:
        profondita = profondita + pedata
        newScalino = T([2,3])([profondita,altezza])(scalino)
        scala = STRUCT([scala,newScalino])
        altezza = altezza + 0.15
    strutturaFinale = STRUCT([scala])
    return strutturaFinale
