# 1629. Viaje

[Timus 1629](https://acm.timus.ru/problem.aspx?space=1&num=1629) · dificultad 786 · simulation

Problema original de Alex Samsonov, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que volar por los aeropuertos 1, 2, …, N, siempre del aeropuerto i
al i + 1, y a medianoche en punto se está en el aeropuerto 1. Cada día
salen Q_i vuelos del aeropuerto i según un horario fijo, pero desde
ahora cada uno sale D_i minutos tarde; el vuelo al aeropuerto i + 1 dura
T_i minutos y el transbordo es instantáneo. ¿En cuántos minutos se llega
al aeropuerto N?

## Entrada

La primera línea contiene N (2 ≤ N ≤ 100). Después se describen los
aeropuertos 1 a N − 1 con dos líneas cada uno: Q_i, D_i y T_i
(1 ≤ Q_i ≤ 10; 0 ≤ D_i, T_i < 1440), y luego las Q_i horas de salida del
horario en formato HH:MM.

## Salida

El número de minutos tras la medianoche en que se aterriza en el
aeropuerto N.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2 60 1200
00:00 01:00
2 0 300
20:30 21:30
```

Salida:

```
1590
```

### Ejemplo 2

Entrada:

```
3
1 0 600
10:00
1 60 60
19:00
```

Salida:

```
1260
```

## Solución

Esperar más nunca ayuda, así que en cada aeropuerto se toma el primer
vuelo que sale no antes de la llegada. Un vuelo programado a las HH:MM
sale hoy en el minuto 60 · HH + MM + D_i, y en días siguientes múltiplos
enteros de 1440 después; si ya salió, redondear la diferencia hacia
arriba a días enteros da su siguiente salida. El menor de los Q_i
candidatos más T_i es la llegada al siguiente aeropuerto. `O(ΣQ_i)`.

Detalles a tener en cuenta:

- un vuelo que sale justo en el minuto de llegada todavía se puede tomar
  (el segundo ejemplo);
- los retrasos rigen desde la medianoche, así que un vuelo de ayer por la
  noche no pasa a hoy: con un retraso de 120 minutos el vuelo de las
  23:00 sale a las 25:00, no a la 01:00 (prueba 06);
- con el retraso, el vuelo de hoy puede salir después de la siguiente
  medianoche; sigue siendo su salida más temprana (prueba 04).

Las respuestas coinciden con una implementación aceptada independiente
en 150 rutas aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1629_simulation.cpp](1629_simulation.cpp) | G++ 13.2 x64 | simulation | O(ΣQ_i) | AC | 0.015 s | 132 KB |
| [1629_simulation.go](1629_simulation.go) | Go 1.14 x64 | simulation | O(ΣQ_i) | AC | 0.031 s | 1160 KB |
| [1629_simulation.java](1629_simulation.java) | Java 1.8 | simulation | O(ΣQ_i) | AC | 0.109 s | 876 KB |
| [1629_simulation.py](1629_simulation.py) | Python 3.12 x64 | simulation | O(ΣQ_i) | AC | 0.093 s | 500 KB |
| [1629_simulation.rs](1629_simulation.rs) | Rust 1.75 x64 | simulation | O(ΣQ_i) | AC | 0.046 s | 220 KB |
