# 1142. Contar las ordenaciones con empates de N objetos

[Timus 1142](https://acm.timus.ru/problem.aspx?space=1&num=1142) · dificultad 154 · combinatorics

Problema original de Timus; no se indican autor ni fuente.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Entre dos cualesquiera de `N` objetos comparables se cumple una de
`a = b`, `a < b`, `b < a`. Cuenta las formas distintas de ordenar `N`
objetos en este sentido, con empates permitidos: para tres objetos hay
13, de `a = b = c` a `c < b < a`. Responde para varios `N` de 2 a 10; la
entrada termina con `-1`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Valores de `N`, uno por línea, y luego `-1`.

## Salida

La cantidad para cada `N`, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
3
-1
```

Salida:

```
3
13
```

## Solución

Una ordenación con empates es una sucesión de grupos de objetos iguales,
con los grupos estrictamente crecientes. Mirando el primer grupo: es
cualquier conjunto no vacío de `k` objetos, elegido de `C(n, k)` formas,
y los `n − k` objetos restantes forman su propia ordenación con empates.
Así que, con `a(0) = 1`,

`a(n) = Σ_{k=1..n} C(n, k)·a(n − k)`.

Son los números de Bell ordenados (números de Fubini) 1, 1, 3, 13, 75,
541, …; el mayor que hace falta, `a(10) = 102247563`, cabe en 32 bits. La
tabla se construye una vez con el triángulo de Pascal, y cada consulta es
una búsqueda. `O(10²)` para construirla.

Detalles a tener en cuenta:

- la entrada no trae la cantidad; se lee hasta `-1`;
- el mismo `N` puede preguntarse varias veces.

Los valores se compararon con la fórmula independiente
`a(n) = Σ k!·S(n, k)` con números de Stirling de segunda especie, y para
`n ≤ 6` con un listado de todas las ordenaciones.

## Notas por lenguaje

- Todos los lenguajes construyen la misma tabla antes de leer las
  consultas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1142_combinatorics.cpp](1142_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(1) per query | AC | 0.001 s | 128 KB |
| [1142_combinatorics.go](1142_combinatorics.go) | Go 1.14 x64 | combinatorics | O(1) per query | AC | 0.001 s | 1084 KB |
| [1142_combinatorics.java](1142_combinatorics.java) | Java 1.8 | combinatorics | O(1) per query | AC | 0.093 s | 1604 KB |
| [1142_combinatorics.py](1142_combinatorics.py) | Python 3.12 x64 | combinatorics | O(1) per query | AC | 0.031 s | 436 KB |
| [1142_combinatorics.rs](1142_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(1) per query | AC | 0.001 s | 220 KB |
