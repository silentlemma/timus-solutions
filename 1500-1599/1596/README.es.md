# 1596. El caballo de pesadilla

[Timus 1596](https://acm.timus.ru/problem.aspx?space=1&num=1596) · dificultad 8902 · constructive

Problema original de Vladimir Basunkov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que hallar un recorrido cerrado del caballo en un tablero N × M
(6 ≤ N, M ≤ 1000): el caballo visita cada casilla exactamente una vez y
vuelve a la inicial. Para cada casilla se imprime con cuál de los 8
saltos del caballo se sale de ella, numerados en el orden (2, 1),
(2, −1), (−2, 1), (−2, −1), (1, 2), (1, −2), (−1, 2), (−1, −2) como
pasos (fila, columna), o `No solution`. Vale cualquier recorrido.

Límite de tiempo: 5 segundos. Límite de memoria: 64 MB.

## Entrada

N y M: N filas y M columnas.

## Salida

N filas de M números de salto, o `No solution`.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 7
```

Salida:

```
5 1 5 6 2 6 2
7 2 6 8 7 8 8
1 4 8 6 7 6 4
1 2 6 1 1 6 4
5 5 4 3 5 3 8
7 3 7 7 7 3 4
```

### Ejemplo 2

Entrada:

```
7 7
```

Salida:

```
No solution
```

## Solución

El caballo siempre cambia el color de la casilla, así que un recorrido
cerrado necesita tantas casillas claras como oscuras: con N y M impares
no lo hay. Con lados de al menos 6 es el único obstáculo (teorema de
Schwenk), y el recorrido se arma con piezas pequeñas.

Cada lado se corta en trozos de 6 a 11: ochos mientras queden al menos
14, luego un seis si hace falta y luego el resto. Un lado par solo da
trozos pares, así que cada bloque tiene área par. Para cada una de las
27 formas de bloque posibles el programa guarda un recorrido cerrado,
elegido para que contenga dos saltos extra: (1, C − 2)–(3, C − 1) junto
a la esquina superior derecha y (R − 2, 1)–(R − 1, 3) junto a la inferior
izquierda. Todo recorrido cerrado contiene además los saltos
(0, 0)–(2, 1) y (0, 0)–(1, 2), porque la casilla de la esquina solo tiene
esos dos vecinos. Los recorridos guardados se hallaron una vez, de
antemano, con una búsqueda en profundidad con el orden de Warnsdorff,
desempates aleatorios y reinicios.

El recorrido se guarda como un ciclo no dirigido, dos vecinos por
casilla. Dos bloques vecinos de una fila se unen quitando el salto
(1, C − 2)–(3, C − 1) del bloque izquierdo y el salto de esquina
(0, 0)–(2, 1) del derecho, y añadiendo los dos saltos de caballo entre
sus extremos a través del borde. Quitar un salto de cada uno de dos
ciclos separados deja dos caminos, y los dos saltos nuevos los cierran
en un solo ciclo. Después las filas de bloques se unen igual,
traspuesto, por sus extremos izquierdos: el salto (R − 2, 1)–(R − 1, 3)
del bloque de arriba y (0, 0)–(1, 2) del de abajo. Cada esquina
participa como mucho en una unión, así que los saltos que una unión
necesita siguen ahí. Un paseo por el ciclo desde la casilla superior
izquierda escribe los números de dirección: `O(N·M)`.

Las pruebas usan un verificador que sigue los saltos. Aceptó la salida
en varios cientos de tamaños de tablero con lados de hasta 31 y en los
tableros más grandes.

Detalles a tener en cuenta:

- (2, 1) significa dos filas abajo y una columna a la derecha; el primer
  ejemplo lo confirma, e intercambiarlos da una respuesta inválida;
- 10⁶ casillas son unos 2 MB de salida, que hay que escribir de una vez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1596_constructive.cpp](1596_constructive.cpp) | G++ 13.2 x64 | constructive | O(N·M) | AC | 0.031 s | 9516 KB |
| [1596_constructive.go](1596_constructive.go) | Go 1.14 x64 | constructive | O(N·M) | AC | 0.078 s | 11700 KB |
| [1596_constructive.java](1596_constructive.java) | Java 1.8 | constructive | O(N·M) | AC | 0.140 s | 13892 KB |
| [1596_constructive.py](1596_constructive.py) | Python 3.12 x64 | constructive | O(N·M) | AC | 1.109 s | 13332 KB |
| [1596_constructive.rs](1596_constructive.rs) | Rust 1.75 x64 | constructive | O(N·M) | AC | 0.062 s | 17648 KB |
