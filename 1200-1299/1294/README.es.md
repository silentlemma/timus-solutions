# 1294. Satélites marcianos

[Timus 1294](https://acm.timus.ru/problem.aspx?space=1&num=1294) · dificultad 317 · geometry

Problema original de Vladimir Yakovlev, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuatro satélites A, B, C y D están en una misma órbita circular, en
este orden. Se conocen las distancias AD, AC, BD y BC en miles de
kilómetros (enteros de 1 a 10 000); el radio de la órbita no. Hay que
hallar la distancia CD en kilómetros, redondeada a entero, o indicar
que no se puede determinar de forma única.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

AD, AC, BD y BC.

## Salida

`Distance is X km.` o `Impossible.`

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 7 5 7
```

Salida:

```
Distance is 5385 km.
```

## Actualización de envíos aceptados

Archivos actualizados: [1294_geometry.py](1294_geometry.py). Las tablas de soluciones muestran los nuevos Accepted correspondientes exactamente al código fuente de estos archivos. Las mediciones y posiciones comparativas anteriores pertenecen a versiones previas y se conservan como datos históricos. La auditoría en caché confirma implementaciones que cumplen los criterios en todos los lenguajes disponibles. Se conservan las versiones didácticas por su claridad; si un mismo archivo cubre también la versión rápida, debe cumplir el criterio de rendimiento.

## Solución

Sean a = AD, b = AC, c = BD, d = BC y x = CD. Los puntos A y B están en
el mismo arco que corta la cuerda CD, así que la ven con el mismo
ángulo inscrito t. El teorema del coseno en los triángulos ACD y BCD da

x² = a² + b² − 2ab cos t = c² + d² − 2cd cos t,

dos ecuaciones en x² y cos t. Por tanto

cos t = (a² + b² − c² − d²) / (2 (ab − cd)),

x² = (ab (c² + d²) − cd (a² + b²)) / (ab − cd).

- Si ab = cd, las ecuaciones o se contradicen o no dicen nada sobre t.
  En el segundo caso, por ejemplo un trapecio isósceles, CD de verdad
  puede tomar muchos valores (prueba 02). En ambos casos la respuesta es
  `Impossible.` (pruebas 02 y 03).
- Si |a² + b² − c² − d²| ≥ 2 |ab − cd|, no existe un triángulo no
  degenerado: la igualdad también falla, porque tres puntos distintos
  de una circunferencia no pueden ser colineales (pruebas 04 y 07).
- El teorema de Ptolomeo exige AB · CD = bc − ad > 0 para el orden dado.
  Si bc ≤ ad, la respuesta es `Impossible.` (pruebas 05 y 07). Junto con
  la cota estricta del coseno, esta comprobación garantiza el orden
  correcto de los puntos reconstruidos.
- Si no, x = 1000 · √x² kilómetros, redondeado.

Todas las comprobaciones de existencia usan enteros exactos de 64 bits
(los productos originales son menores que 2 · 10¹⁶). Se normalizan el
numerador y el denominador para que sean positivos. Una raíz cuadrada
en coma flotante estima la parte entera m de la distancia en kilómetros;
se redondea hacia arriba exactamente si
(2m + 1)² ≤ floor(4 · 1000² · num / den). Para evitar desbordamientos,
se calcula la cota como s · (num div den) + (s · (num mod den)) div den,
donde s = 4 · 1000². Los nuevos valores intermedios son menores que
2 · 10¹⁵. El tiempo y el espacio auxiliar son `O(1)`.

Las comprobaciones corregidas y los resultados redondeados se verifican
con un oráculo exacto independiente basado en el teorema de Ptolomeo,
los ángulos opuestos y las desigualdades estrictas del triángulo.

Detalles a tener en cuenta:

- los datos están en miles de kilómetros y la respuesta en kilómetros
  (prueba 01);
- AD · AC = BD · BC no siempre significa datos contradictorios: a veces
  significa muchas respuestas (pruebas 02 y 03);
- un coseno en [−1, 1] no basta: hay que excluir los triángulos
  degenerados y comprobar el orden cíclico (prueba 07).

## Soluciones optimizadas

`1294_geometry_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado.

Frente a `1294_geometry.java`: tiempo 0.109 s → 0.093 s; memoria 1 600 KB → 452 KB.

Rust factoriza el cuadrado de la cuerda en numerador y denominador enteros tras comprobar la unicidad geométrica. Escala el cuadrado racional para obtener el doble de la distancia en kilómetros, separando cociente y resto antes de multiplicar. Corrige la estimación de raíz con cuadrados enteros y usa su parte entera para redondear, sin formato de coma flotante. La entrada y la respuesta completa usan búferes fijos de bytes. Rust lee y escribe mediante la biblioteca de ejecución de C.

El envío aceptado en Rust 1.75 x64 tarda 0.031 s frente a 0.015 s de la base y usa 56 KB frente a 220 KB.

Las implementaciones base aceptadas [1294_geometry.cpp](1294_geometry.cpp), [1294_geometry.go](1294_geometry.go), [1294_geometry.java](1294_geometry.java), [1294_geometry.py](1294_geometry.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1294_geometry_parsing_implementation_optimized.go`. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios. Un búfer recargable de 8192 bytes sustituye el almacenamiento de toda la entrada, manteniendo tokens, lecturas parciales y fin de archivo.

Accepted #11328935 (Go 1.14 x64): **0.015 s / 804 KB**. Comparación archivada: `1294_geometry.go` (Go 1.14 x64) — 0.015 s / 1080 KB (#11325573).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

`1294_geometry_optimized.java`: puesto de tiempo 5/20 y de memoria 2/20 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1294_geometry.cpp](1294_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.001 s | 112 KB | 11325577 |
| [1294_geometry.go](1294_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1080 KB | 11325573 |
| [1294_geometry.java](1294_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1600 KB | 11325554 |
| [1294_geometry.py](1294_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 424 KB | 11330228 |
| [1294_geometry.rs](1294_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 220 KB | 11325604 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1294_geometry_optimized.rs](1294_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 56 KB | 11311233 |
| [1294_geometry_optimized.java](1294_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 452 KB | 11325015 |
| [1294_geometry_parsing_implementation_optimized.go](1294_geometry_parsing_implementation_optimized.go) | Go 1.14 x64 | geometry, parsing, implementation | O(1) | AC | 0.015 s | 804 KB | 11328935 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
