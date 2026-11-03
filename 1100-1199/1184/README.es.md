# 1184. Los trozos iguales más largos en que se pueden cortar los cables

[Timus 1184](https://acm.timus.ru/problem.aspx?space=1&num=1184) · dificultad 244 · binary_search

Problema original de Vladimir Pinaev y Roman Elizarov, del concurso regional ACM ICPC del noreste de Europa 2001–2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados N cables, corta al menos K piezas de una misma longitud entera
en centímetros y maximízala. Cada pieza sale de un solo cable, sin unir
sobrantes. `1≤N,K≤10000`; cada cable mide entre 1 m y 100 km, inclusive,
con precisión de un centímetro. Límites: 1 segundo y 64 MB.

## Entrada

La primera línea contiene N y K; las siguientes N líneas dan una
longitud en metros cada una, con exactamente dos cifras decimales.

## Salida

Imprime la mayor longitud factible en metros con exactamente dos
decimales. Si ninguna longitud entera positiva en centímetros permite K
piezas, imprime `0.00`.

## Evaluación

Se compara el único token decimal, con exactamente dos cifras
fraccionarias. Cada programa nuevo pasó 13 entradas del repositorio y 39
extra independientes en su compilador/intérprete real. Se releyeron las
156 salidas extra y códigos contra un oráculo racional exacto: fusionar
las secuencias decrecientes `c/1,c/2,...`, tomar el valor K-ésimo mayor y
redondearlo hacia abajo a centímetros, sin binaria de factibilidad. Python
también ejecutó 2889 stocks anfitriones; los pequeños probaron cada longitud
entera. Se cubren 1,13 m, cero, N/K=10000, suma 10¹¹, longitud máxima,
signos más y conversión solo después del mínimo de 64 bits. Las 2889 son
ejecuciones Python, no nativas. Las cuatro fuentes tienen Accepted exacto.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 11
8.02
7.43
4.57
5.39
```

Salida:

```
2.00
```

## Solución

Lee cada longitud como centímetros enteros c. Con dos decimales,
quitar el punto es exacto; convertir a coma flotante binaria y multiplicar
por 100 puede fallar. El rango es `100≤c≤10⁷`.

Para L positiva, un cable aporta `floor(c/L)` piezas. La suma
`F(L)=Σ floor(c/L)` no crece, así que `F(L)≥K` es monótona. Las bases
buscan por binaria la mayor L entera entre cero y el cable más largo.
Cero es un centinela sin respuesta positiva, nunca divisor. El punto medio
superior es positivo si la búsqueda itera, incluso con límite inferior cero.

Si L es factible, todas las longitudes positivas menores también; si falla,
todas las mayores fallan. Conservar el lado inferior factible y descartar
lo imposible deja el máximo al terminar. Se imprime `L/100` y el resto con
dos dígitos, incluido cero inicial. Tiempo `O(N log C)` y espacio `O(N)`,
`C=max(c)≤10⁷`, contando tokens retenidos. Puede salir cero aunque cada
cable original mida al menos un metro.

## Soluciones optimizadas

Los `_optimized` conservan la misma binaria entera exacta con límites
demostrados más estrechos y representaciones compactas. Sea M el máximo,
S la suma. El cable mayor por sí solo da K piezas de `floor(M/K)`, así
que `low=M/K` es factible si es positivo; cero conserva su interpretación
de centinela. Toda L factible cumple `L≤M` y `K·L≤S`, luego
`high=min(M,floor(S/K))`. No se descarta el óptimo.

Mientras low<high, `mid=(low+high+1)/2` es positivo incluso con low=0.
Se deja de contar piezas al llegar a K: los términos restantes son no
negativos y el predicado no cambia. A menudo reduce trabajo, manteniendo
el peor `O(N log C)`. Longitudes y límites caben en 32 bits. S alcanza
`10¹¹`, por lo que los nativos la acumulan en 64 bits, igual que la cuenta
de piezas. Hay que minimizar `S/K` con M en 64 bits antes de convertir a
32. La regresión `S/K=2³²+100` detecta convertir antes del mínimo.

C++ y Java leen búferes de bytes acotados hacia arrays de 32 bits,
saltando el punto decimal. Java evita strings de entrada completa, long[]
y formato regional. Rust usa lectura acotada y Vec<u32>, sin string
completo ni reemplazos por token. CPython lee cada línea prescrita en
`array('I')`, sin retener todos los tokens ni una lista de enteros objeto.
Búferes acotados y almacenamiento lineal; las cinco bases quedan idénticas.

Memoria Accepted exacta: C++ 168 frente a 280 KB (40,0% menos), Java 448
frente a 6284 KB (92,9% menos), Python 516 frente a 1580 KB (67,3% menos),
Rust 220 frente a 420 KB (47,6% menos). C++ 0,031→0,015 s difiere solo
en una unidad del reloj: no se admite por tiempo solamente. Java
0,125→0,093 s; Python sigue en 0,078 s y Rust en 0,015 s. Los cuatro
cumplen por memoria medida, independientemente del ruido temporal.

## Notas por lenguaje

Las cinco versiones anteriores conservan su búsqueda directa. El nuevo
Python fue aceptado en CPython 3.12, sin sustituir métricas de PyPy.
C++, Java y Rust cumplen el objetivo actual. Python es segundo en tiempo
y primero en memoria en la muestra filtrada: conserva asterisco y margen
de mejora. Go no tiene autores ajenos elegibles: cobertura formal, no
superioridad demostrada. C++ exige 15% superior o primeros diez lugares
en ambas métricas; las otras familias, primero en ambas. Cada mejora de
memoria compara con su propia base Accepted sencilla e intacta del lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1184_binary_search.cpp](1184_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(N log C) | AC | 0.031 s | 280 KB | 11283357 |
| [1184_binary_search.go](1184_binary_search.go) | Go 1.14 x64 | binary_search | O(N log C) | AC | 0.031 s | 1688 KB | 11283358 |
| [1184_binary_search.java](1184_binary_search.java) | Java 1.8 | binary_search | O(N log C) | AC | 0.125 s | 6284 KB | 11283361 |
| [1184_binary_search.py](1184_binary_search.py) | Python 3.12 x64 | binary_search | O(N log C) | AC | 0.078 s | 1580 KB | 11283360 |
| [1184_binary_search.rs](1184_binary_search.rs) | Rust 1.75 x64 | binary_search | O(N log C) | AC | 0.015 s | 420 KB | 11283363 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1184_binary_search_optimized.cpp](1184_binary_search_optimized.cpp) | G++ 13.2 x64 | binary_search | O(N log C) | AC | 0.015 s | 168 KB | 11308739 |
| [1184_binary_search_optimized.java](1184_binary_search_optimized.java) | Java 1.8 | binary_search | O(N log C) | AC | 0.093 s | 448 KB | 11308743 |
| [1184_binary_search_optimized.py](1184_binary_search_optimized.py) \* | Python 3.12 x64 | binary_search | O(N log C) | AC | 0.078 s | 516 KB | 11308745 |
| [1184_binary_search_optimized.rs](1184_binary_search_optimized.rs) | Rust 1.75 x64 | binary_search | O(N log C) | AC | 0.015 s | 220 KB | 11308751 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
