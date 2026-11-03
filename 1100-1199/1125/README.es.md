# 1125. Deshacer cambios de color a distancias enteras en una cuadrícula

[Timus 1125](https://acm.timus.ru/problem.aspx?space=1&num=1125) · dificultad 236 · bitmask

Problema original de Dmitry Filimonenkov, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un campo de `M × N` celdas unitarias (`0 ≤ M, N ≤ 50`) está pintado de
negro (`B`) y blanco (`W`). Cada vez que se visita una celda, cambian de
color todas las celdas cuyo centro está a distancia entera de su centro,
incluida la propia celda visitada (distancia 0). Dados los colores
finales y cuántas veces se visitó cada celda (hasta `2·10^9`), imprime los
colores iniciales.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

`M N`, luego `M` líneas con los colores finales y luego `M` líneas de `N`
números de visitas.

## Salida

`M` líneas con los colores iniciales.

## Evaluación

Se comparan los tokens de las filas. Python de simulación y Python
nuevo de máscaras fueron comprobados cada uno en 5748 campos contra
enumeración independiente de parejas con distancias enteras exactas,
sin máscaras ni ejes agrupados. Incluye colores/paridades exhaustivos
en 2×2 y 2×3, todas las paridades con dos colores finales uniformes en
3×3, vacíos/estrechos, aleatorios, 50×50 con visitas pares/impares/aleatorias
y visitas impares individuales.

Cada uno de los ocho programas añadidos (cinco simulaciones y tres máscaras
nuevas) pasó 11 entradas del repositorio y 78 ejecuciones extra reales
en Docker, con su Accepted de fuente exacta. Sus salidas/códigos guardados
se revalidan contra parejas recalculadas, vinculados a SHA. Las 5748
ejecuciones corresponden a Python, no a cada fuente nativa. Cuatro entradas
de estrés CPython de simulación alcanzaron 0,0687 s CPU y 17288 KB RSS,
dentro de 0,25 s/64 MB; las métricas del juez se mantienen separadas.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 6
BWBBWW
BWBBWB
BBWWBW
BBBBBW
BBWWWW
BBWBBW
2 0 12 46 2 0
3 0 0 0 0 200
4 2 1 1 4 2
4 2 1 1 4 4
0 0 0 0 0 0
2 56 24 4 2 2
```

Salida:

```
WWBBWW
WBWWBW
WBBBBW
WBWWBW
WBWWBW
WBWWBW
```

## Solución

La base didáctica preferida simula los cambios directamente. Un cambio
es XOR con uno: dos se anulan y el orden no importa, por lo que basta
la paridad de cada visita. Se generan todos los desplazamientos con signo
`(dr,dc)` posibles cuya longitud al cuadrado es un cuadrado perfecto,
incluido `(0,0)`. Por cada origen con visitas impares, se cambia cada
destino válido en esos desplazamientos.

Cada pareja a distancia entera tiene exactamente uno de ellos y aporta
una vez. Aplicar los mismos cambios a los colores finales recupera los
iniciales, pues cambiar color es su propia inversa. Con lados hasta 50,
`K≤405`: generación `O((M+N)²)` pruebas elementales, simulación `O(MNK)`
y espacio `O(MN+K)`. Los cinco programas nuevos usan celdas y coordenadas,
sin desplazar máscaras de filas, y cada uno tiene su propio Accepted.

La distancia cero cuenta. Hasta dos mil millones de visitas caben en
32 bits con signo y solo importa la paridad. Con una dimensión cero se
imprimen `M` líneas vacías. Todas las implementaciones anteriores se conservan.

## Soluciones optimizadas

Cambiar color es XOR con uno: dos cambios se anulan y el orden no
importa. Conservamos solo la paridad de visitas. Sea `R[r]` la máscara de
visitas impares de la fila `r`. Para cada desplazamiento `(dr,dc)` con
`dr²+dc²` cuadrado perfecto, desplazamos la fila fuente y hacemos XOR.
Recortamos a los `N` bits inferiores. Cada pareja fuente-destino aparece
una vez, y deshacer un cambio es el mismo cambio: aplicar esa paridad
a los colores finales recupera los iniciales.

Las cinco fuentes Accepted anteriores enumeran todos los desplazamientos
con signo, incluido `(0,0)`: 405 en 50×50; un campo menor usa un subconjunto.
Con `K` desplazamientos, tiempo `O(MN+MK)` operaciones de máscaras, incluidos
entrada, salida y generación. `N≤50` cabe en un word nativo de 64 bits;
Python usa enteros grandes y paga sus bloques en cada desplazamiento/XOR.
Los datos nativos ocupan `O(MN+M+K)` words/caracteres; Python original
también guarda todos los tokens y enteros, `O(MN+M+K)` objetos.
Se conservan las cinco fuentes.

La distancia cero cuenta. Hasta dos mil millones de visitas caben en
enteros con signo de 32 bits; solo hace falta su bit bajo. Si alguna
dimensión es cero, se imprimen `M` líneas vacías.

Los tres nuevos programas mantienen el algoritmo de paridad y máscaras,
por eso usan `_optimized`. Agrupan ejes y los cuatro signos de cada
desplazamiento positivo. Sea `C` el XOR de todas las filas y `F` los `N`
bits bajos encendidos. Los orígenes en la misma fila aportan `F` si
`popcount(R[r])` es impar; los de la misma columna aportan `C`. El origen
se cuenta dos veces: otro XOR con `R[r]` restaura su contribución única.

Para cada `dr>0,dc>0` de longitud entera, tomamos
`T = R[r−dr] XOR R[r+dr]`, considerando cero una fila fuera del campo,
y aplicamos `(T<<dc) XOR (T>>dc)`. Incluye una vez los cuatro signos,
sin ejes ni origen. Al final se retienen las columnas del campo. Hay
hasta `P=52` parejas positivas en vez de 405 desplazamientos con signo.
Tiempo `O(MN+MP)` operaciones de máscaras. Se guardan colores, máscaras
y `P` parejas; C++/Java añaden una tabla fija de 5000 cuadrados, Python
un conjunto de `O(M+N)` cuadrados. Sus enteros intermedios pueden alcanzar
`2N−1` bits, sin suponer un word único. Los desplazamientos nativos son
menores de 64; descartar bits superiores no afecta los `N` bajos.
Java utiliza `>>>` lógico.

## Notas por lenguaje

Los cinco nuevos `simulation` son las bases sencillas preferidas;
toda comparación actual usa la simulación del mismo lenguaje. Ambos
Python de máscaras registran 0,046 frente a 0,093 s, 50,5% menos tiempo.
El anterior usa 900/564 KB, 59,6% más memoria; el agrupado 580/564 KB,
2,8% más. Se admiten por tiempo con el coste de memoria explícito.

C++ agrupado usa 132/136 KB, solo 2,9% menos, y Java 424/536 KB, solo
20,9% menos, con tiempos iguales en cada pareja. Figuran como alternativas
Accepted. Sus nombres `_optimized` identifican las parejas conservadas
del algoritmo original de máscaras, donde sí redujeron memoria 71,1%
y 56,2%. Son comparaciones históricas, no porcentajes frente a la actual
simulación. No se borran, renombran ni duplican fuentes, y el nombre no
otorga admisión actual.

Instantánea del 2 de noviembre de 2026: simulación C++ 1/1 frente a
55 entradas filtradas de otros autores, Java 1/1 frente a una, Python
agrupado 1/1 frente a ocho. Python anterior es 1/3 y mantiene asterisco
aunque el otro alcance la meta. Go/Rust tienen muestras vacías, solo
cobertura formal. C++ exige el 15% superior o primeros diez en ambas
métricas; otras familias primero en ambas. Todas tienen una fuente válida.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1125_simulation.cpp](1125_simulation.cpp) | G++ 13.2 x64 | simulation | O(MNK+(M+N)²), K ≤ 405 | AC | 0.001 s | 136 KB | 11308651 |
| [1125_simulation.go](1125_simulation.go) | Go 1.14 x64 | simulation | O(MNK+(M+N)²), K ≤ 405 | AC | 0.015 s | 1144 KB | 11308665 |
| [1125_simulation.java](1125_simulation.java) | Java 1.8 | simulation | O(MNK+(M+N)²), K ≤ 405 | AC | 0.093 s | 536 KB | 11308659 |
| [1125_simulation.py](1125_simulation.py) | Python 3.12 x64 | simulation | O(MNK+(M+N)²), K ≤ 405 | AC | 0.093 s | 564 KB | 11308679 |
| [1125_simulation.rs](1125_simulation.rs) | Rust 1.75 x64 | simulation | O(MNK+(M+N)²), K ≤ 405 | AC | 0.015 s | 200 KB | 11308669 |

### Otros enfoques Accepted

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1125_bitmask.cpp](1125_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(MN+MK), K ≤ 405 | AC | 0.001 s | 456 KB | 11279311 |
| [1125_bitmask.go](1125_bitmask.go) | Go 1.14 x64 | bitmask | O(MN+MK), K ≤ 405 | AC | 0.031 s | 1092 KB | 11279315 |
| [1125_bitmask.java](1125_bitmask.java) | Java 1.8 | bitmask | O(MN+MK), K ≤ 405 | AC | 0.078 s | 968 KB | 11279320 |
| [1125_bitmask.rs](1125_bitmask.rs) | Rust 1.75 x64 | bitmask | O(MN+MK), K ≤ 405 | AC | 0.015 s | 240 KB | 11279322 |

### Optimizadas

**Mejoras actuales frente a la simulación preferida**

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1125_bitmask.py](1125_bitmask.py) \* | Python 3.12 x64 | bitmask | O(MN+MK), K ≤ 405 | AC | 0.046 s | 900 KB | 11279316 |
| [1125_bitmask_optimized.py](1125_bitmask_optimized.py) | Python 3.12 x64 | bitmask | O(MN+MP), P ≤ 52 | AC | 0.046 s | 580 KB | 11308647 |

**Mejoras históricas del par de máscaras; sin cumplir el30% frente a la simulación actual**

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1125_bitmask_optimized.cpp](1125_bitmask_optimized.cpp) | G++ 13.2 x64 | bitmask | O(MN+MP), P ≤ 52 | AC | 0.001 s | 132 KB | 11308644 |
| [1125_bitmask_optimized.java](1125_bitmask_optimized.java) | Java 1.8 | bitmask | O(MN+MP), P ≤ 52 | AC | 0.093 s | 424 KB | 11308646 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
