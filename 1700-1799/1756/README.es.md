# 1756. Excavador y medio

[Timus 1756](https://acm.timus.ru/problem.aspx?space=1&num=1756) · dificultad 179 · math

Problema original de Magaz Asanov, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

m excavadores cavan una zanja en exactamente d₁ días, trabajando todos
cada día. Planificar cuántos excavadores trabajan cada uno de d₂ días
para cavar la misma zanja en exactamente d₂ días contratando el menor
número posible. Se permiten días sin nadie trabajando.

## Entrada

m, d₁ y d₂ (1 ≤ m, d₁, d₂ ≤ 10000).

## Salida

d₂ números: los excavadores que trabajan cada día. Se acepta cualquier
plan óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1 2
```

Salida:

```
1 2
```

## Solución

La zanja requiere W = m·d₁ días-excavador. Hay que contratar tantos
excavadores como trabajan el día de más carga, y d₂ días con a lo sumo
k excavadores cada uno dan a lo sumo k·d₂ días-excavador, así que hacen
falta al menos ⌈W / d₂⌉. Esa cantidad basta: con W = q·d₂ + r, se ponen
q excavadores en d₂ − r días y q + 1 en los otros r. `O(d₂)`.

En el ejemplo W = 3 en 2 días: un día con 1 excavador y otro con 2, así
que se contratan dos excavadores, no uno y medio.

Trampas:

- m·d₁ llega a 10⁸, que cabe en 32 bits pero conviene tenerlo en
  cuenta;
- cuando W < d₂ algunos días no trabaja nadie;
- los números diarios deben sumar exactamente W, no solo alcanzarlo.

Los planes pasan un verificador que comprueba la suma y el día de más
carga, en entradas pequeñas, aleatorias y cercanas al límite; una
implementación aceptada independiente imprime los mismos días en otro
orden.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1756_math.cpp](1756_math.cpp) | G++ 13.2 x64 | math | O(d2) | AC | 0.015 s | 128 KB |
| [1756_math.go](1756_math.go) | Go 1.14 x64 | math | O(d2) | AC | 0.031 s | 1060 KB |
| [1756_math.java](1756_math.java) | Java 1.8 | math | O(d2) | AC | 0.109 s | 1996 KB |
| [1756_math.py](1756_math.py) | Python 3.12 x64 | math | O(d2) | AC | 0.125 s | 1148 KB |
| [1756_math.rs](1756_math.rs) | Rust 1.75 x64 | math | O(d2) | AC | 0.015 s | 620 KB |
