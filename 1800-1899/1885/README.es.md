# 1885. Comodidad de los pasajeros

[Timus 1885](https://acm.timus.ru/problem.aspx?space=1&num=1885) · dificultad 186 · math

Problema original de Denis Dublennykh, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un avión debe subir a h metros en los primeros t segundos y luego
mantener esa altura. Sube como mucho v metros por segundo y no puede
bajar antes de llegar a h. A los pasajeros se les tapan los oídos
exactamente mientras el avión sube a más de x metros por segundo. Hay
que hallar el menor y el mayor tiempo posible con los oídos tapados.

## Entrada

h, t, v, x (5000 ≤ h ≤ 12 000, 50 ≤ t ≤ 1200, 1 ≤ x < v ≤ 100,
h ≤ t·v).

## Salida

El menor y el mayor tiempo, cada uno con error absoluto o relativo de como mucho 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
10000 500 50 10
```

Salida:

```
125.0 500.0
```

## Solución

El menor: cada segundo a velocidad x o menos no cuenta, y en cada uno se
ganan como mucho x metros. Si t·x ≥ h, el avión sube a x y los oídos
nunca se tapan. Si no, debe subir a x todos los segundos menos τ, y a v
durante τ, con τ·v + (t − τ)·x = h, así que τ = (h − t·x)/(v − x).
Hacer los segundos rápidos a menos de v solo los alarga.

El mayor: los oídos solo se tapan al subir, así que como mucho t
segundos y como mucho h/x segundos. Subir un poco por encima de x
se aproxima a este último límite, o, si
h/x > t, el avión sube a h/t > x durante los t segundos. La respuesta es
min(t, h/x). `O(1)`.

En el ejemplo t·x = 5000 < 10 000, así que hacen falta 5000/40 = 125
segundos a 50 m/s, y subir a h/t = 20 > 10 m/s durante los 500 segundos
mantiene los oídos tapados todo el tiempo.

Trampas:

- el mayor tiempo es un límite: subir exactamente a x no tapa los
  oídos, pero cualquier velocidad mayor sí, así que la respuesta es min(t, h/x);
- cuando t·x ≥ h el menor tiempo es 0;
- subir a menos de x no cuenta, así que mezclar velocidades lentas
  nunca mejora una subida a x.

Las respuestas coinciden con una implementación aceptada independiente
en todas las pruebas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1885_math.cpp](1885_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 152 KB |
| [1885_math.go](1885_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1088 KB |
| [1885_math.java](1885_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1788 KB |
| [1885_math.py](1885_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 392 KB |
| [1885_math.rs](1885_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 264 KB |
