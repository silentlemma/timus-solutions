# 1483. Futbolín

[Timus 1483](https://acm.timus.ru/problem.aspx?space=1&num=1483) · dificultad 384 · math

Problema original de Sergey Pupyrev, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N equipos (1 ≤ N ≤ 1000) juegan una liga a una vuelta: cada pareja se
enfrenta una vez, una victoria da 3 puntos, un empate 1 y una derrota 0.
Los equipos con los mismos puntos comparten puesto. Un equipo quedó
primero y otro último. Hay que hallar el menor número de puntos que
pudo tener el primero y el mayor que pudo tener el último.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

Los dos números.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
1 1
```

## Solución

Cada partido reparte al menos 2 puntos (un empate) y como mucho 3 (una
victoria). Así que entre todos suman al menos N(N − 1) puntos y el
líder tiene al menos la media N − 1; si todos los partidos acaban en
empate, cada equipo tiene exactamente N − 1.

Entre todos suman como mucho 3·N(N − 1)/2 puntos, así que el último
tiene como mucho ⌊3(N − 1)/2⌋. Con N impar cada equipo puede ganar
justo la mitad de sus N − 1 partidos, y todos tienen 3(N − 1)/2. Con N
par, los equipos empatan por parejas, un empate cada uno, y el resto de
partidos se reparte para que cada equipo gane la mitad de sus otros
N − 2: todos tienen 3(N − 2)/2 + 1 = ⌊3(N − 1)/2⌋. `O(1)`.

Detalles a tener en cuenta:

- con un solo equipo no hay partidos: 0 y 0 (prueba 02);
- con N par la cota necesita un empate por equipo, porque sin empates
  los puntos son múltiplos de 3 (prueba 04);
- las dos respuestas se optimizan por separado, no en la misma liga
  (prueba 03).

## Soluciones optimizadas

Go conserva las fórmulas n−1 y floor(3(n−1)/2). Lee el número de equipos con un pequeño búfer de bytes y lo reutiliza para formatear ambas respuestas sin entrada ni salida de formato general. Usa los descriptores estándar mediante syscall.Read y syscall.Write, reintenta llamadas interrumpidas y completa escrituras parciales.

Las implementaciones base aceptadas [1483_math.cpp](1483_math.cpp), [1483_math.java](1483_math.java), [1483_math.py](1483_math.py), [1483_math.rs](1483_math.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

`1483_math_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado.

Frente a `1483_math.java`: tiempo 0.093 s → 0.078 s; memoria 1588 KB → 456 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1483_math.cpp](1483_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.001 s | 128 KB | 11286749 |
| [1483_math.go](1483_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1084 KB | 11286751 |
| [1483_math.java](1483_math.java) \* | Java 1.8 | math | O(1) | AC | 0.093 s | 1588 KB | 11286754 |
| [1483_math.py](1483_math.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 320 KB | 11286753 |
| [1483_math.rs](1483_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB | 11286756 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1483_math_optimized.go](1483_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 268 KB | 11311199 |
| [1483_math_optimized.java](1483_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 456 KB | 11324807 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
