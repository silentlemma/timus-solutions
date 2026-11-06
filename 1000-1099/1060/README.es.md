# 1060. El menor número de volteos para dejar un tablero 4 × 4 de un color

[Timus 1060](https://acm.timus.ru/problem.aspx?space=1&num=1060) · dificultad 378 · bruteforce, bitmask

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

## Soluciones optimizadas

Go prueba las 16 máscaras de pulsación de la primera fila para cada color objetivo. Cada discrepancia restante obliga a pulsar la celda justo debajo, determinando las demás filas. Cuenta los bits pulsados y acepta solo si no quedan discrepancias tras la última fila. Cada fila del tablero ocupa un byte. Python divide las 16 celdas en dos mitades y enumera el efecto XOR de los subconjuntos de pulsaciones, guardando el mínimo número por efecto. Para cada objetivo uniforme y efecto izquierdo, una consulta encuentra el efecto derecho necesario. Usa O(2^(C/2)) tiempo y espacio con C = 16 celdas. Go usa pequeños búferes fijos y los descriptores estándar directamente; reintenta llamadas interrumpidas y completa escrituras parciales.

Las implementaciones base aceptadas [1060_bruteforce_bitmask.cpp](1060_bruteforce_bitmask.cpp), [1060_bruteforce_bitmask.java](1060_bruteforce_bitmask.java), [1060_bruteforce_bitmask.rs](1060_bruteforce_bitmask.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- **C++**, **Go**, **Java**, **Rust**: un bucle sobre los 65536
  conjuntos.
- **Python**: los tableros de todos los conjuntos se construyen casilla a
  casilla, duplicando una lista (cada casilla nueva añade su máscara a
  todos los tableros anteriores), lo que evita un bucle de Python sobre los
  16 bits de cada conjunto.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1060_bruteforce_bitmask.cpp](1060_bruteforce_bitmask.cpp) | G++ 13.2 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.015 s | 124 KB | 11278793 |
| [1060_bruteforce_bitmask.go](1060_bruteforce_bitmask.go) | Go 1.14 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.031 s | 1068 KB | 11278795 |
| [1060_bruteforce_bitmask.java](1060_bruteforce_bitmask.java) \* | Java 1.8 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.109 s | 1580 KB | 11278797 |
| [1060_bruteforce_bitmask.py](1060_bruteforce_bitmask.py) | Python 3.12 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.109 s | 4840 KB | 11278796 |
| [1060_bruteforce_bitmask.rs](1060_bruteforce_bitmask.rs) | Rust 1.75 x64 | bruteforce, bitmask | O(2^16 · 16) | AC | 0.015 s | 232 KB | 11278798 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1060_bitmask.go](1060_bitmask.go) \* | Go 1.14 x64 | bitmask | O(H·2^W), H = W = 4 | AC | 0.015 s | 284 KB | 11311214 |
| [1060_bitmask_meet_in_middle.py](1060_bitmask_meet_in_middle.py) | Python 3.12 x64 | bitmask, meet_in_middle | O(2^(C/2)), C = 16 | AC | 0.078 s | 624 KB | 11310331 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
