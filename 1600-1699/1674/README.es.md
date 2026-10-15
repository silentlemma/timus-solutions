# 1674. El rey borracho

[Timus 1674](https://acm.timus.ru/problem.aspx?space=1&num=1674) · dificultad 5742 · constructive

Problema original de Igor Chevdar, del Ural SU Contest en el campus de verano de Petrozavodsk, agosto de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un rey borracho se mueve como el rey de ajedrez a una casilla vecina,
pero nunca hace dos movimientos seguidos en la misma dirección.
Empezando en la esquina superior izquierda de un tablero N × M, debe
pasar por cada casilla una vez y volver, sin que su camino se cruce.
Hay que imprimir `No` si es imposible y, si no, `Yes` y un dibujo del
recorrido: casillas como `o` y movimientos como `-`, `|`, `/` y `\`
entre ellas.

## Entrada

N y M (2 ≤ N, M ≤ 500).

## Salida

`No`, o `Yes` y el dibujo en 2N − 1 líneas.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 8
```

Salida:

```
Yes
o-o o-o o-o o-o
|  \| |/  |/  |
o-o o o o o o-o
  |    / \   \
o-o o-o o-o o-o
|    \   \   \
o-o o-o o-o o-o
  |  \   \   \
o-o o o o-o o o
|  /| | |  /| |
o-o o-o o-o o-o
```

### Ejemplo 2

Entrada:

```
5 5
```

Salida:

```
No
```

Se acepta cualquier recorrido válido; para el primer ejemplo esta
solución dibuja otro.

## Solución

Hay recorrido para 2 × 2 y para todo tablero con ambos lados de al menos
4 salvo 5 × 5; los tableros con un lado de 2 o 3 (salvo 2 × 2) no tienen.
Una búsqueda exhaustiva lo confirma para lados 2 y 3 de largo hasta 8 y
para 5 × 5; la construcción siguiente cubre los tableros con recorrido.

- Un tablero 4 × m tiene un recorrido cerrado, la franja: zigzag por las
  dos filas de arriba hasta el extremo derecho, bajada, zigzag de vuelta
  por las dos filas de abajo y subida por el extremo izquierdo. Su
  traspuesta sirve para m × 4.
- El tablero se reduce a una base cuyos lados son de 4 a 7 más un
  múltiplo de 4. Las bases que no son franjas (5 × 6, 5 × 7, 6 × 6,
  6 × 7, 7 × 7 y sus traspuestas) son recorridos guardados. Cuando ambos
  lados son de la forma 4k + 1 la base es 5 × 9, porque 5 × 5 no tiene
  recorrido. Los recorridos guardados salen de una búsqueda,
  [1674_constructive_table.py](1674_constructive_table.py).
- El tablero crece de cuatro en cuatro columnas y luego de cuatro en
  cuatro filas. El bloque nuevo tiene su propia franja, y tres
  movimientos en la junta se cambian por tres diagonales: se quitan la
  vertical del borde derecho antiguo, la vertical del borde izquierdo
  nuevo y una diagonal de la franja nueva, y se ponen tres diagonales que
  no se cruzan. Cada casilla conserva dos movimientos, ninguna se cruza
  en línea recta y los dos ciclos pasan a ser uno.

El dibujo se hace directamente en una rejilla de caracteres, así que
cambiar un movimiento es sobrescribir un carácter. `O(N · M)`.

Detalles a tener en cuenta:

- 2 × 2 tiene recorrido aunque sus lados sean menores que 4 (prueba 03)
  y 5 × 5 no lo tiene aunque no lo sean (prueba 02);
- con ambos lados de la forma 4k + 1 la reducción llegaría a 5 × 5, de
  ahí la base 5 × 9 (pruebas 07 y gen4);
- las líneas del dibujo conservan los espacios finales; el comprobador
  acepta ambas formas.

Un comprobador analiza el dibujo y verifica que cada casilla tenga dos
movimientos, que ninguna se atraviese en línea recta y que los
movimientos formen un solo ciclo (dos diagonales cruzadas necesitarían el
mismo carácter, así que no pueden dibujarse ambas). Acepta todos los
tableros hasta 30 × 30 y los más grandes, y las respuestas coinciden con
una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1674_constructive.cpp](1674_constructive.cpp) | G++ 13.2 x64 | constructive | O(N M) | AC | 0.062 s | 2868 KB |
| [1674_constructive.go](1674_constructive.go) | Go 1.14 x64 | constructive | O(N M) | AC | 0.031 s | 7140 KB |
| [1674_constructive.java](1674_constructive.java) | Java 1.8 | constructive | O(N M) | AC | 0.140 s | 10252 KB |
| [1674_constructive.py](1674_constructive.py) | Python 3.12 x64 | constructive | O(N M) | AC | 0.390 s | 6260 KB |
| [1674_constructive.rs](1674_constructive.rs) | Rust 1.75 x64 | constructive | O(N M) | AC | 0.031 s | 3120 KB |
