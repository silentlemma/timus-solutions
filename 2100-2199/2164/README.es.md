# 2164. Contar subcadenas que son partidas terminadas de cuatro en raya

[Timus 2164](https://acm.timus.ru/problem.aspx?space=1&num=2164) · dificultad 1593 · simulation

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2021.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El cuatro en raya se juega con 7 filas y 9 columnas; una jugada nombra
una columna, y jugar en una columna llena es un pase que aun así gasta
una de las 63 fichas. Una partida termina cuando quien acaba de jugar
tiene cuatro en una fila, columna o diagonal (una victoria), o cuando se
han gastado las 63 fichas: tablas si el tablero está lleno, y final
abierto si no. En una cadena de jugadas, contar las subcadenas que son
partidas completas ganadas y las que son partidas completas en tablas.
Los límites son 1 segundo y 256 MB.

## Entrada

La cadena de cifras 1 … 9, de longitud N, 1 ≤ N ≤ 10⁴.

## Salida

El número de partidas ganadas y el de partidas en tablas.

## Ejemplos

### Ejemplo 1

Entrada:

```
34353637
```

Salida:

```
2 0
```

## Solución

Una posición de inicio determina toda la partida: se juegan las jugadas
desde allí hasta que termina. Si una jugada gana, la subcadena hasta ella
es una partida ganada y ninguna subcadena más larga desde ese inicio es
una partida. Si pasan 63 jugadas sin victoria, la subcadena de longitud
63 es tablas exactamente cuando ninguna jugada fue un pase. Así que cada
inicio se simula a lo sumo 63 jugadas, N · 63 en total.

Las fichas de cada jugador son un tablero de 63 bits, un bit por
casilla, columna a columna. Una jugada pone un bit, y hay cuatro en raya
en una dirección con desplazamiento s cuando
b & (b ≫ s) & (b ≫ 2s) & (b ≫ 3s) tiene algún bit, calculado con dos AND
de pares desplazados. Una máscara de las casillas donde puede empezar
una línea de cuatro impide que los desplazamientos crucen el borde de
una columna. Las victorias solo se comprueban desde la séptima jugada,
cuando un color puede tener cuatro fichas.

En el ejemplo "3435363" gana en la columna 3 y "4353637" en la fila de
abajo; ninguna otra subcadena es una partida terminada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2164_simulation.cpp](2164_simulation.cpp) | G++ 13.2 x64 | simulation | O(63 N) | AC | 0.031 s | 452 KB |
| [2164_simulation.go](2164_simulation.go) | Go 1.14 x64 | simulation | O(63 N) | AC | 0.031 s | 1152 KB |
| [2164_simulation.java](2164_simulation.java) | Java 1.8 | simulation | O(63 N) | AC | 0.109 s | 1424 KB |
| [2164_simulation.py](2164_simulation.py) | PyPy 3.10 x64 | simulation | O(63 N) | AC | 0.187 s | 2888 KB |
| [2164_simulation.rs](2164_simulation.rs) | Rust 1.75 x64 | simulation | O(63 N) | AC | 0.046 s | 244 KB |
