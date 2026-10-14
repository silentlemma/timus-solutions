# 1625. Matriz de Hankel

[Timus 1625](https://acm.timus.ru/problem.aspx?space=1&num=1625) · dificultad 1046 · math

Problema original del SPbSU ITMO Contest en el campus de Petrozavodsk, invierno de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una matriz de Hankel de tamaño n tiene α(i + j − 1) en la fila i,
columna j, así que se construye a partir de α1, …, α(2n−1). Para
1 ≤ n ≤ 100, halla enteros no negativos de a lo sumo 300 cifras tales
que toda submatriz cuadrada que contenga la celda superior izquierda
tenga determinante 1. Se acepta cualquier conjunto así.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n.

## Salida

α1, …, α(2n−1), uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
2
```

Salida:

```
1
6
37
```

### Ejemplo 3

Entrada:

```
3
```

Salida:

```
1
3
10
7
630
```

## Solución

Los números de Catalan 1, 1, 2, 5, 14, … sirven: la matriz de Hankel
[C(i + j)] tiene determinante 1 en cada cuadrado principal. Por el lema
de Lindström–Gessel–Viennot ese determinante cuenta familias de caminos
reticulares que no se cruzan, y C(i + j) cuenta los caminos de tipo Dyck
de un punto inicial a uno final; para estos puntos solo una familia no se
cruza, así que todo determinante es 1.

C(198) tiene 116 cifras, holgadamente dentro del límite. Cada número sale
del anterior: C(k + 1) = C(k) · 2(2k + 1) / (k + 2), y la división es
exacta. Python, Go y Java usan sus enteros grandes; C++ y Rust guardan el
número en dígitos de base 10⁹ con multiplicación y división por un
número pequeño. `O(n²)`.

Detalles a tener en cuenta:

- las respuestas de los ejemplos son otras, así que un verificador
  comprueba los determinantes (módulo tres primos grandes, por
  eliminación cuyos pivotes son los menores principales);
- con n = 1 basta el número 1.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1625_math.cpp](1625_math.cpp) | G++ 13.2 x64 | math | O(n²) | AC | 0.015 s | 228 KB |
| [1625_math.go](1625_math.go) | Go 1.14 x64 | math | O(n²) | AC | 0.015 s | 1164 KB |
| [1625_math.java](1625_math.java) | Java 1.8 | math | O(n²) | AC | 0.125 s | 2116 KB |
| [1625_math.py](1625_math.py) | Python 3.12 x64 | math | O(n²) | AC | 0.078 s | 416 KB |
| [1625_math.rs](1625_math.rs) | Rust 1.75 x64 | math | O(n²) | AC | 0.015 s | 288 KB |
