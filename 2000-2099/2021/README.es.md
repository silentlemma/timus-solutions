# 2021. Retrasar la Certeza del Ganador

[Timus 2021](https://acm.timus.ru/problem.aspx?space=1&num=2021) · dificultad 462 · sorting

Problema original de Oleg Dolgorukov, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos equipos tienen `n` participantes cada uno, con puntuaciones enteras
predeterminadas de 0 a 6. Organice `n` rondas, con una persona de cada
equipo por ronda y cada participante exactamente una vez. Las dos
puntuaciones de la ronda se anuncian simultáneamente. Gana el equipo de
mayor suma final; si las sumas coinciden, hay empate. El público solo
conoce los límites de puntuación.

Elija ambos órdenes para retrasar al máximo la primera ronda en que los
resultados anunciados garanticen un equipo ganador. Tras `k` rondas, con
`r=n−k` restantes y diferencia `d`, hay victoria garantizada si y solo si
`|d| > 6r`. La igualdad todavía permite un empate. Si no se garantiza una
victoria antes, todo el resultado se conoce al terminar la última ronda.

Se cumple `2 ≤ n ≤ 1 000`, con puntuaciones entre 0 y 6.
Límites: 1 segundo y 64 MB.

## Entrada

La primera línea contiene `n`; la segunda y la tercera, los `n` puntos de
cada equipo. Sus participantes se numeran independientemente de 1 a `n`
en el orden de entrada.

## Salida

Imprima `n` líneas con los dos índices de la ronda, primero del primer
equipo y luego del segundo. Cada columna debe ser una permutación completa.
Se admite cualquier orden globalmente óptimo.

## Evaluación

Un comprobador verifica ambas permutaciones, reproduce las puntuaciones
y acepta cualquier orden cuya primera ronda decisiva sea la más tardía
posible.

## Ejemplos

```
5
0 1 4 3 6
6 5 1 3 0
```

```
5 1
1 5
4 4
2 3
3 2
```

## Solución

Compare las **sumas finales**, independientes del orden. Si gana el primer
equipo, ordene sus participantes por puntos crecientes y los del segundo por
puntos decrecientes. Si gana el segundo, intercambie las direcciones. En
empate sirve cualquier orden; el programa ordena ambos crecientemente.
Conserve los índices originales y empareje ambas listas por posición.

Suponga que el primero gana por una diferencia final `D>0`. Tras cualquier
prefijo con `r` rondas pendientes, sea `R` la diferencia que añadirán quienes
quedan. Cada ronda aporta de −6 a 6, luego `R≤6r` y
`d=D−R≥D−6r>−6r`. El equipo que acabará perdiendo nunca puede tener una
victoria garantizada en ningún orden. Solo importa la barrera superior `d>6r`.

Para cada longitud `k`, el orden creciente del primero toma la menor
suma posible de sus primeros `k` resultados; el decreciente del segundo
toma la mayor suma rival. Juntos minimizan `d(k)` entre **todos** los
órdenes y para cada `k` a la vez. Si esta programación garantiza
victoria por primera vez en `k<n`, cualquier otra tiene una diferencia
al menos igual en esa ronda y ya garantiza victoria. Ninguna puede
retrasarla más. Llegar a la última ronda ya consigue el máximo retraso
posible. El otro ganador es simétrico.

Cuando `D=0`, todo prefijo cumple `d=−R`, de donde `|d|≤6r`. Ningún orden
garantiza ganador antes de revelarse el empate final, así que todos son
óptimos. Una gran ventaja temporal del futuro perdedor no causa certeza
prematura: las puntuaciones reales restantes impiden rebasar la barrera.

En el ejemplo las sumas finales son 14 y 15. Las primeras cuatro parejas
mostradas dan los mismos puntos a ambos equipos y la última da 4 frente a 5.
El ganador solo se conoce en la quinta ronda, lo que es óptimo.

Ordenar dos listas de índices cuesta `O(n log n)` tiempo y `O(n)` espacio.
Las sumas y diferencias tienen magnitud máxima 6 000; bastan enteros ordinarios.

Trampas:

- Determinar las direcciones con las sumas finales, no con la ventaja actual.
- Usar `|d| > 6r` estrictamente: la igualdad todavía permite empate.
- Anunciar ambos puntos juntos y usar cada índice una vez en su propio equipo.
- Emitir índices originales desde uno, no puntos ni posiciones ordenadas.
- Admitir cualquier óptimo, incluidos todos los órdenes cuando empatan
  los totales.

## Soluciones optimizadas

`2021_sorting_greedy.java`. El mismo orden voraz de puntuaciones extremas usa siete cubetas enlazadas. Guarda solo vectores next-ID y cabezas por puntuación, acumulando totales. Equipo de total menor desciende y el mayor asciende; empate ambos ascienden. Insertar en cabeza invierte IDs de igual puntuación, permitido pues no cambia puntuaciones ni certeza. O(N+7) tiempo/espacio más I/O de 1024 bytes, sin offsets prefijos, ordenación con objetos ni matriz/cadena completa. Nombre sorting_greedy; conserva alternativa estable con prefijos y base de ordenación. Certeza estricta |difference|>6*remaining.

Fuente exacto: Java 1.8 Accepted #11327334: 0.093 s / 524 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 2/47; 1/47. Admisión estricta usa solo tiempo bajo 1024 KB: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Conserva asterisco por la meta propia de primer puesto en ambas. La variante anterior conservada tiene su par propio #11325033 (Java 1.8): 0.14 s / 496 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `2021_sorting_greedy.java`: 0.093 s / 524 KB; base didáctica conservada `2021_sorting.java` (Java 1.8): 0.14 s / 2824 KB.

`2021_sorting_prefix_sums.java`. Conserva el orden extremo de puntuaciones que retrasa certeza, pero reemplaza comparación con objetos por conteo estable de siete puntuaciones0..6. Extremos prefijos y relleno inverso mantienen IDs empatados. Equipo de menor total desciende y el mayor asciende; con empate ambos ascienden. Invierte al indexar, sin copias. sorting_prefix_sums cuesta O(n+7) y O(n) espacio, sin IDs con objetos, matriz de parejas ni cadena completa. La certeza sigue siendo estricta: |difference|>6·remaining.

Frente a `2021_sorting.java`: tiempo 0.14 s → 0.14 s; memoria 2 824 KB → 496 KB.

C++, Go y Rust sustituyen la comparación por S=7 cubetas de puntuación. Una lista enlazada por puntuación guarda un siguiente de 16 bits por participante. Según los totales finales, el ganador recorre cubetas crecientes y el perdedor decrecientes; con empate ambos crecientes. Cada equipo mantiene un cursor y extrae un ID por ronda: cada cubeta y participante se visita una vez, tiempo y espacio O(n+S). Sigue vigente la prueba de minimizar prefijos; el orden entre empates es libre. Go/Rust reservan 10000 bytes de salida, suficientes para 1000 filas de dos IDs de hasta cuatro cifras. Se conservan las bases; Java/Python reutilizan las admitidas.

Las implementaciones base aceptadas [2021_sorting.java](2021_sorting.java), [2021_sorting.py](2021_sorting.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

`2021_sorting_prefix_sums.java`: puesto de tiempo 22/47 y de memoria 1/47 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2021_sorting.cpp](2021_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 472 KB | 11292703 |
| [2021_sorting.go](2021_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.015 s | 1252 KB | 11292708 |
| [2021_sorting.java](2021_sorting.java) \* | Java 1.8 | sorting | O(n log n) | AC | 0.14 s | 2824 KB | 11325567 |
| [2021_sorting.py](2021_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.093 s | 764 KB | 11292714 |
| [2021_sorting.rs](2021_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.015 s | 340 KB | 11292728 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2021_sorting_greedy.cpp](2021_sorting_greedy.cpp) | G++ 13.2 x64 | sorting, greedy | O(n + S) | AC | 0.015 s | 88 KB | 11315199 |
| [2021_sorting_greedy.go](2021_sorting_greedy.go) \* | Go 1.14 x64 | sorting, greedy | O(n + S) | AC | 0.015 s | 284 KB | 11315209 |
| [2021_sorting_greedy.rs](2021_sorting_greedy.rs) \* | Rust 1.75 x64 | sorting, greedy | O(n + S) | AC | 0.015 s | 56 KB | 11315222 |
| [2021_sorting_prefix_sums.java](2021_sorting_prefix_sums.java) \* | Java 1.8 | sorting, prefix_sums | O(n+7) | AC | 0.14 s | 496 KB | 11325033 |
| [2021_sorting_greedy.java](2021_sorting_greedy.java) | Java 1.8 | sorting, greedy | O(N+7) time and storage + bounded I/O | AC | 0.093 s | 524 KB | 11327334 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
