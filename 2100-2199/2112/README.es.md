# 2112. Comprobar el registro de una partida de tiros y adivinar los equipos

[Timus 2112](https://acm.timus.ru/problem.aspx?space=1&num=2112) · dificultad 818 · dsu, greedy, simulation

Problema original de Ivan Sychev, de la Olimpiada Académica Universitaria Escolar de Informática 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n jugadores juegan en equipos ocultos de cuatro. Cada jugador tiene un
estado 3 (sano), 2 (herido), 1 (derribado) o 0 (muerto) y empieza en 3.
El registro tiene tres clases de eventos: un impacto en el cuerpo o en la
cabeza baja el estado del objetivo en 1 o 2 (no por debajo de 0), un
botiquín devuelve a quien lo usa a 3, y una reanimación pasa a un
compañero de 1 a 2. Solo puede actuar un jugador en estado 3 o 2, y solo
se puede reanimar a un compañero derribado. Imprimir "FAKE" si ningún
reparto en equipos de cuatro hace válido el registro, y si no "CORRECT"
y cualquier reparto válido. Los límites son 1 segundo y 256 MB.

## Entrada

n, 4 ≤ n ≤ 1000, divisible por 4, los n nombres distintos, luego m,
0 ≤ m ≤ 10⁴, y los eventos "X HIT Y IN BODY", "X HIT Y IN HEAD",
"X USES MEDKIT" y "X REVIVE Y".

## Salida

"FAKE", o "CORRECT" seguido de n / 4 líneas con cuatro nombres.

## Evaluación

Un comprobador acepta cualquier reparto válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
Shroud
Forsen
Wycc
Ragyra
BeastQT
Lirik
Asmadey
Ninja
12
Wycc HIT Shroud IN BODY
Shroud HIT Wycc IN HEAD
Ragyra REVIVE Wycc
Wycc USES MEDKIT
Lirik HIT BeastQT IN BODY
Asmadey HIT BeastQT IN BODY
Asmadey REVIVE BeastQT
Ragyra HIT Forsen IN HEAD
Shroud REVIVE Forsen
BeastQT HIT Shroud IN HEAD
Wycc HIT Forsen IN HEAD
Ninja HIT BeastQT IN HEAD
```

Salida:

```
CORRECT
Wycc Ragyra BeastQT Asmadey
Lirik Ninja Shroud Forsen
```

### Ejemplo 2

Entrada:

```
8
Shroud
Forsen
Wycc
Ragyra
BeastQT
Lirik
Asmadey
Ninja
8
Shroud HIT Wycc IN HEAD
Shroud HIT Ragyra IN HEAD
Shroud HIT BeastQT IN HEAD
Shroud HIT Asmadey IN HEAD
Lirik REVIVE Wycc
Lirik REVIVE Ragyra
Lirik REVIVE BeastQT
Lirik REVIVE Asmadey
```

Salida:

```
FAKE
```

### Ejemplo 3

Entrada:

```
4
Shroud
Forsen
Wycc
Ragyra
3
Shroud HIT Wycc IN HEAD
Wycc HIT Shroud IN HEAD
Wycc HIT Shroud IN BODY
```

Salida:

```
FAKE
```

## Solución

Los estados no dependen de los equipos, así que se simula el registro
directamente. Un evento cuyo actor está en estado 1 o 0 es falso, igual
que reanimar a un objetivo que no está en estado 1. Los impactos sobre
cualquiera están permitidos, incluso sobre uno mismo.

El único vínculo con los equipos es que una reanimación pone a los dos
jugadores en el mismo equipo. Se unen en una estructura de conjuntos
disjuntos. Cada grupo resultante debe caber en un equipo, así que un
grupo de más de cuatro es falso. Después los grupos se empaquetan en
equipos de cuatro:

- los grupos de cuatro ya son equipos;
- cada grupo de tres necesita un jugador suelto, y si hay menos sueltos
  que tríos el registro es falso;
- los grupos de dos se emparejan entre sí;
- una pareja impar sobrante toma dos sueltos, que existen porque n es
  divisible por cuatro;
- los sueltos restantes forman equipos de cuatro.

La simulación y el empaquetado cuestan O(n + m) con hashing de los
nombres.

En el tercer ejemplo Wycc queda derribado por un disparo a la cabeza y
aun así dispara, así que el registro es falso.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2112_dsu_greedy_simulation.cpp](2112_dsu_greedy_simulation.cpp) | G++ 13.2 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.031 s | 644 KB |
| [2112_dsu_greedy_simulation.go](2112_dsu_greedy_simulation.go) | Go 1.14 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.046 s | 2824 KB |
| [2112_dsu_greedy_simulation.java](2112_dsu_greedy_simulation.java) | Java 1.8 | dsu, greedy, simulation | O(n + m) | AC | 0.156 s | 4712 KB |
| [2112_dsu_greedy_simulation.py](2112_dsu_greedy_simulation.py) | Python 3.12 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.109 s | 1140 KB |
| [2112_dsu_greedy_simulation.rs](2112_dsu_greedy_simulation.rs) | Rust 1.75 x64 | dsu, greedy, simulation | O(n + m) | AC | 0.046 s | 1280 KB |
