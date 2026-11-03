# 2141. Suma alterna máxima de un segmento

[Timus 2141](https://acm.timus.ru/problem.aspx?space=1&num=2141) · dificultad 251 · dp

Problema original de Alexander Lozhkin, del Concurso por Equipos de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elegir un segmento contiguo de una sucesión, posiblemente vacío, y
sumarlo con signos alternos: el primer elemento elegido con más, el
segundo con menos y así sucesivamente. Hallar el mayor valor posible.
Los límites son 1 segundo y 256 MB.

## Entrada

n, 1 ≤ n ≤ 10⁵, y luego a₁ … aₙ, −10⁵ ≤ aᵢ ≤ 10⁵.

## Salida

La mayor suma alterna (0 para el segmento vacío).

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1 2 3 4 5
```

Salida:

```
5
```

### Ejemplo 2

Entrada:

```
5
1 -2 3 -4 5
```

Salida:

```
15
```

### Ejemplo 3

Entrada:

```
5
-1 -2 -3 -4 -5
```

Salida:

```
2
```

## Solución

Se recorre la sucesión guardando dos valores para los segmentos que
terminan en el elemento actual: P, la mejor suma cuando este elemento
lleva más, y M, cuando lleva menos. Un elemento con más empieza un
segmento nuevo o va tras uno con menos, y un elemento con menos siempre
va tras uno con más:

- P = a + max(0, M anterior),
- M = P anterior − a.

El primer elemento solo puede llevar más, así que se empieza con P = a₁,
y M se pone a 0, lo que en el paso siguiente solo significa "empezar de
nuevo". La respuesta es el mayor P o M visto, o 0. Las sumas llegan a
10¹⁰, así que hacen falta enteros de 64 bits. El recorrido cuesta O(n).

En el segundo ejemplo 1 − (−2) + 3 − (−4) + 5 = 15.

## Soluciones optimizadas

Se mantiene la DP de dos estados para segmentos de signos alternos, incluyendo la respuesta vacía. El nuevo estado negativo usa el positivo anterior, que debe guardarse antes de sobrescribir. Comparaciones directas evitan llamadas repetidas. La lectura acotada de tokens con signo reemplaza listas completas y cortes, conservando correctamente tokens divididos entre bloques. Las sumas nativas usan 64 bits.

- `2141_dp_optimized.cpp`: 0.031 s / 84 KB; base `2141_dp.cpp`: 0.078 s / 140 KB; cambio respecto a la base: tiempo -60.3%, memoria -40.0%.
- `2141_dp_optimized.go`: 0.031 s / 924 KB; base `2141_dp.go`: 0.078 s / 1916 KB; cambio respecto a la base: tiempo -60.3%, memoria -51.8%.
- `2141_dp_optimized.py`: 0.156 s / 1392 KB; base `2141_dp.py`: 0.156 s / 12300 KB; cambio respecto a la base: tiempo -0.0%, memoria -88.7%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `2141_dp.cpp`; versión que cubre `2141_dp_optimized.cpp`; puestos tiempo/memoria 6/1, registros de otros autores 105/105.

- Go: base didáctica preferida `2141_dp.go`; versión que cubre `2141_dp_optimized.go`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Java: base didáctica preferida `2141_dp.java`; versión que cubre `2141_dp.java`; puestos tiempo/memoria 1/1, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `2141_dp.py`; versión que cubre `2141_dp_optimized.py`; puestos tiempo/memoria 8/1, registros de otros autores 22/22.

- Rust: base didáctica preferida `2141_dp.rs`; versión que cubre `2141_dp.rs`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2141_dp.cpp](2141_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.078 s | 140 KB | 11294922 |
| [2141_dp.go](2141_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.078 s | 1916 KB | 11294923 |
| [2141_dp.java](2141_dp.java) | Java 1.8 | dp | O(n) | AC | 0.109 s | 488 KB | 11309242 |
| [2141_dp.py](2141_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.156 s | 12300 KB | 11309243 |
| [2141_dp.rs](2141_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.031 s | 2136 KB | 11309244 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2141_dp_optimized.cpp](2141_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.031 s | 84 KB | 11308803 |
| [2141_dp_optimized.go](2141_dp_optimized.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 924 KB | 11308805 |
| [2141_dp_optimized.py](2141_dp_optimized.py) \* | Python 3.12 x64 | dp | O(N) | AC | 0.156 s | 1392 KB | 11308802 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
