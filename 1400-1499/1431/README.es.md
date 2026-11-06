# 1431. Diplomas

[Timus 1431](https://acm.timus.ru/problem.aspx?space=1&num=1431) · dificultad 362 · greedy

Problema original de Stanislav Vasiliev, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N tipos de diplomas (N ≤ 18), de 1 a 30 de cada uno. Todos los
diplomas de un tipo cuelgan en una fila. Una fila tiene un tipo, o dos
tipos que se alternan estrictamente, y cada fila debe ser simétrica
respecto al centro de la pared. Hay que hallar el menor número de filas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego el número de diplomas de cada tipo.

## Salida

El menor número de filas.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
8 15 13 8 14 8
```

Salida:

```
5
```

## Solución

Una fila de un solo tipo siempre vale. Dos tipos que se alternan
estrictamente forman ABAB…, y esa fila se lee igual al revés solo si
empieza y acaba con el mismo tipo, A B A … B A, así que las cantidades
difieren exactamente en uno. La respuesta es N menos el mayor número de
pares disjuntos de tipos cuyas cantidades difieren en uno.

Los pares unen valores vecinos de una cadena 1, 2, …, 30. Subiendo por
la cadena, los tipos de cantidad c aún sin pareja solo pueden
emparejarse ya con la cantidad c + 1, así que emparejar en seguida tantos
como se pueda nunca es peor. `O(N + 30)`.

Detalles a tener en cuenta:

- cantidades iguales no pueden compartir fila: una fila alterna de
  longitud par no es simétrica (prueba 06);
- en 1, 2, 3, 4 los pares son 1–2 y 3–4, no 2–3 (prueba 07);
- varios tipos pueden tener la misma cantidad (pruebas 08, 12).

## Soluciones optimizadas

Go y Rust guardan las frecuencias de cantidades de uno a 30 en vectores de bytes. En cada cantidad emparejan tantos tipos como sea posible con los pendientes de la cantidad anterior. Cada pareja elimina una fila necesaria. Solo trasladan el resto sin pareja, sin lista ordenada ni grafo de emparejamiento. Ambas usan búferes fijos de bytes para la entrada y la salida decimal. Go accede directamente a los descriptores de entrada y salida estándar y Rust usa la biblioteca de ejecución de C.

El envío aceptado en Rust 1.75 x64 tarda 0.031 s frente a 0.015 s de la base y usa 56 KB frente a 220 KB.

Las implementaciones base aceptadas [1431_greedy.cpp](1431_greedy.cpp), [1431_greedy.java](1431_greedy.java), [1431_greedy.py](1431_greedy.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1431_greedy.cpp](1431_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + 30) | AC | 0.015 s | 128 KB | 11286206 |
| [1431_greedy.go](1431_greedy.go) | Go 1.14 x64 | greedy | O(N + 30) | AC | 0.015 s | 1076 KB | 11286207 |
| [1431_greedy.java](1431_greedy.java) \* | Java 1.8 | greedy | O(N + 30) | AC | 0.156 s | 1644 KB | 11286209 |
| [1431_greedy.py](1431_greedy.py) \* | Python 3.12 x64 | greedy | O(N + 30) | AC | 0.078 s | 420 KB | 11286208 |
| [1431_greedy.rs](1431_greedy.rs) | Rust 1.75 x64 | greedy | O(N + 30) | AC | 0.015 s | 220 KB | 11286210 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1431_greedy_optimized.go](1431_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(N + 30) | AC | 0.015 s | 348 KB | 11311231 |
| [1431_greedy_optimized.rs](1431_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N + 30) | AC | 0.031 s | 56 KB | 11311246 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
