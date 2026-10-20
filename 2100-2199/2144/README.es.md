# 2144. Ordenar cajas cerradas en una sola fila ordenada

[Timus 2144](https://acm.timus.ru/problem.aspx?space=1&num=2144) · dificultad 221 · sorting

Problema original de Ivan Smirnov, del Concurso Escolar de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n cajas, cada una con una fila fija de tamaños de figuras que no se
puede reordenar ni invertir. Decidir si las cajas se pueden poner en
algún orden de modo que todos los tamaños juntos formen una fila no
decreciente. Los límites son 0.5 segundos y 256 MB.

## Entrada

n, 1 ≤ n ≤ 100, y luego para cada caja kᵢ, 1 ≤ kᵢ ≤ 100, y sus tamaños,
1 ≤ aᵢⱼ ≤ 10⁴.

## Salida

YES o NO.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2 1 2
3 7 7 7
1 5
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
2
2 1 3
1 2
```

Salida:

```
NO
```

## Solución

Cada caja debe ser no decreciente por dentro. Después solo importan su
primer tamaño f y su último tamaño l, y un orden válido necesita que l de
cada caja sea a lo sumo f de la siguiente.

En cualquier orden válido los primeros tamaños no decrecen, porque
f ≤ l ≤ f de la caja siguiente. Entre las cajas con el mismo primer
tamaño f, todas menos la última tienen l ≤ f, es decir, l = f. Por eso
ordenar las cajas por (f, l) da un orden válido siempre que exista, y
basta comprobar los vecinos en ese orden. El trabajo es
O(Σ kᵢ + n log n).

En el primer ejemplo las cajas (1, 2), (5, 5) y (7, 7) encajan en ese
orden; en el segundo (1, 3) y (2, 2) se solapan.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2144_sorting.cpp](2144_sorting.cpp) | G++ 13.2 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 192 KB |
| [2144_sorting.go](2144_sorting.go) | Go 1.14 x64 | sorting | O(sum k + n log n) | AC | 0.031 s | 1328 KB |
| [2144_sorting.java](2144_sorting.java) | Java 1.8 | sorting | O(sum k + n log n) | AC | 0.187 s | 6900 KB |
| [2144_sorting.py](2144_sorting.py) | Python 3.12 x64 | sorting | O(sum k + n log n) | AC | 0.062 s | 1140 KB |
| [2144_sorting.rs](2144_sorting.rs) | Rust 1.75 x64 | sorting | O(sum k + n log n) | AC | 0.015 s | 336 KB |
