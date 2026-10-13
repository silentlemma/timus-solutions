# 1366. Regalos

[Timus 1366](https://acm.timus.ru/problem.aspx?space=1&num=1366) · dificultad 523 · math

Problema original con idea de Stanislav Vasiliev, preparado por Pavel Egorov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de n ≤ 1000 niños trae un regalo, y los regalos se intercambian
de modo que cada niño reciba exactamente un regalo y nadie se quede con
el suyo. Hay que contar las formas de hacerlo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número n.

## Salida

La cantidad de intercambios.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
2
```

## Solución

Un intercambio es una permutación sin puntos fijos, un desarreglo. Por
inclusión–exclusión su número es d(k) = Σ (−1)ⁱ · k! / i! con
i = 0 … k, y multiplicar d(k − 1) por k da todos los términos de d(k)
salvo el último, (−1)ᵏ. Así que d(1) = 0 y d(k) = k · d(k − 1) + (−1)ᵏ:
se empieza en 0 y se aplica para k = 2 … n.

La respuesta para n = 1000 tiene 2 568 cifras, así que hace falta
aritmética larga: cada paso multiplica por un número pequeño y suma o
resta 1. `O(n² log n)` operaciones con cifras.

Detalles a tener en cuenta:

- un solo niño no puede intercambiar: la respuesta es 0 (prueba 02);
- d(21) es el primer valor que ya no cabe en 64 bits (prueba 06);
- tras la multiplicación el número vale al menos 3 para k ≥ 3, así que
  restar 1 nunca baja de cero.

La recurrencia se comparó con contar todas las permutaciones para n ≤ 8
y con la suma de inclusión–exclusión para n = 50.

## Notas por lenguaje

- Python usa enteros grandes incorporados; Go y Java, los de su biblioteca estándar.
- C++ y Rust guardan el número en trozos de nueve cifras decimales,
  empezando por el más bajo, e imprimen todos los trozos salvo el más
  alto completados a nueve cifras.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1366_math.cpp](1366_math.cpp) | G++ 13.2 x64 | math | O(n² log n) | AC | 0.031 s | 196 KB |
| [1366_math.go](1366_math.go) | Go 1.14 x64 | math | O(n² log n) | AC | 0.031 s | 1268 KB |
| [1366_math.java](1366_math.java) | Java 1.8 | math | O(n² log n) | AC | 0.125 s | 3320 KB |
| [1366_math.py](1366_math.py) | Python 3.12 x64 | math | O(n² log n) | AC | 0.093 s | 412 KB |
| [1366_math.rs](1366_math.rs) | Rust 1.75 x64 | math | O(n² log n) | AC | 0.046 s | 252 KB |
