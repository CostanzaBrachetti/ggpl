from pyplasm import*
from larlib import* 
import math
import csv
import fpformat

def stringToFloat(str):
    l = str.split(',')
    newList=[]
    for c in l:
        elem = float(c)/20.
        newList.append(elem)
    return newList


def strutturaInterna(file_name):
    #interni = STRUCT([QUOTE([0])])
    interni = 0
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            if interni != 0: 
                interni = STRUCT([interni,riga])
            else:
                interni = riga     
        interni = OFFSET([0.1,0.1,3])(interni)
    #listaPunti = UKPOL(interni)
    #V = listaPunti[0]
    #V.remove(0)
    #listaPunti[0] = V
    return interni


def creaBuchiFin(file_name): 
    finestre = 0
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            if finestre != 0:
                finestre = STRUCT([finestre,riga])     
            else:
                finestre = riga
    finestre = T(3)(1.3)(finestre)
    return finestre

def creaFinestre(file_name): 
    finestre = 0
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            riga = OFFSET([0.18,0.18,1])(riga)
            riga = T(3)(1.3)(riga)
            riga = TEXTURE("vetro.jpg")(riga)
            if finestre != 0:
                finestre = STRUCT([finestre,riga])     
            else:
                finestre = riga
    return finestre
        
def lunghezzaCella(lista):
    newLista = []
    for i in range(len(lista)):
        newLista.append(i+1)
    return newLista   

def porteInterne(file_name):
    porte = 0
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            if porte != 0:
                porte = STRUCT([porte,riga])
            else:
                porte = riga
        porte = OFFSET([0.15,0.15,0])(porte)
        porte = OFFSET([-0.10,0,2])(porte)
    return porte


def rimuoviDoppioni(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

def creaBucoScala(file_name):
    bucoScala = STRUCT([QUOTE([0])])
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            bucoScala = STRUCT([bucoScala,riga])
    listaPunti = UKPOL(bucoScala)
    V = listaPunti[0]
    V.remove(V[0])
    #V = rimuoviDoppioni(V)
    #print V
    EV = listaPunti[1]
    FV = []
    listaVer = []
    buco = STRUCT([QUOTE([0])])
    for i in range(0,len(V)):
        elem = V[i]
        listaVer.append([elem[0],elem[1]])
    for i in range(0,len(listaVer)-1):
        if listaVer[i+1] != None:
            buco = STRUCT([buco,POLYLINE([listaVer[i],listaVer[i+1]])])
        else: 
            buco = STRUCT([buco,POLYLINE([listaVer[i],listaVer[0]])])
        i+2
    buco = SOLIDIFY(buco)
    return buco

def contScala(file_name):
    muretto = 0
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            if muretto != 0:
                muretto = STRUCT([muretto,riga])
            else:
                muretto = riga
    muretto = OFFSET([0.1,0.1,1])(muretto)
    return muretto
    
def creaPavimento(file_name):
    pavimento = STRUCT([QUOTE([0])])
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            pavimento = STRUCT([pavimento,riga])
    listaPunti = UKPOL(pavimento)
    V = listaPunti[0]
    V.remove(V[0])
    #V = rimuoviDoppioni(V)
    #print V
    EV = listaPunti[1]
    FV = []
    listaVer = []
    pav = STRUCT([QUOTE([0])])
    for i in range(0,len(V)):
        elem = V[i]
        listaVer.append([elem[0],elem[1]])
    for i in range(0,len(listaVer)-1):
        if listaVer[i+1] != None:
            pav = STRUCT([pav,POLYLINE([listaVer[i],listaVer[i+1]])])
        else: 
            pav = STRUCT([pav,POLYLINE([listaVer[i],listaVer[0]])])
        i+2
    pav = SOLIDIFY(pav)
    #pavimento = EXPLODE(1,1,1)(MKPOLS((V,FV)))
    #pavimento = OFFSET([0,0,0.1])(pavimento)
    
    return pav

def creaMuri(file_name):
    planimetria = 0
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            if planimetria != 0:
                planimetria= STRUCT([planimetria,riga]) 
            else:
                planimetria = riga
    #planimetria = OFFSET([0.2,0.2,3])(planimetria)
    return planimetria

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
   
    tetto = MKPOL([[[3,42,0],[32,42,0],[32,11,0],[3,11,0],[10,35,3],[25,35,3],[25,18,3],[10,18,3]],[[1,2,6,5],[2,3,7,6],[3,4,8,7],                [1,5,8,4],[5,6,7,8]],1])
    tetto = OFFSET([0.2,0.2,0.2])(tetto)
    tetto = T([1,2])([0.5,0.2])(tetto)
    pavimento = OFFSET([0.2,0.2,0.1])(pavimento)
    tetto = provaMaterial(tetto)
    tetto = STRUCT([pavimento,tetto])
    tetto = T(3)(3)(tetto)
    return tetto

def provaMaterial(tetto):
    tetto = TEXTURE(["textureTetto.jpg",True,False,1,1,0,3,3])(tetto)
    tetto = MATERIAL([84,42,12,1,  0,0,0,1,  0,0,0,1, 0,0,0,1, 1])(tetto)
    return tetto
    
def pulisciLista(lista):
    newL = []
    for i in lista:
        elem = []
        for j in i:
            a = int(j)
            elem.append(a)
        newL.append(elem)
    noDop = rimuoviDoppioni(newL)
    return noDop
    
    

def creaPlanimetria2(file_name):
    muri = creaMuri("muriEst.lines")
    
    interni = strutturaInterna("interni2.lines")
    porte = porteInterne("porte2.lines")
    
    pavimento = creaPavimento("muriEst.lines")

    interni = DIFFERENCE([interni,porte])
    
    bucoScala = creaBucoScala("scala.lines")
    pavimento = DIFFERENCE([pavimento,bucoScala])
    muretto = contScala("muroScala.lines")
    buchiFin = creaBuchiFin("finestre2.lines")
    
    buchiFin = OFFSET([0.03,0.03,0])(buchiFin)
    buchiFin = OFFSET([-0.03,-0.03,1])(buchiFin)
    muri = OFFSET([0.01,0.01,3])(muri)

 
    muri = DIFFERENCE([muri,buchiFin])
    muri = OFFSET([0.2,0.2,0.01])(muri)

    finestre = creaFinestre("finestre2.lines")
    tetto = creaTetto("muriEst.lines")
   
    interni = COLOR(Color4f([205/255.,127/255.,50/255.,1]))(interni)
    muri = TEXTURE(["textureMuro.jpg",True,False,1,1,0,100,100])(muri)
    pavimento = COLOR(Color4f([1,228/255.,196/255.,1]))(pavimento)
    porte = COLOR(Color4f([123/255.,27/255.,2/255.,1]))(porte)
    planimetria = STRUCT([muri,interni,pavimento,muretto,finestre,porte])
    planimetria = T(3)(3)(planimetria)
    return planimetria
