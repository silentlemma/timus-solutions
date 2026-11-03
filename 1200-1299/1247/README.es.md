# 1247. Ningún tramo pesa más que su longitud más N

[Timus 1247](https://acm.timus.ru/problem.aspx?space=1&num=1247) · dificultad 240 · bitmask, dp, prefix_sums

Problema original de Alexander Mironenko, del Concurso Individual de la Universidad Estatal de los Urales, 1 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan `S, N` positivos, ambos hasta 30000, y `S` enteros `0 ≤ A_i ≤ 100`, con la GARANTÍA `sum(A_i) = S + N`. Decide si todo segmento contiguo no vacío cumple `A_i + … + A_j ≤ (j − i + 1) + N`. Tiempo: 0,5 segundos. Memoria: 64 MB.

## Entrada

`S N`, seguidos de `S` líneas con un elemento por línea.

## Salida

Imprime `YES` en mayúsculas si todos los segmentos cumplen, o `NO` en otro caso.

## Evaluación

Tokens exactos. Cada fuente nueva tiene pruebas completas del entorno destino, comparaciones matemáticas independientes y Accepted propio ligado al hash; las bases conservan sus propias medidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
2
3
0
2
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
4 5
1
0
5
3
```

Salida:

```
NO
```

## Solución

Resta uno a cada valor y define `p_0 = 0`,
`p_i = sum(A_1 − 1, …, A_i − 1)`. La garantía da `p_S = N`.
La condición de un segmento pasa a ser `p_j − p_(i−1) ≤ N`.

Necesidad: cada prefijo es un segmento, luego `p_i ≤ N`; el sufijo que
queda también lo es, por lo que `N − p_i ≤ N` y `p_i ≥ 0`. Suficiencia:
si todos los prefijos están en `[0, N]`, toda diferencia de segmento
es como máximo `N − 0 = N`. Basta comprobar `0 ≤ p_i ≤ N` en flujo.
Un prefijo mayor que `N` ya infringe; uno negativo hace demasiado pesado
el sufijo restante. Se puede terminar con `NO` inmediatamente.
La equivalencia depende de la suma prometida, no de entradas arbitrarias.

Las cinco versiones `prefix_sums` son las bases sencillas preferidas:
tiempo `O(S)` y un solo prefijo, estado algorítmico `O(1)`. Rust retiene
además el texto de entrada. Se conservan intactas todas las fuentes
Accepted anteriores. Su Kadane general mantiene la suma máxima que
termina aquí, `ending = max(0, ending + A_i − 1)`, y compara el máximo
con `N`. También cuesta `O(S)` y no necesita la promesa sobre la suma.

## Soluciones optimizadas

Se conservan las alternativas DP antiguas y las cinco bases de prefijos en flujo; estas últimas son la referencia. La sumaS+N equivale a que cada p_i=sum(A_1..A_i)-i esté en[0,N]. C++ mantiene el algoritmo con búfer acotado de 4096 bytes y salida directa. Python usa iteradores en C: acumular sumas, restar posiciones y dividir hacia abajo porN+1. ParaN>0,p//(N+1)==0 equivale exactamente a 0<=p<=N, también para pnegativo. any detecta el primer cociente no nulo, sin bucle Python ni secuencia almacenada. O(S)tiempo/O(1)memoria de trabajo. Se compara Python con la base actual 0,109 s/328 KB, no con la DP antigua 1312 KB.

- `1247_prefix_sums_optimized.cpp`: 0.015 s / 64 KB; base `1247_prefix_sums.cpp`: 0.031 s / 104 KB; cambio respecto a la base: tiempo -51.6%, memoria -38.5%.
- `1247_prefix_sums_optimized.py`: 0.078 s / 416 KB; base `1247_prefix_sums.py`: 0.109 s / 328 KB; cambio respecto a la base: tiempo -28.4%, memoria +26.8%.

## Notas por lenguaje

Las instantáneas se guardaron el 2 y el 4 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1247_prefix_sums.cpp`; fuente que cubre `1247_prefix_sums_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 75/75.

- Go: base didáctica preferida `1247_prefix_sums.go`; fuente que cubre `1247_prefix_sums.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1247_prefix_sums.java`; fuente que cubre `1247_prefix_sums.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1247_prefix_sums.py`; fuente que cubre `1247_prefix_sums_optimized.py`; puestos tiempo/memoria 1/1, registros de otros autores 17/17.

- Rust: base didáctica preferida `1247_prefix_sums.rs`; fuente que cubre `1247_prefix_sums.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1247_prefix_sums.cpp](1247_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(S) | AC | 0.031 s | 104 KB | 11308243 |
| [1247_prefix_sums.go](1247_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(S) | AC | 0.046 s | 1316 KB | 11308245 |
| [1247_prefix_sums.java](1247_prefix_sums.java) | Java 1.8 | prefix_sums | O(S) | AC | 0.109 s | 444 KB | 11308247 |
| [1247_prefix_sums.py](1247_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(S) | AC | 0.109 s | 328 KB | 11308241 |
| [1247_prefix_sums.rs](1247_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(S) | AC | 0.031 s | 468 KB | 11308248 |

### Otros enfoques Accepted

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1247_dp.cpp](1247_dp.cpp) | G++ 13.2 x64 | dp | O(S) | AC | 0.031 s | 124 KB | 11283945 |
| [1247_dp.go](1247_dp.go) | Go 1.14 x64 | dp | O(S) | AC | 0.031 s | 1348 KB | 11283948 |
| [1247_dp.java](1247_dp.java) | Java 1.8 | dp | O(S) | AC | 0.109 s | 528 KB | 11283951 |
| [1247_dp.py](1247_dp.py) | Python 3.12 x64 | dp | O(S) | AC | 0.093 s | 1312 KB | 11283950 |
| [1247_dp.rs](1247_dp.rs) | Rust 1.75 x64 | dp | O(S) | AC | 0.062 s | 840 KB | 11283953 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1247_prefix_sums_optimized.cpp](1247_prefix_sums_optimized.cpp) | G++ 13.2 x64 | prefix_sums | O(S) time; O(1) working storage | AC | 0.015 s | 64 KB | 11309382 |
| [1247_prefix_sums_optimized.py](1247_prefix_sums_optimized.py) | Python 3.12 x64 | prefix_sums | O(S) time; O(1) working storage | AC | 0.078 s | 416 KB | 11309921 |
