# 1521. Maniobras militares 2

[Timus 1521](https://acm.timus.ru/problem.aspx?space=1&num=1521) · dificultad 121 · fenwick

Problema original de Ilya Grebnov, Nikita Rybak y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N soldados (1 ≤ N ≤ 100000), numerados de 1 a N, marchan en círculo. En
cada ronda sale un soldado: primero el soldado K (1 ≤ K ≤ N), y luego
cada vez el que está K puestos por delante del último en salir,
contando solo los que siguen marchando. Hay que escribir los soldados
en el orden en que salen.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y K.

## Salida

Los números de los soldados en el orden en que salen.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
```

Salida:

```
3 1 5 2 4
```

## Solución

Se numeran los soldados que siguen marchando 0, 1, … en el orden del
círculo. Si el último en salir tenía el rango r entre ellos, el
siguiente tiene el rango (r + K − 1) mod (soldados restantes), porque
el puesto del que sale lo ocupa el soldado de detrás. Un árbol de
Fenwick guarda 1 por cada soldado que sigue marchando; descender por
potencias de dos encuentra el soldado de un rango dado en `O(log N)`,
y quitar un soldado es una actualización puntual. `O(N log N)` en
total.

Detalles a tener en cuenta:

- borrar de una lista simple cuesta `O(N)` por ronda, `O(N²)` en total,
  demasiado lento para 100000 soldados (gen1);
- con K = 1 los soldados salen en orden (prueba 03, gen5);
- con K = N empieza el último soldado (prueba 04, gen4).

## Soluciones optimizadas

La solución optimizada en C++ llena el árbol directamente, cada nodo con
la longitud de su intervalo, ya que al principio marchan todos los
soldados, y retira al soldado durante la propia búsqueda: los nodos
donde el descenso no avanza son justo aquellos cuyo intervalo contiene
al soldado encontrado, así que los decrementa por el camino en lugar de
hacer una segunda pasada. Guarda el árbol en un arreglo estático e
imprime cada número enseguida con `printf` en lugar de reunir la salida
en una cadena: {1521_fenwick_optimized.cpp}.

La solución optimizada en Go llena el árbol directamente, cada nodo con
la longitud de su intervalo, ya que al principio marchan todos los
soldados, y retira al soldado durante la propia búsqueda: los nodos
donde el descenso no avanza son justo aquellos cuyo intervalo contiene
al soldado encontrado, así que los decrementa por el camino en lugar de
hacer una segunda pasada. Los contadores son `int32`, que basta porque
no pasan de N ≤ 100000; N y K se leen byte a byte en lugar de con
`fmt.Scan`, y los números se formatean con `strconv.AppendInt` en un
único búfer reutilizado: {1521_fenwick_optimized.go}.

La solución optimizada en Java llena el árbol directamente, cada nodo
con la longitud de su intervalo, ya que al principio marchan todos los
soldados, y retira al soldado durante la propia búsqueda: los nodos
donde el descenso no avanza son justo aquellos cuyo intervalo contiene
al soldado encontrado, así que los decrementa por el camino en lugar de
hacer una segunda pasada. Lee N y K cifra a cifra desde `System.in` en
lugar de usar `BufferedReader` y `StringTokenizer`, y escribe los
dígitos con un `BufferedOutputStream` de 4 KB en lugar de reunir la
salida en un `StringBuilder`: {1521_fenwick_optimized.java}.

La solución optimizada en Python llena el árbol directamente, cada nodo
con la longitud de su intervalo, ya que al principio marchan todos los
soldados, y retira al soldado durante la propia búsqueda: los nodos
donde el descenso no avanza son justo aquellos cuyo intervalo contiene
al soldado encontrado, así que los decrementa por el camino en lugar de
hacer una segunda pasada. El árbol es un `array` de enteros sin signo de
32 bits, que basta porque los contadores no pasan de N ≤ 100000, en
lugar de una lista de enteros de Python, y las respuestas se imprimen en
tandas de 1024 en lugar de guardarse hasta el final:
{1521_fenwick_optimized.py}.

La solución optimizada en Rust llena el árbol directamente, cada nodo
con la longitud de su intervalo, ya que al principio marchan todos los
soldados, y retira al soldado durante la propia búsqueda: los nodos
donde el descenso no avanza son justo aquellos cuyo intervalo contiene
al soldado encontrado, así que los decrementa por el camino en lugar de
hacer una segunda pasada. Los contadores son `u32` en lugar de `usize`;
`u32` basta porque no pasan de N ≤ 100000, y los números pasan por un
`BufWriter` en lugar de reunirse en un `String`:
{1521_fenwick_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1521_fenwick_optimized.cpp`: reducción de tiempo -48.39%; reducción
  de memoria +75.84%; base: `1521_fenwick.cpp`.

- `1521_fenwick_optimized.go`: reducción de tiempo +25.81%; reducción de
  memoria +46.34%; base: `1521_fenwick.go`.

- `1521_fenwick_optimized.java`: reducción de tiempo +26.90%; reducción
  de memoria +82.85%; base: `1521_fenwick.java`.

- `1521_fenwick_optimized.py`: reducción de tiempo +4.84%; reducción de
  memoria +88.83%; base: `1521_fenwick.py`.

- `1521_fenwick_optimized.rs`: reducción de tiempo +0.00%; reducción de
  memoria +74.68%; base: `1521_fenwick.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1521_fenwick.cpp](1521_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(N log N) | AC | 0.031 s | 2136 KB | 11287371 |
| [1521_fenwick.go](1521_fenwick.go) | Go 1.14 x64 | fenwick | O(N log N) | AC | 0.062 s | 2460 KB | 11287372 |
| [1521_fenwick.java](1521_fenwick.java) | Java 1.8 | fenwick | O(N log N) | AC | 0.171 s | 5016 KB | 11287374 |
| [1521_fenwick.py](1521_fenwick.py) | Python 3.12 x64 | fenwick | O(N log N) | AC | 0.640 s | 12028 KB | 11287373 |
| [1521_fenwick.rs](1521_fenwick.rs) | Rust 1.75 x64 | fenwick | O(N log N) | AC | 0.031 s | 2512 KB | 11287375 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1521_fenwick_optimized.cpp](1521_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(N log N) | AC | 0.046 s | 516 KB | 11304369 |
| [1521_fenwick_optimized.go](1521_fenwick_optimized.go) | Go 1.14 x64 | fenwick | O(N log N) | AC | 0.046 s | 1320 KB | 11304370 |
| [1521_fenwick_optimized.java](1521_fenwick_optimized.java) \* | Java 1.8 | fenwick | O(N log N) | AC | 0.125 s | 860 KB | 11304371 |
| [1521_fenwick_optimized.py](1521_fenwick_optimized.py) \* | Python 3.12 x64 | fenwick | O(N log N) | AC | 0.609 s | 1344 KB | 11304372 |
| [1521_fenwick_optimized.rs](1521_fenwick_optimized.rs) | Rust 1.75 x64 | fenwick | O(N log N) | AC | 0.031 s | 636 KB | 11304373 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
