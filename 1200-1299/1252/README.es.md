# 1252. Ordenar piedras con intercambios a distancia K

[Timus 1252](https://acm.timus.ru/problem.aspx?space=1&num=1252) · dificultad 397 · number_theory

Problema original de Alexey Lakhtin, del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N piedras (1 ≤ N ≤ 130 000) de pesos distintos están en fila. Dos piedras se
pueden intercambiar si entre ellas hay exactamente K piedras más. Hay que
hallar el mayor K (0 ≤ K < N) con el que la fila se puede ordenar por
peso, en orden creciente o decreciente.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N pesos, uno por línea. Cada peso es un entero entre 1 y
130 000, ambos inclusive.

## Salida

El mayor K así.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
30
21
56
40
17
```

Salida:

```
1
```

## Solución

Un intercambio con K piedras en medio mueve las dos piedras d = K + 1
puestos, así que una piedra se queda en su clase de posiciones módulo d,
y dentro de una clase se puede obtener cualquier orden con intercambios
de vecinas de la clase. Por tanto se puede ordenar justo cuando d divide
la distancia de cada piedra desde su sitio actual hasta su sitio en la
fila ordenada.

Así que se halla, para el orden creciente y para el decreciente, el mcd g
de esas distancias. El mayor d que divide a g es el propio g, que es
menor que N, así que K = g − 1; si la fila ya está en ese orden, g = 0 y
sirve cualquier K, así que K = N − 1. La respuesta es el mayor de los
dos. `O(N log N)` por la ordenación.

Detalles a tener en cuenta:

- el orden decreciente también cuenta (prueba 04), y los dos órdenes
  pueden dar K distintos;
- una fila ya ordenada admite el mayor K, N − 1, aunque entonces no se
  pueda hacer ningún intercambio (pruebas 03 y gen4).

La regla se comparó con una búsqueda de todos los órdenes alcanzables
para cada K en 300 filas aleatorias de hasta 7 piedras.

## Notas por lenguaje

- Java ordena los pesos empaquetados con sus posiciones en un solo
  arreglo `long`, en vez de ordenar índices en objetos con un
  comparador.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1252_number_theory.cpp](1252_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log N) | AC | 0.093 s | 1212 KB |
| [1252_number_theory.go](1252_number_theory.go) | Go 1.14 x64 | number_theory | O(N log N) | AC | 0.125 s | 4012 KB |
| [1252_number_theory.java](1252_number_theory.java) | Java 1.8 | number_theory | O(N log N) | AC | 0.093 s | 1596 KB |
| [1252_number_theory.py](1252_number_theory.py) | Python 3.12 x64 | number_theory | O(N log N) | AC | 0.140 s | 13612 KB |
| [1252_number_theory.rs](1252_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log N) | AC | 0.031 s | 3652 KB |
