# 1688. Team.GOV!

[Timus 1688](https://acm.timus.ru/problem.aspx?space=1&num=1688) · dificultad 134 · implementation

Problema original de Alexander Ipatov, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres miembros de un equipo piden lo mismo y uno de ellos paga siempre
la cuenta. Otro miembro puede irse en cuanto lo pagado por su parte, un
tercio de cada cuenta, supere n. Dadas las cuentas en orden, decir
después de qué visita ocurre.

## Entrada

n y m (1 ≤ n ≤ 2 · 10⁹; 0 ≤ m ≤ 3000), y luego m cuentas, enteros de 1
a 2 · 10⁶.

## Salida

«Free after x times.» para la primera visita x así, o «Team.GOV!» si
nunca ocurre.

## Ejemplos

### Ejemplo 1

Entrada:

```
1666 5
2000
1024
900
1156
1200
```

Salida:

```
Free after 4 times.
```

### Ejemplo 2

Entrada:

```
3000 5
2000
1024
900
1156
1200
```

Salida:

```
Team.GOV!
```

## Solución

Se lleva la suma acumulada de las cuentas. La parte total / 3 supera n
exactamente cuando total > 3n, lo que evita fracciones; se para en la
primera visita en que se cumple. `O(m)`.

Trampas:

- 3n llega a 6 · 10⁹ y la suma también: hacen falta enteros de 64 bits
  (test 06);
- una parte igual a n no basta, la comparación es estricta (tests 04
  y 06).

Las respuestas coinciden con una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1688_implementation.cpp](1688_implementation.cpp) | G++ 13.2 x64 | implementation | O(m) | AC | 0.015 s | 136 KB |
| [1688_implementation.go](1688_implementation.go) | Go 1.14 x64 | implementation | O(m) | AC | 0.015 s | 1124 KB |
| [1688_implementation.java](1688_implementation.java) | Java 1.8 | implementation | O(m) | AC | 0.078 s | 1016 KB |
| [1688_implementation.py](1688_implementation.py) | Python 3.12 x64 | implementation | O(m) | AC | 0.078 s | 788 KB |
| [1688_implementation.rs](1688_implementation.rs) | Rust 1.75 x64 | implementation | O(m) | AC | 0.015 s | 224 KB |
