# 1166. ¿Puede un jugador soltar toda su mano sin dejar jugar al rival?

[Timus 1166](https://acm.timus.ru/problem.aspx?space=1&num=1166) · dificultad 3552 · games

Problema original de Andrew Lopatine, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Quedan dos jugadores en un juego de cartas con una baraja de 54 cartas que
incluye dos comodines. Cada carta jugada debe cubrirse con una del mismo
palo o del mismo valor; tras una reina solo cuenta el palo anunciado con
ella. Tras un 6, un 7, un as o el rey de picas el rival pierde el turno,
así que vuelve a jugar el mismo jugador y cubre su propia carta. Un
comodín puede jugarse como cualquier carta que nombre su dueño. Dada la
mano del primer jugador (ya no puede robar) y la carta boca arriba, hay
que decidir si puede jugar todas sus cartas una tras otra sin que el
rival juegue nunca y, si es así, imprimir ese orden.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La mano en cartas de dos letras (`T` para el diez, `*` para un comodín)
en una línea y luego la carta boca arriba; si es una reina va seguida del
palo anunciado, y si es un comodín, de la carta que representa.

## Salida

`YES` y el orden de las cartas, con cada comodín jugado seguido de la
carta que representa y cada reina del palo que anuncia, o `NO`.

## Evaluación

Se acepta cualquier orden que juegue exactamente la mano, en el que cada
carta cubra a la anterior, toda carta salvo la última haga perder el
turno al rival y las reinas y comodines estén escritos completos. El
veredicto `YES` o `NO` se toma de la respuesta guardada.

## Ejemplos

### Ejemplo 1

Entrada:

```
6C QD 6S KS 7S *
*QHS
```

Salida:

```
YES
7S KS 6S 6C *6D QDS
```

## Solución

Tras cualquier carta que no sea una de las trece que hacen perder el turno
(el 6, el 7 y el as de cada palo y el rey de picas) juega el rival. Así
que toda carta salvo la última debe ser una de ellas, real o un comodín
nombrado como tal. Una mano con dos cartas de otro tipo es un `NO`
inmediato, y una sola carta de otro tipo tiene que ir la última.

Lo que queda es un camino que empieza en la carta boca arriba y recorre la
mano, cubriendo cada carta a la anterior. El estado es qué cartas reales
de las trece ya se jugaron (a lo sumo `2^13` conjuntos), cuántos
comodines se usaron (son intercambiables, así que solo importa su número)
y la carta de arriba: una de las trece o la carta boca arriba. Una
búsqueda en profundidad recuerda los estados desde los que falló y
devuelve el orden cuando se han jugado todas las cartas. Cuando queda una
carta, se comprueba contra la de arriba: la carta de otro tipo si la hay
y si no la última de las trece; un comodín final siempre puede nombrarse,
por ejemplo, el dos del palo de arriba. `O(2^13·3·14·26)` en el peor caso.

Detalles a tener en cuenta:

- una reina en la mesa solo se cubre con el palo anunciado, incluso con
  otra reina;
- un comodín en la mesa cuenta como la carta que se nombró;
- un ocho o una reina dan turno al rival, así que solo pueden ir al final;
- una reina jugada necesita el palo anunciado en la salida, aunque sea la
  última carta.

Los veredictos se compararon con una solución escrita aparte en 495
repartos aleatorios, y cada orden impreso pasó el comprobador.

## Notas por lenguaje

- Todos los lenguajes hacen la misma búsqueda con la misma tabla de
  estados fallidos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1166_games.cpp](1166_games.cpp) | G++ 13.2 x64 | games | O(2^13·3·14·26) | AC | 0.015 s | 556 KB |
| [1166_games.go](1166_games.go) | Go 1.14 x64 | games | O(2^13·3·14·26) | AC | 0.031 s | 1168 KB |
| [1166_games.java](1166_games.java) | Java 1.8 | games | O(2^13·3·14·26) | AC | 0.109 s | 952 KB |
| [1166_games.py](1166_games.py) | Python 3.12 x64 | games | O(2^13·3·14·26) | AC | 0.093 s | 940 KB |
| [1166_games.rs](1166_games.rs) | Rust 1.75 x64 | games | O(2^13·3·14·26) | AC | 0.062 s | 380 KB |
