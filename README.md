# Blackjack
This is a card game named blackjack made in python

## Descripción

Este es un juego simple de BlackJack implementado en Python. En este juego, un jugador compite contra una máquina (dealer) siguiendo las reglas estándar del BlackJack. El objetivo es alcanzar una suma de cartas lo más cercana posible a 21 sin exceder este número.

## Reglas del Juego

1. **Objetivo**: Obtener una suma de cartas de 21 puntos o lo más cercano posible sin excederlo.
2. **Valor de las cartas**:
    - Cartas numéricas: Valen su valor nominal.
    - J, Q y K: Valen 10 puntos.
    - As: Vale 11 puntos si la suma de las cartas es 10 o menos; de lo contrario, vale 1 punto.
3. **Juego**:
    - El jugador y el dealer comienzan con 2 cartas cada uno.
    - El jugador puede pedir cartas adicionales o quedarse con las cartas actuales.
    - El dealer tomará cartas adicionales hasta tener 14 o mas.
4. **Fin del Juego**:
    - Gana quien mas se acerque a 21 puntos
    - Si el jugador se pasa de 21 puntos, independientemente de la puntuacion del dealer, pierde.
    - Si el dealer se pasa de 21 puntos y el jugador no, el jugador gana.

## ciclo de juego

1. **Inicio del Juego**:
    - El juego comienza con dos cartas para el jugador y dos para el dealer. La primera carta del dealer permanece oculta hasta el final del juego.

2. **Turno del Jugador**:
    - Se muestra la mano actual del jugador y la mano visible del dealer.
    - El jugador decide si quiere una carta adicional o si se queda con las cartas actuales.

3. **Turno del Dealer**:
    - El dealer toma cartas adicionales hasta que su suma sea mayor a 14 puntos.

4. **Resultado**:
    - se revela la carta oculta del dealer.
    - Se comparan las sumas de cartas del jugador y del dealer.
    - El ganador se determina y se muestra el resultado del juego.

## Glosario

-CU: "Carta usuario" Es una variable temporal que almacena el valor de la nueva carta que vamos a agregar a MU
-MU: "Mano usuario" Es una lista que almacena todas las cartas del usuario 
-CD: "Carta dealer" Es una variable temporal que almacena el valor de la nueva carta que vamos a agregar a MD
-MD: "Mano dealer" Es una lista que almacena las cartas del dealer
-CM: "carta misteriosa" Es la primer carta que recibe el dealer 
-RU: "respuesta usuario" Almacena una respuesta "Si" o "No" del usuario respecto a si quiere mas cartas
-inicio: indica si nos encontramos en la primera ronda
-Estanjugando: indica que tanto el usuario como el dealer siguen recibiendo cartas
-Uquiere: indica que el usuario aun quiere cartas
-Dquiere: indica que el dealer aun quiere cartas
