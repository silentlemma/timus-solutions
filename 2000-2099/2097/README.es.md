# 2097. Hallar un tramo que difiere en una función lineal

[Timus 2097](https://acm.timus.ru/problem.aspx?space=1&num=2097) · dificultad 2202 · strings

Problema original de Dmitry Ivankov, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una pista nueva tiene alturas x₀ … x_m, y se dan del mismo modo n pistas
antiguas. Un tramo y₀ … y_m de una pista antigua es parecido si
xᵢ − yᵢ = a·i + b para todo i y algunos a y b. Hallar una pista y el
inicio de un tramo parecido con el menor |a|, o imprimir −1. Se acepta
cualquier respuesta así. Los límites son 1 segundo y 64 MB.

## Entrada

n ≤ 10⁵, después m ≤ 10⁵ y x₀ … x_m, y después cada pista antigua como
su longitud y sus alturas; las longitudes suman a lo sumo 10⁵ y las
alturas son de hasta 10⁹ en valor absoluto.

## Salida

El número de la pista y el inicio del tramo (los metros desde su
comienzo), o −1.

## Evaluación

Un comprobador acepta −1 solo cuando la salida esperada lo dice, y si no
comprueba que el tramo es parecido y que su |a| es el menor.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
2 3 2 1
5 21 15 10 6 3 2
4 10 7 5 3 2
```

Salida:

```
2 1
```

### Ejemplo 2

Entrada:

```
3
2 0 0 0
1 0 0
2 1 2 4
1 5 17
```

Salida:

```
-1
```

## Solución

La diferencia xᵢ − yᵢ es lineal exactamente cuando sus segundas
diferencias se anulan, es decir, cuando las segundas diferencias de x y
del tramo coinciden. Así que las m − 1 segundas diferencias de x se
buscan en las segundas diferencias de cada pista antigua con el
algoritmo de Knuth–Morris–Pratt; cada aparición en la posición j es un
tramo parecido que empieza en j, y su a es (x₁ − x₀) − (y_{j+1} − y_j).
Se guarda el menor |a| sobre todas las apariciones. Cuando m = 1 el
patrón es vacío y encaja todo inicio de toda pista suficientemente
larga. Los valores llegan a 4·10⁹, así que se usan enteros de 64 bits, y
el trabajo es lineal en el tamaño de la entrada.

En el primer ejemplo la pista nueva 3, 2, 1 tiene segunda diferencia 0,
que aparece en la segunda pista 10, 7, 5, 3, 2 solo en la posición 1.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2097_strings.cpp](2097_strings.cpp) | G++ 13.2 x64 | strings | O(input) | AC | 0.218 s | 2808 KB |
| [2097_strings.go](2097_strings.go) | Go 1.14 x64 | strings | O(input) | AC | 0.078 s | 9636 KB |
| [2097_strings.java](2097_strings.java) | Java 1.8 | strings | O(input) | AC | 0.140 s | 15548 KB |
| [2097_strings.py](2097_strings.py) | Python 3.12 x64 | strings | O(input) | AC | 0.265 s | 24900 KB |
| [2097_strings.rs](2097_strings.rs) | Rust 1.75 x64 | strings | O(input) | AC | 0.046 s | 5388 KB |
