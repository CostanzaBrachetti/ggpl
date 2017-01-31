from pyplasm import*
from scala import*
import csv

def stringToFloat(str):
    l = str.split(',')
    newList=[]
    for c in l:
        elem = float(c)/20.
        newList.append(elem)
    return newList

def creaScala(file_name):
    scala = STRUCT([QUOTE([0])])
    with open(file_name,'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=' ', quotechar='|')
        for row in reader:
            l = stringToFloat(row[0])
            riga = MKPOL([[[l[0],l[1],0],[l[2],l[3],0]],[[1,2]],1])
            scala = STRUCT([scala,riga])
    return scala

def larghezzaScala():
    s = creaScala("scala.lines")
    l = UKPOL(s)
    vertici = l[0]
    vertici.remove(vertici[0])
    v = vertici[0]
    xMin = v[0]
    xMax = v[0]
    for v in vertici:
        if v[0]<=xMin:
            xMin = v[0]
        if v[0]>= xMax:
            xMax = v[0]
    dxScala = xMax-xMin
    return dxScala


def puntiScala(scala):
    s = creaScala("scala.lines")
    l = UKPOL(s)
    vertici = l[0]
    vertici.remove(vertici[0])
    v = vertici[0]
    xMin = v[0]
    yMin = v[1]
    for v in vertici:
        if v[0]<=xMin and v[1]<=yMin:
            xMin = v[0]
            yMin = v[1]
    print (xMin,yMin)
    #l = rimuoviDoppioni(l)
    #scala = ggpl_My_Stair_Type(3,10,4)
    scala = T([1,2])([xMin,yMin])(scala)
    return (scala)
