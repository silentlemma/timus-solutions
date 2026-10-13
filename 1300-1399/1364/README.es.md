# 1364. LaraKiller

[Timus 1364](https://acm.timus.ru/problem.aspx?space=1&num=1364) · dificultad 949 · simulation

Problema original de Stanislav Vasiliev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cementerio tiene N filas de M tumbas, 2 ≤ N, M ≤ 100. El túnel de
Lara empieza en la tumba (1, 1) y va hacia el este: sigue recto
mientras la tumba siguiente está intacta, y gira a la derecha ante el
muro o una tumba ya saqueada. El túnel llega al tesoro en (rT, cT).
Cuando Lara está en la tumba (rL, cL) del túnel, una alarma deja
T ≤ 27 000 segundos, y por el túnel se corre a una tumba por segundo.
Hay que imprimir todas las tumbas saqueadas a las que Lara llega a
tiempo, en el orden en que se saquearon.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, luego rT y cT, luego rL y cL, luego T.

## Salida

Las tumbas alcanzables, un par `fila columna` por línea, en orden de
saqueo.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4
4 3
2 2
5
```

Salida:

```
5 2
5 1
4 1
3 1
2 1
2 2
2 3
3 3
4 3
```

## Solución

La regla de excavación dibuja una espiral en sentido horario, y el
túnel acaba en el tesoro. Se simula: un marco de celdas «saqueadas»
alrededor del cementerio hace de muro, y se gira a la derecha cuando la
celda siguiente ya está saqueada. Así salen las tumbas en orden de
saqueo, y el túnel es un camino donde la distancia entre dos tumbas es
la diferencia de sus puestos en la lista.

Si la tumba de Lara está en el puesto p y el tesoro en el puesto q, la
respuesta son los puestos de max(0, p − T) a min(q, p + T).
`O(N · M)`.

Detalles a tener en cuenta:

- el túnel acaba en el tesoro, y más allá no se llega (prueba 06);
- T puede ser 0, y entonces solo queda la tumba de Lara (prueba 02);
- T puede superar todo el túnel, que entonces es la respuesta (prueba
  03 y prueba generada 1).

## Notas por lenguaje

- Las cinco soluciones construyen la misma espiral con un marco en
  lugar del muro.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1364_simulation.cpp](1364_simulation.cpp) | G++ 13.2 x64 | simulation | O(N·M) | AC | 0.015 s | 300 KB |
| [1364_simulation.go](1364_simulation.go) | Go 1.14 x64 | simulation | O(N·M) | AC | 0.015 s | 2096 KB |
| [1364_simulation.java](1364_simulation.java) | Java 1.8 | simulation | O(N·M) | AC | 0.093 s | 2068 KB |
| [1364_simulation.py](1364_simulation.py) | Python 3.12 x64 | simulation | O(N·M) | AC | 0.093 s | 1992 KB |
| [1364_simulation.rs](1364_simulation.rs) | Rust 1.75 x64 | simulation | O(N·M) | AC | 0.015 s | 452 KB |
