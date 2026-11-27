# 1416. Confidencial

[Timus 1416](https://acm.timus.ru/problem.aspx?space=1&num=1416) · dificultad 385 · graphs

Problema original de Den Raskovalov, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo conexo tiene n vértices (2 ≤ n ≤ 500) y m aristas con costes
de 0 a 1000, con como mucho una arista entre dos vértices. Hay que
imprimir el coste de un árbol generador mínimo y el coste del siguiente
árbol generador por coste (que puede ser igual al primero), o −1 si no
hay otro árbol generador.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Primera línea: n vértices y m aristas no dirigidas, 2≤n≤500 y 1≤m≤n(n−1)/2. Siguen m líneas con extremos a,b en 1..n y coste w en 0..1000. No hay bucles ni aristas paralelas y el grafo es conexo.

## Salida

«Cost: » y el primer coste, luego «Cost: » y el segundo.

## Comprobación

Se compara exactamente la salida completa tras quitar sólo espacio en blanco final: dos líneas con Cost: y los costes del primer y segundo árbol. Importan mayúsculas, dos puntos, el espacio siguiente y salto interior. El segundo coste puede igualar el primero; -1 sólo si no existe otro conjunto de aristas de árbol generador.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 6
1 2 2
2 3 2
3 4 2
4 1 2
1 3 1
2 4 1
```

Salida:

```
Cost: 4
Cost: 4
```

### Ejemplo 2

Entrada:

```
3 2
1 2 2
2 3 2
```

Salida:

```
Cost: 4
Cost: -1
```

## Solución

Un segundo mejor árbol generador difiere de algún árbol mínimo en
exactamente una arista: entra una arista de fuera del árbol y sale la
arista más pesada del camino del árbol entre sus extremos. Así que el
segundo coste es el mínimo más el menor valor de w − (arista más pesada
del camino) entre las aristas de fuera del árbol, y −1 si todas las
aristas están en el árbol.

Con hasta 500 vértices, el algoritmo de Prim sobre la matriz de costes
cuesta O(n²). La arista más pesada de cada camino del árbol sale de
paso: cuando el vértice v entra por el padre p con una arista de coste
c, para cada vértice u ya en el árbol
heaviest(u, v) = max(heaviest(u, p), c). `O(n² + m)`.

Detalles a tener en cuenta:

- el segundo árbol puede costar lo mismo que el primero (prueba 01);
- un grafo que ya es un árbol no tiene segundo árbol (pruebas 02, 03,
  gen2);
- los costes pueden ser 0 (pruebas 04, 06).

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

La versión compacta en C++ mantiene la recurrencia de Prim y usa entradas de 16 bits para ambas matrices. Al incorporar una arista al árbol, se marca como ausente en la matriz de pesos. Los dos extremos ya están en el árbol y el cambio no afecta a Prim. La pasada final solo examina aristas externas al árbol y puede detenerse si el coste adicional es cero.

El conjunto rápido reutiliza las bases válidas Java/Python y usa C++, Go y Rust optimizados. Go/Rust sencillos se conservan para enseñanza, pero incumplen los límites de memoria actuales y no se presentan como fuentes rápidas válidas. No se duplican fuentes idénticos; los pares históricos Accepted permanecen en sus versiones.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1416_graphs_parsing_implementation_optimized.go`. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios. Un búfer recargable de 8192 bytes sustituye el almacenamiento de toda la entrada, manteniendo tokens, lecturas parciales y fin de archivo.

Accepted #11328937 (Go 1.14 x64): **0.031 s / 8892 KB**. Comparación archivada: `1416_graphs.go` (Go 1.14 x64) — 0.203 s / 10568 KB (#11286112).

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1416_graphs_implementation_optimized.rs`. Los pesos acotados y los extremos usan 32 bits; los totales de los árboles conservan 64 bits. Se mantienen ambos cálculos y su orden. Se leen tokens con un búfer nativo acotado; los cortos se guardan dentro del objeto y solo los largos reservan espacio extra. La conversión decimal conserva las cotas con signo sin guardar toda la entrada de comandos. La entrada de C llama directamente al solucionador y vacía la salida de Rust antes de volver; se conserva la implementación de entrada habitual.

Accepted #11328963 (Rust 1.75 x64): **0.031 s / 3908 KB**. Comparación archivada: `1416_graphs.rs` (Rust 1.75 x64) — 0.015 s / 9656 KB (#11286115).

## Notas por lenguaje

Las bases guardan matrices de pesos, máximos de caminos y pertenencia al árbol, una lista de aristas y O(n) estado Prim: espacio auxiliar O(n²+m). Los analizadores completos, especialmente Python/Rust sencillo, retienen además I bytes/tokens de entrada, total O(n²+m+I). C++ compacto usa dos matrices uint16, marca aristas del árbol como ausentes y recorre la matriz sin lista/matriz de pertenencia separada, espacio O(n²). El centinela supera todo peso≤1000. Go optimizado mantiene estructuras y rellena un búfer de 8192 bytes; Rust usa entrada acotada, campos de arista de 32 bits y totales de 64 bits. Todos mantienen tiempo algorítmico O(n²+m).

Los [criterios comunes](../../RATING_CRITERIA.md) ignoran memoria sólo estrictamente bajo 1024 KB. C++ optimizado cumple ambas 1/89 y 2/89, Java sencilla ambas 1/14. Python sencilla cumple límites de tercera referencia entre ocho rivales exactos, 0.52095 s / 53847.60 KB. El rival Go da 1.8860 s / 9117.20 KB: optimizado de 8892 KB cumple, sencillo de 10568 KB incumple memoria. El rival Rust da 0.1610 s / 7015 KB: optimizado de 3908 KB cumple, sencillo de 9656 KB no. Se excluyen rivales menores de 0.015 s y sólo nuestros tiempos usan suelo.

En `1416_graphs_parsing_implementation_optimized.go` los comentarios describen entrada con relleno y salida formateada sólo %d; se nombra la capacidad inline de 128 bytes sin cambiarla. Valores, algoritmo y explicaciones sustantivas intactos.

En `1416_graphs_implementation_optimized.rs` sólo se nombran constantes exigidas por el lint; valores, algoritmo y comentarios no cambian. Accepted #11328963 y sus medidas corresponden a los bytes exactos previos.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1416_graphs.cpp](1416_graphs.cpp) | G++ 13.2 x64 | graphs | O(n^2 + m) | AC | 0.187 s | 3448 KB | 11286111 |
| [1416_graphs.go](1416_graphs.go) | Go 1.14 x64 | graphs | O(n^2 + m) | AC | 0.203 s | 10568 KB | 11286112 |
| [1416_graphs.java](1416_graphs.java) | Java 1.8 | graphs | O(n^2 + m) | AC | 0.109 s | 8164 KB | 11286114 |
| [1416_graphs.py](1416_graphs.py) | Python 3.12 x64 | graphs | O(n^2 + m) | AC | 0.39 s | 44108 KB | 11328275 |
| [1416_graphs.rs](1416_graphs.rs) | Rust 1.75 x64 | graphs | O(n^2 + m) | AC | 0.015 s | 9656 KB | 11286115 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1416_graphs_optimized.cpp](1416_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(n^2 + m) | AC | 0.015 s | 1132 KB | 11310409 |
| [1416_graphs_parsing_implementation_optimized.go](1416_graphs_parsing_implementation_optimized.go) | Go 1.14 x64 | graphs, parsing, implementation | O(n^2 + m) | AC | 0.046 s | 8900 KB | 11331024 |
| [1416_graphs_implementation_optimized.rs](1416_graphs_implementation_optimized.rs) | Rust 1.75 x64 | graphs, implementation | O(n^2 + m) | AC | 0.031 s | 3908 KB | 11331119 |
