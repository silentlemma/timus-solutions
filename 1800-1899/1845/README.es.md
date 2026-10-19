# 1845. Determinante complejo de valores enteros

[Timus 1845](https://acm.timus.ru/problem.aspx?space=1&num=1845) · dificultad 4252 · number_theory

Problema original de Dmitry Poletaev e Ivan Burmistrov, del Ural SU Contest en la sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un entero gaussiano es un número complejo con partes real e imaginaria
enteras. Si a = bq + r para enteros gaussianos con |r| < |b|, entonces r
es un resto de a módulo b. Dada una matriz n × n de enteros gaussianos y
un entero gaussiano p no nulo, hallar un resto del determinante de la
matriz módulo p.

## Entrada

n (1 ≤ n ≤ 50), luego las n filas de la matriz, cada elemento con su
parte real e imaginaria, y al final p igual. Todas las partes valen como
mucho 10 000 en valor absoluto.

## Salida

La parte real e imaginaria de un resto. Se acepta cualquier resto.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
2 0 -7 0
1 0 0 -1
3 1
```

Salida:

```
3 0
```

## Solución

El determinante puede tener cientos de cifras, así que las soluciones
compiladas nunca lo construyen. El determinante módulo p no cambia al
sustituir cada elemento por su resto módulo p, y no cambia en absoluto
al sumar a una fila un múltiplo de otra. Los enteros gaussianos tienen
división con resto: redondear ambas partes de x / y al entero más
cercano da un cociente q con |x − qy|² ≤ |y|² / 2. Así cada columna se
anula bajo la diagonal con el algoritmo de Euclides sobre filas: restar
a la fila del pivote q veces la fila de abajo, intercambiarlas
(cambiando el signo) y repetir hasta que el elemento de abajo sea cero.
Los elementos de la columna solo se achican, y todos los demás
elementos modificados se reducen otra vez módulo p, así que los números
quedan por debajo de unos 2·10⁸ y caben en 64 bits. El determinante es
el producto de la diagonal, reducido módulo p tras cada factor.
`O(n³ log |p|)`.

La solución en Python va por el otro camino: calcula el determinante
exacto con la eliminación de Bareiss, donde cada elemento se actualiza
como (a·c − b·d) / pivote anterior y la división siempre es exacta, y lo
reduce una vez al final. Los enteros grandes de Python manejan rápido
unos cientos de cifras.

En el ejemplo el determinante es 2·(−i) − (−7)·1 = 7 − 2i. Como
(3 + i)(1 − i) = 4 − 2i, el resto puede ser 3; como
(3 + i)(2 − i) = 7 − i, también puede ser −i, que es lo que imprimen
las soluciones.

Trampas:

- el resto no es único, así que las respuestas se juzgan con un
  verificador;
- un p unidad solo deja el resto 0;
- el redondeo debe ser el suelo de (2x + n) / 2n, no un truncamiento,
  para partes negativas.

Los restos pasan un verificador que calcula el determinante exacto y
comprueba la divisibilidad, en matrices aleatorias de hasta 50 × 50 con
pivotes nulos, filas iguales, unidades y módulos compuestos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1845_number_theory.cpp](1845_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n^3 log p) | AC | 0.015 s | 264 KB |
| [1845_number_theory.go](1845_number_theory.go) | Go 1.14 x64 | number_theory | O(n^3 log p) | AC | 0.031 s | 1156 KB |
| [1845_number_theory.java](1845_number_theory.java) | Java 1.8 | number_theory | O(n^3 log p) | AC | 0.125 s | 4096 KB |
| [1845_number_theory.py](1845_number_theory.py) | Python 3.12 x64 | number_theory | O(n^3 log p) | AC | 0.250 s | 1880 KB |
| [1845_number_theory.rs](1845_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n^3 log p) | AC | 0.046 s | 308 KB |
