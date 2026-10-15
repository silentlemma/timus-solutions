# 1665. La pirámide financiera del decano

[Timus 1665](https://acm.timus.ru/problem.aspx?space=1&num=1665) · dificultad 438 · number_theory

Problema original de Alex Samsonov, del Ural SU Contest en el campus de invierno de Petrozavodsk, enero de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Al final del día 1 hay una solicitud sobre la mesa. Cada día siguiente
el número de solicitudes se multiplica por un factor entero que es 2 o
un impar mayor que 1, quizá distinto cada día. El dinero solo se paga
en un día par y solo si esa tarde hay exactamente N solicitudes. Para
cada N hay que decidir si esto puede ocurrir.

## Entrada

T (1 ≤ T ≤ 100) y luego T números N (1 ≤ N ≤ 2²⁵ − 1).

## Salida

`YES` o `NO` para cada N.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
4
7
6
30
```

Salida:

```
NO
YES
NO
YES
```

## Solución

El día d la cantidad es un producto de d − 1 factores y d debe ser par,
así que la pregunta es si N es producto de un número impar de factores,
cada uno 2 o un impar mayor que 1. Sea N = 2ᵃ · r con r impar. Solo los
factores 2 aportan doses, así que hay exactamente a factores iguales a 2
y los factores impares multiplican r.

- Si r = 1, hay exactamente a factores: `YES` cuando a es impar (N = 1
  es el día 1 y nunca se paga).
- Si a es par y r > 1, los a doses y el propio r dan a + 1 factores, un
  número impar: `YES`.
- Si a es impar, r debe partirse en un número par de factores impares
  mayores que 1, lo que es posible exactamente cuando r no es primo (dos
  factores, o más si hace falta): `YES` si r es compuesto, `NO` si es
  primo.

La primalidad se comprueba dividiendo por impares hasta √r, a lo sumo
unos 2900 divisores. `O(T · √N)`.

Detalles a tener en cuenta:

- N = 1 y N = 2ᵃ con a par son `NO`; 2ᵃ con a impar es `YES` (prueba 02);
- una potencia de dos de exponente impar por un primo es `NO` (6 en el
  ejemplo, 2²³ · 3 en la prueba 03).

Las respuestas coinciden con una búsqueda exhaustiva de todas las
sucesiones de factores para cada N hasta 3000 y con una implementación
aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1665_number_theory.cpp](1665_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T sqrt N) | AC | 0.015 s | 128 KB |
| [1665_number_theory.go](1665_number_theory.go) | Go 1.14 x64 | number_theory | O(T sqrt N) | AC | 0.015 s | 1084 KB |
| [1665_number_theory.java](1665_number_theory.java) | Java 1.8 | number_theory | O(T sqrt N) | AC | 0.125 s | 448 KB |
| [1665_number_theory.py](1665_number_theory.py) | Python 3.12 x64 | number_theory | O(T sqrt N) | AC | 0.093 s | 412 KB |
| [1665_number_theory.rs](1665_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T sqrt N) | AC | 0.031 s | 208 KB |
