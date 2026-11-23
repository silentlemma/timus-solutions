# 1600. El aeropuerto

[Timus 1600](https://acm.timus.ru/problem.aspx?space=1&num=1600) · dificultad 552 · geometry

Problema original de Vladimir Yakovlev, del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hasta 500 objetos vuelan en línea recta a velocidad constante en el
espacio; todos empiezan a más distancia entre sí que una distancia
crítica d. Hay que hallar el primer momento en que algún par se acerca a
distancia d, e imprimir `ALARM!` y luego el tiempo con tres decimales y
el par, u `OK` si eso nunca ocurre. Si en ese momento se acercan varios
pares, se puede imprimir cualquiera.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y d, y luego la posición y la velocidad de cada objeto, seis números.

## Salida

`OK`, o `ALARM!` y luego el tiempo y los números de los dos objetos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1.0
1.0 1.0 -1.0 0.0 0.0 10.0
0.0 0.0 4.0 2.0 0.0 0.0
```

Salida:

```
ALARM!
0.500 1 2
```

## Solución

Visto desde un objeto del par, el otro se mueve por la recta p + v·t,
donde p y v son las diferencias de posiciones y velocidades. Están a
distancia d cuando |p + v·t|² = d², una ecuación cuadrática:
(v·v)t² + 2(p·v)t + (p·p − d²) = 0. Con velocidades iguales o
discriminante negativo, el par nunca se acerca. Si no, la raíz menor es
el momento en que la distancia llega por primera vez a d; como todos los
pares empiezan separados, una raíz negativa significa que se alejan. El
momento más temprano entre todos los pares es la respuesta: `O(n²)`,
unos 125000 pares.

Las pruebas usan un verificador que acepta cualquier par que se acerque
en el momento correcto, con el redondeo a tres decimales. Los tiempos se
contrastaron con una bisección sobre la distancia antes del máximo
acercamiento.

Detalles a tener en cuenta:

- un par que solo toca la distancia d en su máximo acercamiento también
  da la alarma: el discriminante es entonces exactamente 0 (prueba 04);
- con una velocidad relativa diminuta el tiempo puede ser grande, casi
  10⁶ segundos en la prueba 07, así que no hay que acotarlo de antemano;
- con el semidiscriminante, b = p·v y b² − a·c, no hace falta arrastrar
  el factor 4.

La versión sencilla en C++ escala los datos decimales a enteros y calcula exactamente el signo del discriminante. La versión sencilla en Java escala los datos decimales a enteros y calcula exactamente el signo del discriminante.

La versión sencilla en Rust escala los datos decimales a enteros y calcula exactamente el signo del discriminante.

## Soluciones optimizadas

`1600_geometry_optimized.cpp`. Conserva geometría de todos los pares, rechazo exacto en centésimas, fórmula estable de producto cruzado, ruta double y fallback cuádruple cerca de tangencia. Solo cambia scanf por fread de 4096 bytes y tokens hasta 127 caracteres para mismo parser decimal. Sin reducir precisión ni relajar tolerancia. O(N²) pares, O(N) objetos más búfer fijo. Conserva base y ambas alternativas Python. Nuevo par C++ 0.015 s/264 KB; anterior 0.031 s/256 KB.

Fuente exacto: G++ 13.2 x64 Accepted #11327842: 0.015 s / 264 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 1/46; 5/46. Admisión estricta usa solo tiempo bajo 1024 KB: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Cumple ambas metas de C++, sin asterisco. La variante anterior conservada tiene su par propio #11321905 (G++ 13.2 x64): 0.031 s / 256 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `1600_geometry_optimized.cpp`: 0.015 s / 264 KB; base didáctica conservada `1600_geometry.cpp`: 0.328 s / 664 KB.

Python ordena los objetos por la coordenada x y descarta los pares cuya separación en ese eje no puede llegar a la distancia crítica. Tras encontrar un encuentro, una cota superior entera de su tiempo limita el recorrido. El signo del discriminante se calcula exactamente para los pares restantes. Python 3.12 x64, envío 11322507. Tiempo 0,203 → 0,078 s, memoria 1492 → 1084 KB.

La versión de Python que ahorra memoria recorre todos los pares y omite los que se alejan. Usa la fórmula equivalente `c / (−b + √(b² − ac))` para calcular el instante de entrada sin restar valores casi iguales. El envío 11316939 tardó 0.156 s y usó 764 KB. La versión que ordena por x examina menos pares y tardó 0.078 s con 1084 KB. Frente a la versión sencilla, la enumeración ahorra un 48.8% de memoria y la ordenación reduce el tiempo un 61.6%.

El envío de Java 11321903 tardó 0,125 s y usó 1780 KB. La versión sencilla actual tardó 0,281 s y usó 7020 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322335 · Go 1.14 x64 №11322334 · Java 1.8 №11322333 · Python 3.12 x64 №11322332 · Rust 1.75 x64 №11322336.

Go omite los pares que se alejan. Para los pares cerca de la tangencia vuelve a calcular el discriminante con aritmética racional a partir de los valores decimales de entrada y aplica la fórmula estable del tiempo de entrada.

Descripción y mediciones históricas de la revisión anterior: C++ calcula la separación mínima con el producto vectorial y revisa las trayectorias casi tangentes en precisión cuádruple.

Rust escala la entrada decimal a enteros. Si todos los valores escalados tienen magnitud de hasta 500 000 000, calcula el discriminante exactamente con enteros de 128 bits. En los demás casos usa enteros de precisión arbitraria.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1600_geometry_math_optimized.rs`. Se elige el cálculo exacto acotado en i128 antes de reservar dígitos de enteros grandes. Se mantienen la cota de coordenadas y el discriminante exacto; valores mayores o escalas más finas usan la ruta de precisión arbitraria conservada. Permanecen ambas versiones públicas anteriores.

Accepted #11328703 (Rust 1.75 x64): **0.015 s / 380 KB**. Comparación archivada: `1600_geometry_optimized.rs` (Rust 1.75 x64) — 0.031 s / 560 KB (#11322367).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1600_geometry.cpp](1600_geometry.cpp) | G++ 13.2 x64 | geometry | O(n²) | AC | 0.328 s | 664 KB | 11322335 |
| [1600_geometry.go](1600_geometry.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.093 s | 2428 KB | 11322334 |
| [1600_geometry.java](1600_geometry.java) | Java 1.8 | geometry | O(n²) | AC | 0.281 s | 7020 KB | 11322333 |
| [1600_geometry.py](1600_geometry.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.203 s | 1492 KB | 11322332 |
| [1600_geometry.rs](1600_geometry.rs) | Rust 1.75 x64 | geometry | O(n²) | AC | 0.234 s | 616 KB | 11322336 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1600_geometry_optimized.py](1600_geometry_optimized.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.078 s | 1084 KB | 11322507 |
| [1600_bruteforce_geometry.py](1600_bruteforce_geometry.py) | Python 3.12 x64 | bruteforce, geometry | O(n²) | AC | 0.156 s | 764 KB | 11316939 |
| [1600_geometry_optimized.java](1600_geometry_optimized.java) | Java 1.8 | geometry | O(n²) | AC | 0.125 s | 1780 KB | 11321903 |
| [1600_geometry_optimized.go](1600_geometry_optimized.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.031 s | 1304 KB | 11322026 |
| [1600_geometry_optimized.cpp](1600_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(N²) time; O(N) storage | AC | 0.015 s | 264 KB | 11327842 |
| [1600_geometry_optimized.rs](1600_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n²) | AC | 0.031 s | 560 KB | 11322367 |
| [1600_geometry_math_optimized.rs](1600_geometry_math_optimized.rs) | Rust 1.75 x64 | geometry, math | O(n²) | AC | 0.015 s | 380 KB | 11328703 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
