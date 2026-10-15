# 1699. Tortugas que giran

[Timus 1699](https://acm.timus.ru/problem.aspx?space=1&num=1699) · dificultad 1079 · trees

Problema original de Alex Samsonov, del Ural SU Contest en el campus de invierno de Petrozavodsk, febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un campo cuadriculado las casillas transitables están unidas de una
sola manera: entre dos cualesquiera hay un único camino. Las tortugas se
mueven entre vecinas por un lado, y una ruta cuesta su número de giros
de 90°. Responder q consultas: el número de giros de una casilla
transitable a otra.

## Entrada

h y w (1 ≤ w · h ≤ 100000), el mapa de `#` (transitable) y `.`, y luego
q (1 ≤ q ≤ 50000) y las consultas r1 c1 r2 c2.

## Salida

El número de giros de cada consulta, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4
.#..
###.
..##
.##.
....
4
1 2 2 1
2 3 4 3
4 2 3 4
1 2 4 2
```

Salida:

```
1
0
2
3
```

## Solución

Las casillas transitables forman un árbol. Se enraíza en cualquier
casilla transitable con una búsqueda en anchura. Para cada casilla se
guarda su padre, su profundidad, la dirección del paso desde el padre y
T, el número de giros en el camino desde la raíz. T de un hijo es T del
padre, más uno si el paso cambia allí de dirección.

Una ruta entre a y b sube de a a su casilla de encuentro m y baja hasta
b. Sean a′ y b′ los hijos de m por cada lado. Los giros del tramo de m
a b son T(b) − T(b′), y lo mismo del lado de a. En m la ruta gira salvo
que pase de largo en línea recta, es decir, salvo que los pasos hacia
a′ y hacia b′ apunten en sentidos opuestos. Si m es la propia b, solo
cuenta el lado de a. El ascenso binario halla m junto con a′ y b′: se
sube la casilla más profunda hasta justo debajo de la profundidad de la
otra, y luego se suben ambas mientras sus antepasados difieran.
`O((n + q) log n)`.

Trampas:

- el giro en la casilla de encuentro se olvida fácilmente, igual que el
  caso recto en que no lo hay (test 04);
- las profundidades iguales y una ruta en que un extremo es antepasado
  del otro necesitan un trato aparte;
- un pasillo sinuoso hace el árbol de 50000 de profundidad, así que los
  recorridos no usan recursión.

Las respuestas coinciden con un recorrido de cada ruta en campos
pequeños y con una implementación aceptada independiente en campos
grandes aleatorios, serpenteantes y muy ramificados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1699_trees.cpp](1699_trees.cpp) | G++ 13.2 x64 | trees | O((n + q) log n) | AC | 0.156 s | 9112 KB |
| [1699_trees.go](1699_trees.go) | Go 1.14 x64 | trees | O((n + q) log n) | AC | 0.093 s | 21240 KB |
| [1699_trees.java](1699_trees.java) | Java 1.8 | trees | O((n + q) log n) | AC | 0.171 s | 14812 KB |
| [1699_trees.py](1699_trees.py) | Python 3.12 x64 | trees | O((n + q) log n) | AC | 0.703 s | 44716 KB |
| [1699_trees.rs](1699_trees.rs) | Rust 1.75 x64 | trees | O((n + q) log n) | AC | 0.062 s | 20416 KB |
