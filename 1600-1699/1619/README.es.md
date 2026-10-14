# 1619. Hermano mayor

[Timus 1619](https://acm.timus.ru/problem.aspx?space=1&num=1619) · dificultad 719 · math

Problema original del SPbSU ITMO Contest en el campus de Petrozavodsk, invierno de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Durante un año el hermano mayor recibe K monedas de un euro y el menor
recibe M, una moneda cada vez, en un orden aleatorio uniforme. El mayor
se enfada si en algún momento el menor tiene más dinero. Para cada uno
de N casos (N ≤ 2004, 0 ≤ K, M ≤ 10⁴) imprime la probabilidad de que eso
no ocurra nunca, con un error de a lo sumo 10⁻⁶.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas `K M`.

## Salida

Las probabilidades, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 0
0 1
1 1
```

Salida:

```
1
0
0.5
```

## Solución

Los órdenes son caminos en la red con K pasos de un tipo y M del otro,
C(K + M, M) en total. Si M > K el menor termina por delante y la
respuesta es 0. Si no, los caminos malos son los que en algún momento
tienen al menor una moneda por delante; reflejar uno de ellos después de
su primer momento malo lo convierte en un camino con K + 1 y M − 1
monedas, de forma biyectiva, así que hay C(K + M, M − 1) caminos malos.
La probabilidad es

1 − C(K + M, M − 1) / C(K + M, M) = 1 − M / (K + 1) = (K − M + 1) / (K + 1).

`O(1)` por caso.

Detalles a tener en cuenta:

- las cantidades iguales no importan: solo ir estrictamente por delante
  enfada al mayor, así que K = M = 1 da 1/2, no 0 (ejemplo);
- K = M = 0 da 1, y M > K da exactamente 0 (prueba 03).

La fórmula coincide con contar todos los órdenes para todo K, M ≤ 8.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1619_math.cpp](1619_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.001 s | 144 KB |
| [1619_math.go](1619_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1160 KB |
| [1619_math.java](1619_math.java) | Java 1.8 | math | O(N) | AC | 0.218 s | 4280 KB |
| [1619_math.py](1619_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.046 s | 800 KB |
| [1619_math.rs](1619_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 260 KB |
