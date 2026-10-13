# 1500. Permisos de paso

[Timus 1500](https://acm.timus.ru/problem.aspx?space=1&num=1500) · dificultad 641 · bitmask

Problema original de Magaz Asanov, Alexander Mironenko, Anton Botov y Evgeny Krokhalev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad tiene N cruces (2 ≤ N ≤ 30) unidos por M tramos de calle,
cada uno de una de K categorías (1 ≤ K ≤ 20); dos cruces pueden estar
unidos por calles de varias categorías. Un permiso de una categoría
deja circular por todas sus calles. Hay que hallar el menor número de
permisos que permiten ir del cruce 0 al cruce 1 y dar sus categorías.

Límite de tiempo: 2.5 segundos. Límite de memoria: 64 MB.

## Entrada

K, N y M, y luego M líneas con dos cruces y una categoría.

## Salida

El número de permisos y luego las categorías. Se acepta cualquier
conjunto mínimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3 3
0 2 0
0 2 1
1 2 2
```

Salida:

```
2
0 2
```

## Solución

Elegir el menor número de categorías es un problema de cobertura sin
atajos, pero hay como mucho 2²⁰ conjuntos de categorías, así que se
prueban por tamaño y se para en el primero que une 0 con 1.

La prueba de un conjunto debe ser rápida. Para cada cruce u y categoría
c se guarda la máscara de los cruces unidos a u por una calle de
categoría c. Los vecinos de u bajo un conjunto entero son la unión de
esas máscaras; está precalculada para cada subconjunto de las diez
categorías bajas y de las diez altas, así que bastan dos consultas. Una
búsqueda desde el cruce 0 hace crecer la máscara de cruces alcanzados y
se detiene en cuanto contiene el cruce 1. `O(2^K · N)`.

Detalles a tener en cuenta:

- la ruta más corta no siempre es la más barata: una ruta larga por una
  categoría gana a una corta por dos (prueba 04);
- un par de cruces puede tener calles de varias categorías, y basta con
  cualquiera de ellas (pruebas 01, 03);
- cuando la respuesta necesita las 20 categorías se prueban casi todos
  los conjuntos, así que cada prueba debe reducirse a unas pocas
  consultas a tablas (gen2).

## Notas por lenguaje

- Python se ejecuta con PyPy: la cadena que necesita las 20 categorías
  tarda unos 1,25 s con CPython y unos 0,14 s con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1500_bitmask.cpp](1500_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^K N) | AC | 0.093 s | 576 KB |
| [1500_bitmask.go](1500_bitmask.go) | Go 1.14 x64 | bitmask | O(2^K N) | AC | 0.171 s | 1596 KB |
| [1500_bitmask.java](1500_bitmask.java) | Java 1.8 | bitmask | O(2^K N) | AC | 0.343 s | 6136 KB |
| [1500_bitmask.py](1500_bitmask.py) | PyPy 3.10 x64 | bitmask | O(2^K N) | AC | 0.718 s | 4484 KB |
| [1500_bitmask.rs](1500_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^K N) | AC | 0.140 s | 680 KB |
