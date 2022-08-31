import os
import cards
import funciones as fun

dinero=1000

cartas_mesa={"corazones":[], "diamantes":[], "treboles":[], "picas":[]}
mis_cartas=[]
casa_cartas=[]

print(cards.logo)
print("Bienvenido! preparado para jugar blackjack?")
input("Presiona enter para empezar")

def setgame():

    seleccion=[]
    seleccion=fun.sacar_carta(cartas_mesa)
    cartas_mesa[seleccion[0]].append(seleccion[1])
    casa_cartas.extend(seleccion)

    for i in range(2):
        seleccion=[]
        seleccion=fun.sacar_carta(cartas_mesa)
        cartas_mesa[seleccion[0]].append(seleccion[1])
        mis_cartas.extend(seleccion)

def menu(vueltas):
    print("Indique que hacer: ")
    print("pedir")
    print("quedarse")
    if vueltas==0 and dinero>=apuesta:
        print("doblar")

def doblar():
    global apuesta, dinero
    dinero-=apuesta
    apuesta*=2

def quedarse():
    
    cerrar=False
    while not cerrar:
        if fun.calcular_valor(casa_cartas)<17:
            seleccion=[]
            seleccion=fun.sacar_carta(cartas_mesa)
            cartas_mesa[seleccion[0]].append(seleccion[1])
            casa_cartas.extend(seleccion)
        else:
            cerrar=True

def pedir():
    seleccion=[]
    seleccion=fun.sacar_carta(cartas_mesa)
    cartas_mesa[seleccion[0]].append(seleccion[1])
    mis_cartas.extend(seleccion)

def comprobar():

    global dinero, apuesta
    if fun.calcular_valor(casa_cartas)==21:
        print("La casa tiene 21, has perdido...")
    elif fun.calcular_valor(casa_cartas)>21:
        print("La casa tiene mas de 21, has ganado!")
        dinero+=apuesta*2
    elif fun.calcular_valor(mis_cartas)<=21:
        if fun.calcular_valor(casa_cartas)>fun.calcular_valor(mis_cartas):
            print("La casa esta mas cerca de 21, has perdido...")
        elif fun.calcular_valor(casa_cartas)<fun.calcular_valor(mis_cartas):
            print("Estas mas cerca de 21, has ganado!")
            dinero+=apuesta*2
        else:
            print("Empate...")
            dinero+=apuesta

opciones={"quedarse":quedarse, "pedir":pedir, "doblar":doblar}

while dinero>0:
    cartas_mesa={"corazones":[], "diamantes":[], "treboles":[], "picas":[]}
    mis_cartas=[]
    casa_cartas=[]
    saltar=False

    apuesta=fun.apuesta_inicial(dinero)
    setgame()
    vueltas=0
    dinero-=apuesta
    ultima=False

    ronda_terminada=False
    while not ronda_terminada:
        if ultima==True:
            ronda_terminada=True

        os.system("cls")
        print(f"dinero: {dinero}")
        print(f"apuesta: {apuesta}\n")

        print(f"Carta del dealer: (valor:{fun.calcular_valor(casa_cartas)})")
        for i in range(len(casa_cartas)):
            if i%2==0:
                imprimir_pinta=casa_cartas[i]
            else:
                imprimir_color=casa_cartas[i]
                cards.imprimir_cartas(imprimir_pinta,imprimir_color)
        
        print("")
        
        print(f"Tus cartas: (valor:{fun.calcular_valor(mis_cartas)})")
        for i in range(len(mis_cartas)):
            if i%2==0:
                imprimir_pinta=mis_cartas[i]
            else:
                imprimir_color=mis_cartas[i]
                cards.imprimir_cartas(imprimir_pinta,imprimir_color)
        
        if(fun.calcular_valor(mis_cartas)==21):
            print("Blacjack! Ganaste")
            dinero+=apuesta*2
            ronda_terminada=True
            saltar=True
        elif (fun.calcular_valor(mis_cartas)>21):
            print("El valor de tus cartas es mayor a 21...")
            print("has perdido...")
            ronda_terminada=True
            saltar=True
        else:
            if not ronda_terminada:
                menu(vueltas)
                o=input("=> ")
                if o!="quedarse" and o!="pedir" and o!="doblar":
                    print("Su respuesta no pudo ser procesada...")
                    input("Presiona enter para continuar")
                else:
                    if o=="pedir":
                        vueltas+=1
                    elif o=="quedarse":
                        ultima=True
                    funcion=opciones[o]
                    funcion()
                    if o=="doblar":
                        pedir()
                        quedarse()
                        ultima=True
    if ultima==True and not saltar:
        comprobar()
    input("Presiona enter para continuar")

os.system("cls")
print(cards.logo)
print("Lastima, has acabado el dinero...")
input("Presione enter para continuar")