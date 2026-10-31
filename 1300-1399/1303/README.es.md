# 1303. Cobertura mínima

[Timus 1303](https://acm.timus.ru/problem.aspx?space=1&num=1303) · dificultad 174 · greedy

Problema original del Segundo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 3–4 de abril de 1998.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados entre 1 y 99 999 segmentos [Li, Ri] con extremos enteros
(−50 000 ≤ Li < Ri ≤ 50 000), hay que elegir el menor número de ellos
que juntos cubran [0, M], 1 ≤ M ≤ 5000. Se imprime cuántos son y los
segmentos elegidos en orden creciente de extremo izquierdo, o
`No solution`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

M y luego los segmentos, un par por línea, terminados por el par `0 0`.

## Salida

La cantidad y luego los segmentos, uno por línea, o `No solution`.

## Evaluación

Se acepta cualquier cobertura mínima. El verificador comprueba que la
cantidad es la mínima, que cada segmento impreso aparece en la entrada
(no más veces que allí), que los extremos izquierdos no decrecen y que
los segmentos no dejan ningún punto de [0, M] sin cubrir. Si no existe
cobertura, la salida debe ser `No solution`.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
-1 0
-5 -3
2 5
0 0
```

Salida:

```
No solution
```

### Ejemplo 2

Entrada:

```
1
-1 0
0 1
0 0
```

Salida:

```
1
0 1
```

## Solución

El voraz clásico. Se guarda el extremo derecho c de la parte [0, c] ya
cubierta, empezando con c = 0. Entre los segmentos con L ≤ c se toma el
de mayor R. Si ni ese R pasa de c, un punto justo a la derecha de c no
se puede cubrir nunca: `No solution`. Si no, se toma y c = R. Se para
cuando c ≥ M.

Tomar el que llega más lejos es seguro: el segmento que use una
cobertura óptima en ese punto no termina más lejos, así que cambiarlo
por el nuestro mantiene la cobertura y la cantidad.

Con los segmentos ordenados por extremo izquierdo, un puntero los
recorre una sola vez, porque un segmento que se pasó una vez no puede
ayudar después (su R no supera el c actual). Los segmentos elegidos
salen solos en orden creciente de extremo izquierdo. `O(N log N)` por
la ordenación.

Detalles a tener en cuenta:

- cubrir significa no dejar huecos dentro de [0, M]: segmentos que
  solo se tocan en un punto, como [0, 2] y [2, 5], valen (prueba 04),
  pero [0, 4] y [5, 10] dejan un hueco (prueba 06);
- un segmento que termina en 0 no ayuda (pruebas 02 y 09);
- el par `0 0` es solo la marca de fin, porque todo segmento real
  tiene L < R.

Las cantidades del voraz se compararon con una búsqueda en anchura
sobre los extremos derechos alcanzables en 400 entradas aleatorias
pequeñas.

## Soluciones optimizadas

La solución optimizada en C++ no guarda ni ordena los segmentos. Como
los extremos son enteros y M ≤ 5000, mantiene un cubo por cada extremo
izquierdo de 0 a M − 1 con el segmento que llega más lejos desde allí;
los segmentos que empiezan antes de 0 comparten el cubo de 0, y los que
empiezan en M o después o terminan en 0 o antes se descartan, porque
nunca ayudan. Con alcances iguales el cubo guarda el extremo izquierdo
menor, así que se imprime el mismo recubrimiento. Después el voraz
recorre los M cubos una vez: tiempo `O(N + M)` y memoria `O(M)`. Los
números se analizan a mano desde bloques de 4 KB en lugar de con
`scanf`: {1303_greedy_optimized.cpp}.

La solución optimizada en Go no guarda ni ordena los segmentos. Como los
extremos son enteros y M ≤ 5000, mantiene un cubo por cada extremo
izquierdo de 0 a M − 1 con el segmento que llega más lejos desde allí;
los segmentos que empiezan antes de 0 comparten el cubo de 0, y los que
empiezan en M o después o terminan en 0 o antes se descartan, porque
nunca ayudan. Con alcances iguales el cubo guarda el extremo izquierdo
menor, así que se imprime el mismo recubrimiento. Después el voraz
recorre los M cubos una vez: tiempo `O(N + M)` y memoria `O(M)`. Los
números se analizan byte a byte desde el lector con búfer en lugar de
como palabras de un `bufio.Scanner`: {1303_greedy_optimized.go}.

La solución optimizada en Java no guarda ni ordena los segmentos. Como
los extremos son enteros y M ≤ 5000, mantiene un cubo por cada extremo
izquierdo de 0 a M − 1 con el segmento que llega más lejos desde allí;
los segmentos que empiezan antes de 0 comparten el cubo de 0, y los que
empiezan en M o después o terminan en 0 o antes se descartan, porque
nunca ayudan. Con alcances iguales el cubo guarda el extremo izquierdo
menor, así que se imprime el mismo recubrimiento. Después el voraz
recorre los M cubos una vez: tiempo `O(N + M)` y memoria `O(M)`, en
lugar de un arreglo de hasta 99 999 pares `long[]` ordenado con un
comparador. Los números se analizan a mano desde bloques de 4 KB en
lugar de con `StreamTokenizer`: {1303_greedy_optimized.java}.

La solución optimizada en Python no guarda ni ordena los segmentos. Como
los extremos son enteros y M ≤ 5000, mantiene un cubo por cada extremo
izquierdo de 0 a M − 1 con el segmento que llega más lejos desde allí;
los segmentos que empiezan antes de 0 comparten el cubo de 0, y los que
empiezan en M o después o terminan en 0 o antes se descartan, porque
nunca ayudan. Con alcances iguales el cubo guarda el extremo izquierdo
menor, así que se imprime el mismo recubrimiento. Después el voraz
recorre los M cubos una vez: tiempo `O(N + M)` y memoria `O(M)`. La
entrada se lee línea a línea, contando con un par por línea, en lugar de
leerla y partirla entera de una vez: {1303_greedy_optimized.py}.

La solución optimizada en Rust no guarda ni ordena los segmentos. Como
los extremos son enteros y M ≤ 5000, mantiene un cubo por cada extremo
izquierdo de 0 a M − 1 con el segmento que llega más lejos desde allí;
los segmentos que empiezan antes de 0 comparten el cubo de 0, y los que
empiezan en M o después o terminan en 0 o antes se descartan, porque
nunca ayudan. Con alcances iguales el cubo guarda el extremo izquierdo
menor, así que se imprime el mismo recubrimiento. Después el voraz
recorre los M cubos una vez: tiempo `O(N + M)` y memoria `O(M)`. La
entrada se lee línea a línea, contando con un par por línea, en lugar de
leerla entera en una cadena: {1303_greedy_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1303_greedy_optimized.cpp`: reducción de tiempo +88.00%; reducción de
  memoria +87.46%; base: `1303_greedy.cpp`.

- `1303_greedy_optimized.go`: reducción de tiempo +67.39%; reducción de
  memoria +85.08%; base: `1303_greedy.go`.

- `1303_greedy_optimized.java`: reducción de tiempo +57.34%; reducción
  de memoria +89.70%; base: `1303_greedy.java`.

- `1303_greedy_optimized.py`: reducción de tiempo +31.60%; reducción de
  memoria +95.40%; base: `1303_greedy.py`.

- `1303_greedy_optimized.rs`: reducción de tiempo -106.67%; reducción de
  memoria +93.76%; base: `1303_greedy.rs`.

## Notas por lenguaje

- Todos los lenguajes deshacen los empates igual, con el primer
  segmento en el orden de clasificación, así que imprimen la misma
  cobertura.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1303_greedy.cpp](1303_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.125 s | 1372 KB | 11284796 |
| [1303_greedy.go](1303_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.046 s | 8068 KB | 11284802 |
| [1303_greedy.java](1303_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.218 s | 8312 KB | 11284806 |
| [1303_greedy.py](1303_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.250 s | 24780 KB | 11284804 |
| [1303_greedy.rs](1303_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 3716 KB | 11284810 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1303_greedy_optimized.cpp](1303_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N + M) | AC | 0.015 s | 172 KB | 11307319 |
| [1303_greedy_optimized.go](1303_greedy_optimized.go) | Go 1.14 x64 | greedy | O(N + M) | AC | 0.015 s | 1204 KB | 11307326 |
| [1303_greedy_optimized.java](1303_greedy_optimized.java) | Java 1.8 | greedy | O(N + M) | AC | 0.093 s | 856 KB | 11307323 |
| [1303_greedy_optimized.py](1303_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(N + M) | AC | 0.171 s | 1140 KB | 11307328 |
| [1303_greedy_optimized.rs](1303_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(N + M) | AC | 0.031 s | 232 KB | 11307329 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
