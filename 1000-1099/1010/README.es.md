# 1010. La cuerda más empinada sobre una función discreta

[Timus 1010](https://acm.timus.ru/problem.aspx?space=1&num=1010) · dificultad 293 · math

Problema original del Third Open USTU Collegiate Programming Contest (PhysTech Cup), 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una función viene dada por sus valores `f(1), ..., f(N)`
(`2 ≤ N ≤ 100 000`, `-2^31 ≤ f(i) ≤ 2^31 - 1`). Un par de puntos
`A = (a, f(a))` y `B = (b, f(b))`, `a < b`, es **válido** si todo punto
`(i, f(i))` con `a < i < b` queda estrictamente por debajo de la recta `AB`.
Entre los pares válidos, encuentra uno con el mayor valor absoluto de la
pendiente de `AB`; si hay varios, el de menor `a`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego los `N` valores `f(1), ..., f(N)`, uno por línea.

## Salida

`a` y `b`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1
5
2
-4
```

Salida:

```
3 4
```

### Ejemplo 2

Entrada:

```
2
7
7
```

Salida:

```
1 2
```

## Solución

La respuesta siempre es un par de vecinos `(a, a + 1)`: el primero con el
mayor `|f(a + 1) - f(a)|`.

Por qué: la pendiente de una cuerda de `a` a `b` es la media de las pendientes
de los `b - a` pasos unitarios bajo ella, así que su valor absoluto no supera
la mayor pendiente absoluta de un paso. Los pares vecinos siempre son válidos
(no hay nada entre ellos), de modo que el máximo se alcanza en un paso. Una
cuerda más larga solo puede empatar si todos sus pasos tienen la misma
pendiente, pero entonces los puntos intermedios están sobre la recta, no
estrictamente por debajo, y la cuerda no es válida. Así, los pasos con la
mayor `|diferencia|` son exactamente los pares óptimos, y el primero tiene el
menor `a`.

Una pasada: tiempo `O(N)` y memoria `O(1)` (u `O(N)` si se guardan los
valores).

Detalles a tener en cuenta:

- la diferencia de dos valores llega a `2^32 - 1`: usa enteros de 64 bits;
- empates: conserva el primer máximo (comparación estricta al recorrer de
  izquierda a derecha);
- la condición de validez parece pedir una envolvente convexa, pero nunca
  influye en la respuesta.

## Notas por lenguaje

El mismo recorrido en todos los lenguajes. Java usa un pequeño lector con
búfer de bytes, porque `Scanner` es lento para `10^5` números.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1010_math.cpp](1010_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.046 s | 136 KB |
| [1010_math.go](1010_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 2668 KB |
| [1010_math.java](1010_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 580 KB |
| [1010_math.py](1010_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 14648 KB |
| [1010_math.rs](1010_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.046 s | 3696 KB |
