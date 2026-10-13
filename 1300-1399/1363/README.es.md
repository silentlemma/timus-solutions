# 1363. Medios tonos

[Timus 1363](https://acm.timus.ru/problem.aspx?space=1&num=1363) · dificultad 4703 · greedy

Problema original con idea de Pavel Atnashev, preparado por Evgeny Krokhalev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una imagen gris A de N × M píxeles, 75 ≤ N, M ≤ 300, con brillo de 0 a
255, hay que imprimirla en blanco y negro: cada píxel de B vale 0 o
255. Para cada píxel (i, j) se toma la ventana de píxeles (k, l) con
|k − i| ≤ 10 y |l − j| ≤ 10 que caen dentro de la imagen. La media de
B − A en esa ventana debe ser a lo sumo 20 en valor absoluto. Hay que
imprimir cualquier B así.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, luego N líneas de M brillos.

## Salida

N líneas de M números, cada uno 0 o 255.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
255 255 0
0 0 255
254 0 253
```

Salida:

```
255 255 0
0 0 255
255 0 255
```

## Solución

Cada fila se redondea por separado, arrastrando el error a lo largo de
ella. Se guarda e, la suma de B − A sobre los píxeles ya hechos de la
fila. En el píxel siguiente se resta su brillo de e; si baja de −127,
se imprime blanco y se suma 255. Así e se queda en [−127, 127] en cada
paso. El error de cualquier tramo de la fila es la diferencia de dos de
esas sumas: a lo sumo 254, y a lo sumo 127 si el tramo empieza donde
empezó el recorrido de la fila.

Una ventana tiene r ≥ 11 filas y c ≥ 11 columnas, y su error es la suma
de sus tramos de fila:

- una ventana lejos de los bordes izquierdo y derecho mide 21 de ancho,
  y un error de tramo de 254 queda muy por debajo de los 20 · 21 = 420
  permitidos por fila;
- una ventana en un borde lateral puede medir solo 11 de ancho, lo que
  permite 220 por fila, menos que 254. Por eso las filas se recorren en
  sentidos alternos; entonces en una de cada dos filas el tramo toca el
  inicio del recorrido y se desvía a lo sumo 127. Con r ≥ 11 filas,
  ⌈r/2⌉ · 254 + ⌊r/2⌋ · 127 ≤ 220 · r.

`O(N · M)`.

Detalles a tener en cuenta:

- recorrer todas las filas desde la izquierda no basta: una imagen del
  gris 46 de 97 de ancho deja la ventana del borde derecho con un error
  medio de 22,8 (prueba generada 2);
- el ejemplo incumple a propósito los límites de tamaño y solo muestra
  el formato.

Las pruebas se juzgan con un verificador que comprueba cada ventana con
sumas prefijas bidimensionales; el mismo verificador rechaza el
redondeo en un solo sentido en la prueba generada 2.

## Notas por lenguaje

- Las cinco soluciones usan el mismo redondeo entero.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1363_greedy.cpp](1363_greedy.cpp) | G++ 13.2 x64 | greedy | O(N·M) | AC | 0.062 s | 848 KB |
| [1363_greedy.go](1363_greedy.go) | Go 1.14 x64 | greedy | O(N·M) | AC | 0.031 s | 1536 KB |
| [1363_greedy.java](1363_greedy.java) | Java 1.8 | greedy | O(N·M) | AC | 0.109 s | 3568 KB |
| [1363_greedy.py](1363_greedy.py) | Python 3.12 x64 | greedy | O(N·M) | AC | 0.156 s | 6956 KB |
| [1363_greedy.rs](1363_greedy.rs) | Rust 1.75 x64 | greedy | O(N·M) | AC | 0.031 s | 1636 KB |
