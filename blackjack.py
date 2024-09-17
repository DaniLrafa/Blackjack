'''
Juego de BlackJack
'''
#damos instrucciones
#
print ("Vas a jugar un juego de blackjack contra el dealer, quien en este caso es la máquina.")
print ("Las reglas son las siguientes:")
print ("Gana quien consiga 21 puntos en la suma de sus cartas, o se acerque más a este número.")
print ("Comenzarás con 2 cartas.")
print ("Puedes pedir tantas cartas como quieras.")
print ("J, Q y K valen 10 puntos.")
print ("Si sumas 10 puntos o menos, el As vale 11, en caso contrario, vale 1.")

#Creamos las cartas
#
import random
cartas = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]

#creamos listas para la mano del usuario y del dealer
#
MU = []
MD = []

#creamos variables para el ciclo de juego
#
inicio = True
Estanjugando = True
Uquiere = True
Dquiere = True

#Ciclo de juego
#
while Estanjugando:
    if inicio:
        #Primera y segunda carta
        #
        CU = random.choice(cartas)
        CD = random.choice(cartas)
        MU.append(CU)
        CM = CD

        CU = random.choice(cartas)
        CD = random.choice(cartas)
        if sum(MU) + CU > 21 and CU == 11:
            CU = 1
        if sum(MD) + CD > 21 and CD == 11:
            CD = 1
        MU.append(CU)
        MD.append(CD)
        inicio = False

    else:
        if Uquiere:
            #mano del usuario
            #
            print ("Esta es tu mano actual:")
            print ("//////////////////////////////////////")
            print (MU)
            print (f"La suma de tus cartas es: {sum(MU)}")
            print ("//////////////////////////////////////")

            #mano del dealer con una carta oculta
            #
            print ("Esta es la mano actual del dealer:")
            print ("//////////////////////////////////////")
            print (f"???, {MD}")
            print (f"La suma de sus cartas visibles: {sum(MD)}")
            print ("//////////////////////////////////////")

            #preguntamos si el usuario quiere más cartas
            #
            RU = input("¿Quieres otra carta? (Y/N): ").lower()
            if RU == "y":
                CU = random.choice(cartas)
                if sum(MU,CU) > 21 and CU == 11:
                    CU = 1
                MU.append(CU)
            if RU == "n":
                Uquiere = False
                print("Ya no recibirás más cartas.")
            else:
                print("Respuesta inválida, por favor responde Y o N.")

        if Dquiere:
            if sum(MD,CM) <= 14:
                CD = random.choice(cartas)
                if sum(MD,CD) > 21 and CD == 11:
                    CD = 1
                MD.append(CD)
            else:
                Dquiere = False
                print("El dealer ya no tomará más cartas.")

    if not Uquiere and not Dquiere:
        #agregamos la carta escondida del dealer       
        #
        MU.append(CM)

        #mostramos resultados finales
        #
        print ("Esta es tu mano final:")
        print ("//////////////////////////////////////")
        print (MU)
        print (f"La suma de tus cartas es: {sum(MU)}")
        print ("//////////////////////////////////////")
        print ("Esta es la mano final del dealer:")
        print ("//////////////////////////////////////")
        print (MD)
        print (f"La suma de sus cartas es: {sum(MD)}")
        print ("//////////////////////////////////////")

        #Decidimos el ganador
        #
        #Empates
        #
        if sum(MU) == sum(MD):
            print("Es un empate")
        elif sum(MU) > 21 and sum(MD) > 21:
            print("Es un empate")
        #victorias
        #
        elif sum(MU) > sum(MD) and sum(MU) <= 21:
            print("Ganaste")
        elif sum(MU) < sum(MD) and sum(MD) > 21:
            print("Ganaste")
        #Derrotas
        #
        elif sum(MD) > sum(MU) and sum(MD) <= 21:
            print("Perdiste")
        elif sum(MD) < sum(MU) and sum(MU) > 21:
            print("Perdiste")
        
        Estanjugando = False