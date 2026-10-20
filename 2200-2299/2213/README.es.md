# 2213. Mover un comando de un programa de robot para minimizar la suma

[Timus 2213](https://acm.timus.ru/problem.aspx?space=1&num=2213) · dificultad 2005 · prefix_sums

Problema original de Ignat Nigmatullin, de la Olimpiada Académica Universitaria Escolar de Informática 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un robot empieza en la casilla (1, 1) de una cuadrícula infinita donde
solo un rectángulo N × M tiene valores no nulos, sigue un programa de
movimientos R, D, L y U, y suma el valor de cada casilla que visita,
incluida la inicial. Mover exactamente un comando a cualquier posición
del programa, incluso la suya, para que la suma sea lo menor posible, e
imprimir el nuevo programa. Los límites son 1.5 segundos y 256 MB.

## Entrada

N y M con N · M ≤ 10⁵, la cuadrícula con valores de valor absoluto
hasta 10⁹, y luego el programa de longitud 2 … 10⁵.

## Salida

Un programa óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
1 2 3
1 -1 2
DRULL
```

Salida:

```
DRLLU
```

### Ejemplo 2

Entrada:

```
2 2
-1 1
1 -1
RDULD
```

Salida:

```
DULRD
```

### Ejemplo 3

Entrada:

```
2 3
1 1 1
1 1 1
RRD
```

Salida:

```
RRD
```

## Solución

Se toma un comando c de dirección d en la posición i y se reinserta en
la posición j. Las casillas visitadas antes de ambas posiciones y
después de ambas no cambian. Si j > i, las casillas visitadas entre
ellas son las originales desplazadas en −d, porque el paso d ahora llega
más tarde; si j < i, las casillas intermedias se desplazan en +d. Así el
cambio de la suma es una suma sobre un intervalo contiguo del camino de
cell(p + desplazamiento) − cell(p).

Para cada una de las cuatro direcciones, ambos casos se vuelven
problemas de mejor intervalo sobre una suma de prefijo a lo largo del
camino:

- adelantar un comando necesita, para cada posición i con ese comando,
  el mejor inicio del intervalo que termina en i, dado por el máximo
  acumulado de las sumas de prefijo con desplazamiento +d;
- atrasar un comando necesita, para cada final del intervalo, la mejor
  posición de un comando de esa dirección antes de él, dada por el
  máximo acumulado de las sumas de prefijo con desplazamiento −d.

El mejor de los ocho recorridos da el comando a mover y su nueva
posición. Dejar el programa igual siempre está permitido, así que el
cambio nunca es positivo.

En el primer ejemplo mover la U de la posición 3 al final desplaza las
dos últimas casillas del camino una fila abajo y baja la suma de 4 a 2.

Esto cuesta O(NM + |S|).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2213_prefix_sums.cpp](2213_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(NM + L) | AC | 0.031 s | 2792 KB |
| [2213_prefix_sums.go](2213_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(NM + L) | AC | 0.062 s | 8332 KB |
| [2213_prefix_sums.java](2213_prefix_sums.java) | Java 1.8 | prefix_sums | O(NM + L) | AC | 0.171 s | 6292 KB |
| [2213_prefix_sums.py](2213_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(NM + L) | AC | 0.671 s | 21304 KB |
| [2213_prefix_sums.rs](2213_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(NM + L) | AC | 0.046 s | 4512 KB |
