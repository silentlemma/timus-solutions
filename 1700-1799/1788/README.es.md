# 1788. Sobre la utilidad de los paraguas

[Timus 1788](https://acm.timus.ru/problem.aspx?space=1&num=1788) · dificultad 162 · greedy

Problema original de Sofia Tekhazheva (preparado por Denis Dublennykh), del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n chicas sin paraguas y m chicos con paraguas salen de una fiesta bajo
la lluvia. Cada chico puede acompañar a una chica bajo su paraguas. Una
chica que se moja se disgusta en gᵢ. Un chico que no acompaña a nadie
se disgusta en bⱼ·k, donde k es el número de chicos que sí acompañan a
una chica. Las chicas y chicos en pareja no se disgustan. Hallar el
menor disgusto total.

## Entrada

n y m (1 ≤ n, m ≤ 100), luego g₁, …, gₙ, luego b₁, …, bₘ, todos de 1 a
1000.

## Salida

El menor disgusto total.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 4
1 100
10 8 6 4
```

Salida:

```
19
```

## Solución

Se fija el número de parejas k. Entonces conviene mantener secas a las
k chicas con mayor gᵢ y que acompañen los k chicos con mayor bⱼ, ya que
cada persona sola cuesta su propio valor (multiplicado por k en los
chicos). Así el total es la suma de los n − k menores gᵢ más k por la
suma de los m − k menores bⱼ. Se ordenan ambas listas y se prueba cada
k de 0 a min(n, m). `O((n + m)²)`.

En el ejemplo sin parejas el coste es 101, y con dos parejas los chicos
con 6 y 4 dan 2·10 = 20. Una pareja, con la chica que se disgustaría en
100, deja a la chica con 1 y a los chicos con 8, 6 y 4 en 1·18, 19 en
total.

Trampas:

- el coste de los chicos crece con k, así que más parejas no siempre es
  mejor;
- también hay que probar k = 0: entonces ningún chico se disgusta;
- los mayores totales rondan 10⁷, bien dentro de enteros de 32 bits.

Las respuestas coinciden con una implementación aceptada independiente
en 150 grupos aleatorios: grupos cualesquiera, pequeños, y chicas
sensibles con chicos tranquilos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1788_greedy.cpp](1788_greedy.cpp) | G++ 13.2 x64 | greedy | O((n + m)^2) | AC | 0.015 s | 408 KB |
| [1788_greedy.go](1788_greedy.go) | Go 1.14 x64 | greedy | O((n + m)^2) | AC | 0.031 s | 1100 KB |
| [1788_greedy.java](1788_greedy.java) | Java 1.8 | greedy | O((n + m)^2) | AC | 0.140 s | 1824 KB |
| [1788_greedy.py](1788_greedy.py) | Python 3.12 x64 | greedy | O((n + m)^2) | AC | 0.078 s | 472 KB |
| [1788_greedy.rs](1788_greedy.rs) | Rust 1.75 x64 | greedy | O((n + m)^2) | AC | 0.015 s | 228 KB |
