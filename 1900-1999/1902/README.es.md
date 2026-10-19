# 1902. Meeting Times

[Timus 1902](https://acm.timus.ru/problem.aspx?space=1&num=1902) · difficulty 116 · math

Original problem by Denis Dublennykh, from Ural Championship 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un objeto entra en un segmento en el instante s. Otros n objetos recorren
el mismo segmento en sentido contrario, entrando en los instantes sᵢ.
Todos llevan la misma velocidad constante y tardan t unidades de tiempo
en recorrerlo. Calcula los encuentros. Límites: 1 segundo y 64 MB.

## Entrada

Primero n, t, s, con 1 ≤ n ≤ 100, 1 ≤ t ≤ 100 y 360 ≤ s ≤ 1200.
Después vienen n entradas enteras estrictamente crecientes:
s−t < s₁ < … < sₙ < s+t. Se cumplen todas las restricciones simultáneamente.

## Salida

Imprime n instantes de encuentro en el orden de entrada, separados por
espacios o saltos de línea. Se admite error absoluto o relativo de 10⁻⁶.

## Evaluación

Se comparan exactamente n valores finitos con tolerancia absoluta/relativa
10⁻⁶. Las pruebas usan el modo `float:1e-6`.

## Ejemplos

```
2 60 600
600 630
```

```
630.000000
645.000000
```

## Solución

Mide la distancia en unidades recorridas por unidad de tiempo: ambas
velocidades son 1 y el segmento mide t. En el instante de encuentro u,
el primer objeto ha recorrido u−s y el opuesto u−sᵢ. Su suma es t:

`(u − s) + (u − sᵢ) = t`, por tanto `2u = s + sᵢ + t`.

Para cada entrada imprime `(s + sᵢ + t) / 2`. Las desigualdades estrictas
garantizan `max(s, sᵢ) < u < min(s+t, sᵢ+t)`: el encuentro ocurre durante
ambos recorridos. No hace falta filtrar ni simular eventos.

La ecuación es necesaria porque los objetos ocupan el mismo punto.
La suma de las distancias aumenta estrictamente a ritmo 2, así que hay
una sola solución. Está dentro de ambos viajes y es el encuentro buscado.

El numerador es entero, por lo que la respuesta es entera o semientera.
Imprime el cociente entero y `.000000` si el numerador es par, o `.500000`
si es impar. La representación es exacta y no depende de la configuración
regional. No pierdas el resto mediante una división entera sin sufijo.
El numerador es menor que 2600; basta un entero de 32 bits.

El ejemplo da `(600+600+60)/2=630` y `(600+630+60)/2=645`.

Tiempo `O(n)` y estado aritmético `O(1)` por encuentro. Las implementaciones
que guardan tokens de entrada o acumulan salida usan espacio total `O(n)`.

## Notas por lenguaje

Las cinco versiones imprimen cociente y sufijo según la paridad. Basta
entrada/salida con búfer; Python usa CPython 3.12. Lee exactamente n
instantes adicionales; t es una duración y no un instante absoluto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1902_math.cpp](1902_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 436 KB |
| [1902_math.go](1902_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1104 KB |
| [1902_math.java](1902_math.java) | Java 1.8 | math | O(n) | AC | 0.109 s | 388 KB |
| [1902_math.py](1902_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 336 KB |
| [1902_math.rs](1902_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 228 KB |
