# 1397. Juego de puntos

[Timus 1397](https://acm.timus.ru/problem.aspx?space=1&num=1397) · dificultad 1663 · geometry, games

Problema original de Michael Medvedev, del Concurso Abierto de Programación Universitaria de toda Ucrania de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay 2n puntos en el plano, n ≤ 500. Dos jugadores los colorean por
turnos, el primero de blanco y el segundo de negro, hasta que cada uno
ha coloreado n puntos. La puntuación de un jugador es la suma de las
distancias entre todos los pares de puntos de su color. Con el mejor
juego de ambos, hay que imprimir la puntuación del ganador menos la del
perdedor, con tres cifras decimales. La entrada tiene varias partidas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las partidas una tras otra: n y luego 2n líneas con los puntos.

## Salida

La diferencia de cada partida.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 0
0 1
1 0
1 1
2
0 0
1 0
0 3
1 5
```

Salida:

```
0.000
1.937
```

## Solución

Sea Dᵢ la suma de las distancias del punto i a todos los demás. Al sumar
sobre los puntos blancos, cada par blanco cuenta dos veces y cada par de
colores distintos una: ΣW Dᵢ = 2·WW + WB, e igualmente
ΣB Dᵢ = 2·BB + WB. Así que la diferencia de puntuaciones es

WW − BB = (ΣW Dᵢ − ΣB Dᵢ) / 2,

y la partida solo suma un valor fijo por punto. Entonces a cada jugador
le conviene tomar el punto de mayor Dᵢ que quede: se ordenan los Dᵢ de
mayor a menor, al primero le tocan los de posición par, y la respuesta
es la mitad de la suma alternada. `O(n²)` por partida para las
distancias.

Detalles a tener en cuenta:

- la entrada tiene varias partidas y sigue hasta el final del fichero;
- en una partida igualada la suma alternada puede salir como un número
  negativo diminuto, que se imprimiría como -0.000, así que se imprime
  su valor absoluto;
- en Java Math.hypot es mucho más lento que Math.sqrt con un millón de
  pares por partida.

Las respuestas se compararon con un minimax completo sobre todas las
coloraciones en 200 partidas aleatorias de hasta 8 puntos.

## Notas por lenguaje

- Python se ejecuta con PyPy: diez partidas de 1 000 puntos tardan unos
  0,7 s con CPython y menos de 0,1 s con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1397_greedy.cpp](1397_greedy.cpp) | G++ 13.2 x64 | greedy | O(n^2) | AC | 0.001 s | 244 KB |
| [1397_greedy.go](1397_greedy.go) | Go 1.14 x64 | greedy | O(n^2) | AC | 0.015 s | 1180 KB |
| [1397_greedy.java](1397_greedy.java) | Java 1.8 | greedy | O(n^2) | AC | 0.078 s | 1064 KB |
| [1397_greedy.py](1397_greedy.py) | PyPy 3.10 x64 | greedy | O(n^2) | AC | 0.140 s | 6328 KB |
| [1397_greedy.rs](1397_greedy.rs) | Rust 1.75 x64 | greedy | O(n^2) | AC | 0.031 s | 372 KB |
