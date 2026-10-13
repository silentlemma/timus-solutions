# 1473. Granja 2

[Timus 1473](https://acm.timus.ru/problem.aspx?space=1&num=1473) · dificultad 5041 · geometry

Problema original de Alexander Ipatov, del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada experto elige enteros a_i, b_i (|a_i|, |b_i| ≤ 2·10⁹) y declara
camello a un animal de parámetros (A, B) si a_i·A + b_i·B > 0, oveja si
es < 0, y no opina si es 0. Una comisión de K expertos declara camello
(oveja) a un animal cuando así lo dice estrictamente más de la mitad.
Dados N animales conocidos (1 ≤ N ≤ 10000, 0 ≤ A, B ≤ 10000, tipo 1
para camello y 2 para oveja), hay que hallar el menor K y los números
de los expertos que clasifican bien a todos los animales, o escribir −1
si ninguna comisión puede.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego N líneas A B tipo.

## Salida

−1, o K y K líneas a_i b_i. Se acepta cualquier comisión válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
10 0 1
0 10 2
```

Salida:

```
1
1 -1
```

## Solución

El voto de un experto solo depende de la dirección de (A, B): nadie vota
por un animal en el origen, y dos animales en un mismo rayo desde el
origen reciben los mismos votos, así que un animal en el origen o tipos
distintos en un mismo rayo dan −1. Se reduce cada punto por el mcd y se
ordenan los rayos por ángulo; todos están en el primer cuadrante, un
arco menor que π, así que cada experto cambia el voto entre tipos a lo
sumo una vez, pudiendo abstenerse. Sea r el número de tramos de un mismo
tipo.

Se cuentan los expertos que dicen «camello». Con K impar, esa cuenta
debe cruzar K / 2 en cada frontera entre tramos, lo que exige que al
menos un experto cambie ahí; con K par debe cambiar entre K/2 + 1 o más
y K/2 − 1 o menos, lo que exige dos.
Por tanto K ≥ r − 1 para K impar y K ≥ 2(r − 1) para K par, y el menor K
es r − 1 si es impar y r en otro caso (incluido K = 1 para un solo tramo).
Se alcanza: en cada frontera entre los rayos p y q, la recta por el
origen en la dirección p + q pasa estrictamente entre ambos, y el experto
perpendicular a ella vota por el tipo anterior antes de ella y por el
otro después. Si esos expertos son un número par, se añade uno más,
(1, 1) o (−1, −1), que vota por el primer tipo en todas partes; así el
margen de votos alterna entre +1 y −1 de tramo en tramo. Todos los
números quedan por debajo de 20001. `O(N log N)`.

Detalles a tener en cuenta:

- un animal en el origen nunca puede clasificarse (prueba 02);
- los puntos de un mismo rayo, como (2, 4) y (1, 2), son una misma
  dirección: tipos distintos ahí dan −1 y tipos iguales forman un tramo
  (pruebas 03, 05, gen3, gen5);
- un número impar de tramos necesita un experto más, porque una comisión
  par necesita dos cambios en cada frontera (pruebas 06, 12);
- se usan productos vectoriales enteros exactos para ordenar rayos tan
  cercanos como (9999, 9998) y (10000, 9999) (prueba 07).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1473_geometry.cpp](1473_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.031 s | 516 KB |
| [1473_geometry.go](1473_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 2544 KB |
| [1473_geometry.java](1473_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 4224 KB |
| [1473_geometry.py](1473_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.109 s | 5840 KB |
| [1473_geometry.rs](1473_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.046 s | 832 KB |
