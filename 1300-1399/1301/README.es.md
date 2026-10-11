# 1301. Cubo en el laberinto

[Timus 1301](https://acm.timus.ru/problem.aspx?space=1&num=1301) · dificultad 720 · bfs

Problema original del Segundo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 3–4 de abril de 1998.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cubo del tamaño de una casilla está sobre un campo X × Y
(2 ≤ X, Y ≤ 10). Cada movimiento lo hace rodar sobre una arista a una
casilla vecina; no puede rodar a través de una pared ni salir del
campo. Hay que hallar el mínimo de movimientos que llevan el cubo de la
casilla (A, B) a la (C, D) con la misma cara arriba que al principio, o
indicar que es imposible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

X e Y, luego A y B, luego C y D. Después, opcionalmente, una línea `v`
seguida de pares `N M`, cada uno una pared entre las casillas (N, M) y
(N + 1, M), y una línea `h` seguida de pares `N M`, cada uno una pared
entre (N, M) y (N, M + 1).

## Salida

El número de movimientos, o `No solution`.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 2
1 1
10 1
v
2 1
6 2
h
4 1
```

Salida:

```
11
```

## Solución

La orientación completa de un cubo tiene 24 estados, pero solo importa
una cara: la que empieza arriba. Dónde está ahora (arriba, abajo,
norte, sur, este u oeste) cambia con cada vuelta según una regla fija.
Rodar hacia el este, por ejemplo, lleva arriba al este, el este abajo,
abajo al oeste y el oeste arriba, y deja quietos el norte y el sur.

Así que el estado es (casilla, lado de la cara marcada), como mucho
10 · 10 · 6 = 600 estados, y una búsqueda en anchura desde
(A, B, arriba) halla el camino más corto a (C, D, arriba). Cada pared
bloquea el paso en ambos sentidos. `O(X · Y)`.

Detalles a tener en cuenta:

- el inicio puede ser la meta: 0 movimientos (prueba 02);
- la casilla correcta con la cara equivocada arriba no cuenta. En un
  pasillo recto la cara marcada queda arriba solo si el desplazamiento es
  múltiplo de 4, así que un pasillo de longitud 2 o 3 no tiene solución (pruebas 04 y
  08), y uno de longitud 4 sí (prueba 09);
- incluso una casilla vecina puede exigir un rodeo: 3 movimientos en un
  campo abierto de 2 × 2 (prueba 03);
- cualquiera de las secciones de paredes puede faltar.

Las respuestas se compararon con una búsqueda sobre las 24
orientaciones de un cubo con caras etiquetadas en 120 campos
aleatorios.

## Notas por lenguaje

- Las secciones de paredes se leen palabra a palabra, así que la forma
  de la entrada (saltos de línea, espacios de más) no importa.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1301_bfs.cpp](1301_bfs.cpp) | G++ 13.2 x64 | bfs | O(X * Y) | AC | 0.015 s | 200 KB |
| [1301_bfs.go](1301_bfs.go) | Go 1.14 x64 | bfs | O(X * Y) | AC | 0.031 s | 1172 KB |
| [1301_bfs.java](1301_bfs.java) | Java 1.8 | bfs | O(X * Y) | AC | 0.109 s | 564 KB |
| [1301_bfs.py](1301_bfs.py) | Python 3.12 x64 | bfs | O(X * Y) | AC | 0.078 s | 680 KB |
| [1301_bfs.rs](1301_bfs.rs) | Rust 1.75 x64 | bfs | O(X * Y) | AC | 0.015 s | 244 KB |
