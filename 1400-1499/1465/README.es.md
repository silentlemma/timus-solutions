# 1465. El juego de los peones

[Timus 1465](https://acm.timus.ru/problem.aspx?space=1&num=1465) · dificultad 489 · games

Problema original de Alexander Toropov, del concurso de la Universidad Estatal de los Urales en el campus de invierno de Petrozavodsk, enero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un tablero de 3 × N casillas (1 ≤ N ≤ 10⁹) la primera fila está
llena de peones blancos y la tercera de negros; la del medio está vacía.
Los peones mueven y capturan como en el ajedrez, capturar es
obligatorio, y pierde quien no puede mover. Las blancas mueven primero.
Ambos juegan perfectamente: hay que imprimir «White» si ganan las
blancas y «Black» en otro caso.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

«White» o «Black».

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
White
```

### Ejemplo 2

Entrada:

```
4
```

Salida:

```
Black
```

### Ejemplo 3

Entrada:

```
5
```

Salida:

```
White
```

## Solución

Es el ajedrez de Dawson. Un peón empujado a la fila del medio queda
atacado por los peones rivales de las columnas vecinas, y las capturas
obligatorias que siguen terminan con la columna empujada y sus vecinas
muertas: ningún peón allí podrá volver a mover. Así, una jugada en la
columna i de una fila de n columnas vivas deja dos filas independientes
de i − 2 y n − i − 1 columnas; una jugada junto a un borde mata dos
columnas, y una columna sola muere por sí misma. Es el juego octal
0.137: quitar una columna solo si es toda la fila, quitar dos dejando
como mucho una fila, o quitar tres dejando hasta dos filas.

El primer jugador gana justo cuando el valor de Grundy de n no es cero;
el valor de una fila es el menor número que no está entre los valores de
sus jugadas, y dos filas se combinan con xor. Los valores se calculan
hasta 200 en O(200²). Desde n = 52 se repiten con periodo 34, y por el
teorema de periodicidad de los juegos octales basta comprobarlo hasta
2 · 52 + 34 + 3; así que un N mayor se pliega al último periodo por
debajo de 200. `O(1)` por respuesta.

Detalles a tener en cuenta:

- un tablero de N = 10⁹ no se puede simular, solo plegar (pruebas 12 a
  15);
- los valores solo se estabilizan desde n = 52: 14 y 48 columnas, o 34
  y 68, tienen ganadores distintos (pruebas 07, 08, 17, 18);
- en los lenguajes tipo C el resto de un número negativo es negativo,
  así que al plegar hay que restar en el orden correcto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1465_games.cpp](1465_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 172 KB |
| [1465_games.go](1465_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 1144 KB |
| [1465_games.java](1465_games.java) | Java 1.8 | games | O(1) | AC | 0.140 s | 1720 KB |
| [1465_games.py](1465_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.109 s | 444 KB |
| [1465_games.rs](1465_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 440 KB |
