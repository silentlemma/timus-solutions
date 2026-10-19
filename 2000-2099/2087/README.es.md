# 2087. Cambiar las agujas solo donde el último tren fue a otro lado

[Timus 2087](https://acm.timus.ru/problem.aspx?space=1&num=2087) · dificultad 3539 · trees, segment_tree

Problema original de Denis Mukhametianov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un ferrocarril dibujado en una cuadrícula es un árbol: el depósito y las
estaciones son hojas, las agujas nodos internos, cada arista mide 1, y
cada aguja empieza en una posición dada (recto, izquierda o derecha).
Los trenes salen del depósito uno a uno en tiempos dados, avanzan una
unidad por unidad de tiempo y deben llegar a estaciones dadas; una aguja
solo puede cambiarse en el momento en que llega un tren. Imprimir el
menor número de cambios, cada uno con su momento, aguja y nueva
posición. Se acepta cualquier orden de los cambios. Los límites son
4 segundos y 256 MB.

## Entrada

N y M, 2 ≤ N, M ≤ 500, el mapa de (2N − 1) × (2M − 1) y después
Q ≤ 2·10⁵ trenes con sus tiempos de salida y estaciones de destino, en
orden de salida.

## Salida

El número de cambios y después los cambios `T X Y C`.

## Evaluación

El comprobador local compara el número de cambios y el multiconjunto de
eventos con la respuesta de referencia, permitiendo cualquier orden de
salida. No simula el movimiento de los trenes.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
S-F-X
..|..
L-R-R
|...|
X.X-R
4
1 1 3
2 3 1
4 1 3
6 3 2
```

Salida:

```
4
3 1 2 R
5 1 2 F
7 1 2 R
8 2 2 L
```

### Ejemplo 2

Entrada:

```
2 3
S-F-X
..|..
..X..
3
1 2 2
2 1 3
4 1 3
```

Salida:

```
2
2 1 2 R
3 1 2 F
```

## Solución

Los trenes van a la misma velocidad y salen en orden, así que pasan cada
aguja en orden de salida, un tren que sale en T llega a una aguja de
profundidad h en el momento T + h, y cada aguja apunta adonde fue el
último tren que la pasó (o sigue en su posición inicial). Un tren
necesita un cambio exactamente en las agujas de su camino que apuntan
lejos de su estación, y esos cambios son forzosos, así que el mínimo es
la suma de esos desajustes sobre todos los trenes.

El mapa se lee como un árbol enraizado con profundidades, intervalos de
Euler y una descomposición en caminos pesados para los ancestros comunes
más bajos. Para cada nodo se precalcula la hoja a la que llevan las
posiciones iniciales. Para un tren nuevo con destino d se parte de la
hoja e adonde lo llevarían las posiciones actuales desde la raíz (el
destino anterior, pues el tren anterior fijó todas las agujas de su
camino). Mientras e ≠ d, el ancestro común más bajo j de d y e es una
aguja desajustada: un cambio en el momento T + depth(j) hacia el hijo c
en el camino a d. Bajo c las agujas apuntan adonde fue el último tren
con destino dentro del subárbol de c, que un árbol de segmentos sobre el
orden de Euler (guardando el último tren de cada estación) halla como
máximo de un rango; si ningún tren ha entrado aún en ese subárbol, se
usa la hoja inicial de c. Esa hoja es la nueva e. Cada paso produce un
cambio de la respuesta. Tras procesar un destino distinto del anterior,
se actualiza su índice de última visita en el árbol de segmentos. Al final
se ordenan los R eventos para la salida. Incluyendo el preprocesamiento
O(NM), el tiempo total es O(NM + (Q + R) log(NM) + R log R) y la memoria
es O(NM + Q + R), donde R ≤ 2·10⁵ es el número de cambios.

Trampa (prueba 12): un tren solo cambia las agujas de su propio camino;
una rama no visitada conserva el estado dejado por su último visitante,
que puede ser anterior al tren precedente.

En el segundo ejemplo el primer tren necesita la aguja a la derecha en
el momento 2, el segundo la necesita recta otra vez en el momento 3, y
el tercero va por el mismo lado que el segundo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2087_trees_segment_tree.cpp](2087_trees_segment_tree.cpp) | G++ 13.2 x64 | trees, segment_tree | O(NM + (Q + R) log(NM) + R log R) | AC | 0.218 s | 19964 KB |
| [2087_trees_segment_tree.go](2087_trees_segment_tree.go) | Go 1.14 x64 | trees, segment_tree | O(NM + (Q + R) log(NM) + R log R) | AC | 0.328 s | 67884 KB |
| [2087_trees_segment_tree.java](2087_trees_segment_tree.java) | Java 1.8 | trees, segment_tree | O(NM + (Q + R) log(NM) + R log R) | AC | 0.390 s | 27940 KB |
| [2087_trees_segment_tree.py](2087_trees_segment_tree.py) | Python 3.12 x64 | trees, segment_tree | O(NM + (Q + R) log(NM) + R log R) | AC | 2.968 s | 111308 KB |
| [2087_trees_segment_tree.rs](2087_trees_segment_tree.rs) | Rust 1.75 x64 | trees, segment_tree | O(NM + (Q + R) log(NM) + R log R) | AC | 0.218 s | 44632 KB |
