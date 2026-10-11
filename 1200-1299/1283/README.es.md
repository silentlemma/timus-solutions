# 1283. Enano

[Timus 1283](https://acm.timus.ru/problem.aspx?space=1&num=1283) · dificultad 115 · math

Problema original de Leonid Volkov (preparado por Ivan Dashkevich), del Concurso Individual de la Universidad Estatal de los Urales 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un enano tiene G unidades de oro, y cada año un banco se queda con el p
por ciento como comisión (1 ≤ p ≤ 99), así que el oro queda en
(100 − p)/100 de lo que era. Cuando el oro no pasa de L, la vida del
enano pierde el sentido. G y L llegan a 2³¹ − 1. ¿Cuántos años quedan?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

G, L y p.

## Salida

El número de años.

## Ejemplos

### Ejemplo 1

Entrada:

```
19 10 50
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
1000 1 1
```

Salida:

```
688
```

## Solución

Tras k años el oro es exactamente G · ((100 − p)/100)^k, y la respuesta
es el primer k con eso como mucho L. En números enteros la prueba es

```text
G · (100 − p)^k ≤ L · 100^k
```

así que cada año se multiplican los dos lados, por 100 − p y por 100,
hasta que el izquierdo deja de ser mayor. El bucle da como mucho unas
2140 vueltas, con G = 2³¹ − 1, L = 1 y p = 1, y los números crecen hasta
unos miles de cifras. `O(Y²)` operaciones con cifras para Y años.

Detalles a tener en cuenta:

- el oro puede caer justo en el límite, y la coma flotante no lo ve:
  300 · 0,81 da 243,00000000000003, un año de más con L = 243
  (prueba 05), y ln(9801/10000) / ln(0,99) redondea hacia arriba a tres
  años en vez de dos (prueba 06);
- si el oro ya no pasa de L, la respuesta es 0 (pruebas 03, 04).

## Notas por lenguaje

- Python, Go y Java usan sus enteros grandes; C++ y Rust guardan el
  número en cifras de base 10⁹ y solo lo multiplican por factores
  pequeños y comparan.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1283_math.cpp](1283_math.cpp) | G++ 13.2 x64 | math | O(Y²) | AC | 0.015 s | 204 KB |
| [1283_math.go](1283_math.go) | Go 1.14 x64 | math | O(Y²) | AC | 0.031 s | 1276 KB |
| [1283_math.java](1283_math.java) | Java 1.8 | math | O(Y²) | AC | 0.109 s | 5600 KB |
| [1283_math.py](1283_math.py) | Python 3.12 x64 | math | O(Y²) | AC | 0.078 s | 480 KB |
| [1283_math.rs](1283_math.rs) | Rust 1.75 x64 | math | O(Y²) | AC | 0.015 s | 232 KB |
