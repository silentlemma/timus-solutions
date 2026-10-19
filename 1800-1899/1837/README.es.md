# 1837. El número de Isenbaev

[Timus 1837](https://acm.timus.ru/problem.aspx?space=1&num=1837) · dificultad 60 · bfs

Problema original del folclore, del XV Campeonato Abierto de los Urales de Programación Competitiva, abril de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El número de Isenbaev vale 0 para el propio Vladislav Isenbaev, 1 para
sus compañeros de equipo, 2 para los compañeros de estos que nunca
jugaron con Isenbaev, y así sucesivamente. Dados los equipos, imprimir
el número de cada concursante, o "undefined" si no hay cadena de equipos
hasta Isenbaev.

## Entrada

n (1 ≤ n ≤ 100), luego n equipos de tres apellidos (una mayúscula
seguida de minúsculas, como mucho 20 letras). El apellido de Isenbaev
es "Isenbaev".

## Salida

Cada concursante con su número, ordenados por apellido.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
Isenbaev Oparin Toropov
Ayzenshteyn Oparin Samsonov
Ayzenshteyn Chevdar Samsonov
Fominykh Isenbaev Oparin
Dublennykh Fominykh Ivankov
Burmistrov Dublennykh Kurpilyanskiy
Cormen Leiserson Rivest
```

Salida:

```
Ayzenshteyn 2
Burmistrov 3
Chevdar 3
Cormen undefined
Dublennykh 2
Fominykh 1
Isenbaev 0
Ivankov 2
Kurpilyanskiy 3
Leiserson undefined
Oparin 1
Rivest undefined
Samsonov 2
Toropov 1
```

## Solución

Se unen en un grafo cada dos miembros de un mismo equipo. El número es
la distancia desde Isenbaev, hallada con una búsqueda en anchura; los
concursantes a los que no llega son undefined. Los nombres se imprimen
ordenados. Con como mucho 300 concursantes, cualquier método es
rápido. `O(n log n)` por la ordenación.

En el ejemplo Oparin jugó con Isenbaev (1), Ayzenshteyn con Oparin (2),
Chevdar con Ayzenshteyn (3), y el equipo de Cormen está aislado.

Trampas:

- Isenbaev puede no aparecer; entonces todos son undefined;
- el mismo equipo puede aparecer dos veces;
- los nombres se comparan como cadenas simples, todos con mayúscula
  inicial.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1837_bfs.cpp](1837_bfs.cpp) | G++ 13.2 x64 | bfs | O(n log n) | AC | 0.015 s | 552 KB |
| [1837_bfs.go](1837_bfs.go) | Go 1.14 x64 | bfs | O(n log n) | AC | 0.031 s | 1420 KB |
| [1837_bfs.java](1837_bfs.java) | Java 1.8 | bfs | O(n log n) | AC | 0.171 s | 4192 KB |
| [1837_bfs.py](1837_bfs.py) | Python 3.12 x64 | bfs | O(n log n) | AC | 0.093 s | 560 KB |
| [1837_bfs.rs](1837_bfs.rs) | Rust 1.75 x64 | bfs | O(n log n) | AC | 0.046 s | 468 KB |
