# 1452. Pascal contra C++

[Timus 1452](https://acm.timus.ru/problem.aspx?space=1&num=1452) · dificultad 608 · hashing

Problema original de Ilya Grebnov, Dmitry Kovalioff y Nikita Rybak, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una sucesión tiene N elementos (2 ≤ N ≤ 2000), enteros de 0 a 10⁹. Hay
que elegir tantos elementos como se pueda, con valores distintos, que
formen términos consecutivos de una progresión aritmética creciente; su
orden en la sucesión no importa. Se imprime la cantidad y los números de
los elementos elegidos en cualquier orden.

Límite de tiempo: 0.25 segundos. Límite de memoria: 16 MB.

## Entrada

N y luego los N elementos.

## Salida

La cantidad y luego los números de los elementos. Se acepta cualquier
progresión más larga.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
7 3 2 3 5 9
```

Salida:

```
4
4 5 1 6
```

## Solución

Solo importa el conjunto de valores, así que cada valor se guarda una
vez en una tabla hash junto con el número de un elemento que lo tiene, y
los valores distintos se ordenan. Toda progresión de al menos dos
términos queda fijada por sus dos primeros términos x < y, con paso
d = y − x. Se recorre solo desde su verdadero comienzo, es decir,
cuando x − d no está: luego se sigue por y + d, y + 2d, ... mientras
estén en la tabla.

Cada par de términos vecinos de una progresión maximal cae en un solo
recorrido, y cada par (x, y) cuesta una consulta para comprobar el
comienzo, así que la búsqueda completa hace O(m²) consultas para m
valores distintos, sin tabla de pares: la memoria se queda en O(m), que
es lo que exige el límite de 16 MB. Con un solo valor distinto la
respuesta es un elemento. `O(m²)` en tiempo esperado.

Detalles a tener en cuenta:

- los valores repetidos cuentan una vez (pruebas 02, 04, 07, gen4);
- una progresión que pasa por todos los valores es el caso más lento
  para los recorridos (gen3);
- una tabla de todos los pares, como en la programación dinámica
  habitual en O(N²), necesita más memoria de la permitida en la mayoría
  de los lenguajes.

## Notas por lenguaje

- Python corre en CPython y poda los pares. Primero descarta los valores
  extremos que no terminan ninguna progresión de tres términos, y un par
  x < y solo se recorre cuando una progresión desde x con paso y − x aún
  podría superar a la mejor hallada: su término en esa longitud debe ser
  como mucho el mayor valor y estar en la tabla. La versión anterior,
  que recorría todos los pares, excedía el límite de 0,25 s en la prueba
  9 del juez con CPython y en la prueba 28 con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1452_hashing.cpp](1452_hashing.cpp) | G++ 13.2 x64 | hashing | O(m^2) | AC | 0.093 s | 264 KB |
| [1452_hashing.go](1452_hashing.go) | Go 1.14 x64 | hashing | O(m^2) | AC | 0.125 s | 1380 KB |
| [1452_hashing.java](1452_hashing.java) | Java 1.8 | hashing | O(m^2) | AC | 0.203 s | 952 KB |
| [1452_hashing.py](1452_hashing.py) | Python 3.12 x64 | hashing | O(m^2) | AC | 0.187 s | 1300 KB |
| [1452_hashing.rs](1452_hashing.rs) | Rust 1.75 x64 | hashing | O(m^2) | AC | 0.109 s | 632 KB |
