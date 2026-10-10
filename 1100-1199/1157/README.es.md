# 1157. Las menos baldosas que forman N rectángulos, cuando K baldosas menos formaban M

[Timus 1157](https://acm.timus.ru/problem.aspx?space=1&num=1157) · dificultad 200 · number_theory

Problema original del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda en inglés.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un niño coloca todas sus baldosas cuadradas en forma de rectángulo. Dados
`M`, `N` y `K` (`M, N ≤ 50`, `K ≤ 9999`), halla el menor número de
baldosas `L` tal que con `L` baldosas se formen exactamente `N`
rectángulos distintos y con `L − K` baldosas exactamente `M`. Imprime `0`
si no hay tal `L` hasta 10000.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`M`, `N` y `K`.

## Salida

El menor `L`, o `0`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3 1
```

Salida:

```
16
```

## Solución

Con `x` baldosas se forma un rectángulo `a × b` por cada manera de
escribir `x = a·b` con `a ≤ b`, así que el número de rectángulos es el
número de divisores de `x` dividido entre dos y redondeado hacia arriba
(la raíz cuadrada, si la hay, se empareja consigo misma). Una criba sobre
`d` de 1 a 10000 suma uno a cada múltiplo de `d` y cuenta los divisores de
todos los números hasta 10000 en `O(10000·log 10000)` pasos. Después se
prueba `L` desde `K + 1` hacia arriba y se para en el primero con `N`
rectángulos cuyo `L − K` tiene `M`.

Detalles a tener en cuenta:

- `L − K` debe ser al menos una baldosa, así que `L` empieza en `K + 1`;
- un cuadrado perfecto tiene un número impar de divisores, y su
  rectángulo cuadrado cuenta una vez;
- ningún número hasta 10000 tiene más de 64 divisores, así que con `N` o
  `M` mayor que 32 la respuesta es siempre `0`.

Las respuestas se compararon en todas las pruebas con contar los
rectángulos directamente por división de prueba.

## Notas por lenguaje

- Todos los lenguajes hacen la misma criba y la misma búsqueda.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1157_number_theory.cpp](1157_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(L log L) | AC | 0.015 s | 216 KB |
| [1157_number_theory.go](1157_number_theory.go) | Go 1.14 x64 | number_theory | O(L log L) | AC | 0.031 s | 1172 KB |
| [1157_number_theory.java](1157_number_theory.java) | Java 1.8 | number_theory | O(L log L) | AC | 0.125 s | 1620 KB |
| [1157_number_theory.py](1157_number_theory.py) | Python 3.12 x64 | number_theory | O(L log L) | AC | 0.078 s | 712 KB |
| [1157_number_theory.rs](1157_number_theory.rs) | Rust 1.75 x64 | number_theory | O(L log L) | AC | 0.046 s | 300 KB |
