# 1202. El camino más corto a través de una cadena de rectángulos

[Timus 1202](https://acm.timus.ru/problem.aspx?space=1&num=1202) · dificultad 442 · greedy

Problema original de Leonid Volkov, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Menos de `10⁵` rectángulos en papel cuadriculado forman una cadena de
izquierda a derecha: el primero tiene la esquina inferior izquierda en
`(0, 0)`, cada uno empieza donde termina horizontalmente el anterior y
cada lado mide de 2 a 100 casillas. Donde dos vecinos se tocan, su borde
común desaparece. Un viajero camina por las líneas de la cuadrícula
desde `(1, 1)` hasta el punto una casilla hacia dentro de la esquina
superior derecha del último rectángulo, no puede andar por ningún borde
de rectángulo y solo pasa de un rectángulo al siguiente por la parte
desaparecida del borde. Hay que hallar la longitud del camino más corto,
o `-1` si no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y luego cada rectángulo como `x1 y1 x2 y2`, las esquinas inferior
izquierda y superior derecha.

## Salida

La longitud del camino más corto, o `-1`.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 0 3 5
3 1 5 7
```

Salida:

```
8
```

## Solución

El camino debe ir de `x = 1` a `x = x2 − 1` del último rectángulo, y
siempre puede hacerlo sin dar ningún paso a la izquierda, así que la
parte horizontal es fija. Entre los rectángulos `i` e `i + 1` el camino
cruza la recta `x = x2ᵢ` a una altura entera estrictamente dentro de
ambos, es decir en `[max(y1) + 1, min(y2) − 1]`; si ese rango está
vacío, no hay camino. Dentro de un rectángulo la altura se puede cambiar
libremente por una línea vertical interior, así que la longitud vertical
es el cambio total de altura entre el inicio, las alturas de cruce
elegidas y la meta.

Para minimizarla, se mueve solo cuando es obligado: se mantiene la altura
actual y en cada borde se lleva al rango permitido. Por inducción, la
forma más barata de estar a altura `h` tras el borde `i` cuesta el total
voraz hasta ahí más `|h − altura voraz|`, así que la elección voraz nunca
es peor. `O(n)`.

Detalles a tener en cuenta:

- los rectángulos que se tocan en menos de dos unidades, o solo por una
  esquina, no dejan paso alguno;
- los rectángulos pueden extenderse por debajo de cero;
- con un solo rectángulo la respuesta es la distancia de `(1, 1)` a la
  meta, y 0 para un rectángulo de 2×2.

Las respuestas se compararon con una solución escrita aparte en 400
cadenas aleatorias y en todas las pruebas.

## Soluciones optimizadas

`1202_greedy_optimized.py`. Mantiene el ajuste voraz de altura al punto más cercano del solapamiento de rectángulos. Lee cuatro coordenadas por bloques de 4096 bytes, guardando intervalo anterior, altura y recorrido vertical. Elimina lista entera de entrada y lista copiada de rectángulos. Solapamiento vacío da -1; si no, usa límites derecho/superior del último rectángulo como antes. O(n) tiempo, O(B) espacio para tokens acotados y bloque B. Vacía respuesta antes de salir del intérprete.

Frente a `1202_greedy.py`: tiempo 0.328 s → 0.203 s; memoria 39384 KB → 6 920 KB.

C++ y Go mantienen la misma proyección sobre el intervalo de cada borde compartido. Ya bastan el rectángulo anterior, la altura actual y la distancia vertical acumulada; no se añade una lista. C++ sustituye scanf por un lector de 8192 bytes, y Go cambia bufio/fmt por E/S acotada de manejadores estándar. Se analizan signos negativos y se conservan cálculos de 64 bits en los destinos. Un intervalo vacío devuelve −1 inmediatamente. Tiempo O(n), espacio auxiliar acotado. Se conservan las bases; Java, Python y Rust reutilizan las admitidas para el conjunto rápido.

Las implementaciones base aceptadas [1202_greedy.java](1202_greedy.java), [1202_greedy.py](1202_greedy.py), [1202_greedy.rs](1202_greedy.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1202_greedy_optimized.py`. Se reutiliza exactamente el código en flujo bajo CPython 3.12 en vez de PyPy. No cambian los rectángulos ni el búfer acotado. La nueva medición tarda más pero usa menos memoria; por debajo de 1024 KB supera el criterio basado solo en tiempo. No se duplica el archivo.

Accepted #11328666 (Python 3.12 x64): **0.421 s / 844 KB**. Comparación archivada: `1202_greedy_optimized.py` (PyPy 3.10 x64) — 0.203 s / 6920 KB (#11325482).

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1202_greedy_parsing_optimized.rs`. La cadena de rectángulos se procesa en flujo, guardando solo los adyacentes, la altura de paso y la distancia vertical acumulada. Ajustar la altura solo cuando es necesario conserva el óptimo voraz con estado constante. Se leen tokens con un búfer nativo acotado; los cortos se guardan dentro del objeto y solo los largos reservan espacio extra. La conversión decimal conserva las cotas con signo sin guardar toda la entrada de comandos. Esta alternativa conserva el inicio y cierre habituales de Rust con el mismo estado compacto.

Accepted #11329005 (Rust 1.75 x64): **0.015 s / 188 KB**. Comparación archivada: `1202_greedy.rs` (Rust 1.75 x64) — 0.031 s / 8696 KB (#11283565).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1202_greedy_optimized.py`: puesto de tiempo 3/15 y de memoria 8/15 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1202_greedy.cpp](1202_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.234 s | 132 KB | 11283557 |
| [1202_greedy.go](1202_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.046 s | 1088 KB | 11283561 |
| [1202_greedy.java](1202_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.140 s | 540 KB | 11283564 |
| [1202_greedy.py](1202_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.328 s | 39384 KB | 11283563 |
| [1202_greedy.rs](1202_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.031 s | 8696 KB | 11283565 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1202_greedy_optimized.cpp](1202_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 88 KB | 11315050 |
| [1202_greedy_optimized.go](1202_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(n) | AC | 0.046 s | 312 KB | 11315069 |
| [1202_greedy_optimized.py](1202_greedy_optimized.py) | Python 3.12 x64 | greedy | O(n) time; O(B) space | AC | 0.421 s | 844 KB | 11328666 |
| [1202_greedy_parsing_optimized.rs](1202_greedy_parsing_optimized.rs) | Rust 1.75 x64 | greedy, parsing | O(n) time; O(1) state + bounded input buffer | AC | 0.015 s | 188 KB | 11329005 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
