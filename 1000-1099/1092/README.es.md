# 1092. Limpiar una tabla de signos volteando transversales

[Timus 1092](https://acm.timus.ru/problem.aspx?space=1&num=1092) · dificultad 2322 · constructive

Problema original de Dmitry Filimonenkov, del USU Open Collegiate Programming Contest, marzo de 2001, Senior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tabla de tamaño `(2N + 1) × (2N + 1)` (`N ≤ 20`) contiene signos `+`
y `-`. Una transversal es un conjunto de `2N + 1` casillas con
exactamente una en cada fila y cada columna. Una operación invierte todos
los signos de una transversal. Halla una secuencia de operaciones tras la
cual queden como mucho `2N` signos más, o indica que no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego las `2N + 1` filas de la tabla.

## Salida

`There is solution:` y una línea por operación, con la columna de la
transversal en cada fila; o `No solution`.

## Evaluación

Se acepta cualquier secuencia adecuada. El comprobador aplica las
operaciones y cuenta los signos más que quedan.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
+++
++-
+-+
```

Salida:

```
There is solution:
2 1 3
3 1 2
2 1 3
2 3 1
1 2 3
1 3 2
```

## Solución

Se trabaja módulo 2 con `n = 2N + 1`. Dos transversales que coinciden en
todo salvo en las filas `i` y `l`, donde una toma las columnas `j`, `l` y
la otra `l`, `j`, invierten juntas exactamente las cuatro esquinas de un
rectángulo. Invertir rectángulos conserva la paridad de cada fila y cada
columna, y permite convertir la tabla en cualquier otra con las mismas
paridades: recorriendo las casillas fuera de la última fila y la última
columna, cada casilla incorrecta se arregla con el rectángulo de esquina
`(l, l)`, y la última fila y columna coinciden solas porque sus paridades
coinciden. Una sola transversal, en cambio, invierte la paridad de todas
las filas y columnas.

Una tabla con filas impares `R` y columnas impares `C` necesita al menos
`max(|R|, |C|)` signos más, y con eso basta: se emparejan filas impares
con columnas impares, y las líneas sobrantes, que van por parejas porque
`|R|` y `|C|` tienen la misma paridad, se ponen en la fila o la columna 0.
Esto es como mucho `2N` salvo que las `n` filas o las `n` columnas sean
todas impares; entonces una transversal las vuelve antes todas pares, y
el otro lado no podía ser todo par, porque `n` es impar. Así que siempre
hay solución:

1. si todas las filas o todas las columnas son impares, se invierte la
   diagonal principal;
2. se construye la tabla objetivo con `max(|R|, |C|)` signos más;
3. para cada casilla fuera de la última fila y columna que difiere del
   objetivo, se invierte su rectángulo con dos transversales.

Como mucho `2(n − 1)² + 1` operaciones, tiempo `O(n³)` contando las
inversiones.

Detalles a tener en cuenta:

- `No solution` nunca es la respuesta;
- la línea de números da la columna de cada fila, así que una
  transversal se imprime como una permutación;
- una tabla que ya tiene pocos signos más puede cambiar igualmente, y no
  importa: se acepta cualquier tabla final con como mucho `2N` signos más.

El comprobador repite las operaciones; la versión en Python también se
ejecutó sobre cientos de tablas aleatorias de todos los tamaños.

## Notas por lenguaje

- Todos los lenguajes guardan una copia de cada transversal, porque el
  mismo arreglo se modifica para la segunda inversión del par.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1092_constructive.cpp](1092_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^3) | AC | 0.015 s | 1752 KB |
| [1092_constructive.go](1092_constructive.go) | Go 1.14 x64 | constructive | O(n^3) | AC | 0.031 s | 4832 KB |
| [1092_constructive.java](1092_constructive.java) | Java 1.8 | constructive | O(n^3) | AC | 0.140 s | 7252 KB |
| [1092_constructive.py](1092_constructive.py) | Python 3.12 x64 | constructive | O(n^3) | AC | 0.109 s | 3592 KB |
| [1092_constructive.rs](1092_constructive.rs) | Rust 1.75 x64 | constructive | O(n^3) | AC | 0.031 s | 2116 KB |
