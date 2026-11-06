# 1032. Elegir números cuya suma sea múltiplo de N

[Timus 1032](https://acm.timus.ru/problem.aspx?space=1&num=1032) · dificultad 302 · prefix_sums, math

Problema original del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `N` enteros positivos (`1 ≤ N ≤ 10 000`, cada uno como mucho 15 000,
con repeticiones posibles), elige uno o más cuya suma sea divisible entre
`N`. Si no hay tal elección, imprime 0.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego los `N` números, uno por línea.

## Salida

La cantidad de números elegidos y luego esos números, uno por línea, en
cualquier orden; o 0.

## Evaluación

Se acepta cualquier elección válida. El verificador comprueba que cada
número se usa como mucho tantas veces como aparece, que se elige al menos
uno y que la suma es múltiplo de `N`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3
8
6
1
```

Salida:

```
1
8
```

### Ejemplo 2

Entrada:

```
1
15000
```

Salida:

```
1
15000
```

## Solución

**Siempre existe una elección**, e incluso puede ser un bloque de números
consecutivos. Mira las `N + 1` sumas prefijas `S_0 = 0, S_1, ..., S_N`
módulo `N`. Toman como mucho `N` valores distintos, así que por el
**principio del palomar** dos coinciden, `S_i ≡ S_j (mod N)` con `i < j`;
entonces `a_{i+1} + ... + a_j = S_j - S_i` es múltiplo de `N`.

Se recorren los números manteniendo la suma prefija módulo `N` y la primera
posición en que apareció cada resto (el resto 0 en la posición 0). El primer
resto repetido da el bloque. `O(N)`.

Así que la respuesta 0 nunca hace falta.

Detalles a tener en cuenta:

- el resto 0 debe darse por «visto» en la posición 0, para encontrar un
  prefijo que ya sea múltiplo de `N`;
- en la salida van los valores, no sus posiciones;
- `N = 1`: cualquier número sirve.

## Soluciones optimizadas

La versión compacta en Python usa el mismo algoritmo de sumas de prefijos. Un arreglo denso guarda las primeras posiciones y reserva el cero para restos aún no vistos. Las posiciones y los valores caben en enteros sin signo de 16 bits. Lee hasta el primer resto repetido e imprime el bloque correspondiente. El tiempo y el espacio adicional son O(N). El envío aceptado usó 1068 KB en lugar de 2608 KB, un 59,0% menos. El tiempo subió de 0,093 s a 0,109 s.

Las implementaciones base aceptadas [1032_prefix_sums.cpp](1032_prefix_sums.cpp), [1032_prefix_sums.go](1032_prefix_sums.go), [1032_prefix_sums.java](1032_prefix_sums.java), [1032_prefix_sums.rs](1032_prefix_sums.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

La misma pasada en todos los lenguajes.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1032_prefix_sums.cpp](1032_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.015 s | 232 KB | 11278431 |
| [1032_prefix_sums.go](1032_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 1368 KB | 11278432 |
| [1032_prefix_sums.java](1032_prefix_sums.java) \* | Java 1.8 | prefix_sums | O(N) | AC | 0.156 s | 944 KB | 11278435 |
| [1032_prefix_sums.py](1032_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.093 s | 2608 KB | 11278433 |
| [1032_prefix_sums.rs](1032_prefix_sums.rs) \* | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.046 s | 464 KB | 11278437 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1032_prefix_sums_optimized.py](1032_prefix_sums_optimized.py) \* | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.109 s | 1068 KB | 11310314 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
