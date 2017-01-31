from pyplasm import*
from creaPiano1 import*
from creaPiano2 import*
from traslaScala import*
import csv

def casaDuePiani():
    pianoTerra = creaPlanimetria1("muriEst.lines")
    dxScala = larghezzaScala()
    scala = ggpl_My_Stair_Type(dxScala,7.2,3) 
    scalaTraslata = puntiScala(scala)
    scalaTraslata = T([1,2])([-0.4,0.8])(scalaTraslata)
    secondoPiano = creaPlanimetria2("muriEst.lines")
    struttura = STRUCT([pianoTerra,secondoPiano,scalaTraslata])
    primopiano = STRUCT([pianoTerra,scalaTraslata])
    difetto = CUBOID([1,1,3])
    return(struttura)

def creaTetto(file_name):
    planimetria = STRUCT([QUOTE([0])])
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            planimetria = STRUCT([planimetria,riga]) 
    listaPunti = UKPOL(planimetria)
    V = listaPunti[0]
    lista = pulisciLista(V)
    EV = listaPunti[1]
    FV = []
    for i in range(1,len(V)):
        FV.append(i)
    FV = [FV]
    pavimento = EXPLODE(1,1,1)(MKPOLS((V,FV)))
   
    tetto = MKPOL([[[3,42,0],[32,42,0],[32,11,0],[3,11,0],[10,35,4],[25,35,4],[25,18,4],[10,18,4]],[[1,2,6,5],[2,3,7,6],[3,4,8,7],                [1,5,8,4],[5,6,7,8]],1])
    tetto = OFFSET([0.2,0.2,0.2])(tetto)
    tetto = T([1,2])([0.5,0.2])(tetto)
    pavimento = OFFSET([0.2,0.2,0.1])(pavimento)
    tetto = TEXTURE(["textureTetto.jpg",True,False,1,1,0,3,3])(tetto)
    tetto = MATERIAL([84,42,12,1,  0,0,0,1,  0,0,0,1, 0,0,0,1, 1])(tetto)
    tetto = STRUCT([pavimento,tetto])
    tetto = T(3)(3)(tetto)
    return tetto

def casaUnPiano():
    pianoTerra = creaPlanimetria1("muriEst.lines")
    tetto = creaTetto("muriEst.lines")
    casa = STRUCT([pianoTerra,tetto])
    return(casa)