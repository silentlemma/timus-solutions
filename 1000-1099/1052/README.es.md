# 1052. El máximo de puntos en una recta

[Timus 1052](https://acm.timus.ru/problem.aspx?space=1&num=1052) · dificultad 238 · geometry

Problema original de Stanislav Vasiliev, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `N` puntos distintos (`3 ≤ N ≤ 200`) con coordenadas enteras de
−2000 a 2000, halla el mayor número de ellos que están en una misma recta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas con `x` e `y`.

## Salida

El mayor número de puntos en una recta.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
7 122
8 139
9 156
10 173
11 190
-100 1
```

Salida:

```
5
```

### Ejemplo 2

Entrada:

```
3
0 0
1 0
0 1
```

Salida:

```
2
```

## Solución

Se fija un punto `i` y se miran las direcciones hacia los puntos que van
después. Dos puntos `j`, `k` están en una recta con `i` exactamente cuando
los vectores `i → j` e `i → k` son paralelos. Se hace canónico cada
vector: se divide `(dx, dy)` entre `gcd(|dx|, |dy|)` y se cambia el signo
para que `dx > 0`, o `dx = 0` y `dy > 0`. Así los vectores paralelos
quedan iguales, y contar direcciones iguales en un mapa da la recta más
larga por `i` (más el propio `i`). Basta tomar `i` como el primer punto de
cada recta en el orden de la entrada, así que solo se cuentan los puntos
posteriores. `O(N^2 log C)`.

Los enteros hacen exacta la comparación; con pendientes en coma flotante,
las rectas verticales y las pendientes casi iguales exigen cuidado.

Detalles a tener en cuenta:

- rectas verticales (`dx = 0`) y horizontales (`dy = 0`);
- vectores opuestos describen la misma recta: hay que normalizar el
  signo;
- dos puntos cualesquiera están en una recta, así que la respuesta es al
  menos 2.

Una alternativa es la comprobación `O(N^3)` de cada par con cada punto
mediante un producto vectorial, también bastante rápida para `N = 200`;
las pruebas se comprobaron con ella.

## Notas por lenguaje

- **C++**, **Go**, **Python**, **Rust**: un mapa con la pareja de
  componentes como clave.
- **Java**: la pareja se empaqueta en una sola clave `long`
  (`dx · 8192 + dy`, ya que `|dy| ≤ 4000`).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1052_geometry.cpp](1052_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2 log C) | AC | 0.001 s | 208 KB |
| [1052_geometry.go](1052_geometry.go) | Go 1.14 x64 | geometry | O(N^2 log C) | AC | 0.015 s | 3264 KB |
| [1052_geometry.java](1052_geometry.java) | Java 1.8 | geometry | O(N^2 log C) | AC | 0.156 s | 4180 KB |
| [1052_geometry.py](1052_geometry.py) | Python 3.12 x64 | geometry | O(N^2 log C) | AC | 0.078 s | 508 KB |
| [1052_geometry.rs](1052_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2 log C) | AC | 0.015 s | 412 KB |
