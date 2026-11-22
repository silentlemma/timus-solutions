# 1009. Contar números en base K sin dos ceros seguidos

[Timus 1009](https://acm.timus.ru/problem.aspx?space=1&num=1009) · dificultad 95 · dp, combinatorics

Problema original del Campeonato de la Universidad Estatal de los Urales 1997.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuenta los números de `N` dígitos en base `K` (el primer dígito no es cero)
cuyos dígitos no contienen dos ceros seguidos. `2 ≤ K ≤ 10`, `N ≥ 2`,
`N + K ≤ 18`.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `K`, cada uno en su propia línea.

## Salida

La cantidad.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
10
```

Salida:

```
891
```

### Ejemplo 2

Entrada:

```
2
2
```

Salida:

```
2
```

## Solución

**Programación dinámica.** Se cuentan los prefijos válidos según su último
dígito: `zero` terminan en `0`, `other` en un dígito no nulo. Con un dígito,
`zero = 0` y `other = K - 1`. Al añadir un dígito:

- un cero solo puede ir tras un dígito no nulo: `zero' = other`;
- un dígito no nulo puede ir tras cualquiera:
  `other' = (zero + other) · (K - 1)`.

Tras `N` dígitos la respuesta es `zero + other`. Tiempo `O(N)`.

**Combinatoria.** Un número con `z` ceros los tiene entre las `N - 1`
posiciones posteriores a la primera, sin dos adyacentes: `C(N - z, z)` formas;
cada uno de los otros `N - z` dígitos toma uno de `K - 1` valores. La respuesta
es `Σ C(N - z, z) · (K - 1)^(N - z)` sobre `0 ≤ z ≤ N / 2`.

Detalles a tener en cuenta:

- la mayor respuesta, `1 434 392 064` (`N = 11`, `K = 7`), está cerca del
  límite de 32 bits, y los valores intermedios de una fórmula descuidada pueden
  desbordarse: usa enteros de 64 bits;
- con `K = 2` la respuesta es un número de Fibonacci, una comprobación útil.

## Soluciones optimizadas

`1009_math.py`. Añade función generadora exacta junto a DP y combinatoria didácticas. q=K−1,B=2^36: cuenta dada por 1/(1−qx−qx²), coeficiente N=floor(B^(N+2)/(B²−qB−q)) mod B. Para todo N≥2,K≥2,N+K≤18, f_j≤K^j y cola fraccional ≤K^(N+1)/(B−K)<1 impiden acarreo. Las 99 parejas contrastadas con conteo binomial independiente en ambos runtimes. Sin flotantes ni respuestas incrustadas. Una división de enteros O(N) bits, numerador hasta 649 bits, no costo constante para N ilimitado. CPython actual 0.062 s/684 KB separado de DP PyPy conservada 0.109 s/196 KB.

Fuente exacto: Python 3.12 x64 Accepted #11327875: 0.062 s / 684 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 10/175; 153/175. Admisión estricta usa solo tiempo bajo 1024 KB: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Conserva asterisco por la meta propia de primer puesto en ambas. La variante anterior conservada tiene su par propio #11324917 (PyPy 3.10 x64): 0.109 s / 196 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `1009_math.py`: 0.062 s / 684 KB; base didáctica conservada `1009_combinatorics.py` (Python 3.12 x64): 0.078 s / 404 KB.

`1009_dp_optimized.java`. Mantiene DP de dos estados, prefijos acabados en cero/no cero, con la misma transición y long. Lee ambos enteros con 128 bytes y después reutiliza ese arreglo para hasta diecinueve cifras y salto. Sin llamadas de entrada por carácter ni segundo arreglo de respuesta. O(N) tiempo DP, O(1) estado; conserva DP y combinatoria didácticas.

Accepted exacto Java 1.8 #11327757: 0.062 s / 292 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/401, memoria 2/401. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303698 era 0.093 s / 336 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1009_dp_optimized.java`: 0.062 s / 292 KB; base didáctica conservada `1009_dp.java`: 0.125 s / 1576 KB.

`1009_dp_optimized.go`. Go mantiene la DP de dos estados según la última cifra. La entrada por bytes y un búfer fijo de salida sustituyen el análisis y la impresión con fmt; solo se conservan los dos conteos del prefijo anterior. Se realizan O(N) actualizaciones de enteros acotados por el enunciado, con O(1) espacio auxiliar.

Frente a `1009_dp.go`: tiempo 0.031 s → 0.015 s; memoria 1104 KB → 796 KB.

`1009_dp.py`. El nuevo código de Python usa DP por cifras en lugar de la suma combinatoria. Sean z y q los conteos de prefijos terminados en cero y en otra cifra. Se empieza con (z,q)=(0,K-1), excluyendo el cero inicial, y se actualiza (z,q)=(q,(z+q)(K-1)). Un cero solo puede seguir a una cifra no nula, mientras que cualquier prefijo tiene K-1 extensiones no nulas. Así se cuentan exactamente las cadenas válidas en O(N) actualizaciones y O(1) posiciones enteras auxiliares. Se conserva por separado la versión combinatoria didáctica.

Frente a `1009_combinatorics.py`: tiempo 0.078 s → 0.109 s; memoria 404 KB → 196 KB.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: la DP de dos estados.
- **C++** y **Python** tienen además la suma cerrada; `math.comb` de Python
  calcula los coeficientes binomiales de forma exacta.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1009_combinatorics.cpp](1009_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N^2) | AC | 0.001 s | 128 KB | 11277725 |
| [1009_combinatorics.py](1009_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N^2) | AC | 0.078 s | 404 KB | 11277735 |
| [1009_dp.cpp](1009_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB | 11277718 |
| [1009_dp.go](1009_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1104 KB | 11277734 |
| [1009_dp.java](1009_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1576 KB | 11277739 |
| [1009_dp.rs](1009_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 216 KB | 11277743 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1009_dp_optimized.java](1009_dp_optimized.java) \* | Java 1.8 | dp | O(N) DP time; O(1) state | AC | 0.062 s | 292 KB | 11327757 |
| [1009_dp_optimized.go](1009_dp_optimized.go) | Go 1.14 x64 | dp | O(N) | AC | 0.015 s | 796 KB | 11328257 |
| [1009_dp.py](1009_dp.py) \* | PyPy 3.10 x64 | dp | O(N) | AC | 0.109 s | 196 KB | 11324917 |
| [1009_math.py](1009_math.py) \* | Python 3.12 x64 | math | One O(N)-bit integer division; O(N) bits | AC | 0.062 s | 684 KB | 11327875 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
