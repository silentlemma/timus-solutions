# 2224. Dos jugadores en una franja de 2 × N sin repetir casillas

[Timus 2224](https://acm.timus.ru/problem.aspx?space=1&num=2224) · dificultad 1477 · games

Problema original de Vadim Barinov, del Campeonato de los Urales 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos jugadores están en casillas distintas de un tablero 2 × N y mueven
por turnos, empezando Blue, cada vez a una casilla vecina por un lado
que nadie ha visitado y que no está ocupada. Quien no puede mover
pierde. ¿Quién gana con juego óptimo? Los límites son 0.5 segundos y
256 MB.

## Entrada

N, 3 ≤ N ≤ 10⁹, y luego la casilla de Blue y la de Red.

## Salida

Blue o Red.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 2
2 3
```

Salida:

```
Blue
```

### Ejemplo 2

Entrada:

```
3
1 1
2 1
```

Salida:

```
Red
```

## Solución

Se refleja el tablero para que Blue no esté a la derecha de Red. Sea
left el número de columnas a la izquierda de Blue, right el de columnas
a la derecha de Red, y gap la distancia entre sus columnas. Una cola de
k columnas libres detrás de un jugador vale hasta 2k movimientos en
zigzag, así que el juego trata de quién conserva la cola más larga, y
las casillas entre los jugadores deciden quién debe ceder primero.

- **Misma fila.** Cada jugador puede irse enseguida a su cola, mientras
  la parte central es compartida. Blue gana con la cola más larga, y con
  colas iguales exactamente cuando gap es par, porque entonces es Blue
  quien llega primero al centro y se queda las casillas sobrantes.
- **Filas distintas.** Con gap 0 los jugadores están en una misma
  columna y Red puede responder a cada jugada de forma simétrica, así
  que gana Red; con colas iguales Red también puede imitar a Blue y
  gana. Con gap 1 Blue se coloca en diagonal delante de Red y le corta
  la fila, y gana Blue. Cuando las colas difieren en exactamente una
  columna, decide la carrera por el centro, y Blue gana exactamente
  cuando gap es impar. En otro caso gana la cola más larga.

Estas reglas se comprobaron con un minimax exhaustivo sobre todas las
posiciones iniciales de todos los tableros de 2 × 3 a 2 × 8.

En el primer ejemplo Blue está a una columna de Red en la otra fila y
gana; en el segundo comparten columna y gana Red.

Esto cuesta O(1).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2224_games.cpp](2224_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.031 s | 180 KB |
| [2224_games.go](2224_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 892 KB |
| [2224_games.java](2224_games.java) | Java 1.8 | games | O(1) | AC | 0.187 s | 1388 KB |
| [2224_games.py](2224_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.093 s | 248 KB |
| [2224_games.rs](2224_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 16 KB |
