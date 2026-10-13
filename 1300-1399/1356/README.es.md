# 1356. Algo más fácil

[Timus 1356](https://acm.timus.ru/problem.aspx?space=1&num=1356) · dificultad 298 · number_theory

Problema original de Aleksandr Bikbaev, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada uno de T ≤ 20 números N, 2 ≤ N ≤ 10⁹, hay que escribir N como
suma del menor número posible de primos e imprimir esos primos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

T, luego T líneas con N.

## Salida

Para cada N, una línea con los primos. Se acepta cualquier suma con el
menor número de términos.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
2
27
85
192
14983
3
7
```

Salida:

```
2
23 2 2
2 83
11 181
14983
3
7
```

## Solución

- Si N es primo, basta uno.
- Si N es par, bastan dos: la conjetura de Goldbach no está demostrada,
  pero se ha comprobado mucho más allá de 10⁹. Se prueba p = 2, 3, 4, …
  hasta que p y N − p sean primos.
- Si N es impar, una suma de dos primos tiene que contener el 2, porque
  dos primos impares suman un par. Así que dos primos sirven justo
  cuando N − 2 es primo.
- Si no, hacen falta tres y bastan: se toma el mayor primo p ≤ N − 4. El
  resto N − p es par y al menos 4, y se parte en dos primos como antes.

La primalidad se comprueba con Miller–Rabin en las bases 2, 3, 5, 7, que
es exacto para todo número menor que 3,2·10⁹. Los huecos entre primos
por debajo de 10⁹ miden menos de 300, y en 200 000 números pares justo
por debajo de 10⁹ el menor primo de Goldbach nunca pasó de 919, así que
cada respuesta necesita solo unos cientos de pruebas.
`O(T · g · log N)`, con g la cantidad de candidatos probados.

Detalles a tener en cuenta:

- un N impar nunca se parte en dos primos impares, así que el caso con
  2 debe comprobarse aparte (`85 = 2 + 83` en el ejemplo);
- 4 = 2 + 2 es la única partición par que usa el 2 (prueba 03);
- el resto tras el mayor primo debe ser al menos 4, porque 2 no es suma
  de dos primos;
- T puede ser 0 (prueba 04).

Se comprobó que las respuestas son primos con la suma correcta y el
menor número de términos para todo N hasta 20 000 y para 2 000 N
aleatorios hasta 10⁹, y la prueba de Miller–Rabin se comparó con la
división por tanteo en 203 000 números. Las pruebas se juzgan con un
verificador que acepta cualquier suma mínima.

## Notas por lenguaje

- Los productos de Miller–Rabin quedan por debajo de 10¹⁸, así que los
  enteros de 64 bits bastan en todos los lenguajes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1356_number_theory.cpp](1356_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T·g·log N) | AC | 0.015 s | 192 KB |
| [1356_number_theory.go](1356_number_theory.go) | Go 1.14 x64 | number_theory | O(T·g·log N) | AC | 0.031 s | 1100 KB |
| [1356_number_theory.java](1356_number_theory.java) | Java 1.8 | number_theory | O(T·g·log N) | AC | 0.109 s | 516 KB |
| [1356_number_theory.py](1356_number_theory.py) | Python 3.12 x64 | number_theory | O(T·g·log N) | AC | 0.109 s | 664 KB |
| [1356_number_theory.rs](1356_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T·g·log N) | AC | 0.015 s | 224 KB |
