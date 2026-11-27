# 1407. Un-dos, un-dos

[Timus 1407](https://acm.timus.ru/problem.aspx?space=1&num=1407) · dificultad 388 · constructive

Problema original de Sergey Pupyrev, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para 1 ≤ N ≤ 100, hay que imprimir un número de a lo sumo 10 000 cifras,
todas 1 o 2, divisible por 2ᴺ, o «No solution» si no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

Un número así; se acepta cualquiera.

## Evaluación

El verificador acepta cualquier número de 1 a 10000 dígitos, todos 1 o 2, divisible por `2^N`. Rechaza la salida adicional.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
12
```

## Solución

Siempre hay uno de exactamente N cifras, construido desde la derecha.
Sea aₖ de k cifras 1 y 2 divisible por 2ᵏ; se pone delante la cifra d:
d·10ᵏ + aₖ = 2ᵏ·(d·5ᵏ + aₖ / 2ᵏ). Como 5ᵏ es impar, exactamente una de
d = 1 y d = 2 hace par el paréntesis, lo que da aₖ₊₁ divisible por
2ᵏ⁺¹. Se empieza de la nada y se repite N veces. `O(N²)` en Go/Java,
`O(N³)` en Python.

Solo los N + 1 bits más bajos deciden la elección, así que C++ y Rust
guardan el número en 128 bits y dejan que las sumas den la vuelta; Go y
Java usan enteros grandes y miran el bit encendido más bajo.

Detalles a tener en cuenta:

- la respuesta nunca es «No solution»;
- 2¹⁰⁰ pasa de 64 bits con mucho (pruebas 07 a 09).

Históricamente se comprobó cada N de 1 a 100 con una construcción divisible de N cifras. Las pruebas actuales usan el verificador semántico de Evaluación: aceptan cualquier respuesta de 1..10000 unos/doses divisible por 2^N, incluso una más corta como 112 para N=4. No exigen igualdad exacta con la construcción única de N cifras.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1407_constructive_optimized.java`. Java conserva la construcción de derecha a izquierda: tras k cifras, el bit k del valor actual elige 2 si es cero y 1 en caso contrario. Frente a la base con BigInteger, guarda el valor y la potencia de diez en pares de palabras long módulo 2^128. Para N<=100 no se pierde ningún bit consultado; el acarreo sin signo y la multiplicación por diez mediante mitades de 32 bits dan aritmética modular exacta. Escribe las cifras directamente en N+1 bytes. En este dominio acotado: tiempo O(N), almacenamiento de respuesta O(N) y estado aritmético O(1); no presupone ancho fijo para N ilimitado. Conserva las fuentes didácticas.

Accepted exacto Java 1.8 #11327478: 0.093 s / 312 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 5/44, memoria 1/44. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Tiempo 5/44 cumple el criterio común de sólo tiempo; la fila sin asterisco es correcta, sin meta separada de primer puesto. El registro optimizado documentado antes #11324811 era 0.125 s / 524 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1407_constructive_optimized.java`: 0.093 s / 312 KB; base didáctica conservada `1407_constructive.java`: 0.109 s / 1668 KB.

`1407_constructive_optimized.py`. Construye de menor a mayor posición. Tras k posiciones el valor es divisible por 2^k; el bit k elige 1 o 2 porque 10^k/2^k es impar, evitando dos restos de prueba. Guarda bytes y revierte una vez. Los enteros crecen a O(n) bits: O(n²) trabajo de bits y O(n) almacenamiento de bits/dígitos, sin prometer tiempo lineal con palabras fijas. La fila Accepted indica el runtime real y sus medidas emparejadas. Vacía salida antes de os._exit(0), que omite cierre del intérprete; la mejora medida de memoria depende del runtime y no implica aceleración asintótica.

Frente a `1407_constructive.py`: tiempo 0.078 s → 0.125 s; memoria 416 KB → 244 KB.

Go y Rust construyen la respuesta de derecha a izquierda y guardan el valor parcial y la siguiente potencia de diez módulo 2¹²⁸. Tras k cifras, los k bits inferiores son cero, por lo que el bit k decide si la siguiente cifra es uno o dos. Solo importan los N ≤ 100 bits inferiores. Go usa dos palabras de 64 bits y Rust operaciones u128 con desbordamiento modular. Go lee el exponente directamente de un pequeño búfer de bytes reutilizable y escribe las cifras construidas sin convertirlas en cadenas.

El envío aceptado en Go 1.14 x64 tarda 0.031 s frente a 0.015 s de la base y usa 784 KB frente a 1140 KB.

El conjunto rápido reutiliza las bases válidas C++ y Python y usa Java optimizada. Java sencilla se conserva para enseñanza sin afirmar que cumpla: tiempo 15/44 y memoria 19/44 no pasan. El Accepted previo de Java optimizada #11327478 es 0.093 s / 312 KB; tiempo 5/44 cumple comparando sólo tiempo. No se duplican fuentes idénticos; las filas didácticas no son objetivos separados de optimización.

## Notas por lenguaje

Se aplican los [criterios comunes](../../RATING_CRITERIA.md): memoria ignorada sólo estrictamente bajo 1024 KB, rivales menores de 0.015 s excluidos y suelo sólo para nuestros tiempos. Cohortes normales usan los diez primeros o el 15%, con empates y corte redondeado hacia arriba; no hay excepción de primer puesto ni mejora del 30%. C++ cumple tiempo 1/19 en la caché. Python sencilla cumple 4/27; PyPy optimizada 22/27 incumple y mantiene asterisco. Go sin rivales actuales usa comparación alternativa del mismo lenguaje con dos resultados Go 1.3, y ambas versiones cumplen. Rust usa análogamente tres rivales antiguos, con tiempo sencillo/optimizado 4/4 y 1/4 válidos. Las medidas históricas emparejadas siguen como observaciones separadas.

Sólo se añaden comentarios explicativos en `1407_constructive_optimized.java`: comparación de acarreo sin signo mediante XOR, multiplicación por mitades de 32 bits y elección de cifra por el bit k módulo 2^128. El código ejecutable no cambia.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1407_constructive.cpp](1407_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 188 KB | 11286054 |
| [1407_constructive.go](1407_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.015 s | 1140 KB | 11286055 |
| [1407_constructive.java](1407_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.109 s | 1668 KB | 11286057 |
| [1407_constructive.py](1407_constructive.py) | Python 3.12 x64 | constructive | O(N^3) | AC | 0.078 s | 416 KB | 11286056 |
| [1407_constructive.rs](1407_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.046 s | 216 KB | 11286058 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1407_constructive_optimized.go](1407_constructive_optimized.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.031 s | 784 KB | 11311119 |
| [1407_constructive_optimized.rs](1407_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.015 s | 188 KB | 11310807 |
| [1407_constructive_optimized.java](1407_constructive_optimized.java) | Java 1.8 | constructive | O(N) time; O(N) answer space | AC | 0.078 s | 324 KB | 11331218 |
| [1407_constructive_optimized.py](1407_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(n²) bit work; O(n) bits | AC | 0.125 s | 244 KB | 11325484 |

\* Accepted; esta versión PyPy optimizada distinta incumple el criterio actual de tiempo. La base cubre Python.
