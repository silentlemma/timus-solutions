# 1101. Un robot guiado por una expresión booleana

[Timus 1101](https://acm.timus.ru/problem.aspx?space=1&num=1101) · dificultad 527 · parsing, simulation

Problema original de Pavel Atnashev, del Tetrahedron Team Contest, mayo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un robot parte de `(0, 0)` en el campo `[−N..N] × [−N..N]` (`N ≤ 100`)
en la dirección `(1, 0)` y avanza de casilla en casilla. En cada una de
las `M ≤ 100` bifurcaciones evalúa una expresión booleana (hasta 250
caracteres, con `NOT`, `AND` y `OR` de mayor a menor prioridad,
paréntesis, `TRUE`, `FALSE` y los registros `A`–`Z`, todos `FALSE` al
principio) y gira a la derecha si el valor es `TRUE`, a la izquierda si
no. Cada una de otras `K ≤ 100` casillas invierte un registro cuando el
robot está en ella. Imprime cada casilla de la ruta del robot hasta que
sale del campo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La expresión; `N`, `M` y `K`; `M` líneas con una bifurcación; `K` líneas
con una casilla y el registro que invierte.

## Salida

Las casillas de la ruta, una por línea.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
NOT((A OR NOT B) AND (A OR B)) OR NOT (A AND NOT B OR TRUE)
1 5 2
1 0
1 1
1 -1
-1 -1
-1 1
0 1 A
-1 0 D
```

Salida:

```
0 0
1 0
1 -1
0 -1
-1 -1
-1 0
-1 1
0 1
1 1
```

## Solución

La expresión se parte en palabras (`NOT`, `AND`, `OR`, `TRUE`, `FALSE`,
un registro) y paréntesis, y se construye un árbol una sola vez por
descenso recursivo con una función por nivel de prioridad: un `OR` de
`AND`s de `NOT`s de átomos, donde un átomo es una constante, un registro
o una expresión entre paréntesis.

Después se camina. En cada casilla dentro del campo: se imprime; si es un
interruptor, se invierte su registro; si es una bifurcación, se evalúa el
árbol y se gira a la derecha (`(dx, dy) → (dy, −dx)`) con `TRUE` o a la
izquierda (`(dx, dy) → (−dy, dx)`) con `FALSE`; se avanza un paso. Se para
en cuanto el robot queda fuera del campo. `O(L · |E|)` para una ruta de
`L` casillas y una expresión de longitud `|E|`.

Detalles a tener en cuenta:

- `NOT A AND B` significa `(NOT A) AND B`, y `A OR B AND C` significa
  `A OR (B AND C)`;
- las palabras pueden ir pegadas a los paréntesis, como en
  `NOT(A OR(B))`, así que se recortan del texto en lugar de partirlo por
  los espacios;
- el giro depende de los registros en el momento en que el robot llega a
  la bifurcación, tras los interruptores que ya pasó.

Las respuestas se comprobaron con un recorrido que traduce la expresión
a `not`, `and` y `or` de Python, que tienen las mismas prioridades, y la
evalúa con `eval`.

## Soluciones optimizadas

C++ y Go usan descenso recursivo con prioridad NOT > AND > OR para generar código posfijo y reunir la máscara de registros que lee la expresión. Los registros ocupan 26 bits. En cada cruce se reutiliza el último resultado si los bits relevantes coinciden con la máscara guardada. Si difieren o aún no hay un resultado, se ejecuta todo el código con una pila booleana. Cada casilla ocupa un byte y un búfer de 8192 bytes permite imprimir la ruta a medida que se recorre. Se imprime cada casilla antes de accionar su interruptor o girar. Sean E la longitud de la expresión, S las casillas impresas y F las visitas a cruces que requieren evaluación. Preparar la rejilla cuesta O(N²). El tiempo total es O(N² + E + S + FE) y el espacio es O(N² + E). Las bases de Java, Python y Rust también cubren las versiones rápidas.

El envío aceptado en G++ 13.2 x64 tarda 0.031 s frente a 0.015 s de la base y usa 224 KB frente a 628 KB.

Las implementaciones base aceptadas [1101_parsing.java](1101_parsing.java), [1101_parsing.py](1101_parsing.py), [1101_parsing.rs](1101_parsing.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Los originales conservan árboles y sus propios Accepted. C++/Go nuevos usan postfix fijo, rejilla de bytes y salida acotada, cacheando solo registros pertinentes. La rejilla ocupa O(N²) incluso con pocos objetos, pero la ruta no se acumula. Las ganancias dependen del envío medido, sin prometer acelerar toda expresión.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1101_parsing.cpp](1101_parsing.cpp) | G++ 13.2 x64 | parsing | O(L·len(E)) | AC | 0.015 s | 628 KB | 11279157 |
| [1101_parsing.go](1101_parsing.go) | Go 1.14 x64 | parsing | O(L·len(E)) | AC | 0.031 s | 1780 KB | 11279158 |
| [1101_parsing.java](1101_parsing.java) \* | Java 1.8 | parsing | O(L·len(E)) | AC | 0.093 s | 2192 KB | 11279160 |
| [1101_parsing.py](1101_parsing.py) \* | Python 3.12 x64 | parsing | O(L·len(E)) | AC | 0.078 s | 1408 KB | 11279159 |
| [1101_parsing.rs](1101_parsing.rs) \* | Rust 1.75 x64 | parsing | O(L·len(E)) | AC | 0.015 s | 552 KB | 11279161 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1101_parsing_optimized.cpp](1101_parsing_optimized.cpp) \* | G++ 13.2 x64 | parsing | O(N² + E + S + FE) | AC | 0.031 s | 224 KB | 11315671 |
| [1101_parsing_optimized.go](1101_parsing_optimized.go) \* | Go 1.14 x64 | parsing | O(N² + E + S + FE) | AC | 0.031 s | 912 KB | 11315890 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
