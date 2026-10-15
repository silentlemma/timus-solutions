# 1636. Tiempo de penalización

[Timus 1636](https://acm.timus.ru/problem.aspx?space=1&num=1636) · dificultad 60 · implementation

Problema original de Alex Samsonov, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los equipos QXX y ZZZ resolvieron los diez problemas; QXX ganó con un
tiempo de penalización T1 frente al T2 de ZZZ. Cada intento rechazado
suma 20 minutos. Dado cuántos intentos rechazados hizo ZZZ en cada
problema, hay que decidir si ZZZ habría ganado sin ellos. A igualdad de
tiempo los equipos se ordenan por nombre, así que ZZZ seguiría segundo.

## Entrada

T1 y T2 (250 ≤ T1 ≤ T2 ≤ 2400) en la primera línea y luego diez números
de intentos rechazados de ZZZ.

## Salida

`Dirty debug :(` si los intentos le costaron el primer puesto a ZZZ, y
`No chance.` en otro caso.

## Ejemplos

### Ejemplo 1

Entrada:

```
290 420
0 0 0 2 1 0 2 0 1 0
```

Salida:

```
No chance.
```

### Ejemplo 2

Entrada:

```
300 719
0 0 0 0 0 0 21 0 0 0
```

Salida:

```
Dirty debug :(
```

## Solución

Restar a T2 20 minutos por cada intento rechazado. ZZZ habría ganado
solo con un tiempo estrictamente menor que T1, ya que un empate es para
QXX por orden alfabético. `O(1)`.

Detalles a tener en cuenta:

- el mismo tiempo limpio sigue siendo derrota (prueba 03), un minuto
  menos es victoria (prueba 04);
- las respuestas terminan en un punto y en una cara triste, ambos parte
  del texto esperado.

Las respuestas coinciden con una implementación aceptada independiente
en 100 pruebas aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1636_implementation.cpp](1636_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 120 KB |
| [1636_implementation.go](1636_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB |
| [1636_implementation.java](1636_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1600 KB |
| [1636_implementation.py](1636_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 428 KB |
| [1636_implementation.rs](1636_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 236 KB |
