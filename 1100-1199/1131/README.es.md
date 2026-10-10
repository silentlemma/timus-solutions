# 1131. Copiar un programa a N ordenadores con K cables, una copia por cable y hora

[Timus 1131](https://acm.timus.ru/problem.aspx?space=1&num=1131) · dificultad 77 · math

Problema original de Stanislav Vasiliev y Alexander Mironenko, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un programa está en uno de `N` ordenadores. En una hora, un ordenador que
lo tiene puede copiarlo a otro por un cable, y hay `K` cables. Halla el
menor número de horas hasta que los `N` ordenadores tengan el programa,
con `1 ≤ N, K ≤ 10⁹`.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `K` en una línea.

## Salida

El menor número de horas.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 3
```

Salida:

```
4
```

## Solución

En una hora reciben el programa `min(have, K)` ordenadores nuevos, donde
`have` es el número de ordenadores que ya lo tienen; copiar lo máximo
posible cada hora es claramente lo mejor. Mientras `have < K`, todos los
ordenadores copian y la cantidad se duplica; esto dura como mucho unas 30
horas. Cuando `have ≥ K`, cada hora se añaden exactamente `K`
ordenadores, así que los `N − have` restantes necesitan
`⌈(N − have) / K⌉` horas más. La duplicación se detiene antes si `have`
ya llega a `N`. `O(log min(N, K))`.

Detalles a tener en cuenta:

- con `N = 1` no hacen falta horas;
- con `K = 1` y `N = 10⁹` la respuesta es casi `10⁹`, así que las horas
  tras la duplicación se calculan con una división, no una a una;
- durante la duplicación la cantidad puede pasar de `2³¹`, así que se usan
  enteros de 64 bits.

Las respuestas se compararon con una búsqueda binaria sobre el número de
horas en todas las pruebas y con una simulación hora a hora para todos los
`N < 200` y `K < 70`.

## Notas por lenguaje

- Todos los lenguajes usan el mismo bucle y la misma división.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1131_math.cpp](1131_math.cpp) | G++ 13.2 x64 | math | O(log min(N, K)) | AC | 0.015 s | 128 KB |
| [1131_math.go](1131_math.go) | Go 1.14 x64 | math | O(log min(N, K)) | AC | 0.015 s | 1076 KB |
| [1131_math.java](1131_math.java) | Java 1.8 | math | O(log min(N, K)) | AC | 0.125 s | 1592 KB |
| [1131_math.py](1131_math.py) | Python 3.12 x64 | math | O(log min(N, K)) | AC | 0.078 s | 424 KB |
| [1131_math.rs](1131_math.rs) | Rust 1.75 x64 | math | O(log min(N, K)) | AC | 0.046 s | 216 KB |
