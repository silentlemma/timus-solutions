# 1869. Crucero de Año Nuevo

[Timus 1869](https://acm.timus.ru/problem.aspx?space=1&num=1869) · dificultad 239 · prefix_sums, simulation

Problema original de Denis Dublennykh, del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tren va de Vladivostok (estación 1) a Moscú (estación n) parando en
las estaciones 1, …, n, y luego vuelve por el mismo camino. aᵢⱼ
personas compraron billete de la estación i a la j: viajan en el tren
de ida si i < j y en el de vuelta si i > j. Cada vagón tiene 36
asientos. ¿Cuántos vagones necesita el tren para que todos tengan
asiento?

## Entrada

n (2 ≤ n ≤ 100), luego la matriz n × n de aᵢⱼ (0 ≤ aᵢⱼ ≤ 1000,
aᵢᵢ = 0).

## Salida

El menor número de vagones.

## Evaluación

Tokens exactos. Cada fuente nueva tiene pruebas completas del entorno destino, comparaciones matemáticas independientes y Accepted propio ligado al hash; las bases conservan sus propias medidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 180 180
0 0 180
360 0 0
```

Salida:

```
10
```

## Solución

El tren debe llevar el mayor número de personas a bordo a la vez, en
cualquier tramo y en cualquier sentido. Para cada sentido se suma aᵢⱼ
en la estación de menor número y se resta en la de mayor número. La suma acumulada de
estos cambios por orden de estación es la carga de cada tramo. La
respuesta es la mayor carga dividida entre 36 y redondeada hacia
arriba. `O(n²)`.

En el ejemplo viajan 360 personas en el tren de ida en ambos tramos
(los 180 de la estación 1 a la 3 junto con los 180 de la 1 a la 2 o de
la 2 a la 3), y 360 vuelven todo el camino: 10 vagones.

Trampas:

- los dos sentidos son viajes distintos, así que sus cargas no se
  suman;
- la división redondea hacia arriba: 37 personas necesitan dos vagones;
- sin ningún billete la respuesta es 0.

Las respuestas coinciden con una implementación aceptada independiente
en 150 matrices aleatorias.

## Soluciones optimizadas

`1869_prefix_sums_optimized.go`. Acumula diferencias de subida/bajada por dirección al leer la matriz, calcula prefijos y redondea el pico mayor hacia arriba entre 36. Go conserva el algoritmo O(n²), sustituye lectura formateada por búfer fijo y elimina centinelas sin usar. Rust tarda O(n²) frente a la simulación directa O(n³) conservada; también queda el prefijo original, por eso el nuevo se llama prefix_sums_optimized. No retienen matriz ni texto completo; usan O(n) cargas de 64 bits con signo. n<=100 y entradas<=1000 garantizan sumas seguras; demanda cero da cero vagones.

Frente a `1869_prefix_sums.go`: tiempo 0.031 s → 0.015 s; memoria 1244 KB → 808 KB.

`1869_prefix_sums_optimized.rs`. Acumula diferencias de subida/bajada por dirección al leer la matriz, calcula prefijos y redondea el pico mayor hacia arriba entre 36. Go conserva el algoritmo O(n²), sustituye lectura formateada por búfer fijo y elimina centinelas sin usar. Rust tarda O(n²) frente a la simulación directa O(n³) conservada; también queda el prefijo original, por eso el nuevo se llama prefix_sums_optimized. No retienen matriz ni texto completo; usan O(n) cargas de 64 bits con signo. n<=100 y entradas<=1000 garantizan sumas seguras; demanda cero da cero vagones.

Frente a `1869_simulation.rs`: tiempo 0.046 s → 0.015 s; memoria 320 KB → 64 KB.

Las cinco simulaciones directas suman cada billete en todos los tramos que recorre, con tiempo O(N³) y espacio O(N). Se usan como bases educativas junto con las soluciones matriciales originales. Python optimizado lee una fila por estación. Los sufijos derechos aportan a los tramos de ida y los prefijos izquierdos a los de vuelta. Cada vector se empaqueta en un entero con campos de 32 bits. Desplazar un campo y dividir por 2^32−1 calcula los sufijos y la multiplicación por un número de unos en esa base, con truncamiento, calcula los prefijos. Cada campo vale como máximo 1000N² y no hay acarreo entre campos. La respuesta es la carga máxima en ambos sentidos dividida por 36, redondeando hacia arriba. El tiempo es O(N²) y el espacio de trabajo O(N). La versión tarda menos y usa más memoria que la simulación directa.

- `1869_prefix_sums_optimized.py`: 0.062 s / 468 KB; base `1869_simulation.py`: 0.093 s / 396 KB; cambio respecto a la base: tiempo -33.3%, memoria +18.2%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1869_prefix_sums_optimized.go`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

`1869_prefix_sums_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1869_simulation.cpp](1869_simulation.cpp) | G++ 13.2 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.015 s | 108 KB | 11308691 |
| [1869_simulation.go](1869_simulation.go) | Go 1.14 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.015 s | 1228 KB | 11308696 |
| [1869_simulation.java](1869_simulation.java) | Java 1.8 | simulation | O(N^3) time; O(N) working loads | AC | 0.093 s | 388 KB | 11308693 |
| [1869_simulation.py](1869_simulation.py) | Python 3.12 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.093 s | 396 KB | 11308701 |
| [1869_simulation.rs](1869_simulation.rs) | Rust 1.75 x64 | simulation | O(N^3) time; O(N) working loads | AC | 0.046 s | 320 KB | 11308699 |

### Otros enfoques Accepted

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1869_prefix_sums.cpp](1869_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 180 KB | 11309204 |
| [1869_prefix_sums.go](1869_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(n^2) | AC | 0.031 s | 1244 KB | 11290934 |
| [1869_prefix_sums.java](1869_prefix_sums.java) | Java 1.8 | prefix_sums | O(n^2) | AC | 0.093 s | 444 KB | 11309206 |
| [1869_prefix_sums.py](1869_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(n^2) | AC | 0.078 s | 1324 KB | 11309207 |
| [1869_prefix_sums.rs](1869_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 336 KB | 11309208 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1869_prefix_sums_optimized.py](1869_prefix_sums_optimized.py) | Python 3.12 x64 | prefix_sums | O(N^2) time, O(N) working space | AC | 0.062 s | 468 KB | 11310099 |
| [1869_prefix_sums_optimized.go](1869_prefix_sums_optimized.go) \* | Go 1.14 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 808 KB | 11325129 |
| [1869_prefix_sums_optimized.rs](1869_prefix_sums_optimized.rs) \* | Rust 1.75 x64 | prefix_sums | O(n^2) | AC | 0.015 s | 64 KB | 11325130 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
