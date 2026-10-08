# 1011. La menor población con una proporción estrictamente entre dos porcentajes

[Timus 1011](https://acm.timus.ru/problem.aspx?space=1&num=1011) · dificultad 247 · math, number_theory

Problema original del Campeonato de la Universidad Estatal de los Urales 1997.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados dos porcentajes `P` y `Q` (`0.01 ≤ P, Q ≤ 99.99`, como mucho dos
cifras tras el punto decimal, `P < Q`), encuentra el menor entero positivo
`n` para el que exista un entero `c` con `P% < c / n < Q%`, ambas
desigualdades estrictas.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`P` y `Q`, separados por un espacio o un salto de línea. Pueden escribirse
como enteros (`13`) o con uno o dos decimales (`14.1`, `12.50`).

## Salida

El menor `n`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 12
```

Salida:

```
9
```

### Ejemplo 2

Entrada:

```
12.5
12.6
```

Salida:

```
127
```

## Solución

Primero, evitamos los números en coma flotante. Ambos límites tienen como
mucho dos decimales, así que `p = 100·P` y `q = 100·Q` son enteros
(centésimas de punto porcentual), y la condición se vuelve
`p·n < 10000·c < q·n`.

**Recorrer n.** Para un `n` dado, el menor `c` por encima del límite
inferior es `c = ⌊p·n / 10000⌋ + 1`; `n` sirve exactamente cuando ese `c`
sigue por debajo del límite superior, `10000·c < q·n`. Se prueba
`n = 1, 2, ...`. El intervalo mide al menos `1/10000`, así que siempre sirve
algún `n ≤ 10000` (la mayor respuesta es 5001); el recorrido es instantáneo.

**Árbol de Stern–Brocot.** La respuesta es el menor denominador de una
fracción estrictamente dentro de `(p/10000, q/10000)`. Se desciende por el
árbol de Stern–Brocot desde los límites `0/1` y `1/0`: se toma la mediante
`(a + c)/(b + d)` de los límites actuales; si está en el límite inferior o
por debajo pasa a ser el nuevo límite izquierdo, si está en el superior o
por encima pasa a ser el derecho, y si no, es la respuesta. La primera
fracción del árbol que cae dentro de un intervalo es la de menor
denominador.

Detalles a tener en cuenta:

- leer los límites como números en coma flotante: `14.1` no es exacto en
  binario, y la comparación con `c / n` en el borde puede salir de
  cualquier lado;
- ambas desigualdades son estrictas: con `P = 12.5`, `1/8` no está dentro;
- `n = 1` nunca sirve, porque `0 < P` y `Q < 100`.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: el recorrido sobre `n` con enteros de
  64 bits.
- **C++** y **Python** también descienden por el árbol de Stern–Brocot.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1011_math.cpp](1011_math.cpp) | G++ 13.2 x64 | math | O(answer) | AC | 0.015 s | 352 KB |
| [1011_math.go](1011_math.go) | Go 1.14 x64 | math | O(answer) | AC | 0.015 s | 1088 KB |
| [1011_math.java](1011_math.java) | Java 1.8 | math | O(answer) | AC | 0.125 s | 1580 KB |
| [1011_math.rs](1011_math.rs) | Rust 1.75 x64 | math | O(answer) | AC | 0.015 s | 228 KB |
| [1011_number_theory.cpp](1011_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(answer) tree steps | AC | 0.015 s | 352 KB |
| [1011_number_theory.py](1011_number_theory.py) | Python 3.12 x64 | number_theory | O(answer) tree steps | AC | 0.109 s | 468 KB |
