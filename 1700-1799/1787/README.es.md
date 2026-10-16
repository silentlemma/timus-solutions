# 1787. Giro hacia MEGA

[Timus 1787](https://acm.timus.ru/problem.aspx?space=1&num=1787) · dificultad 25 · simulation

Problema original de Bulat Zaynullin, del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un semáforo deja girar k coches por minuto. Durante el minuto i llegan
aᵢ coches nuevos al giro, que al principio estaba vacío. ¿Cuántos
coches esperan al cabo de n minutos?

## Entrada

k y n (1 ≤ k, n ≤ 100), luego a₁, …, aₙ (0 ≤ aᵢ ≤ 100).

## Salida

El número de coches que esperan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
6 7 2
```

Salida:

```
0
```

### Ejemplo 2

Entrada:

```
5 3
20 0 0
```

Salida:

```
5
```

## Solución

Se sigue el atasco minuto a minuto: se suman los coches nuevos, se
restan k, y si el resultado baja de cero el atasco simplemente está
vacío. `O(n)`.

En el primer ejemplo el atasco es 1, luego 3, luego 0, porque en el
último minuto solo hay 5 coches ante el semáforo. En el segundo es 15,
10, 5.

Trampas:

- el atasco no puede ser negativo: un minuto tranquilo no guarda
  capacidad para después, así que sumar todos los aᵢ y restar n·k es
  incorrecto;
- por la misma razón importa el orden: el primer ejemplo al revés,
  2 7 6, deja 3 coches en lugar de 0.

Las respuestas coinciden con una implementación aceptada independiente
en 150 casos aleatorios con cualquier número de coches y con números
cercanos a k.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1787_simulation.cpp](1787_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.031 s | 396 KB |
| [1787_simulation.go](1787_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.031 s | 1076 KB |
| [1787_simulation.java](1787_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.125 s | 1680 KB |
| [1787_simulation.py](1787_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 420 KB |
| [1787_simulation.rs](1787_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.015 s | 240 KB |
