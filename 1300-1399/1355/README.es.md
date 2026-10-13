# 1355. La calva, otra vez

[Timus 1355](https://acm.timus.ru/problem.aspx?space=1&num=1355) · dificultad 212 · number_theory

Problema original de Aleksandr Bikbaev, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las tabernas se numeran con enteros positivos, y desde la taberna n solo
se puede ir a una taberna cuyo número sea múltiplo de n. Un paseo
empieza en la taberna a y debe acabar en la taberna b, con una jarra de
cerveza en cada taberna del camino, a y b incluidas. Para cada uno de
T ≤ 20 pares con 1 ≤ a, b ≤ 10⁹, hay que imprimir el mayor número de
jarras, o 0 si no se puede llegar a b.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

T, luego T líneas con a y b.

## Salida

T líneas con las respuestas.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
30 89
2 16
3 243
1 1
2 2
```

Salida:

```
0
4
5
1
1
```

## Solución

Cada número del paseo divide al siguiente, así que solo se llega a b si
a divide a b. Entonces cada paso multiplica el número por un factor
mayor que 1, y el producto de todos los factores es q = b / a. Para
visitar tantas tabernas como sea posible, cada factor debe ser un primo,
de modo que el número de pasos es Ω(q), la cantidad de factores primos
de q contados con repetición. La respuesta es 1 + Ω(q), contando la
propia taberna a.

La división por tanteo hasta √q ≤ 31 623 da Ω(q). `O(T · √(b / a))`.

Detalles a tener en cuenta:

- con a = b se bebe una jarra, no cero (ejemplo);
- si b es menor que a o no es múltiplo suyo, la respuesta es 0
  (prueba 04);
- T puede ser 0, y entonces no se imprimen respuestas (prueba 02);
- q = 2²⁹ da más pasos que nadie, 30 jarras (prueba 03).

## Notas por lenguaje

- Python divide primero entre 2 y luego prueba solo divisores impares,
  lo que reduce el bucle a la mitad con primos grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1355_number_theory.cpp](1355_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 132 KB |
| [1355_number_theory.go](1355_number_theory.go) | Go 1.14 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 1100 KB |
| [1355_number_theory.java](1355_number_theory.java) | Java 1.8 | number_theory | O(T·√(b/a)) | AC | 0.078 s | 448 KB |
| [1355_number_theory.py](1355_number_theory.py) | Python 3.12 x64 | number_theory | O(T·√(b/a)) | AC | 0.109 s | 392 KB |
| [1355_number_theory.rs](1355_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 212 KB |
