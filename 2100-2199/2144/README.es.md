# 2144. Ordenar cajas cerradas en una sola fila ordenada

[Timus 2144](https://acm.timus.ru/problem.aspx?space=1&num=2144) · dificultad 221 · sorting

Problema original de Ivan Smirnov, del Concurso Escolar de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n cajas, cada una con una fila fija de tamaños de figuras que no se
puede reordenar ni invertir. Decidir si las cajas se pueden poner en
algún orden de modo que todos los tamaños juntos formen una fila no
decreciente. Los límites son 0.5 segundos y 256 MB.

## Entrada

n, 1 ≤ n ≤ 100, y luego para cada caja kᵢ, 1 ≤ kᵢ ≤ 100, y sus tamaños,
1 ≤ aᵢⱼ ≤ 10⁴.

## Salida

YES o NO.

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2 1 2
3 7 7 7
1 5
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
2
2 1 3
1 2
```

Salida:

```
NO
```

## Solución

Cada caja debe ser no decreciente por dentro. Después solo importan su
primer tamaño f y su último tamaño l, y un orden válido necesita que l de
cada caja sea a lo sumo f de la siguiente.

En cualquier orden válido los primeros tamaños no decrecen, porque
f ≤ l ≤ f de la caja siguiente. Entre las cajas con el mismo primer
tamaño f, todas menos la última tienen l ≤ f, es decir, l = f. Por eso
ordenar las cajas por (f, l) da un orden válido siempre que exista, y
basta comprobar los vecinos en ese orden. El trabajo es
O(Σ kᵢ + n log n).

En el primer ejemplo las cajas (1, 2), (5, 5) y (7, 7) encajan en ese
orden; en el segundo (1, 3) y (2, 2) se solapan.

## Soluciones optimizadas

Se leen en flujo los elementos de cada caja y se rechaza una inversión interna inmediatamente. Una caja válida solo necesita sus dos extremos. Empaquetarlos en un entero acotado permite obtener el orden lexicográfico de intervalos mediante ordenación numérica; se recuperan para la misma comprobación de vecinos de la prueba simple. Java evita objetos y comparadores con claves primitivas; Python evita toda la entrada y tuplas temporales.

- `2144_sorting_optimized.java`: 0.109 s / 2064 KB; base `2144_sorting.java`: 0.187 s / 6916 KB; cambio respecto a la base: tiempo -41.7%, memoria -70.2%.
- `2144_sorting_optimized.py`: 0.078 s / 420 KB; base `2144_sorting.py`: 0.093 s / 1040 KB; cambio respecto a la base: tiempo -16.1%, memoria -59.6%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `2144_sorting.cpp`; versión que cubre `2144_sorting.cpp`; puestos tiempo/memoria 1/6, registros de otros autores 100/100.

- Go: base didáctica preferida `2144_sorting.go`; versión que cubre `2144_sorting.go`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Java: base didáctica preferida `2144_sorting.java`; versión que cubre `2144_sorting_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `2144_sorting.py`; versión que cubre `2144_sorting_optimized.py`; puestos tiempo/memoria 7/2, registros de otros autores 66/66.

- Rust: base didáctica preferida `2144_sorting.rs`; versión que cubre `2144_sorting.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2144_sorting.cpp](2144_sorting.cpp) | G++ 13.2 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 168 KB | 11309245 |
| [2144_sorting.go](2144_sorting.go) | Go 1.14 x64 | sorting | O(sum k + n log n) | AC | 0.031 s | 1328 KB | 11294957 |
| [2144_sorting.java](2144_sorting.java) | Java 1.8 | sorting | O(sum k + n log n) | AC | 0.187 s | 6916 KB | 11309246 |
| [2144_sorting.py](2144_sorting.py) | Python 3.12 x64 | sorting | O(sum k + n log n) | AC | 0.093 s | 1040 KB | 11309247 |
| [2144_sorting.rs](2144_sorting.rs) | Rust 1.75 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 320 KB | 11309248 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2144_sorting_optimized.java](2144_sorting_optimized.java) | Java 1.8 | sorting | O(total sizes+N log N) | AC | 0.109 s | 2064 KB | 11308445 |
| [2144_sorting_optimized.py](2144_sorting_optimized.py) \* | Python 3.12 x64 | sorting | O(total sizes+N log N) | AC | 0.078 s | 420 KB | 11308442 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
