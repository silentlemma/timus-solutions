# 2082. Reconstruir las apuestas desde el último turno del bot

[Timus 2082](https://acm.timus.ru/problem.aspx?space=1&num=2082) · dificultad 6136 · simulation

Problema original de Igor Chevdar.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una mano de Texas hold'em la juegan de 2 a 9 jugadores con ante, ciega
pequeña y ciega grande (con dos jugadores la ciega pequeña la pone el
repartidor). Las apuestas dan la vuelta a la mesa calle a calle
(preflop, flop, turn, river); las acciones son retirarse, pasar, igualar,
apostar y subir, y un jugador sin fichas suficientes puede ir all-in. Un
bot conoce el inicio de la mano, cada acción hasta su turno anterior y
ahora las pilas actuales de todos los jugadores, pero no las apuestas.
Reconstruir todas las acciones desde el turno anterior del bot, o desde
el inicio de la mano en su primer turno, incluidos los cambios de calle.
La respuesta es única. Los límites son 2 segundos y 256 MB.

## Entrada

Las ciegas y el ante, el número de jugadores, el repartidor y el bot, la
calle actual, los nombres y pilas iniciales, las acciones conocidas en
el formato de la salida y las pilas actuales.

## Salida

El número de acciones reconstruidas y después las acciones:
`dealing <street>`, `<name> folds`, `checks`, `calls <amount>`,
`bets <amount>` o `raises <amount> to <total>`.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 20 2
5 3 4
preflop
PhilIvey 500
TomDwan 500
ViktorBlom 500
Grobot 500
Ziigmund 500
0
498 478 438 488 478
```

Salida:

```
3
PhilIvey folds
TomDwan calls 20
ViktorBlom raises 40 to 60
```

### Ejemplo 2

Entrada:

```
10 20 2
5 3 4
flop
PhilIvey 500
TomDwan 500
ViktorBlom 500
Grobot 500
Ziigmund 500
3
PhilIvey folds
TomDwan calls 20
ViktorBlom raises 40 to 60
498 478 438 438 478
```

Salida:

```
4
Grobot calls 50
Ziigmund folds
TomDwan folds
dealing flop
```

### Ejemplo 3

Entrada:

```
10 20 2
5 3 4
flop
PhilIvey 500
TomDwan 500
ViktorBlom 500
Grobot 500
Ziigmund 500
7
PhilIvey folds
TomDwan calls 20
ViktorBlom raises 40 to 60
Grobot calls 50
Ziigmund folds
TomDwan folds
dealing flop
498 478 338 438 478
```

Salida:

```
2
Grobot checks
ViktorBlom bets 100
```

### Ejemplo 4

Entrada:

```
50 100 10
2 2 1
preflop
Grobot 2500
ViktorBlom 2000
0
2390 1890
```

Salida:

```
1
ViktorBlom calls 50
```

## Solución

Se reproduce un pequeño modelo de la mesa. Guarda todas las pilas, la
apuesta de cada jugador en la calle actual, la apuesta vigente, quién se
ha retirado y quién aún debe actuar; una apuesta o subida por encima de
la vigente hace actuar de nuevo a los demás que siguen en la mano con
fichas. Primero se ponen el ante y las ciegas (quien no puede cubrirlas
paga lo que tiene), el preflop empieza tras la ciega grande y las demás
calles tras el repartidor, y una calle termina cuando nadie debe actuar;
entonces el modelo reparte la calle siguiente.

Tras las acciones conocidas el modelo sigue solo. En cada turno la
pérdida de fichas del jugador que actúa, la diferencia entre la pila del
modelo y la informada, dice lo que pagó. No pagar nada es pasar si su
apuesta ya iguala la vigente, y retirarse en otro caso; un pago en una
calle vacía es una apuesta; un nuevo total por encima de la apuesta vigente es
una subida hasta ese total; si no, es igualar, all-in si la pila se
acaba. El único punto delicado es una calle que termina antes del turno
del bot: en ella nadie puede subir después del bot, así que un jugador
paga ahí a lo sumo lo necesario para igualar, y el resto de la pérdida
pertenece a la calle siguiente. La reproducción se detiene cuando le
toca al bot en la calle actual con todas las pilas coincidiendo. El tiempo
es O(k + m), con k acciones conocidas y m reconstruidas.

En el primer ejemplo el bot pone la ciega pequeña, así que PhilIvey,
TomDwan y ViktorBlom actúan antes que él; además del ante de 2, las pilas
muestran que PhilIvey no pagó nada (se retiró), TomDwan igualó 20 y
ViktorBlom subió 40 hasta 60.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2082_simulation.cpp](2082_simulation.cpp) | G++ 13.2 x64 | simulation | O(k + m) | AC | 0.015 s | 492 KB |
| [2082_simulation.go](2082_simulation.go) | Go 1.14 x64 | simulation | O(k + m) | AC | 0.031 s | 1232 KB |
| [2082_simulation.java](2082_simulation.java) | Java 1.8 | simulation | O(k + m) | AC | 0.125 s | 976 KB |
| [2082_simulation.py](2082_simulation.py) | Python 3.12 x64 | simulation | O(k + m) | AC | 0.093 s | 1172 KB |
| [2082_simulation.rs](2082_simulation.rs) | Rust 1.75 x64 | simulation | O(k + m) | AC | 0.015 s | 248 KB |
