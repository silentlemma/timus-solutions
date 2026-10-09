# 1060. El menor número de volteos para dejar un tablero 4 × 4 de un color

[Timus 1060](https://acm.timus.ru/problem.aspx?space=1&num=1060) · dificultad 375 · bruteforce, bitmask

Problema original del concurso regional ACM ICPC del noreste de Europa 2000–2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tablero 4 × 4 tiene fichas con la cara negra (`b`) o blanca (`w`) hacia
arriba. Un movimiento elige una casilla y da la vuelta a la ficha de esa
casilla y a sus vecinas de arriba, abajo, izquierda y derecha (las que
existan). Halla el menor número de movimientos tras el cual todas las
fichas muestran el mismo color (cualquiera), `0` si ya es así, o
`Impossible`.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Cuatro líneas de cuatro caracteres `b` y `w`.

## Salida

El menor número de movimientos, o `Impossible`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
bwbw
wwww
bbwb
bwwb
```

Salida:

```
Impossible
```

### Ejemplo 2

Entrada:

```
bwwb
bbwb
bwwb
bwww
```

Salida:

```
4
```

## Solución

Se escribe el tablero como 16 bits; un movimiento en una casilla hace XOR
del tablero con una máscara fija de hasta cinco bits. El XOR es
conmutativo y una máscara aplicada dos veces se anula, así que el orden de
los movimientos no importa y ninguna casilla necesita más de un
movimiento: una solución es solo un conjunto de casillas.

Hay `2^16 = 65536` conjuntos. Para cada uno se aplica al tablero el XOR de
las máscaras de sus casillas y se guarda el conjunto más pequeño cuyo
resultado son todo ceros o todo unos. `O(2^16 · 16)`.

Solo 4096 de las 65536 posiciones tienen solución, y ninguna necesita más
de seis movimientos (lo muestra una búsqueda en anchura sobre todas las
posiciones, con la que se comprobaron las pruebas).

Detalles a tener en cuenta:

- tanto todo blanco como todo negro son objetivos;
- las casillas del borde y de las esquinas dan la vuelta a menos fichas;
- una posición que ya es de un color necesita 0 movimientos.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: un bucle sobre los 65536
  conjuntos.
- **Python**: los tableros de todos los conjuntos se construyen casilla a
  casilla, duplicando una lista (cada casilla nueva añade su máscara a
  todos los tableros anteriores), lo que evita un bucle de Python sobre los
  16 bits de cada conjunto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1060_bruteforce_bitmask.cpp](1060_bruteforce_bitmask.cpp) | G++ 13.2 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.015 s | 124 KB |
| [1060_bruteforce_bitmask.go](1060_bruteforce_bitmask.go) | Go 1.14 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.031 s | 1068 KB |
| [1060_bruteforce_bitmask.java](1060_bruteforce_bitmask.java) | Java 1.8 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.109 s | 1580 KB |
| [1060_bruteforce_bitmask.py](1060_bruteforce_bitmask.py) | Python 3.12 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.109 s | 4840 KB |
| [1060_bruteforce_bitmask.rs](1060_bruteforce_bitmask.rs) | Rust 1.75 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.015 s | 232 KB |
