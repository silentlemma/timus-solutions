# 1351. Gnusmas bueno, gnusmas muerto

[Timus 1351](https://acm.timus.ru/problem.aspx?space=1&num=1351) · dificultad 518 · geometry

Problema original de Denis Musin, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ametralladora en el origen cubre un sector entre dos rayos: el borde
derecho pasa por (X1, Y1) y el izquierdo por (X2, Y2); el sector es
menor que media vuelta. Su alcance es D ≤ 30 000. Para cada uno de
N ≤ 30 000 puntos hay que imprimir `YES` si el punto está en el sector y
a distancia no mayor que D, y `NO` en otro caso.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Enteros D, X1, Y1, X2, Y2, luego N y N pares de coordenadas;
1 ≤ D, N ≤ 30000, magnitudes de coordenadas hasta 30000. Ningún
objetivo es el origen y ambos vectores frontera son no nulos. El
enunciado guardado exige módulo de cada componente frontera al menos
1, pero su ejemplo oficial contiene ceros. Siguiendo el ejemplo, estas
fuentes admiten rayos no nulos alineados con ejes. El sector antihorario
desde derecha a izquierda es estrictamente menor que 180°.

## Salida

N líneas con `YES` o `NO`.

## Evaluación

Comparación de tokens (`judging: tokens`): exactamente N respuestas
`YES` o `NO` en orden, distinguiendo mayúsculas. Se incluyen rayos
frontera y círculo de alcance; los espacios no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 1 0 0 1
6
1 1
5 6
3 0
-1 2
0 5
-3 0
```

Salida:

```
YES
NO
YES
NO
YES
NO
```

## Solución

El sector va en sentido antihorario del borde derecho R al borde
izquierdo L. Un punto P está en él si no queda en sentido horario de R
ni en sentido antihorario de L:

- cross(R, P) = X1·y − Y1·x ≥ 0;
- cross(P, L) = x·Y2 − y·X2 ≥ 0.

Cada condición corta un semiplano, y como el sector es menor que media
vuelta, los dos semiplanos se cortan exactamente en el sector, con una
excepción: si los dos bordes están en el mismo rayo (un sector de ancho
cero), la prolongación hacia atrás de ese rayo también pasa las dos
condiciones. Así que un punto en la recta de un borde pero detrás de la
ametralladora, con producto cruzado cero y producto escalar negativo,
se descarta aparte. El
alcance se comprueba como x² + y² ≤ D², todo en enteros y sin raíces.
`O(N)`.

Detalles a tener en cuenta:

- los puntos en los bordes y en la circunferencia cuentan: `3 0` y `0 5`
  en el ejemplo;
- un punto en el rayo opuesto a un borde tiene producto cruzado cero con
  ese borde; lo descarta la otra condición, salvo en un sector de ancho
  cero, donde solo lo hace la comprobación aparte (pruebas 02 y 06);
- los productos llegan a 1,8·10⁹, dentro de los enteros de 32 bits con signo;
- con D = 30 000 el punto (30 000, 1) queda justo fuera de alcance
  (prueba 04).

Las respuestas se compararon con una comprobación de ángulos con `atan2`
en 18 pruebas generadas y con una solución independiente en 300
sectores aleatorios, incluidos los de ancho cero.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

C++, Go y Rust conservan la distancia al cuadrado y las dos pruebas de producto cruzado. Cuando el sector mide más de 0° y menos de 180°, la intersección de los semiplanos cerrados coincide con el sector. Si los rayos coinciden, esas pruebas admiten toda su recta. Un producto escalar negativo excluye los puntos de la recta situados detrás del origen. Cada coordenada tiene magnitud máxima 30 000. La suma o diferencia de dos productos de coordenadas está acotada en valor absoluto por 2·30 000² = 1,8·10⁹ y cabe en 32 bits con signo. Procesar los puntos con búferes de entrada y salida de 4096 y 8192 bytes elimina las cadenas crecientes de Rust, las respuestas acumuladas de C++ y Scanner/conversión Go. Tiempo O(N), memoria extra constante, sin ángulos aproximados. Se conservan bases; Java reutiliza la base admitida; Python usa su variante en flujo separada.

Java reutiliza la base: tiempo 8/17 y memoria 5/17, ambos necesarios
y top diez. Python se cubre con
[1351_geometry_optimized.py](1351_geometry_optimized.py), Accepted
#11328774 `0.093 s / 1172 KB`, no la base de 6832 KB. Cinco rivales
exactos CPython dan tercera referencia `0.109 s / 5170.40 KB`;
con 1172 KB cuentan ambas métricas y cumple. La base falla memoria.
Rigen los [criterios comunes](../../RATING_CRITERIA.md); se mantienen
fuentes sencillas útiles sin duplicarlas.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1351_geometry_optimized.py`. Se leen los puntos en flujo con un lector acotado y se escriben bloques de hasta 1024 líneas. Las pruebas geométricas no cambian; ya no se retienen todos los puntos y respuestas. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328774 (Python 3.12 x64): **0.093 s / 1172 KB**. Comparación archivada: `1351_geometry.py` (Python 3.12 x64) — 0.093 s / 6832 KB (#11285173).

## Notas por lenguaje

El recorrido geométrico O(N) no implica espacio constante para todas
las bases. C++/Java guardan O(N) salida; Go transmite con O(B).
Python retiene entrada, tokens, enteros y respuestas: O(I+N+B), I
bytes de entrada. Rust sencillo guarda String de entrada y salida:
O(I+N+B). B son búferes acotados; C++/Java usan O(N+B). Los rápidos
C++/Go/Rust usan búferes fijos O(B). Python rápido guarda bloques de
entrada y lotes de 1024 respuestas, más un token incompleto. Tiempo
total O(I+N), estado geométrico O(1).

Estas notas describen las implementaciones sencillas.

- C++, Go, Java y Rust usan enteros de 64 bits para los productos
  cruzados y los cuadrados; Python usa enteros de precisión arbitraria.
- Java lee con `StreamTokenizer`; sus valores double guardan estos
  enteros con exactitud.

En `1351_geometry_optimized.py` sólo se nombran constantes exigidas por el lint; valores, algoritmo y comentarios no cambian. Accepted #11328774 y sus medidas corresponden a los bytes exactos previos.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1351_geometry.cpp](1351_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.031 s | 320 KB | 11285165 |
| [1351_geometry.go](1351_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1392 KB | 11285171 |
| [1351_geometry.java](1351_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.14 s | 1328 KB | 11285176 |
| [1351_geometry.py](1351_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 6832 KB | 11285173 |
| [1351_geometry.rs](1351_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 1236 KB | 11285179 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1351_geometry_optimized.cpp](1351_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 76 KB | 11315502 |
| [1351_geometry_optimized.go](1351_geometry_optimized.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 904 KB | 11315507 |
| [1351_geometry_optimized.rs](1351_geometry_optimized.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 188 KB | 11315506 |
| [1351_geometry_optimized.py](1351_geometry_optimized.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.078 s | 1280 KB | 11331087 |
