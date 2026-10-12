# 1343. Cuento de hadas

[Timus 1343](https://acm.timus.ru/problem.aspx?space=1&num=1343) · dificultad 417 · number_theory

Problema original de Pavel Atnashev, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan las primeras k de 12 cifras, 0 ≤ k ≤ 12. Hay que imprimir
cualquier número de 12 cifras que empiece por ellas y no tenga más
divisores que 1 y él mismo. Se garantiza que existe respuesta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

k en la primera línea y las k cifras en la segunda.

## Salida

El número de 12 cifras.

## Comprobación

El comprobador acepta cualesquiera 12 cifras que empiecen por las dadas
y formen un número sin otros divisores.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
64631
```

Salida:

```
646310554187
```

## Solución

Se rellenan las cifras libres con ceros y se cuenta hacia arriba hasta
que el número sea primo. Los primos cerca de 10¹² están separados unos
28 en promedio, y ningún hueco por debajo de 10¹² pasa de unos cientos,
así que solo se prueban unos cientos de números. Cada uno se comprueba
con el test de Miller–Rabin con las bases 2, 3, 5, 7, 11 y 13, que no
se equivocan por debajo de 3 · 10¹². Si se dan las 12 cifras, la
respuesta es el propio número. El número se imprime con ceros a la
izquierda cuando un prefijo de ceros lo pide.

Detalles a tener en cuenta:

- las cifras dadas pueden empezar por ceros y la respuesta debe
  conservarlos, como `000000000002` (pruebas 04 y 05);
- los cuadrados dentro del test llegan a 10²⁴, más de 64 bits, así que
  la multiplicación módulo n requiere cuidado;
- con k = 0 la segunda línea está vacía (prueba 02).

## Notas por lenguaje

- C++ y Rust multiplican en 128 bits, y Go usa `bits.Mul64` y
  `bits.Rem64`. Java parte un factor en mitades de 20 bits, lo que
  mantiene cada producto por debajo de 2⁶⁰ para n menor que 2⁴⁰.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1343_number_theory.cpp](1343_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(G·log N) | AC | 0.015 s | 392 KB |
| [1343_number_theory.go](1343_number_theory.go) | Go 1.14 x64 | number_theory | O(G·log N) | AC | 0.031 s | 1024 KB |
| [1343_number_theory.java](1343_number_theory.java) | Java 1.8 | number_theory | O(G·log N) | AC | 0.125 s | 1752 KB |
| [1343_number_theory.py](1343_number_theory.py) | Python 3.12 x64 | number_theory | O(G·log N) | AC | 0.078 s | 524 KB |
| [1343_number_theory.rs](1343_number_theory.rs) | Rust 1.75 x64 | number_theory | O(G·log N) | AC | 0.046 s | 216 KB |
