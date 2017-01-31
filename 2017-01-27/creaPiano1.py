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
    return interni

def creaBuchiFin(file_name): 
    finestre = 0
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            if finestre!= 0:
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
            if finestre!= 0:
                finestre = STRUCT([finestre,riga]) 
            else:
                finestre = riga
            
    #finestre = T(3)(1.3)(finestre)
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

def creaPortaEsterna(file_name):
    porta = 0
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            if porta != 0:
                porta = STRUCT([porta,riga])
            else:
                porta = riga
    #pomello = SPHERE(0.03)([100,100])
    #pomello = T([1,2,3])([l[0],l[1],1.4])(pomello)
    return porta

def rimuoviDoppioni(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

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
    return planimetria


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
    return pav

def creaPlanimetria1(file_name):
    muri = creaMuri("muriEst.lines")
    
    interni = strutturaInterna("interni1.lines")
    porte = porteInterne("porte1.lines")
    
    pavimento = creaPavimento("muriEst.lines")
    
    portaEsterna = creaPortaEsterna("portaEst.lines")
    buchiFin = creaBuchiFin("finestre1.lines")
    
    buchiFin = OFFSET([0.03,0.03,0])(buchiFin)
    buchiFin = OFFSET([-0.03,-0.03,1])(buchiFin)
    muri = OFFSET([0.01,0.01,3])(muri)
    portaEsterna = OFFSET([0.03,0.03,0])(portaEsterna)
    portaEsterna = OFFSET([-0.03,-0.03,2])(portaEsterna)
 
    muri = DIFFERENCE([muri,buchiFin])
    muri = DIFFERENCE([muri,portaEsterna])
    muri = OFFSET([0.2,0.2,0.01])(muri)
    
    portaEsterna = creaPortaEsterna("portaEst.lines")
    portaEsterna = OFFSET([0.1,0.1,2])(portaEsterna)
    portaEsterna = TEXTURE("texturePorta.jpg")(portaEsterna)
    
    finestre = creaFinestre("finestre1.lines")
    interni = DIFFERENCE([interni,porte])
    
    porte = COLOR(Color4f([123/255.,27/255.,2/255.,1]))(porte)
    muri = TEXTURE(["textureMuro.jpg",True,False,1,1,0,100,100])(muri)
    interni = COLOR(Color4f([205/255.,127/255.,50/255.,1]))(interni)
    pavimento = COLOR(Color4f([1,228/255.,196/255.,1]))(pavimento)
    planimetria = STRUCT([muri,interni,pavimento,finestre,portaEsterna,porte])
    return planimetria
