# 1075. El hilo más corto alrededor de una bola fija

[Timus 1075](https://acm.timus.ru/problem.aspx?space=1&num=1075) · dificultad 1982 · geometry

Problema original de Alexander Mironenko, del Ural State University Personal Contest Online, febrero de 2001, Students Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los puntos `A`, `B` y `C` del espacio tienen coordenadas enteras de valor
absoluto hasta 1000. Una bola sólida de radio entero `R` con centro en `C`
está fija, y tanto `A` como `B` están a más de `R` de `C`. Halla la
longitud del hilo más corto de `A` a `B` que no entra en la bola,
redondeada a dos decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las coordenadas de `A`, `B` y `C`, un punto por línea, y luego `R`.

## Salida

La longitud del hilo.

## Evaluación

Los números se comparan con un error absoluto de 0.011: las respuestas se
imprimen con dos decimales, así que la última cifra puede diferir en uno.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 0 12
12 0 0
10 0 10
10
```

Salida:

```
19.71
```

## Solución

El hilo más corto está en el plano que pasa por `A`, `B` y `C`, así que es
el camino más corto alrededor de un disco de radio `R` en ese plano. Sean
`a = |CA|`, `b = |CB|` y `φ` el ángulo `ACB`. Visto desde `C`, el punto
de tangencia desde `A` está a `α = arccos(R/a)` de la dirección de `A`, y
el de `B` a `β = arccos(R/b)` de la dirección de `B`.

- Si `φ ≤ α + β`, el segmento `AB` no entra en la bola, y la respuesta es
  `|AB|`.
- Si no, el hilo va por la tangente desde `A`, por el arco de ángulo
  `φ − α − β` y por la tangente hasta `B`:
  `√(a² − R²) + √(b² − R²) + R·(φ − α − β)`.

`O(1)`.

Detalles a tener en cuenta:

- `φ` obtenido con `arccos` del producto escalar normalizado pierde
  precisión cerca de 0 y de `π`; `atan2(|CA × CB|, CA · CB)` es preciso en
  todas partes, y los productos escalar y vectorial son enteros exactos;
- cuando `A`, `C` y `B` están en una recta con `C` en medio, el plano no
  es único, pero `φ = π` y la fórmula sigue valiendo;
- `A` puede coincidir con `B`; entonces `φ = 0` y la respuesta es 0.

Las respuestas se comprobaron de otra forma: el plano se extiende sobre
un dibujo, el segmento se prueba contra el disco por su distancia a `C`,
y si no, se comparan todos los caminos tangente–arco–tangente, con los dos
puntos de tangencia de cada extremo y los dos sentidos del arco.

## Notas por lenguaje

- C++ guarda los vectores en `long long` para que los productos sean
  exactos antes de las raíces.
- Python usa `math.hypot` con tres argumentos para las longitudes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1075_geometry.cpp](1075_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1075_geometry.go](1075_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1136 KB |
| [1075_geometry.java](1075_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1840 KB |
| [1075_geometry.py](1075_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 620 KB |
| [1075_geometry.rs](1075_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 248 KB |
