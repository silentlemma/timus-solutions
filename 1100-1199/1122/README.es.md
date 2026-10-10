# 1122. El menor número de jugadas para dejar un tablero de 4 × 4 de un solo color

[Timus 1122](https://acm.timus.ru/problem.aspx?space=1&num=1122) · dificultad 250 · bitmask

Problema original de Leonid Volkov, Oleg Kats y Alexander Somov, del USU Open Collegiate Programming Contest, octubre de 2001, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tablero de `4 × 4` tiene fichas de dos caras con el lado blanco (`W`)
o negro (`B`) hacia arriba. Una jugada elige una casilla y voltea las
fichas marcadas por un patrón fijo de `3 × 3` centrado en ella; el patrón
puede ser cualquiera, no necesita ser simétrico, y las partes que caen
fuera del tablero se ignoran. Halla el menor número de jugadas que deja
las 16 fichas del mismo color, o imprime `Impossible`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Cuatro líneas del tablero y luego tres líneas del patrón (`1` voltea,
`0` no).

## Salida

El menor número de jugadas, o `Impossible`.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
WWWW
WBBW
WBWW
WWWW
101
010
101
```

Salida:

```
Impossible
```

## Solución

Como máscaras de bits, una jugada hace un XOR del tablero con una máscara
fija de su casilla. El XOR es conmutativo y una jugada repetida en la
misma casilla se anula, así que cualquier secuencia de jugadas equivale a
un conjunto de casillas, cada una usada una vez. Solo hay `2^16`
conjuntos: se calcula el volteo combinado de cada conjunto a partir del
conjunto sin su casilla más baja, `flips[s] = flips[s − baja] ^ move[baja]`,
y se toma el menor conjunto cuyo volteo es igual al tablero (todo blanco)
o al tablero con todos los bits invertidos (todo negro). `O(2^16)`.

Detalles a tener en cuenta:

- cualquiera de los dos colores vale como meta, así que hay que probar
  ambos objetivos;
- el patrón se centra en la casilla elegida y se recorta en los bordes,
  así que cerca del borde el mismo patrón voltea menos fichas;
- algunos patrones nunca alcanzan ciertas casillas (por ejemplo, una sola
  esquina del patrón nunca llega a la última fila y columna), lo que hace
  imposibles muchos tableros.

Las respuestas se comprobaron con una búsqueda en anchura sobre los
`2^16` estados del tablero, de jugada en jugada, en todas las pruebas y 40
partidas aleatorias.

## Notas por lenguaje

- Todos los lenguajes recorren los mismos `2^16` conjuntos; el bit más
  bajo y la cuenta de bits salen de funciones incorporadas, y Python usa
  `(s & -s).bit_length()` y `bin(s).count("1")`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1122_bitmask.cpp](1122_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(2^16) | AC | 0.015 s | 428 KB |
| [1122_bitmask.go](1122_bitmask.go) | Go 1.14 x64 | bitmask | O(2^16) | AC | 0.031 s | 1608 KB |
| [1122_bitmask.java](1122_bitmask.java) | Java 1.8 | bitmask | O(2^16) | AC | 0.109 s | 1852 KB |
| [1122_bitmask.py](1122_bitmask.py) | Python 3.12 x64 | bitmask | O(2^16) | AC | 0.109 s | 3192 KB |
| [1122_bitmask.rs](1122_bitmask.rs) | Rust 1.75 x64 | bitmask | O(2^16) | AC | 0.031 s | 736 KB |
