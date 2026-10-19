# 2104. Doblar una tira de dos caras hasta que muestre un color

[Timus 2104](https://acm.timus.ru/problem.aspx?space=1&num=2104) · dificultad 375 · games

Problema original de Nikita Sivukhin, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tira de 1 × n tiene sus casillas de colores A y B por ambas caras.
Alice y Bob juegan por turnos, empezando Alice; un turno dobla la tira
por la mitad (solo si su longitud es par), hacia dentro o hacia fuera.
Si tras un turno la tira muestra un solo color por ambas caras, A
significa que gana Alice y B que gana Bob, haya doblado quien haya
doblado. Si el jugador al que toca no puede doblar y nadie ha ganado, es
empate. ¿Quién gana con juego óptimo? Los límites son 2 segundos y
64 MB.

## Entrada

n ≤ 5·10⁵ y después las dos caras como cadenas de A y B.

## Salida

`Alice`, `Bob` o `Draw`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
BBAA
BABB
```

Salida:

```
Bob
```

### Ejemplo 2

Entrada:

```
3
AAA
BBB
```

Salida:

```
Draw
```

### Ejemplo 3

Entrada:

```
2
AA
BB
```

Salida:

```
Alice
```

## Solución

Un doblez pone la mitad derecha encima o debajo de la izquierda. De un
modo, las caras de fuera son la mitad izquierda de la cara superior y la
mitad derecha invertida de la cara superior; del otro, la mitad derecha
invertida de la cara inferior y la mitad izquierda de la cara inferior.
Las caras que quedan dentro no se vuelven a ver. Así que cada posición
tiene a lo sumo dos jugadas, cada una divide la longitud entre dos, y el
juego tiene a lo sumo log₂ n ≈ 19 niveles.

Basta un minimax sencillo sobre este árbol: tras cada doblez se mira si
la tira nueva muestra un solo color; si no, se recurre con el otro
jugador, y una longitud impar es empate. Cada jugador toma el resultado
más favorable a su bando, parando en cuanto una jugada gana. El
nivel k tiene a lo sumo 2ᵏ tiras de longitud n / 2ᵏ, así que el trabajo
es O(n log n).

En el primer ejemplo los dos dobleces de Alice dejan tiras que Bob dobla
en B/B, así que gana Bob.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2104_games.cpp](2104_games.cpp) | G++ 13.2 x64 | games | O(n log n) | AC | 0.031 s | 3832 KB |
| [2104_games.go](2104_games.go) | Go 1.14 x64 | games | O(n log n) | AC | 0.046 s | 8076 KB |
| [2104_games.java](2104_games.java) | Java 1.8 | games | O(n log n) | AC | 0.125 s | 14932 KB |
| [2104_games.py](2104_games.py) | Python 3.12 x64 | games | O(n log n) | AC | 0.265 s | 3968 KB |
| [2104_games.rs](2104_games.rs) | Rust 1.75 x64 | games | O(n log n) | AC | 0.015 s | 2132 KB |
