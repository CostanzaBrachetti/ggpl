from pyplasm import*
def trasla(palazzo,asseX,asseY,asseZ):
    palazzoCompleto = STRUCT([palazzo,T(1)(asseX)(palazzo)])
    palazzoCompleto = STRUCT([palazzoCompleto,T(2)(asseY)(palazzoCompleto)])
    palazzoPianiAlti = STRUCT([palazzoCompleto,T(3)(asseZ)(palazzoCompleto)])
    return palazzoPianiAlti