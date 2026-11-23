# 1783. Carrera nuclear

[Timus 1783](https://acm.timus.ru/problem.aspx?space=1&num=1783) · dificultad 473 · simulation

Problema original de Pavel Atnashev, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un país planea tener exactamente aᵢ cabezas nucleares al final del mes
i. Su rival empieza sin ninguna y, al comienzo del mes i, conociendo
los planes aᵢ, …, aᵢ₊ₘ₋₁, elige el menor cambio entero xᵢ tal que
cambiar sus existencias en xᵢ cada uno de los m meses siguientes las
mantendría al nivel del plan o por encima al final de cada uno. Solo se
hace el cambio de ese mes; al mes siguiente se vuelve a elegir.
Imprimir x₁, …, xₙ.

## Entrada

n y m (1 ≤ n ≤ 10000, 1 ≤ m ≤ 50) y luego a₁, …, aₙ₊ₘ₋₁
(0 ≤ aᵢ ≤ 10⁵).

## Salida

x₁, …, xₙ.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
0 0 4 2 1 0
```

Salida:

```
2 1 1 -1
```

## Solución

Con existencias s al comienzo del mes i, tras t meses del mismo cambio
x las existencias son s + t·x, que debe ser al menos aᵢ₊ₜ₋₁. Así que x es
el mayor de ⌈(aᵢ₊ₜ₋₁ − s)/t⌉ para t = 1…m. Después las existencias crecen
en x y el mes siguiente se repite. El redondeo debe ser hacia arriba
también con números negativos, donde la división entera de muchos
lenguajes redondea hacia cero. `O(n·m)`.

En el ejemplo la primera orden debe llegar a 4 en tres meses: 2. Con 2
en existencias, los planes siguientes 0, 4, 2 piden ⌈2/2⌉ = 1; luego,
con 3, los planes 4, 2, 1 piden 1; y con 4 los planes 2, 1, 0 permiten
−1.

Trampas:

- las órdenes pueden ser negativas cuando los planes bajan;
- ⌈−3/2⌉ es −1, no −2 ni 0, así que la división debe redondear hacia
  arriba de forma explícita;
- cada vez solo se lleva a cabo el primero de los meses planeados.

Las respuestas coinciden con una implementación aceptada independiente
en 60 casos aleatorios, desde unos pocos meses hasta 10000 meses de
planes aleatorios, ondulados y con picos raros.

## Soluciones optimizadas

Revisiones Accepted solo de formato: `1783_simulation.java` #11327472, `1783_simulation.cpp` #11327473, `1783_simulation.py` #11327474, `1783_simulation.rs` #11327475. Cada fila usa esa revisión exacta y su propio par tiempo/memoria; no se atribuye una mejora de rendimiento al formato.

`1783_simulation_optimized.cpp`. Conserva el máximo exacto de techos con signo sobre el mismo anillo de hasta 50 planes futuros. Solo divide delta/t si delta>best*t: para best entero equivale a ceil(delta/t)>best, incluso con delta negativo. Usa (delta+t-1)/t para no negativos y truncamiento hacia cero para negativos. Planes y existencias en 0..100000, t<=50: best*t cabe en int con signo. Búferes de entrada/salida de 16 KiB, mismo algoritmo O(nm) y espacio de planes O(m).

Accepted exacto G++ 13.2 x64 #11326998: 0.015 s / 104 KB. Comparación guardada del 2026-11-20: tiempo 1/43, memoria 1/43; ambas metas de diez primeros cumplidas, sin asterisco. Bajo 1024 KB la admisión estricta usa solo tiempo. Ejecución optimizada anterior #11315303: 0.031 s / 88 KB. Son pares independientes; la memoria registrada nueva es mayor. El C++ didáctico conservado tiene su propio Accepted actual #11327473: 0.031 s / 264 KB, sin cambiar su algoritmo.

C++/Go conservan el máximo exacto de m techos, pero leen los planes en un anillo de hasta50 enteros. Tras cada orden real se sustituye el elemento vencido y avanza la cabeza, conservando la ventana exacta. El índice se envuelve por límite, sin resto por elemento. Delta no negativo usa (delta+t−1)/t; negativo usa truncamiento hacia cero, su techo. Planes y existencias permanecen en0…100000: bastan32 bits con signo. Tiempo O(nm), planes O(m) frente a O(n+m), E/S acotada. Se conservan bases; Java, Python y Rust reutilizan las admitidas.

Los fuentes didácticos Accepted conservados [1783_simulation.java](1783_simulation.java), [1783_simulation.py](1783_simulation.py), [1783_simulation.rs](1783_simulation.rs) cumplen diez primeros o 15% superior en las métricas exigidas de la comparación guardada. La tabla contiene sus pares actuales exactos, incluidas revisiones solo de formato. Algoritmos intactos y sin copias optimizadas idénticas; el asterisco indica la meta propia del lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1783_implementation_parsing_optimized.rs`. Solo se guarda una ventana de m valores en un anillo. Sus dos tramos se recorren en orden mensual y se sustituye el más antiguo. Se conserva el techo exacto incluso para cambios negativos y se escriben las órdenes directamente, usando O(m) en vez de vectores completos. La salida directa se especializa a los tipos usados, evitando despacho genérico y cadenas temporales. El texto fijo usa escrituras nativas y los números se convierten exactamente con el signo requerido. Se conservan decisiones matemáticas y versiones simples.

Accepted #11329204 (Rust 1.75 x64): **0.015 s / 72 KB**. Comparación archivada: `1783_simulation.rs` (Rust 1.75 x64) — 0.031 s / 828 KB (#11327475).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1783_simulation.cpp](1783_simulation.cpp) | G++ 13.2 x64 | simulation | O(n m) | AC | 0.031 s | 264 KB | 11327473 |
| [1783_simulation.go](1783_simulation.go) | Go 1.14 x64 | simulation | O(n m) | AC | 0.031 s | 1384 KB | 11289783 |
| [1783_simulation.java](1783_simulation.java) | Java 1.8 | simulation | O(n m) | AC | 0.14 s | 2388 KB | 11327472 |
| [1783_simulation.py](1783_simulation.py) | Python 3.12 x64 | simulation | O(n m) | AC | 0.187 s | 2584 KB | 11327474 |
| [1783_simulation.rs](1783_simulation.rs) | Rust 1.75 x64 | simulation | O(n m) | AC | 0.031 s | 828 KB | 11327475 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1783_simulation_optimized.cpp](1783_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(n·m) | AC | 0.015 s | 104 KB | 11326998 |
| [1783_simulation_optimized.go](1783_simulation_optimized.go) \* | Go 1.14 x64 | simulation | O(n·m) | AC | 0.031 s | 300 KB | 11315305 |
| [1783_implementation_parsing_optimized.rs](1783_implementation_parsing_optimized.rs) | Rust 1.75 x64 | implementation, parsing | O(nm) time; O(m) space + bounded I/O buffers | AC | 0.015 s | 72 KB | 11329204 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
