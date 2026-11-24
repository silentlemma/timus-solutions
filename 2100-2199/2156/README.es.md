# 2156. Repartir las diferencias alrededor de un círculo en mitades iguales

[Timus 2156](https://acm.timus.ru/problem.aspx?space=1&num=2156) · dificultad 656 · math, constructive

Problema original de Semyon Trifochkin, del Concurso de Programación por Equipos de los Urales 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n amigos con interés a₁ … aₙ se sientan alrededor de una mesa, y la
conversación entre los vecinos i e i + 1 (n y 1 la última) tiene interés
|aᵢ − aᵢ₊₁|. Repartir las n conversaciones en dos conjuntos no vacíos con
el mismo interés total, o imprimir NO. Se acepta cualquier reparto
válido. Los límites son 1 segundo y 256 MB.

## Entrada

n, 3 ≤ n ≤ 10⁵, y luego a₁ … aₙ, 1 ≤ aᵢ ≤ 10⁹.

## Salida

YES, y luego el tamaño y los números del primer conjunto y del segundo,
o NO.

## Evaluación

Un comprobador verifica que los dos conjuntos no estén vacíos, repartan
todas las conversaciones y tengan sumas iguales.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 2 3
```

Salida:

```
YES
2
1 2
1
3
```

## Solución

La respuesta siempre es YES. Dando una vuelta a la mesa, las diferencias
con signo aᵢ − aᵢ₊₁ suman 0. Así que las conversaciones donde el valor
baja (aᵢ > aᵢ₊₁) tienen el mismo interés total que aquellas donde sube,
y las conversaciones entre vecinos iguales tienen interés 0 y pueden ir
a cualquier lado.

Si los valores no son todos iguales, hay al menos una bajada y una
subida, así que ambos conjuntos no están vacíos. Si son todos iguales,
cada conversación tiene interés 0, y vale una conversación contra las
otras n − 1. El trabajo es O(n).

En el ejemplo el valor solo baja de 3 a 1, así que la conversación 3
(interés 2) equilibra las conversaciones 1 y 2 (interés 1 cada una).

## Soluciones optimizadas

`2156_math_constructive_optimized.cpp`. Conserva la partición exacta por descensos circulares. Lee alturas con un búfer fread de 4 KiB, guardando solo la primera y la anterior, y marca las aristas descendentes en bitset. Si todas son iguales, asigna la primera arista a un grupo. Recorre dos veces el bitset y emite los grupos con fwrite y un búfer de 4 KiB, sin arreglo de alturas ni vectores de índices. Tiempo O(n), n bits más búferes fijos; partición y numeración sin cambios.

Accepted del fuente exacto #11326979: 0.015 s / 136 KB. Muestra G++ 13.2 guardada el 2026-11-20: tiempo 1/33, memoria 1/33. Se conservan los fuentes didácticos.

Se leen los valores en orden y solo se guardan el primero y el anterior. Un conjunto de bits marca los descensos. Se recorre dos veces para imprimir ambos grupos sin guardar la entrada ni las listas de índices.

Go guarda un indicador booleano por arista y escribe los índices en un búfer de tamaño fijo.

Python lee y escribe por bloques y guarda un byte por arista.

Rust guarda un indicador booleano por arista y escribe los índices en un búfer de tamaño fijo.

Java usa búferes de entrada y salida y guarda un indicador booleano por arista. La memoria baja de 9008 a 656 KB y el tiempo sube de 0.140 a 0.156 s.

**Envíos de las versiones optimizadas en Timus**

`2156_math_constructive_optimized.cpp` (G++ 13.2 x64) №11326979 · `2156_math_constructive_optimized.go` (Go 1.14 x64) №11317380 · `2156_math_constructive_optimized.java` (Java 1.8) №11317394 · `2156_math_constructive_optimized.py` (Python 3.12 x64) №11317384 · `2156_math_constructive_optimized.rs` (Rust 1.75 x64) №11317388.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321927 · Java 1.8 №11321928 · Python 3.12 x64 №11321930 · Rust 1.75 x64 №11321931.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2156_math_constructive.cpp](2156_math_constructive.cpp) | G++ 13.2 x64 | math, constructive | O(n) | AC | 0.093 s | 2652 KB | 11321927 |
| [2156_math_constructive.go](2156_math_constructive.go) | Go 1.14 x64 | math, constructive | O(n) | AC | 0.109 s | 8676 KB | 11322054 |
| [2156_math_constructive.java](2156_math_constructive.java) | Java 1.8 | math, constructive | O(n) | AC | 0.171 s | 8996 KB | 11321928 |
| [2156_math_constructive.py](2156_math_constructive.py) | Python 3.12 x64 | math, constructive | O(n) | AC | 0.156 s | 21304 KB | 11321930 |
| [2156_math_constructive.rs](2156_math_constructive.rs) | Rust 1.75 x64 | math, constructive | O(n) | AC | 0.078 s | 8860 KB | 11321931 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2156_math_constructive_optimized.cpp](2156_math_constructive_optimized.cpp) | G++ 13.2 x64 | math, constructive | O(n) | AC | 0.015 s | 136 KB | 11326979 |
| [2156_math_constructive_optimized.go](2156_math_constructive_optimized.go) | Go 1.14 x64 | math, constructive | O(n) | AC | 0.031 s | 1068 KB | 11317380 |
| [2156_math_constructive_optimized.py](2156_math_constructive_optimized.py) | Python 3.12 x64 | math, constructive | O(n) | AC | 0.125 s | 1164 KB | 11317384 |
| [2156_math_constructive_optimized.rs](2156_math_constructive_optimized.rs) | Rust 1.75 x64 | math, constructive | O(n) | AC | 0.046 s | 304 KB | 11317388 |
| [2156_math_constructive_optimized.java](2156_math_constructive_optimized.java) | Java 1.8 | math, constructive | O(n) | AC | 0.156 s | 656 KB | 11317394 |
