# 1484. Puntuación de la película

[Timus 1484](https://acm.timus.ru/problem.aspx?space=1&num=1484) · dificultad 629 · math

Problema original de Vladimir Yakovlev, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La puntuación de una película es la media de votos enteros de 1 a 10,
redondeada a un decimal con las mitades hacia arriba (7.55 se muestra
como 7.6). Ahora muestra X tras N votos (1 ≤ X, Y ≤ 10 con un decimal,
1 ≤ N ≤ 10⁶). Hay que hallar el menor número de votos nuevos que hacen
que la puntuación muestre como mucho Y sean cuales sean los votos
anteriores, o escribir «Impossible».

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

X, Y y N.

## Salida

El número de votos o «Impossible».

## Ejemplos

### Ejemplo 1

Entrada:

```
9.5 2.0 12
```

Salida:

```
86
```

## Solución

Se trabaja en décimas: x = 10X e y = 10Y. Una suma S de N votos muestra
x justo cuando (2x − 1)N ≤ 20S < (2x + 1)N, y los votos permiten
N ≤ S ≤ 10N. Si ningún entero S cumple ambas cosas, ningún conjunto de
votos muestra X y la respuesta es «Impossible»: un solo voto, por
ejemplo, nunca muestra 7.1.

Los votos nuevos deben ser todos 1, y el peor caso es el mayor S
posible. Tras k de esos votos la puntuación muestra como mucho y cuando
20(S + k) < (2y + 1)(N + k), es decir, (2y − 19)·k > 20S − (2y + 1)N.
Como Y ≥ 1, 2y − 19 es positivo, así que el menor k es 0 si el lado
derecho ya es negativo y (20S − (2y + 1)N) div (2y − 19) + 1 si no.
`O(1)`.

Detalles a tener en cuenta:

- una puntuación que N votos no pueden mostrar es «Impossible», aunque
  el objetivo fuera fácil (pruebas 02, 09);
- 7.55 se redondea a 7.6, así que los límites son semiabiertos y mejor
  llevarlos en enteros (prueba 07);
- la respuesta llega a 179 000 001 al bajar a 1.0 un millón de dieces
  (prueba 04).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1484_math.cpp](1484_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 132 KB |
| [1484_math.go](1484_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1076 KB |
| [1484_math.java](1484_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1636 KB |
| [1484_math.py](1484_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 456 KB |
| [1484_math.rs](1484_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 232 KB |
