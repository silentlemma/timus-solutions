# 1555. ¡Encuentra el tesoro!

[Timus 1555](https://acm.timus.ru/problem.aspx?space=1&num=1555) · dificultad 8847 · games

Problema original del Novosibirsk SU Contest en el campus de Petrozavodsk, septiembre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos jugadores mueven por turnos en un laberinto de N × N (N ≤ 6, como
mucho 30 paredes; cada casilla puede tener pared en cualquier lado, así
que entre vecinas puede haber dos paredes). Una jugada es un paso a una
casilla vecina libre sin cruzar paredes, pasar, o un disparo del único
cohete de cada jugador: al norte, este, sur, oeste o hacia abajo. El
cohete vuela hasta salir del tablero, chocar con una pared (que se
destruye) o dar al otro jugador (que muere); un cohete disparado hacia
abajo mata al que dispara. Quien muere pierde; un jugador que ha pisado
el cofre también puede ganar saliendo del tablero. Ambos juegan de forma
óptima. Hay que imprimir `Draw`, o `Win` o `Lose` del primer jugador
con el número de turnos (el primer jugador lo hace mínimo y el segundo
máximo) y la primera jugada del primer jugador: `M` o `S` con una
dirección del teclado numérico (8 norte, 6 este, 2 sur, 4 oeste, 5
pasar o hacia abajo).

Límite de tiempo: 5 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego 3N líneas de 3N caracteres: cada casilla es un cuadrado de
3 × 3 con sus paredes `-` y `|` en el centro de cada lado y `1`, `2`,
`*` o un espacio en el centro.

## Salida

`Draw`, o el resultado con el número de turnos y después la primera
jugada.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
.-..-..-.
|1....|2|
.........
.........
|*|.....|
.........
.........
|.......|
.-..-..-.
```

Salida:

```
Win 5
M2
```

### Ejemplo 2

Entrada:

```
2
.-..-.
|2..*|
.-....
.-....
|1||.|
.-..-.
```

Salida:

```
Lose 1
S5
```

## Solución

Un análisis retrógrado. Una posición son las dos casillas, quién lleva
el cofre y a quién le toca; además, cada cohete está cargado, salió del
tablero o se gastó en la pared w. Un disparo solo lleva a estados de
cohetes con menos cohetes cargados, así que los estados se resuelven de
ninguno cargado a los dos cargados, y cada uno es un grafo de juego de
unas 7 500 posiciones cuyos disparos llevan a posiciones ya resueltas.

Dentro de un estado de cohetes los resultados salen por inducción hacia
atrás: una posición se gana en cuanto una jugada gana para quien mueve,
se pierde cuando pierden todas, y lo que queda en ciclos es tablas. El
número de turnos sale luego de una pasada al estilo de Dijkstra con un
montículo: una posición del primer jugador toma el mínimo de turnos
entre sus jugadas que mantienen el resultado, una del segundo el máximo,
una vez conocidas todas esas jugadas. La primera jugada es la mejor por
resultado, luego por turnos, luego en el orden M8, M6, M2, M4, M5, S8,
S6, S2, S4, S5. `O(S² · P log P)` para S ≤ 32 estados de cohetes y P
posiciones.

Detalles a tener en cuenta:

- el primer jugador acorta los turnos incluso perdiendo: en el segundo
  ejemplo dispara hacia abajo en el acto (`Lose 1`);
- de dos paredes entre vecinas un cohete destruye solo la primera que
  encuentra, y una pared destruida no vuelve (prueba 06);
- un cohete que sale del tablero solo se gasta;
- con el cofre un jugador sale del tablero solo por un lado sin pared;
- las posiciones atrapadas en ciclos son tablas (prueba 03).

Las respuestas se compararon con una implementación aceptada
independiente en las pruebas de aquí y en 40 laberintos aleatorios,
entre ellos tableros de 6 × 6 con 30 paredes.

## Notas por lenguaje

- No hay solución en Python: las pruebas más grandes tardan unos 85 s
  con CPython y unos 20 s con PyPy, frente a un límite de 5 s.
- Las cuatro soluciones guardan las jugadas y los predecesores de las
  posiciones en arreglos planos reutilizados para cada estado de
  cohetes: reservarlos de nuevo para cada uno de unos mil estados las
  hacía hasta el doble de lentas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1555_games.cpp](1555_games.cpp) | G++ 13.2 x64 | games | O(S² · P log P) | AC | 2.156 s | 25108 KB |
| [1555_games.go](1555_games.go) | Go 1.14 x64 | games | O(S² · P log P) | AC | 4.078 s | 54920 KB |
| [1555_games.java](1555_games.java) | Java 1.8 | games | O(S² · P log P) | AC | 3.203 s | 29212 KB |
| [1555_games.rs](1555_games.rs) | Rust 1.75 x64 | games | O(S² · P log P) | AC | 2.140 s | 26488 KB |
