# 1031. El conjunto más barato de billetes de tren con tres tarifas

[Timus 1031](https://acm.timus.ru/problem.aspx?space=1&num=1031) · dificultad 392 · dp, two_pointers

Problema original del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` estaciones (`2 ≤ N ≤ 10 000`) están sobre una línea; la estación 1 está
a distancia 0 y las demás a distancias crecientes dadas (como mucho `10^9`, y
estaciones vecinas a como mucho `L3`). Un billete cubre un viaje entre dos
estaciones a distancia `X`: cuesta `C1` si `X ≤ L1`, `C2` si `L1 < X ≤ L2`,
`C3` si `L2 < X ≤ L3`, y los viajes más largos requieren varios billetes,
cambiando en estaciones (`1 ≤ L1 < L2 < L3 ≤ 10^9`,
`1 ≤ C1 < C2 < C3 ≤ 10^9`). Encuentra la forma más barata de viajar entre dos
estaciones dadas; la respuesta no supera `10^9`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`L1 L2 L3 C1 C2 C3`, luego `N` y dos números de estación distintos
en `1..N` (en cualquier orden). Las siguientes `N - 1` líneas dan
distancias enteras positivas y distintas desde la estación 1 hasta
las estaciones 2..`N`, en orden creciente.

## Salida

El menor precio total.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 6 8 20 30 40
7
2 6
3
5
9
12
17
19
```

Salida:

```
70
```

### Ejemplo 2

Entrada:

```
1 2 3 1 2 3
2
2 1
1
```

Salida:

```
1
```

## Solución

Se intercambian las estaciones para que `a < b`; ir hacia atrás nunca
ayuda. Sea `cost[i]` la forma más barata de ir de `a` a la estación `i`,
con `cost[a] = 0`; el último billete va de alguna estación `j` a `i` y cuesta
la tarifa de la distancia `x[i] - x[j]`.

**DP cuadrática.** Se prueban todas las `j` con `x[i] - x[j] ≤ L3`. Son hasta
`N^2 / 2 = 5·10^7` pasos cuando un billete llega lejos: suficiente en C++,
no en Python.

**Tres punteros.** `cost` nunca decrece a lo largo de la línea: un camino a
la estación `i + 1` termina con un billete desde alguna `j`, y el billete de
`j` a `i` no es más largo, así que no es más caro. Por tanto, para un billete
de la tarifa `k` el mejor origen es la estación **más lejana** `j` con
`x[i] - x[j] ≤ Lk`: tiene el menor `cost` entre todos los orígenes que
alcanza esa tarifa. Al crecer `i`, esos orígenes más lejanos solo avanzan,
así que se guarda un puntero por tarifa y se adelanta mientras la distancia
supere `Lk`. Cada paso prueba tres candidatos: `O(N)` en total.

Ambas DP guardan `O(N)` posiciones y costes; los tres punteros añaden
solo estado constante. Las bases Python y Rust también guardan toda
la entrada, `O(I)`, siendo `I` su longitud. Python optimizado usa arreglos
compactos `O(N)` y bloques acotados. Rust optimizado conserva solo
`K = b - a + 1` posiciones/costes: `O(K)`. Go optimizado reserva arreglos
para el límite de 10000 estaciones; su capacidad es lineal en ese límite,
no constante con independencia de él.

Detalles a tener en cuenta:

- las estaciones pueden venir en orden decreciente;
- un billete de una tarifa barata sirve para cualquier viaje más corto, así
  que un viaje de longitud `X ≤ L1` cuesta `C1`, no `C3`;
- la respuesta cabe en 32 bits, pero usa enteros de 64 bits para las sumas.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

Go y Rust mantienen un puntero móvil por tarifa a la primera estación que queda dentro de su alcance. El coste mínimo hasta cada estación no decrece, así que ese puntero da el predecesor más barato para la tarifa. Ambas versiones leen las posiciones en orden y guardan solo el tramo entre los dos extremos. Las posiciones y los costes caben en enteros de 32 bits. Go usa vectores fijos para hasta 10000 estaciones y entrada y salida directa de bytes.

Las bases C++ de tres punteros y Java cubren también el conjunto rápido
sin duplicados. Los [criterios compartidos](../../RATING_CRITERIA.md)
comparan solo tiempo para sus mediciones inferiores a 1 MiB. Python simple
permanece didáctico: sus 1684 KB superan el umbral de memoria de la muestra
pequeña en caché. Python optimizado, de 896 KB, cumple solo por tiempo;
su fuente independiente cubre el conjunto rápido de Python.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1031_dp_two_pointers_optimized.py`. Las posiciones y costes se guardan en arreglos de 64 bits sin signo en vez de listas de enteros Python. Los elementos de 64 bits dejan margen aritmético; las coordenadas válidas siguen limitadas a `10^9`. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328768 (Python 3.12 x64): **0.078 s / 896 KB**. Comparación archivada: `1031_dp_two_pointers.py` (Python 3.12 x64) — 0.078 s / 1684 KB (#11278428).

`1031_dp_two_pointers_optimized.py`: la revisión actual nombra el umbral ASCII de espacio sin cambiarlo.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- **C++**, **Go**, **Python**, **Java**, **Rust**: tres punteros.
- **C++** tiene además la DP cuadrática.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1031_dp.cpp](1031_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.078 s | 284 KB | 11278426 |
| [1031_dp_two_pointers.cpp](1031_dp_two_pointers.cpp) | G++ 13.2 x64 | dp, two_pointers | O(N) | AC | 0.015 s | 280 KB | 11278425 |
| [1031_dp_two_pointers.go](1031_dp_two_pointers.go) | Go 1.14 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 1440 KB | 11278427 |
| [1031_dp_two_pointers.java](1031_dp_two_pointers.java) | Java 1.8 | dp, two_pointers | O(N) | AC | 0.093 s | 668 KB | 11278429 |
| [1031_dp_two_pointers.py](1031_dp_two_pointers.py) | Python 3.12 x64 | dp, two_pointers | O(N) | AC | 0.078 s | 1684 KB | 11278428 |
| [1031_dp_two_pointers.rs](1031_dp_two_pointers.rs) | Rust 1.75 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 516 KB | 11278430 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1031_dp_two_pointers_optimized.go](1031_dp_two_pointers_optimized.go) | Go 1.14 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 884 KB | 11311110 |
| [1031_dp_two_pointers_optimized.rs](1031_dp_two_pointers_optimized.rs) | Rust 1.75 x64 | dp, two_pointers | O(N) | AC | 0.031 s | 276 KB | 11310607 |
| [1031_dp_two_pointers_optimized.py](1031_dp_two_pointers_optimized.py) | Python 3.12 x64 | dp, two_pointers | O(N) | AC | 0.093 s | 928 KB | 11331076 |
