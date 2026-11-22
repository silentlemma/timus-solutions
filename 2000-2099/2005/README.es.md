# 2005. La ruta permitida más corta entre cinco paradas

[Timus 2005](https://acm.timus.ru/problem.aspx?space=1&num=2005) · dificultad 94 · bruteforce

Problema original de Mikhail Rubinchik. (Prepared by Oleg Merkurev), del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Visitar cinco lugares exactamente una vez, empezando en 1 y terminando
en 5. El lugar 3 no puede ser la penúltima parada. Dadas todas las
distancias, hallar una ruta permitida de distancia total mínima y su
longitud. Se admite cualquier óptimo.

## Entrada

Una matriz entera de distancias de 5 por 5. Sus valores están entre 0 y
10000, la diagonal es cero, la matriz es simétrica y satisface la
desigualdad triangular `d[i][j]≤d[i][k]+d[k][j]`. Tiempo 0,5 segundos,
memoria 64 MB.

## Salida

En la primera línea, la distancia total mínima. En la segunda, los cinco
números de lugar en orden de visita, separados por espacios. Los empates
pueden resolverse libremente.

## Evaluación

Un comprobador verifica que la ruta está permitida, que la longitud
impresa es la suya y que es óptima; se acepta cualquier ruta óptima.

## Ejemplos

```
0 2600 3800 2600 2500
2600 0 5300 3900 4400
3800 5300 0 1900 4500
2600 3900 1900 0 3700
2500 4400 4500 3700 0
```

```
13500
1 2 3 4 5
```

La ruta mostrada cuesta `2600+5300+1900+3700=13500`; su penúltima parada
es 4, por lo que cumple la restricción.

## Solución

El punto 1 va primero y el 5 al final, así que solo varía el orden de
los puntos 2, 3 y 4: seis órdenes, de los que los dos con el 3 justo
antes del 5 están prohibidos. Se prueban los otros cuatro, se suman las
cuatro distancias de cada ruta y se queda la más corta. `O(1)`.

Detalles a tener en cuenta:

- la regla se refiere a la parada justo antes de la última;
- una ruta cuesta de 0 a 40 000, así que el mínimo empieza en «todavía
  ninguno», no en 0 ni en 10 000.

## Soluciones optimizadas

`2005_bruteforce_optimized.py`. Python conserva la búsqueda exhaustiva de las cuatro rutas legales. itertools.permutations genera en C los seis órdenes de tres puntos intermedios y descarta los dos con penúltimo punto prohibido; la matriz sigue plana con 25 enteros. Esta versión vuelve deliberadamente a tuplas de permutaciones en lugar de los bucles Python anteriores, sin copiar filas de la matriz didáctica ni guardar estado a nivel de módulo. Emite cualquier ruta óptima empatada en un bloque binario y sale dentro de main. Para cinco puntos fijos, tiempo y espacio O(1), sin respuestas de rutas precalculadas; conserva las bases.

Accepted exacto Python 3.12 x64 #11327537: 0.078 s / 732 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 7/50, memoria 43/50. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11325492 (PyPy 3.10 x64) era 0.109 s / 212 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `2005_bruteforce_optimized.py`: 0.078 s / 732 KB; base didáctica conservada `2005_bruteforce.py`: 0.093 s / 432 KB.

`2005_bruteforce_optimized.java`. Java sigue enumerando todas las rutas permitidas entre cinco puntos. Elige el penúltimo vértice c, con índices desde cero, en {1,3}, luego cualquiera de los otros dos como a; el vértice intermedio restante es b=6-a-c. Genera exactamente las cuatro rutas legales sin filtrar 27 ternas. Una matriz plana de 25 int sustituye los arreglos anidados; durante la búsqueda conserva solo el coste ganador y tres índices, y crea un único arreglo de resultado al final. Entrada y salida de bytes sustituyen el análisis y formato generales. Cualquier testigo óptimo empatado es válido. Tiempo y espacio O(1) para estos cinco puntos fijos.

Accepted exacto Java 1.8 #11327443: 0.078 s / 360 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/170, memoria 3/170. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11324781 era 0.125 s / 496 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `2005_bruteforce_optimized.java`: 0.078 s / 360 KB; base didáctica conservada `2005_bruteforce.java`: 0.125 s / 1616 KB.

`2005_bruteforce_optimized.rs`. Mantiene rutas exhaustivas de cinco puntos, lee directamente a 25 i64 y deriva tercer vértice intermedio 6-a-b. Elimina tercer bucle redundante y vector de entrada. Emite los cinco vértices sin cadenas formateadas. Conserva cuatro rutas legales y orden de empates, con aritmética exacta más ancha. Tiempo y espacio constantes.

Frente a `2005_bruteforce.rs`: tiempo 0.031 s → 0.015 s; memoria 236 KB → 48 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`2005_bruteforce_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2005_bruteforce.cpp](2005_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 124 KB | 11303437 |
| [2005_bruteforce.go](2005_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1104 KB | 11303440 |
| [2005_bruteforce.java](2005_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 1616 KB | 11303442 |
| [2005_bruteforce.py](2005_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.093 s | 432 KB | 11303445 |
| [2005_bruteforce.rs](2005_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.031 s | 236 KB | 11303446 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2005_bruteforce_optimized.java](2005_bruteforce_optimized.java) \* | Java 1.8 | bruteforce | O(1) | AC | 0.078 s | 360 KB | 11327443 |
| [2005_bruteforce_optimized.py](2005_bruteforce_optimized.py) \* | Python 3.12 x64 | bruteforce | O(1), fixed five points | AC | 0.078 s | 732 KB | 11327537 |
| [2005_bruteforce_optimized.rs](2005_bruteforce_optimized.rs) \* | Rust 1.75 x64 | bruteforce | O(1), fixed five points | AC | 0.015 s | 48 KB | 11325508 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
