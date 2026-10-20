# 2165. Triangulación de un polígono convexo con el mayor triángulo mínimo

[Timus 2165](https://acm.timus.ru/problem.aspx?space=1&num=2165) · dificultad 1622 · dp, geometry

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2021.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cortar un polígono convexo de N vértices en triángulos con diagonales que
no se crucen de modo que el triángulo más pequeño sea lo mayor posible, e
imprimir su área con error absoluto o relativo de hasta 10⁻⁹. Los límites son 1 segundo y
256 MB.

## Entrada

N, 3 ≤ N ≤ 200, y luego los vértices en sentido antihorario, con
coordenadas de hasta 10⁸ en valor absoluto.

## Salida

La mayor área posible del triángulo más pequeño.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
5 -1
8 3
0 4
```

Salida:

```
11.5
```

## Solución

Es la DP clásica por intervalos sobre triangulaciones. Sea f(i, j) el
mejor triángulo mínimo en una triangulación del subpolígono de vértices
i … j. Su lado (i, j) pertenece a exactamente un triángulo (i, k, j) con
i < k < j, que lo parte en i … k y k … j, así que

f(i, j) = max sobre k de min(f(i, k), f(k, j), área(i, k, j)),

con f(i, i + 1) = +∞ para un solo lado: una arista no debe limitar el
mínimo. C++ y Python usan el doble del área del polígono; Go, Java y Rust
usan la cota superior segura 8 · 10¹⁶. Usar cero anularía todos los valores,
incluso en el test 02. La respuesta es f(0, N − 1).
Las áreas se guardan dobladas como enteros
exactos, de productos vectoriales de hasta unos 4 · 10¹⁶, así que el
semientero final se imprime de forma exacta. Los candidatos que no
pueden superar al mejor actual se descartan pronto. El trabajo es O(N³).

En el ejemplo las dos triangulaciones del cuadrilátero dan piezas
mínimas de 11.5 y 10, así que la respuesta es 11.5.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2165_dp_geometry.cpp](2165_dp_geometry.cpp) | G++ 13.2 x64 | dp, geometry | O(N^3) | AC | 0.031 s | 764 KB |
| [2165_dp_geometry.go](2165_dp_geometry.go) | Go 1.14 x64 | dp, geometry | O(N^3) | AC | 0.031 s | 1444 KB |
| [2165_dp_geometry.java](2165_dp_geometry.java) | Java 1.8 | dp, geometry | O(N^3) | AC | 0.109 s | 816 KB |
| [2165_dp_geometry.py](2165_dp_geometry.py) | Python 3.12 x64 | dp, geometry | O(N^3) | AC | 0.171 s | 2656 KB |
| [2165_dp_geometry.rs](2165_dp_geometry.rs) | Rust 1.75 x64 | dp, geometry | O(N^3) | AC | 0.015 s | 464 KB |
