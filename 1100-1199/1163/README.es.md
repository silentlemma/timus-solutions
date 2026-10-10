# 1163. ¿Quién gana un juego de lanzar fichas fuera del tablero?

[Timus 1163](https://acm.timus.ru/problem.aspx?space=1&num=1163) · dificultad 3932 · games

Problema original de Nick Durov, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Ocho fichas rojas y ocho blancas, discos de radio `0.4`, están en un
tablero de `8×8` sin tocarse. Se juega por turnos y empiezan las rojas.
Una jugada toma una ficha del propio color y la lanza de un golpe en
cualquier dirección: se desliza en línea recta hasta caer del tablero, y
cada ficha que toca por el camino se retira. Quien no tiene fichas al
llegarle el turno pierde. Hay que hallar el ganador con juego óptimo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Dos líneas con ocho pares de coordenadas cada una: los centros de las
fichas rojas y luego los de las blancas.

## Salida

`RED` o `WHITE`.

## Ejemplos

### Ejemplo 1

Entrada:

```
0.5 7.5 1.5 7.5 2.5 7.5 3.5 7.5 4.5 7.5 5.5 7.5 6.5 7.5 7.5 7.5
0.5 0.5 1.5 0.5 2.5 0.5 3.5 0.5 4.5 0.5 5.5 0.5 6.5 0.5 7.5 0.5
```

Salida:

```
RED
```

## Solución

La ficha en movimiento barre una franja: otra ficha es golpeada
exactamente cuando su centro está por delante del punto de partida y a lo
sumo a `0.8`, dos radios, de la línea de movimiento. Una ficha detrás del
punto de partida nunca se toca, porque las fichas están a más de `0.8`
entre sí y la distancia solo crece.

Al girar la dirección, una ficha a distancia `d` es golpeada dentro de un
arco de direcciones limitado por los dos ángulos tangentes
`atan2 ± asin(0.8/d)`. Así que el conjunto de fichas golpeadas solo cambia
en esos ángulos. Probando cada ángulo tangente, donde el roce todavía
cuenta, y el punto medio de cada hueco entre ángulos vecinos se obtienen
todos los conjuntos posibles: como mucho 60 por ficha, menos tras quitar
repeticiones.

El estado del juego es el conjunto de fichas que quedan y a quién le toca,
`2^17` estados en total. Una jugada retira la propia ficha lanzada y todo
lo que golpea, así que cada partida termina en 16 jugadas como mucho. Una
búsqueda con memoria marca un estado como ganador si alguna jugada lleva a
un estado perdedor para el rival; un bando sin fichas no tiene jugadas y
pierde. `O(2^16·16·60)` en el peor caso.

Detalles a tener en cuenta:

- la ficha lanzada también sale del tablero, así que siempre se pierde;
- un roce es un golpe, así que las direcciones tangentes deben probarse
  exactamente, con una pequeña tolerancia de redondeo, y no solo los
  huecos entre ellas;
- retirar una ficha propia puede ser una buena jugada, así que las jugadas
  no se limitan a golpear al rival.

Las respuestas se compararon en todas las pruebas y en 74 posiciones,
algunas de ellas ganadas por las blancas, con un programa aparte que prueba
200 000 direcciones por ficha y resuelve todos los subconjuntos de abajo
arriba.

## Notas por lenguaje

- Todos los lenguajes construyen los mismos conjuntos golpeados a partir
  de los mismos ángulos.
- Python guarda los resultados de la búsqueda en un diccionario; los demás
  lenguajes usan un arreglo con una casilla por estado.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1163_games.cpp](1163_games.cpp) | G++ 13.2 x64 | games | O(2^16·16·60) | AC | 0.015 s | 340 KB |
| [1163_games.go](1163_games.go) | Go 1.14 x64 | games | O(2^16·16·60) | AC | 0.031 s | 1340 KB |
| [1163_games.java](1163_games.java) | Java 1.8 | games | O(2^16·16·60) | AC | 0.218 s | 4616 KB |
| [1163_games.py](1163_games.py) | Python 3.12 x64 | games | O(2^16·16·60) | AC | 0.484 s | 3688 KB |
| [1163_games.rs](1163_games.rs) | Rust 1.75 x64 | games | O(2^16·16·60) | AC | 0.015 s | 400 KB |
