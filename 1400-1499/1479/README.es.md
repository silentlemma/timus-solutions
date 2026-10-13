# 1479. Control según horario

[Timus 1479](https://acm.timus.ru/problem.aspx?space=1&num=1479) · dificultad 3929 · bitmask

Problema original de Alexander Ipatov, del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo simple no dirigido tiene N paradas (3 ≤ N ≤ 14) y M calles. La empresa
pone tantas rutas como puede, cada una un anillo por al menos tres
paradas distintas sin repetir ninguna, y dos rutas cualesquiera
difieren en al menos una calle. Un horario es una tabla: las filas son
momentos, las columnas son rutas y una casilla contiene la parada donde
se controla el autobús de esa ruta en ese momento. Cada autobús se
controla una vez en cada parada de su ruta, ninguna parada controla dos
autobuses a la vez y ningún autobús está en dos paradas a la vez. Hay
que hallar el menor número posible de filas.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N y M, y luego M líneas con las dos paradas de cada calle.

## Salida

El menor número de filas.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
1 2
2 3
1 3
1 4
```

Salida:

```
3
```

## Solución

Dos ciclos simples distintos siempre difieren en alguna calle, así que
las rutas son todos los ciclos simples del grafo. Se une cada ruta con
cada una de sus paradas: el horario debe cubrir cada par una vez, y una
fila es un conjunto de pares sin ruta ni parada en común, es decir, un
emparejamiento. Cubrir las aristas de un grafo bipartito con
emparejamientos es colorear sus aristas, y por el teorema de König
basta el grado máximo. Así que la respuesta es el mayor entre la ruta
más larga (su número de paradas) y el mayor número de rutas que pasan
por una parada, o 0 si no hay ciclos.

Los ciclos se cuentan por conjuntos de paradas. Para cada conjunto S se
cuentan los caminos simples que empiezan en la menor parada de S,
recorren todo S y acaban en v; los que tienen v junto al inicio se
cierran en ciclos con conjunto de paradas S, contados una vez por
sentido. Cada camino solo crece por paradas mayores que su inicio, así
que cada ciclo se ve solo desde su menor parada. Sumando los ciclos de
cada S a cada parada de S se obtienen las cuentas por parada.
`O(2^N·N²)`.

Detalles a tener en cuenta:

- sin ciclos no hay rutas ni filas (pruebas 02, 03);
- con las 14 paradas unidas entre sí pasan unas 8,5·10⁹ rutas por cada
  parada, lo que necesita 64 bits (prueba 06);
- un anillo solo tiene una ruta por cada parada, así que decide su
  longitud (prueba 04), y dos triángulos con una parada común llevan
  dos rutas por ella pero siguen necesitando 3 filas (prueba 07).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1479_bitmask.cpp](1479_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^N N^2) | AC | 0.015 s | 1676 KB |
| [1479_bitmask.go](1479_bitmask.go) | Go 1.14 x64 | bitmask | O(2^N N^2) | AC | 0.031 s | 3052 KB |
| [1479_bitmask.java](1479_bitmask.java) | Java 1.8 | bitmask | O(2^N N^2) | AC | 0.125 s | 3700 KB |
| [1479_bitmask.py](1479_bitmask.py) | Python 3.12 x64 | bitmask | O(2^N N^2) | AC | 0.343 s | 4408 KB |
| [1479_bitmask.rs](1479_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^N N^2) | AC | 0.031 s | 2016 KB |
