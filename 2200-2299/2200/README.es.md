# 2200. Cuántos tableros separados puede visitar un caballo

[Timus 2200](https://acm.timus.ru/problem.aspx?space=1&num=2200) · dificultad 984 · dsu, sorting

Problema original de Vadim Barinov, de la Olimpiada Académica Universitaria Escolar de Informática 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N tableros rectangulares, cada uno de al menos 3 × 3, están en una
cuadrícula sin tocarse, ni siquiera por las esquinas. Un caballo está en
una casilla y puede moverse dentro de un tablero o saltar entre tableros
en un movimiento. Contar los tableros que puede visitar, incluido el
suyo. Los límites son 4 segundos y 256 MB.

## Entrada

N y M, 1 ≤ N ≤ 5 · 10⁴, 2 ≤ M ≤ 10⁹, luego la casilla del caballo, y
luego cada tablero por sus esquinas inferior izquierda y superior
derecha, con todas las coordenadas de valor absoluto hasta M.

## Salida

El número de tableros.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 12
0 0
0 0 3 3
5 0 8 3
0 4 8 7
9 8 12 11
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
2 10
-1 -1
-2 -2 1 1
-2 2 1 5
```

Salida:

```
1
```

## Solución

Dentro de un tablero de al menos 3 × 3 todas las casillas están
conectadas, salvo si mide exactamente 3 × 3: sus ocho casillas exteriores
forman una componente, mientras que el centro no tiene ningún movimiento.
Si el caballo empieza en un centro así, la respuesta es 1; en otro caso,
puede alcanzar todas las casillas del borde de su tablero. Ningún salto
desde fuera puede caer en ese centro, por lo que cada tablero sigue
representándose como un vértice tras comprobar si el inicio está aislado.

Detalle a tener en cuenta: desde una casilla distinta del centro de un
tablero de 3 × 3 se alcanzan ocho casillas, no nueve (prueba 03); desde
el centro ni siquiera se puede saltar a un tablero cercano (prueba 04).

Dos tableros están a un salto solo cuando los separa exactamente una
columna vacía y sus rangos cerrados de filas se tocan, o exactamente una
fila vacía y se tocan sus rangos cerrados de columnas. Un movimiento de
caballo cambia una coordenada en 2 y la otra en 1. Cruzar un hueco de g
columnas pide un cambio de g + 1 ≤ 2 en x, y como los tableros no se
tocan, g = 1, así que x cambia en 2 e y en 1, lo que es posible
exactamente cuando los rangos de filas, como intervalos cerrados,
comparten un punto. Los casos diagonales también están cubiertos: un
hueco de una fila con columnas que se encuentran en una sola línea es el
segundo caso.

Así los tableros forman un grafo, y la respuesta es el tamaño de la
componente del inicial en una unión de conjuntos disjuntos. Para hallar
las aristas, cada lado derecho en x = R se empareja con los lados
izquierdos en x = R + 1: los eventos se ordenan por línea y luego por el
inicio de su intervalo, y como los lados de un mismo tipo en una línea
nunca se solapan, cada intervalo solo se compara con el intervalo más
reciente del otro tipo. El mismo barrido se hace con los lados
horizontales.

En el primer ejemplo los dos tableros pequeños alcanzan el tablero largo
de arriba a través de una fila vacía, mientras que el último tablero
está en diagonal con huecos en ambas direcciones.

La ordenación da O(N log N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2200_dsu_sorting.cpp](2200_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(N log N) | AC | 0.062 s | 2888 KB |
| [2200_dsu_sorting.go](2200_dsu_sorting.go) | Go 1.14 x64 | dsu, sorting | O(N log N) | AC | 0.140 s | 14944 KB |
| [2200_dsu_sorting.java](2200_dsu_sorting.java) | Java 1.8 | dsu, sorting | O(N log N) | AC | 0.218 s | 11824 KB |
| [2200_dsu_sorting.py](2200_dsu_sorting.py) | Python 3.12 x64 | dsu, sorting | O(N log N) | AC | 0.500 s | 26580 KB |
| [2200_dsu_sorting.rs](2200_dsu_sorting.rs) | Rust 1.75 x64 | dsu, sorting | O(N log N) | AC | 0.046 s | 12828 KB |
