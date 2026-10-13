# 1485. Fútbol y mentiras

[Timus 1485](https://acm.timus.ru/problem.aspx?space=1&num=1485) · dificultad 1675 · graphs

Problema original de Sergey Pupyrev, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N equipos (1 ≤ N ≤ 100) jugaron una liga a una vuelta: 3 puntos por
victoria, 1 por empate, 0 por derrota. La capitanía del equipo i dijo
A_ij = 1 «puntuamos contra j», A_ij = 0 «no puntuamos contra j» o
A_ij = −1 nada. Cada capitanía o siempre miente o siempre dice la
verdad. Hay que escribir cualquier tabla B de puntos que encaje, con
B_ij los puntos del equipo i contra el equipo j, o «Impossible».

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego la matriz A de N × N.

## Salida

La tabla B de N × N, o «Impossible».

## Ejemplos

### Ejemplo 1

Entrada:

```
3
-1 1 0
1 -1 -1
0 1 -1
```

Salida:

```
0 0 1
3 0 3
1 0 0
```

### Ejemplo 2

Entrada:

```
5
-1 1 1 0 0
0 -1 1 -1 -1
1 0 -1 -1 -1
0 -1 -1 -1 1
1 -1 -1 0 -1
```

Salida:

```
Impossible
```

## Solución

Sea T_i que la capitanía i dice la verdad, y s_ij que el equipo i
puntuó contra el equipo j. Una afirmación ata s_ij a T_i: s_ij = T_i
si A_ij = 1 y s_ij = no T_i si A_ij = 0. Un partido solo necesita s_ij
o s_ji, porque un lado que puntúa es una victoria y dos son un empate.
Donde nadie dijo nada, ese lado puede puntuar sin más, así que solo los
pares en que hablaron ambas capitanías dan una condición: una cláusula
de dos literales sobre las variables T.

Eso es 2-SAT. Se construye el grafo de implicaciones sobre los 2N
literales, con no a → b y no b → a para cada cláusula a o b, y se hallan
sus componentes fuertemente conexas con el algoritmo de Tarjan. No hay
solución justo cuando algún T_i y su negación están en la misma
componente. Si no, T_i es verdadero cuando su componente va después que
la de su negación en orden topológico. Entonces cada s_ij queda fijado
o libre, y la tabla sale directamente. `O(N²)`.

Detalles a tener en cuenta:

- una capitanía que no dijo nada no impone nada, y un equipo puede
  jugar solo partidos no mencionados (pruebas 03, 04);
- dos capitanías que afirman no haber puntuado entre sí no pueden decir
  ambas la verdad (prueba 07);
- se acepta cualquier tabla que encaje, así que las pruebas usan un
  comprobador (todas las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1485_graphs.cpp](1485_graphs.cpp) | G++ 13.2 x64 | graphs | O(N^2) | AC | 0.015 s | 392 KB |
| [1485_graphs.go](1485_graphs.go) | Go 1.14 x64 | graphs | O(N^2) | AC | 0.031 s | 1556 KB |
| [1485_graphs.java](1485_graphs.java) | Java 1.8 | graphs | O(N^2) | AC | 0.140 s | 1028 KB |
| [1485_graphs.py](1485_graphs.py) | Python 3.12 x64 | graphs | O(N^2) | AC | 0.109 s | 1368 KB |
| [1485_graphs.rs](1485_graphs.rs) | Rust 1.75 x64 | graphs | O(N^2) | AC | 0.015 s | 448 KB |
