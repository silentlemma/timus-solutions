# 1729. El cofre del hombre muerto

[Timus 1729](https://acm.timus.ru/problem.aspx?space=1&num=1729) · dificultad 630 · geometry

Problema original de Fedor Fominykh (preparado por Denis Dublennykh), del Concurso Regional por Equipos de Programación de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Jack está en el centro de una isla redonda de radio r cubierta de
selva, así que solo ve el mar desde la orilla. Su bote está junto a la
orilla en algún lugar, y se ve desde los puntos de la orilla a lo sumo
a a grados del punto de la orilla más cercano a él. Hallar la longitud
mínima de una ruta que le permita ver el bote en el peor caso.

## Entrada

r y a (1 ≤ r ≤ 1000, 0.001 ≤ a ≤ 45), con a lo sumo tres cifras tras
el punto decimal.

## Salida

La distancia en el peor caso para la mejor ruta, con al menos seis
cifras tras el punto decimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
1.000 30.000
```

Salida:

```
6.0000000
```

## Solución

Llegar a la orilla cuesta r. Desde ahí, cada punto de la orilla que
Jack visita le muestra un arco de 2a grados centrado en él, y en el
peor caso el bote solo se ve desde el último. Entre dos puntos de la
orilla el camino más corto es la cuerda; puntos consecutivos pueden
distar a lo sumo 2a, mientras que el barrido del primero al último debe
cubrir al menos 360 − 2a para que los arcos se cierren alrededor de la isla.

Así la ruta es r más cuerdas cuyos ángulos suman 360 − 2a, cada uno a
lo sumo 2a. Una cuerda de ángulo θ mide 2r·sin(θ/2), que crece más
despacio que θ, así que con el total fijo la suma es mínima cuando los
trozos son lo más desiguales posible: k − 1 cuerdas completas de 2a,
con k = ⌊180/a⌋, y una cuerda corta para el resto, 360 − 2ka grados,
vacía cuando 2a divide a 360. `O(1)`.

En el ejemplo a = 30: seis puntos separados 60°, cinco cuerdas de
longitud r, así que la respuesta es 1 + 5 = 6.

Trampas:

- ⌊180/a⌋ calculado en coma flotante puede salir uno menos; las
  soluciones leen a exactamente en milésimas de grado. Ese error, de
  todos modos, daría la misma longitud, porque la cuerda completa que
  falta vuelve como una cuerda corta de 2a;
- para a = 0.001 la ruta tiene 179 999 cuerdas, así que la suma es un
  producto y no un bucle sobre ellas.

Las respuestas coinciden con una implementación aceptada independiente
en las siete cifras impresas en 300 casos aleatorios.

## Soluciones optimizadas

La versión en C++ usa la entrada y salida estándar de C. El ángulo de entrada tiene como máximo tres decimales. Al multiplicarlo por 1000 y redondear se recupera el número entero de milésimas antes de dividir y tomar el resto. La fórmula de las cuerdas conserva el tiempo y el espacio constantes. Las métricas corresponden al envío 11316978.

El ángulo se convierte en milésimas enteras de grado antes de calcular el número de cuerdas completas y el resto. Rust 1.75 x64, envío 11318489. Tiempo 0,046 → 0,031 s, memoria 260 → 256 KB.

El ángulo se convierte en milésimas enteras de grado antes de calcular el número de cuerdas completas y el resto. Python 3.12 x64, envío 11318496. Tiempo 0,109 → 0,078 s, memoria 464 → 520 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322451 · Rust 1.75 x64 №11321953 · Go 1.14 x64 №11322452 · Java 1.8 №11322453 · Python 3.12 x64 №11322454.

El ángulo se convierte en milésimas enteras de grado antes de calcular el número de cuerdas completas y el resto. Java 1.8, envío 11322411. Tiempo 0,14 → 0,125 s, memoria 1800 → 392 KB.

Go calcula la distancia con la fórmula de la cuerda y escribe el resultado con precisión fija desde un búfer pequeño. Go 1.14 x64, envío 11322864. Tiempo 0,031 → 0,031 s, memoria 1088 → 304 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1729_geometry_parsing_optimized.rs`. Se sustituye la conversión flotante de entrada por milésimas exactas, conservando la fórmula de cuerdas y la salida C de siete decimales.

Accepted #11328988 (Rust 1.75 x64): **0.015 s / 84 KB**. Comparación archivada: `1729_geometry_optimized.rs` (Rust 1.75 x64) — 0.031 s / 256 KB (#11318489).

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1729_geometry_parsing_optimized.java`. Las entradas decimales acotadas se leen como milésimas exactas, conservando la fórmula de cuerdas. Se escriben siete decimales directamente, evitando conversiones flotantes generales. El búfer acotado y los métodos de entrada se colocan en Main, eliminando la carga y asignación de una clase auxiliar. No cambian la fórmula completa, la escala ni el formato de punto fijo. Tras escribir la respuesta completa, el programa vacía ambos flujos antes de Runtime.halt(0).

Accepted #11329243 (Java 1.8): **0.078 s / 476 KB**. Comparación archivada: `1729_geometry_optimized.java` (Java 1.8) — 0.125 s / 392 KB (#11322411).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1729_geometry.cpp](1729_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 452 KB | 11322451 |
| [1729_geometry.go](1729_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB | 11322452 |
| [1729_geometry.java](1729_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.14 s | 1800 KB | 11322453 |
| [1729_geometry.py](1729_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 464 KB | 11322454 |
| [1729_geometry.rs](1729_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 256 KB | 11321953 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1729_geometry_optimized.cpp](1729_geometry_optimized.cpp) \* | G++ 13.2 x64 | geometry | O(1) | AC | 0.031 s | 136 KB | 11316978 |
| [1729_geometry_optimized.rs](1729_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 256 KB | 11318489 |
| [1729_geometry_optimized.py](1729_geometry_optimized.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 520 KB | 11318496 |
| [1729_geometry_optimized.java](1729_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.125 s | 392 KB | 11322411 |
| [1729_geometry_optimized.go](1729_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 304 KB | 11322864 |
| [1729_geometry_parsing_optimized.rs](1729_geometry_parsing_optimized.rs) | Rust 1.75 x64 | geometry, parsing | O(1) | AC | 0.015 s | 84 KB | 11328988 |
| [1729_geometry_parsing_optimized.java](1729_geometry_parsing_optimized.java) | Java 1.8 | geometry, parsing | O(1) | AC | 0.078 s | 476 KB | 11329243 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
