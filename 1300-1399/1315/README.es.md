# 1315. MDPAR y MIIAR

[Timus 1315](https://acm.timus.ru/problem.aspx?space=1&num=1315) · dificultad 1836 · bfs

Problema original con idea de Alexander Klepinin, preparado por Alexander Klepinin e Ivan Dashkevich, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cueva es una cuadrícula W × H de roca (`#`) y casillas libres (`.`),
W, H ≤ 500, con la superficie por encima de la fila superior. El agua
llena toda casilla libre que tenga un camino a la superficie por
casillas libres, pasando por lados comunes, que nunca baje. Un
espeleólogo está en la casilla (X, Y), contada desde la izquierda y
desde abajo, y puede nadar como mucho D ≤ 1000 casillas bajo el agua
antes de necesitar aire. El aire queda en las casillas libres adonde no
llega el agua. ¿Puede salir por su cuenta? Mientras la cueva está seca,
se garantiza una salida.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

W, H, X, Y y D, y luego H filas de la cueva desde arriba.

## Salida

`Can be rescued by himself` o `Rescue operation required`.

## Ejemplos

### Ejemplo 1

Entrada:

```
9 4 8 2 5
##..##..#
##.#.####
##......#
#########
```

Salida:

```
Rescue operation required
```

### Ejemplo 2

Entrada:

```
9 4 8 2 6
##..##..#
##.#.####
##......#
#########
```

Salida:

```
Can be rescued by himself
```

## Solución

Primero el agua. Una casilla se inunda si puede llegar a la superficie
yendo solo hacia arriba, la izquierda o la derecha, así que se busca
hacia atrás desde las casillas libres de la fila superior, bajando y
yendo a izquierda y derecha.

Luego el espeleólogo. Los dos ejemplos fijan cómo se cuenta el nado: un
tramo bajo el agua dura desde la última respiración hasta la siguiente,
y cuenta cada movimiento, incluido el que entra en una casilla con aire
o sale por la fila superior. En el ejemplo, el tramo desde la bolsa de
aire hasta la superficie lleva 6 movimientos, así que con D = 5 no se
puede y con D = 6 sí.

Cada casilla recibe una etiqueta: los menos movimientos hechos bajo el
agua desde la última respiración al estar en ella, sobre todas las
formas de llegar.

- entrar en agua suma 1 a la etiqueta;
- entrar en aire la devuelve a 0, cosa que un nadador solo puede hacer
  con un movimiento de margen, etiqueta + 1 ≤ D (de aire a aire es
  gratis);
- salir por la fila superior exige etiqueta + 1 ≤ D.

Una etiqueta menor nunca es peor, así que solo importa la menor de cada
casilla. Las etiquetas van de 0 a D, de modo que unas cubetas por
etiqueta hacen de cola de prioridad. Cuando aparece una etiqueta 0 en
una bolsa de aire mientras se procesan etiquetas mayores, el recorrido
simplemente vuelve a la cubeta 0. `O(W · H · k)`, donde k es cuántas
veces baja la etiqueta de una casilla, poco en la práctica.

Detalles a tener en cuenta:

- una bolsa de aire es una casilla sobre el agua sin camino hacia
  arriba, como la casilla encima del pasillo del ejemplo, y en ella el
  espeleólogo puede respirar (pruebas 01–04);
- el espeleólogo puede empezar en una bolsa de aire o en el agua, y en
  ambos casos la etiqueta empieza en 0 (pruebas 03 y 06);
- el movimiento a la superficie también cuenta: un pozo inundado de k
  casillas necesita D ≥ k (pruebas 08 y 09).

Las respuestas se compararon con una búsqueda en anchura sobre todos
los estados (casilla, movimientos desde la última respiración) en 700
cuevas aleatorias pequeñas.

## Notas por lenguaje

- Python rodea la cueva con un marco de roca, para que ningún
  movimiento necesite comprobar los bordes, y construye la cuadrícula
  con `bytes.translate`.
- Python se ejecuta con PyPy: una de las pruebas del juez tarda algo más
  de 1 s con CPython, aunque las nuestras no pasan de 0,2 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1315_bfs.cpp](1315_bfs.cpp) | G++ 13.2 x64 | bfs | O(W * H * k) | AC | 0.125 s | 3256 KB |
| [1315_bfs.go](1315_bfs.go) | Go 1.14 x64 | bfs | O(W * H * k) | AC | 0.171 s | 10180 KB |
| [1315_bfs.java](1315_bfs.java) | Java 1.8 | bfs | O(W * H * k) | AC | 0.328 s | 8736 KB |
| [1315_bfs.py](1315_bfs.py) | PyPy 3.10 x64 | bfs | O(W * H * k) | AC | 0.687 s | 9596 KB |
| [1315_bfs.rs](1315_bfs.rs) | Rust 1.75 x64 | bfs | O(W * H * k) | AC | 0.218 s | 6708 KB |
