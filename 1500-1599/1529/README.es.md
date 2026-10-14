# 1529. Juego de cuadrados

[Timus 1529](https://acm.timus.ru/problem.aspx?space=1&num=1529) · dificultad 3542 · games

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos jugadores juegan por turnos con una caja k-dimensional de
n1 × … × nk cubos unidad (1 ≤ k ≤ 8, (n1 + 1)·…·(nk + 1) ≤ 10000), y
luego con las cajas que quedan. Una jugada elige una caja y un cubo
unidad en ella y corta por el centro de ese cubo con los k planos
paralelos a las caras: los cubos cortados desaparecen y quedan hasta
2^k cajas menores. Un corte vale si alguna de las nuevas cajas tiene
cada arista coprima con la arista correspondiente de la caja cortada,
o si no queda nada.
Pierde quien no puede jugar. Suponiendo que ambos juegan de forma
óptima, hay que decir quién gana y, si gana Alice, que juega primero,
su corte ganador lexicográficamente menor.

Límite de tiempo: 5 segundos. Límite de memoria: 64 MB.

## Entrada

k y luego n1 … nk.

## Salida

1 o 2 para el ganador y, con 1, las coordenadas del corte desde 1.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
2 2
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
3
3 4 5
```

Salida:

```
1
1 1 3
```

## Solución

Las cajas que quedan son juegos independientes, así que por el teorema
de Sprague–Grundy cada caja tiene un valor y una jugada vale el XOR de
los valores de las partes que deja; una parte vacía vale 0. Un corte en
la posición c de una arista d deja los trozos c − 1 y d − c a lo largo
de ella, y las partes son todas las combinaciones de los trozos de las
k aristas. Una parte tiene todas sus aristas coprimas justo cuando lo
es cada trozo, así que un corte que deja partes vale cuando cada
arista tiene un trozo no vacío coprimo con ella; como gcd(d − c, d) =
gcd(c, d), un corte central falla solo si c − 1 y c comparten ambos un
factor con d. Una caja con una arista de 1 desaparece con cualquier corte y vale 1. En
una dimensión los dos trozos suman siempre d − 1, lo que da el valor
d mod 2.

El valor no depende del orden de las aristas: se calculan las listas
ordenadas por suma creciente de longitudes y se guardan las permutaciones
que caben en los límites ordenados de entrada. Para una caja se toma la
tabla de valores de sus partes por longitudes de trozos y se
sustituye un eje cada vez por sus cortes válidos, cada corte con el XOR
de las rebanadas c − 1 y d − c: tras todos los ejes la tabla tiene el
valor de cada jugada, y su mex es el valor de la caja. Son unas 2k
operaciones por casilla de la tabla, no 2^k. Alice gana si la caja
entera vale más de 0, y su primera jugada es el primer cero de la tabla
de jugadas de la caja entera, en el orden de aristas de la entrada.

Detalles a tener en cuenta:

- «el paralelepípedo original» de la regla es la caja que se corta en
  esa jugada; esta lectura es la que acepta el juez;
- una caja con una arista de 1 siempre se puede cortar entera, así que
  Alice gana con el corte (1, …, 1) (prueba 05);
- en una dimensión no hace falta buscar: las longitudes impares ganan
  (pruebas 03, 04, 10);
- el rectángulo 6 × 5 tiene cortes que no valen (prueba 06);
- pesan tanto las cajas cuadradas como 99 × 99 como las largas y finas
  como 1046 × 2 (prueba 07, gen1).

## Notas por lenguaje

La solución en Python empaqueta cada fila de valores a lo largo del
último eje en un entero grande con carriles de 16 bits. Un corte en el
último eje une el carril c − 1 con el d − c, que es el carril c − 1 de
la fila invertida, así que se hace el XOR de filas enteras a la vez, y
en los demás ejes también. Hasta el cálculo de los cortes válidos usa
máscaras de bytes.

## Soluciones

P = prod(n_i), M = max(n_i).

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1529_games.cpp](1529_games.cpp) | G++ 13.2 x64 | games | O(k * P^2 + M^2 * log M) | AC | 0.125 s | 3768 KB |
| [1529_games.go](1529_games.go) | Go 1.14 x64 | games | O(k * P^2 + M^2 * log M) | AC | 0.375 s | 12336 KB |
| [1529_games.java](1529_games.java) | Java 1.8 | games | O(k * P^2 + M^2 * log M) | AC | 0.296 s | 7560 KB |
| [1529_games.py](1529_games.py) | Python 3.12 x64 | games | O(k * prod(n_i)^2) | AC | 1.375 s | 2148 KB |
| [1529_games.rs](1529_games.rs) | Rust 1.75 x64 | games | O(k * P^2 + M^2 * log M) | AC | 0.125 s | 4892 KB |
