# 1768. Cuerdas circulares

[Timus 1768](https://acm.timus.ru/problem.aspx?space=1&num=1768) · dificultad 1156 · geometry

Problema original de Dmitry Ivankov, del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados n puntos, decidir si son los vértices de un n-ágono regular no
degenerado, listados en orden a su alrededor.

## Entrada

n (3 ≤ n ≤ 100) y luego n puntos con coordenadas reales de 0 a 1, dadas
con precisión de al menos 10⁻¹⁰. Los puntos pueden coincidir, pero hay
dos a distancia de al menos 0.3. Cuando la respuesta es no, ningún
cambio de los puntos de menos de 10⁻⁵ la hace sí.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
1 0
1 1
0 1
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
3
0 0
1 0
0.5 1
```

Salida:

```
NO
```

## Solución

El centro de un polígono regular es la media de sus vértices, y,
listados en orden, cada vértice es el anterior girado alrededor del
centro 2π/n en un sentido o en el otro. Así que, con los puntos como
números complejos zᵢ medidos desde su media, la respuesta es sí cuando
zᵢ₊₁ = ω·zᵢ para todo i, cíclicamente, con ω = e^(±2πi/n), y z₀ no es
el propio centro. `O(n)`.

Las igualdades se comprueban con una tolerancia de 10⁻⁸. Los puntos
dados con precisión 10⁻¹⁰ fallan como mucho en unos pocos 10⁻¹⁰. Si
cada giro fallara en a lo sumo ε, los puntos estarían a menos de n·ε
del polígono regular construido a partir de z₀, así que un conjunto que
necesita un cambio de 10⁻⁵ falla en más de 10⁻⁵/n ≥ 10⁻⁷ en algún
lugar.

En el primer ejemplo la media es (0.5, 0.5), y un cuarto de vuelta
lleva cada esquina del cuadrado a la siguiente. En el segundo los tres
puntos no están a la misma distancia de su media.

Trampas:

- el orden puede ir en cualquier sentido;
- los puntos correctos en otro orden, como una estrella, no bastan;
- un polígono menor recorrido dos veces repite puntos y no vale.

Las respuestas coinciden con una implementación aceptada independiente
en 160 casos aleatorios: polígonos regulares en orden, con un vértice
movido al menos 0.001, en orden de estrella y recorridos más de una
vez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1768_geometry.cpp](1768_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 212 KB |
| [1768_geometry.go](1768_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1132 KB |
| [1768_geometry.java](1768_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.140 s | 660 KB |
| [1768_geometry.py](1768_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.078 s | 488 KB |
| [1768_geometry.rs](1768_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.062 s | 244 KB |
