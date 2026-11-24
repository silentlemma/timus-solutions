# 1427. SMS

[Timus 1427](https://acm.timus.ru/problem.aspx?space=1&num=1427) · dificultad 364 · greedy

Problema original de Dmitry Kovalioff, Nikita Rybak e Ilya Grebnov, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto de hasta 100 000 caracteres (letras latinas, espacios, cifras
y los signos . , ; : ! ? - ") se corta en mensajes SMS consecutivos. Un
mensaje de solo letras y espacios puede tener hasta M caracteres;
cualquier otro, solo hasta N (1 ≤ N ≤ M ≤ 10 000). Hay que hallar el
menor número de mensajes.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y M, luego el texto en su propia línea.

## Salida

El menor número de mensajes.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 15
On the 11-th of February, 2006 the contest "Timus Top Coders: First Challenge" is held!
```

Salida:

```
8
```

## Solución

Sea run(i) el número de letras y espacios seguidos desde la posición i.
Un mensaje que empieza en i puede terminar en cualquier punto hasta
i + max(N, min(M, run(i))). Este final más lejano nunca retrocede al
crecer i (tanto i + N como el final del tramo de letras solo crecen), y
con un alcance monótono así el voraz que siempre envía el mensaje más
largo posible es óptimo: cualquier otro plan nunca va más adelantado en
ningún paso. Los tramos se cuentan desde el final del texto. `O(L)`.

Detalles a tener en cuenta:

- el texto puede empezar con espacios, así que la segunda línea debe
  leerse entera y no tras saltar blancos (prueba 04);
- las cifras no cuentan como letras (pruebas 03, 06);
- la forma larga solo ayuda cuando el tramo de letras es más largo que
  N (prueba 05).

## Soluciones optimizadas

`1427_greedy_optimized.cpp`. Conserva la regla voraz de mensajes máximos y la clasificación de letras ASCII y espacios. Un búfer fread de4 KiB sustituye una llamada con bloqueo por byte. Descarta solo el resto del encabezado y CR/LF final; preserva espacios iniciales/finales y puntuación. Longitud y bandera de texto sencillo siguen determinando el siguiente mensaje. Tiempo O(L), espacio auxiliar fijo, sin guardar el texto completo.

Accepted del fuente exacto #11326989: 0.015 s / 88 KB. Muestra G++ 13.2 guardada el 2026-11-20: tiempo 1/67, memoria 1/67. Se conservan los fuentes didácticos.

`1427_greedy_optimized.py`. Mantiene elección voraz del alcance máximo e isalpha Unicode. En vez de array de rachas de longitud L, examina solo letras/espacios consumidos por mensaje hasta el máximo. Todo carácter examinado se consume antes de la siguiente iteración: O(L) total. Retiene línea UTF-8: O(L) espacio de entrada y O(1) estado adicional. Quita solo CR/LF, conservando espacios y puntuación.

Frente a `1427_greedy.py`: tiempo 0.093 s → 0.14 s; memoria 4392 KB → 1 852 KB.

C++ y Go amplían el mensaje actual mientras leen el texto. Guardan su longitud y si todos sus caracteres son letras o espacios. Si el carácter siguiente excedería el límite aplicable, cierran el mensaje y usan ese carácter para empezar otro. Es la misma regla voraz y usa tiempo O(L) y espacio adicional O(1).

Las bases aceptadas conservadas [1427_greedy.go](1427_greedy.go), [1427_greedy.java](1427_greedy.java), [1427_greedy.rs](1427_greedy.rs) cumplen la admisión estricta en la comparación guardada: diez primeros puestos o 15% superior en los indicadores requeridos. Se reutilizan sin copias idénticas y se conservan los otros fuentes didácticos. Un asterisco indica el objetivo de clasificación propio del lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1427_greedy_implementation_optimized.go`. El búfer de lectura baja a 8192 bytes y las longitudes de sufijo usan uint32. ReadString sigue leyendo líneas completas y espacios iniciales; no cambia el salto voraz. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios.

Accepted #11329094 (Go 1.14 x64): **0.015 s / 1668 KB**. Comparación archivada: `1427_greedy.go` (Go 1.14 x64) — 0.031 s / 3196 KB (#11286186).

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1427_greedy_implementation_parsing_optimized.rs`. Las longitudes acotadas de rachas de sufijo usan 32 bits en vez del tamaño de máquina. Se conservan la entrada por líneas y el algoritmo de comparación. Se usan lecturas nativas acotadas y escrituras nativas completas, descriptores binarios de Windows y entrada C. Los números se convierten directamente desde bytes a enteros con signo sin reservar tokens; las entradas sensibles a líneas conservan líneas completas.

Accepted #11329172 (Rust 1.75 x64): **0.015 s / 708 KB**. Comparación archivada: `1427_greedy.rs` (Rust 1.75 x64) — 0.031 s / 1252 KB (#11286189).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1427_greedy_optimized.py`: puesto de tiempo 4/11 y de memoria 5/11 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1427_greedy.cpp](1427_greedy.cpp) | G++ 13.2 x64 | greedy | O(L) | AC | 0.031 s | 924 KB | 11286185 |
| [1427_greedy.go](1427_greedy.go) | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 3196 KB | 11286186 |
| [1427_greedy.java](1427_greedy.java) | Java 1.8 | greedy | O(L) | AC | 0.093 s | 1612 KB | 11286188 |
| [1427_greedy.py](1427_greedy.py) | Python 3.12 x64 | greedy | O(L) | AC | 0.093 s | 4392 KB | 11286187 |
| [1427_greedy.rs](1427_greedy.rs) | Rust 1.75 x64 | greedy | O(L) | AC | 0.031 s | 1252 KB | 11286189 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1427_greedy_optimized.cpp](1427_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(L) | AC | 0.015 s | 88 KB | 11326989 |
| [1427_greedy_optimized.go](1427_greedy_optimized.go) | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 912 KB | 11310457 |
| [1427_greedy_optimized.py](1427_greedy_optimized.py) | PyPy 3.10 x64 | greedy | O(L) time; O(L) input space | AC | 0.14 s | 1852 KB | 11325485 |
| [1427_greedy_implementation_optimized.go](1427_greedy_implementation_optimized.go) | Go 1.14 x64 | greedy, implementation | O(L) | AC | 0.015 s | 1668 KB | 11329094 |
| [1427_greedy_implementation_parsing_optimized.rs](1427_greedy_implementation_parsing_optimized.rs) | Rust 1.75 x64 | greedy, implementation, parsing | O(L) | AC | 0.015 s | 708 KB | 11329172 |
