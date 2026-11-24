# 1158. Contar las frases de longitud M que evitan todas las palabras prohibidas

[Timus 1158](https://acm.timus.ru/problem.aspx?space=1&num=1158) · dificultad 500 · strings

Problema original de Nick Durov, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un alfabeto tiene `N ≤ 50` letras, y una frase es cualquier cadena de
exactamente `M ≤ 50` letras. Se dan `P ≤ 10` palabras prohibidas de como
mucho 10 letras; una frase está prohibida si contiene una de ellas como
subcadena. Cuenta las frases que no están prohibidas. Las letras pueden
ser cualquier carácter con código mayor que 32, incluidos los mayores que
127.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N`, `M` y `P`, luego las `N` letras en una línea y luego las `P`
palabras.

## Salida

El número de frases permitidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3 3
QWE
QQ
WEE
Q
```

Salida:

```
7
```

## Solución

Se construye el autómata de Aho–Corasick de las palabras prohibidas: un
trie con enlaces de fallo, completado para que cada estado tenga
transición con cada letra. Un estado representa el final más largo del
texto leído que es prefijo de alguna palabra; es malo si en él termina una
palabra, directamente o a través de sus enlaces de fallo. Una frase está
permitida justo cuando al leerla nunca se entra en un estado malo.

Así que se cuentan caminos: `ways[s]` es el número de comienzos
permitidos de la longitud actual que acaban en el estado `s`. Se empieza
con un comienzo vacío en la raíz y se dan `M` pasos, cada uno enviando
`ways[s]` por las `N` transiciones que no entran en un estado malo. La
respuesta es la suma sobre todos los estados. Con `S ≤ 101` estados,
se necesitan `O(M·S·N)` sumas, unas 5000 por paso.

Detalles a tener en cuenta:

- la cuenta llega a `50⁵⁰ ≈ 8,9·10⁸⁴`, así que hacen falta enteros
  grandes;
- una palabra que contiene otra ya es mala en la más corta, lo que
  transmiten los enlaces de fallo;
- las letras son bytes arbitrarios, quizá mayores que 127, así que la
  entrada se lee como bytes y no se decodifica como texto;
- la misma palabra puede darse dos veces.

Las respuestas se compararon con el listado de todas las frases en 200
entradas aleatorias pequeñas; las pruebas guardan las letras mayores que
127 como caracteres Latin-1 en UTF-8, y el programa de ejecución las pasa
a las soluciones como bytes sueltos.

La versión didáctica de Python representa cada estado por un prefijo propio de una palabra prohibida. Tras añadir una letra, descarta la transición si el sufijo es una palabra prohibida. Si no, elige el sufijo más largo entre los prefijos guardados, incluido el vacío. Todo prefijo más corto que pueda completar una palabra ya es sufijo del estado actual, así que la comprobación directa da las mismas transiciones que los enlaces de fallo. Con P palabras prohibidas de longitud máxima L, construir la tabla cuesta O(SN(P+S)L) y el conteo usa O(MSN) sumas.

## Soluciones optimizadas

Go y Rust conservan Aho–Corasick y conteo exacto. Hasta 101 estados y 50 letras permiten IDs de byte y cola fija. Primero propagar sufijos prohibidos y completar fallos; luego agrupar letras seguras con destino común en una arista con multiplicidad. Dos capas reutilizadas suman conteo por multiplicidad. Cada conteo≤50⁵⁰<10⁸⁵ cabe en diez bloques base10⁹; un bloque por multiplicidad≤50 cabe en uint64. Se conservan ceros y sufijos prohibidos heredados. Los bytes mayores de 127 se leen como letras. Sean W la longitud total de palabras prohibidas, S los estados, N las letras, E las aristas agrupadas y D≤10 los bloques por número. Construir y agrupar cuesta O(W+S(S+N)) por el recorrido de los contadores de destino de cada fila. Limpiar, comprobar y actualizar las capas DP cuesta O(M(S+E)D). El espacio es O(SN+SD) con búferes fijos. C++, Java y Python reutilizan las bases admitidas.

Las implementaciones base aceptadas [1158_strings.cpp](1158_strings.cpp), [1158_strings.java](1158_strings.java), [1158_strings.py](1158_strings.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Go/Python/Java originales usan enteros grandes; C++/Rust originales, bloques dinámicos de nueve cifras. Go/Rust nuevos usan dos capas fijas de diez bloques y autómatas de bytes, conservando Latin-1 sin módulos ni tablas de respuestas.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1158_strings.cpp](1158_strings.cpp) | G++ 13.2 x64 | strings | O(M·S·N) | AC | 0.015 s | 472 KB | 11281469 |
| [1158_strings.go](1158_strings.go) | Go 1.14 x64 | strings | O(M·S·N) | AC | 0.031 s | 1684 KB | 11281489 |
| [1158_strings.java](1158_strings.java) \* | Java 1.8 | strings | O(M·S·N) | AC | 0.109 s | 5476 KB | 11281536 |
| [1158_strings.py](1158_strings.py) \* | Python 3.12 x64 | strings | O(M·S·N) | AC | 0.093 s | 768 KB | 11281520 |
| [1158_strings.rs](1158_strings.rs) | Rust 1.75 x64 | strings | O(M·S·N) | AC | 0.031 s | 340 KB | 11281554 |
| [1158_dp_strings.py](1158_dp_strings.py) | Python 3.12 x64 | dp, strings | O(SN(P+S)L + MSN) | AC | 0.156 s | 584 KB | 11315835 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1158_strings_optimized.go](1158_strings_optimized.go) | Go 1.14 x64 | strings | O(W + S(S+N) + M(S+E)D) | AC | 0.015 s | 812 KB | 11315420 |
| [1158_strings_optimized.rs](1158_strings_optimized.rs) | Rust 1.75 x64 | strings | O(W + S(S+N) + M(S+E)D) | AC | 0.031 s | 204 KB | 11315424 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
