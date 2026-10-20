# 2163. Valores posibles de una casilla dadas las sumas de filas y columnas

[Timus 2163](https://acm.timus.ru/problem.aspx?space=1&num=2163) · dificultad 1184 · math

Problema original de Semyon Trifochkin, del Concurso Escolar de Programación de los Urales 2021.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una matriz de enteros no negativos tiene sumas de filas r₁ … rₙ y sumas
de columnas c₁ … cₘ conocidas. Contar cuántos valores puede tomar la
casilla de la fila a y la columna b sobre todas esas matrices; la
respuesta es 0 si no existe ninguna. Los límites son 1 segundo y 256 MB.

## Entrada

n y m, 1 ≤ n, m ≤ 1000, a y b, las sumas de filas y luego las de
columnas, cada una de 0 a 10⁹.

## Salida

El número de valores posibles.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2
1 1
15
5 10
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
2 2
2 2
10 15
12 13
```

Salida:

```
11
```

## Solución

Existe una matriz exactamente cuando las sumas de filas y las de columnas
tienen el mismo total T: entonces el clásico relleno voraz por filas y
columnas construye una. Ahora se fija la casilla en x. Hace falta
x ≤ rₐ y x ≤ c_b. El resto de la fila a, rₐ − x, tiene que ir a las demás
columnas, cuyas sumas suman T − c_b, y del mismo modo c_b − x tiene que
caber en las demás filas, T − rₐ; ambas condiciones dicen
x ≥ rₐ + c_b − T. Con ellas, lo que queda es de nuevo una matriz con
totales iguales y una casilla fija en cero, que el mismo relleno voraz
construye. Así que los valores forman el intervalo de
max(0, rₐ + c_b − T) a min(rₐ, c_b), y la respuesta es su longitud, al
menos 1. Las sumas necesitan 64 bits. El trabajo es O(n + m).

En el segundo ejemplo T = 25, r₂ = 15 y c₂ = 13, así que la casilla toma
los valores 3 … 13, once en total.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2163_math.cpp](2163_math.cpp) | G++ 13.2 x64 | math | O(n + m) | AC | 0.015 s | 448 KB |
| [2163_math.go](2163_math.go) | Go 1.14 x64 | math | O(n + m) | AC | 0.015 s | 1104 KB |
| [2163_math.java](2163_math.java) | Java 1.8 | math | O(n + m) | AC | 0.093 s | 376 KB |
| [2163_math.py](2163_math.py) | Python 3.12 x64 | math | O(n + m) | AC | 0.093 s | 472 KB |
| [2163_math.rs](2163_math.rs) | Rust 1.75 x64 | math | O(n + m) | AC | 0.031 s | 228 KB |
