# 1374. Miseria

[Timus 1374](https://acm.timus.ru/problem.aspx?space=1&num=1374) · dificultad 8593 · games

Problema original de Den Raskovalov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres jugadores tienen 10 cartas cada uno de una baraja de 32, todas a la
vista. Se juegan diez bazas: quien sale juega cualquier carta, luego el
jugador siguiente y el tercero, y cada uno debe seguir el palo de la
primera carta si puede. La carta más alta de ese palo gana la baza y
sale en la siguiente. No hay triunfos. El jugador 1 ha declarado
miseria y no debe ganar ninguna baza. Hay que imprimir `;)` si el
jugador 1 puede lograrlo juegue como juegue el resto, y `;(` en otro
caso.

Límite de tiempo: 1 segundo. Límite de memoria: 16 MB.

## Entrada

Las manos de los jugadores 1, 2 y 3, una por línea, con cartas como
`10S` o `QH`, y después el número del jugador que sale primero.

## Salida

`;)` o `;(`.

## Ejemplos

### Ejemplo 1

Entrada:

```
7S 8S 9S 10S JS QS KS AS 7C 8C
9C 10C JC QC KC AC 7D 8D 9D 10D
JD QD KD AD 7H 8H 9H 10H JH QH
1
```

Salida:

```
;)
```

## Solución

Es un juego de información completa con resultado de sí o no, así que
se busca: en las cartas del jugador 1 alguna carta tiene que mantener la
miseria, en las de los otros todas tienen que mantenerla. Tres cosas
mantienen pequeña la búsqueda:

- las cartas que se tocan son la misma carta: dos cartas de un jugador
  en un palo sin cartas de otro jugador entre ellas llevan al mismo
  resultado, así que se prueba una sola de cada serie;
- los cuatro palos juegan igual y dentro de un palo solo importa el
  orden de las cartas. Así que una posición entre bazas se recuerda por
  las cadenas ordenadas de dueños de cada palo más quien sale, y las
  posiciones que difieren en un cambio de nombre de palos o valores
  pueden compartir una respuesta guardada;
- las posiciones recordadas viven en una tabla de tamaño fijo, indexada
  por esa cadena. Un choque solo obliga a resolver de nuevo una
  posición, y la memoria queda holgadamente dentro de 16 MB.

En los repartos más difíciles encontrados se guardan unas 30 000
posiciones. Cota factorial en el peor caso, pero rápido en todos los
repartos probados.

Detalles a tener en cuenta:

- el juego va 1 → 2 → 3 alrededor de la mesa, desde quien sale;
- un jugador sin cartas del palo de salida puede jugar cualquiera, y
  esa carta nunca gana la baza;
- la miseria fracasa en cuanto el jugador 1 gana una baza.

Las respuestas se compararon en 300 repartos con una búsqueda simple sin
el cambio de nombre de palos y valores; la equivalencia de las cartas
que se tocan se comprobó con una búsqueda sobre todas las cartas en
otros repartos. Las pruebas 02 a 05 son repartos difíciles publicados
en el foro del problema.

Complejidad: `O((n!)^3)` con n = 10 cartas por jugador: una cota superior
antes de podar.

## Notas por lenguaje

- Go construye las claves y las listas de cartas en arreglos de tamaño
  fijo: los slices creados en cada paso dejan basura, y el recolector
  deja crecer el montículo hasta unas dos veces la tabla de 8 MB, más de
  16 MB.
- Python corre en CPython y poda más el árbol del juego: cada palo se
  sigue con un pequeño autómata precalculado, de las respuestas
  comparables de los defensores solo se conserva la más difícil para el
  declarante, un palo que ya no puede perjudicar al declarante se reduce
  a su número de cartas y al orden de los defensores, y las posiciones
  iguales se unen; su tabla tiene 2¹⁸ entradas de 64 bits.
  Versiones anteriores sin estas podas excedían el
  límite de tiempo en la prueba 62 del juez incluso con PyPy.
- Java usa una tabla de 2¹⁹ entradas en lugar de 2²⁰, para dejar sitio
  a la JVM en 16 MB.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1374_games.cpp](1374_games.cpp) | G++ 13.2 x64 | games | O((n!)^3) | AC | 0.140 s | 8564 KB |
| [1374_games.go](1374_games.go) | Go 1.14 x64 | games | O((n!)^3) | AC | 0.140 s | 10056 KB |
| [1374_games.java](1374_games.java) | Java 1.8 | games | O((n!)^3) | AC | 0.406 s | 10240 KB |
| [1374_games.py](1374_games.py) | Python 3.12 x64 | games | O((n!)^3) | AC | 0.187 s | 3628 KB |
| [1374_games.rs](1374_games.rs) | Rust 1.75 x64 | games | O((n!)^3) | AC | 0.156 s | 8280 KB |
