import os
import cards
from random import choice as seleccionar

cartas=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
pintas=["corazones", "diamantes", "treboles", "picas"]

def apuesta_inicial(dinero):
    
    validar=True
    while validar:
        validar=False
        os.system("cls")
        print(cards.logo)
        print(f"dinero: {dinero}")
        try:
            apuesta=abs(int(input(("Ingrese su apuesta inicial: "))))
            if apuesta>dinero:
                print("No tiene suficiente dinero...")
                input("Presiona enter para continuar")
                validar=True
        except ValueError:
            print("Su respuesta no pudo ser procesada...")
            input("Presiona enter para continuar")
            validar=True
        
    return apuesta

def sacar_carta(cartas_mesa):
    while True:
        seleccion=[]
        seleccion.append(seleccionar(pintas))
        seleccion.append(seleccionar(cartas))
        if seleccion[1] not in cartas_mesa[seleccion[0]]:
            return seleccion

def calcular_valor(cartas):
    ases=0
    acum=0
    for i in range(len(cartas)):
        if i%2!=0:
            if cartas[i]=="J" or cartas[i]=="Q" or cartas[i]=="K":
                acum+=10
            elif cartas[i]=="A":
                ases+=1
            else:
                acum+=int(cartas[i])
    while(ases>0):
        if acum+11+ases-1>21:
            acum+=ases
            break
        elif acum+11+ases-1==21:
            acum+=(11+ases-1)
            break
        else:
            acum+=11
            ases-=1
    return acum