# 1079. El mayor término de la sucesión de Stern hasta n

[Timus 1079](https://acm.timus.ru/problem.aspx?space=1&num=1079) · dificultad 111 · dp

Problema original de Emil Kelevedzhiev, del Torneo de Informática del Festival Matemático de Invierno, Varna 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La sucesión es `a₀ = 0`, `a₁ = 1`, `a₂ᵢ = aᵢ` y `a₂ᵢ₊₁ = aᵢ + aᵢ₊₁` para
`i ≥ 1`. Para cada `n` dado (`1 ≤ n ≤ 99 999`) imprime el mayor de
`a₀, a₁, …, aₙ`.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Hasta diez líneas con `n` y luego una línea con 0.

## Salida

El máximo para cada `n`, uno por línea.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
10
0
```

Salida:

```
3
4
```

## Solución

Cada término solo usa términos de índice menor, así que una pasada de 2 a
99 999 llena toda la tabla, y un segundo máximo acumulado
`best[i] = max(best[i − 1], aᵢ)` responde todas las consultas de una vez.
`O(N)` para la tabla, `O(1)` por consulta.

Es la sucesión diatómica de Stern. Sus récords son números de Fibonacci,
alcanzados cerca de `n = (2^k ± 1)/3`; el mayor valor hasta 99 999 es
2584, así que los enteros de 32 bits sobran.

Detalles a tener en cuenta:

- las consultas llegan en cualquier orden y terminan con 0, que no es una
  consulta;
- la fórmula para índices impares usa `aᵢ₊₁`, cuyo índice sigue siendo
  menor que `2i + 1`, así que el orden de la pasada es correcto.

Las respuestas se comprobaron con la definición calculada por una
recursión memorizada y un recorrido simple para cada consulta.

## Notas por lenguaje

- Todos los lenguajes construyen ambas tablas antes de leer las
  consultas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1079_dp.cpp](1079_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 960 KB |
| [1079_dp.go](1079_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 2764 KB |
| [1079_dp.java](1079_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 2364 KB |
| [1079_dp.py](1079_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.125 s | 3280 KB |
| [1079_dp.rs](1079_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 1004 KB |
