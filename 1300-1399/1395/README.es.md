# 1395. Pascal contra C++. Versión 2

[Timus 1395](https://acm.timus.ru/problem.aspx?space=1&num=1395) · dificultad 2203 · hashing

Problema original de Ilya Grebnov, Dmitry Kovalioff y Nikita Rybak, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una versión más difícil del problema 1452. De N ≤ 10 000 números entre 1
y 10⁹, hay que elegir tantos valores distintos como sea posible que sean
términos consecutivos de una progresión aritmética creciente, en
cualquier orden, e imprimir su número y sus posiciones.

Límite de tiempo: 1 segundo. Límite de memoria: 4 MB.

## Entrada

N y luego los N números.

## Salida

El mayor número de elementos y luego sus posiciones en cualquier orden.

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

Con 4 MB no cabe la tabla habitual sobre todos los pares, así que las
soluciones recorren las progresiones directamente. Cada valor distinto
se guarda una vez, con su primera posición, en una tabla hash de
direccionamiento abierto de 2¹⁵ casillas, y los valores se ordenan. Para
cada par i < j con d = a[j] − a[i]:

- la fila de pares termina en cuanto a[i] + best·d pasa del mayor valor:
  una progresión más larga desde a[i] no cabe, y d solo crece;
- el par se salta si falta a[j] + d, pues dos términos no superan el
  mejor, o si está a[i] − d, pues la progresión se recorre desde su
  término menor;
- si no, se recorre a[j] + d, a[j] + 2d, … mientras los valores existan.

Cada par de vecinos de una progresión da a lo sumo un paso de recorrido,
así que el trabajo es de `O(N²)` consultas, a lo sumo dos por par antes
del recorrido. La expresión de poda a[i] + best·d requiere 64 bits.

Detalles a tener en cuenta:

- los valores repetidos cuentan una vez (ejemplo 1 y prueba 04);
- un único valor repetido da un solo elemento (prueba 02);
- un conjunto sin progresiones de tres términos deja el mejor en 2, y
  ahí la poda es más débil (prueba generada 8, números cuyas cifras en
  base 3 son solo 0 y 1);
- a[i] + best·d puede superar 2³¹ (prueba 10).

Las respuestas se compararon en 3 000 secuencias cortas aleatorias con
una búsqueda sobre todos los pares. Las pruebas se juzgan con un
verificador que exige el número esperado y comprueba que las posiciones
dan valores distintos de una misma progresión.

## Notas por lenguaje

- El enunciado solo admite C, C++ y Pascal, pero el formulario de envío
  de Timus ofrece además Rust 1.75, así que hay soluciones en C++ y Rust;
  Go, Python y Java no se pueden enviar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1395_hashing.cpp](1395_hashing.cpp) | G++ 13.2 x64 | hashing | O(N^2) with O(1) look-ups; O(N^3) worst case | AC | 0.453 s | 504 KB |
| [1395_hashing.rs](1395_hashing.rs) | Rust 1.75 x64 | hashing | O(N^2) with O(1) look-ups; O(N^3) worst case | AC | 0.500 s | 1276 KB |
