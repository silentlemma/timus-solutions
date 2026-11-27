# 1362. Compañeros de clase 2

[Timus 1362](https://acm.timus.ru/problem.aspx?space=1&num=1362) · dificultad 442 · dp

Problema original de Evgeny Krokhalev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una agencia de N ≤ 100 000 empleados es un árbol: todos salvo el
director tienen exactamente un jefe. Tanya tiene una noticia, y quien
la conoce puede llamar a su jefe o a uno de sus subordinados directos;
una llamada dura un minuto, y cada persona hace una sola llamada a la
vez. Hay que imprimir el menor número de minutos hasta que toda la
agencia lo sepa. Es la versión en árbol de
[1323](../1323/README.es.md).

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

1 ≤ N ≤ 100000 empleados tienen ID únicos de 1 a N. Siguen N líneas: la línea K enumera subordinados directos de K y termina en 0. La última línea da el ID de Tanya en el mismo rango; la jerarquía es un árbol.

## Salida

El menor número de minutos.

## Comprobación

Comparación de tokens (`judging: tokens`): un entero, el mínimo tiempo transcurrido en minutos; se ignoran separadores blancos.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
2 3 0
4 5 0
6 0
0
0
0
4
```

Salida:

```
4
```

## Solución

Las llamadas van hacia arriba y hacia abajo, así que el jefe es un
vecino más. Se enraíza el árbol en Tanya; entonces la noticia entra en
cada subárbol una sola vez, por su raíz.

Sea time(v) los minutos que v necesita para avisar a todo su subárbol
tras conocer la noticia. Si v llama a sus hijos en cierto orden, el
hijo i-ésimo se entera en el minuto i y termina en i + time(hijo). El
mejor orden llama primero al subárbol más lento: se ordenan los tiempos
de los hijos de mayor a menor t₁ ≥ t₂ ≥ …, y time(v) = max(tᵢ + i).
Intercambiar dos vecinos que no siguen este orden nunca empeora el resultado, lo que
lo demuestra.

El árbol se recorre en anchura y los tiempos se calculan desde las
hojas hacia arriba, así que ni una cadena de 100 000 necesita
recursión. `O(N log N)`.

Todas las bases conservan O(N) datos de árbol, recorrido, DP y tiempos de hijos. C++/Go/Java en flujo añaden búferes acotados; Python/Rust retienen toda la entrada: O(N+I), I bytes de entrada. Listas de hijos y mayor fila temporal de ordenación suman O(N), sin pila recursiva.

Detalles a tener en cuenta:

- el director no siempre es la raíz: si Tanya es subordinada, la noticia sube y
  luego baja por otras ramas (pruebas 03 y 04);
- una cadena de 100 000 es demasiado profunda para la recursión en la
  mayoría de los lenguajes (prueba generada 2);
- una estrella de 100 000 necesita 99 999 minutos, una llamada cada vez
  (prueba generada 3).

Las respuestas se compararon con una búsqueda sobre todas las formas de
llamar, minuto a minuto, en 400 árboles aleatorios de hasta 8
empleados.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

C++, Go y Rust conservan la llamada primero al subárbol más lento. Cada empleado guarda jefe original, primer hijo y siguiente hermano; enumeran vecinos no dirigidos sin contenedores por vértice ni objetos duplicados por arista. Un orden BFS plano y padres enraízan en el informador; su jefe original es otro vecino y el director puede ser distinto. Se procesa al revés, reuniendo tiempos de hijos en un prefijo reutilizado, ordenando de mayor a menor y tomando max(time[i]+i+1). Las hojas requieren cero. Identificadores y tiempos caben en 32 bits: un horario secuencial termina en N−1 minutos. Tiempo O(N log N), árbol O(N), sin recorrido recursivo. C++ y Go leen en flujo; Rust guarda la entrada y usa O(N+bytes de entrada). Se conservan las bases; Java reutiliza su base válida; Python usa una fuente optimizada separada.

El envío aceptado en Rust 1.75 x64 tarda 0.046 s frente a 0.031 s de la base y usa 3 948 KB frente a 15320 KB.

Java reutiliza su base con ambas métricas necesarias en puesto 1/22. Python usa [1362_dp_optimized.py](1362_dp_optimized.py), Accepted previo de fuente exacta #11328667, 0.312 s / 29520 KB. Siete rivales CPython exactos seleccionan la tercera referencia, límites 0.34040 s / 39495.60 KB: requiere y cumple ambas. La base didáctica 0.468 s / 33988 KB incumple tiempo. Los [criterios comunes](../../RATING_CRITERIA.md) excluyen memoria sólo estrictamente bajo 1024 KB; exactamente 1024 KB requiere ambas, excluyen rivales bajo 0.015 s y sólo nuestro tiempo usa suelo. C++ rápido cumple ambas 1/58; Go/Rust cumplen fallback antiguo del mismo lenguaje. Se conservan bases sin duplicados optimizados idénticos.

Siete archivos reciben sólo correcciones explicativas de comentarios: las cinco bases y Python rápido aclaran que la llamada i desde uno termina al minuto transcurrido i; Go rápido mueve el comentario del arreglo de trabajo junto al bucle inverso de recolección y ordenación. Algoritmos y comentarios útiles se conservan.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1362_dp_optimized.py`. Solo los nodos con hijos reciben listas de tiempos. Se ordenan in situ y el retraso se obtiene con un máximo directo, sin listas vacías para las hojas. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328667 (Python 3.12 x64): **0.312 s / 29520 KB**. Comparación archivada: `1362_dp.py` (Python 3.12 x64) — 0.468 s / 33988 KB (#11285503).

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Java guarda el árbol en arreglos planos y lee la entrada byte a byte;
  Go también la lee byte a byte.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1362_dp.cpp](1362_dp.cpp) | G++ 13.2 x64 | dp | O(N log N) | AC | 0.156 s | 8876 KB | 11331148 |
| [1362_dp.go](1362_dp.go) | Go 1.14 x64 | dp | O(N log N) | AC | 0.046 s | 17960 KB | 11331028 |
| [1362_dp.java](1362_dp.java) | Java 1.8 | dp | O(N log N) | AC | 0.109 s | 6912 KB | 11331053 |
| [1362_dp.py](1362_dp.py) | Python 3.12 x64 | dp | O(N log N) | AC | 0.484 s | 33412 KB | 11331080 |
| [1362_dp.rs](1362_dp.rs) | Rust 1.75 x64 | dp | O(N log N) | AC | 0.031 s | 15508 KB | 11331126 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1362_dp_optimized.cpp](1362_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N log N) | AC | 0.015 s | 2824 KB | 11315122 |
| [1362_dp_optimized.go](1362_dp_optimized.go) | Go 1.14 x64 | dp | O(N log N) | AC | 0.031 s | 4276 KB | 11331029 |
| [1362_dp_optimized.rs](1362_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N log N) | AC | 0.046 s | 3948 KB | 11315130 |
| [1362_dp_optimized.py](1362_dp_optimized.py) | Python 3.12 x64 | dp | O(N log N) | AC | 0.328 s | 29420 KB | 11331081 |
