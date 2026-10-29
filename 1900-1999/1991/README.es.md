# 1991. Contar suministros sin usar y objetivos restantes

[Timus 1991](https://acm.timus.ru/problem.aspx?space=1&num=1991) · dificultad 48 · implementation

Problema original de Denis Dublennykh, preparado por Egor Shchelkonogov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `n` grupos independientes, cada uno con exactamente `k` objetivos.
El grupo `i` recibe `a_i` suministros, cada uno utilizable una vez para
eliminar un objetivo de ese mismo grupo. Cada uso tiene éxito. No se
permite transferir suministros entre grupos. Tras eliminar cuantos
objetivos sea posible, cuente los suministros sin usar y los objetivos
restantes.

Límites: `1≤n,k≤10000`, `0≤a_i≤100000`. Tiempo: 1 segundo; memoria: 64 MB.

## Entrada

La primera línea contiene `n k`; la siguiente, los `n` suministros.

## Salida

Dos enteros: primero los suministros sin usar y luego los objetivos restantes.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

Entrada:

```
4 5
2 7 5 0
```

Salida:

```
2 8
```

Los pares `(suministros,objetivos)` restantes son `(0,3)`, `(2,0)`,
`(0,0)` y `(0,5)`. Suman `(2,8)`.

## Solución

Cada grupo gasta min(aᵢ, k) suministros en min(aᵢ, k) objetivos. Así
deja aᵢ − k suministros sin usar si aᵢ > k, y k − aᵢ objetivos
pendientes en otro caso. Estos números se suman sobre los grupos.
`O(n)`.

Detalles a tener en cuenta:

- los suministros no pasan de un grupo a otro, así que un grupo puede
  tener suministros de sobra mientras otro aún tiene objetivos: comparar
  solo los totales es un error;
- el total sin usar llega a 10 000 · 99 999 ≈ 10⁹, que todavía cabe en
  un entero de 32 bits con signo.

## Soluciones optimizadas

La solución optimizada en C++ lee y escribe con `scanf` y `printf` en
lugar de `iostream`: 132 KB en lugar de 448 KB. Los totales son los
mismos.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1991_implementation.cpp](1991_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 448 KB | 11292383 |
| [1991_implementation.go](1991_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1236 KB | 11292384 |
| [1991_implementation.java](1991_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 472 KB | 11303526 |
| [1991_implementation.py](1991_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 1380 KB | 11292385 |
| [1991_implementation.rs](1991_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 480 KB | 11292387 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1991_implementation_optimized.cpp](1991_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 132 KB | 11303652 |
