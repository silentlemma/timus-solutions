# 1599. Número de vueltas

[Timus 1599](https://acm.timus.ru/problem.aspx?space=1&num=1599) · dificultad 1732 · geometry

Problema original de Vladimir Yakovlev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un ferrocarril cerrado pasa por n uniones (3 ≤ n ≤ 5000) siguiendo vías
rectas, que pueden cruzarse y solaparse. Para cada uno de m puntos de
observación (1 ≤ m ≤ 5000) hay que imprimir `EDGE` si el punto está sobre una
vía y, si no, cuántas vueltas completas en sentido antihorario da quien
sigue al tren durante una vuelta: su número de vueltas. Las coordenadas
son enteros de valor absoluto hasta 10⁹.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La primera línea contiene n, seguida de n líneas de coordenadas x y
de las uniones en orden de recorrido. Las vías unen uniones sucesivas
y la última con la primera. Luego viene m, seguido de m líneas de
coordenadas x y de los puntos de observación.

## Salida

Para cada punto, en una línea aparte, imprimir `EDGE` o el número de
vueltas con signo: positivo en sentido antihorario y negativo en sentido horario.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
-2 -2
-5 1
-2 4
1 3
-2 0
-3 1
-2 2
1 1
3
-2 1
0 0
1 2
```

Salida:

```
-2
EDGE
0
```

## Solución

Se mira a lo largo del rayo que sale del punto hacia la derecha. Cada vez
que el tren lo cruza hacia arriba pasa junto al punto en sentido
antihorario, y hacia abajo en sentido horario. Así que el número de
vueltas es el número de vías que cruzan el rayo hacia arriba menos las
que lo cruzan hacia abajo. Una vía de a a b lo cruza hacia arriba cuando
a.y ≤ p.y < b.y y el punto queda a su izquierda, es decir,
cross(b − a, p − a) > 0, y hacia abajo cuando b.y ≤ p.y < a.y y el punto
queda a su derecha. Contar el extremo inferior de cada vía pero no el
superior cuenta una vez un cruce por una unión; en una tangencia, las
contribuciones se cancelan o ambas quedan excluidas. Las vías
horizontales no contribuyen a la suma de vueltas.

Un punto está sobre una vía cuando el producto vectorial es 0 y el punto
está dentro del rectángulo que la contiene. Para cada punto se recorren
las vías y se comprueba esta condición antes de contar los cruces; si
se cumple, se detiene el recorrido y se imprime `EDGE`. En caso
contrario, se imprime la suma al terminar. El tiempo en el peor caso
es `O(n·m)`, como máximo 2,5·10⁷ comprobaciones de vías solo con enteros.

Los resultados se contrastaron con sumar los ángulos de giro con atan2
en recorridos pequeños, incluidos recorridos que pasan por las filas de
los puntos y recorridos de ida y vuelta.

Detalles a tener en cuenta:

- el valor absoluto del producto vectorial no supera (2·10⁹)² = 4·10¹⁸,
  menor que el máximo de un entero con signo de 64 bits, 2⁶³ − 1;
  los enteros de 32 bits no bastan;
- en las uniones sobre el rayo, los cruces se cuentan una vez y las
  tangencias tienen contribución neta cero; las pruebas semiabiertas
  sobre y lo resuelven, y las vías horizontales solo importan para `EDGE`;
- los recorridos opuestos de una misma vía se cancelan en la suma de
  vueltas, y las vías de longitud cero aportan cero; ambos casos
  siguen requiriendo la comprobación de `EDGE`.

## Notas por lenguaje

- Python se ejecuta con PyPy, construye de antemano las tuplas de las
  aristas y usa enteros de precisión arbitraria. C++, Go, Java y Rust
  obtienen el siguiente extremo por índice y usan aritmética geométrica
  con enteros con signo de 64 bits.
- Java lee los números mediante `StreamTokenizer` como double, que
  representa exactamente todas las coordenadas enteras permitidas,
  y los convierte a `long` antes de los cálculos geométricos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1599_geometry.cpp](1599_geometry.cpp) | G++ 13.2 x64 | geometry | O(n·m) | AC | 0.250 s | 228 KB |
| [1599_geometry.go](1599_geometry.go) | Go 1.14 x64 | geometry | O(n·m) | AC | 0.515 s | 1572 KB |
| [1599_geometry.java](1599_geometry.java) | Java 1.8 | geometry | O(n·m) | AC | 0.781 s | 936 KB |
| [1599_geometry.py](1599_geometry.py) | PyPy 3.10 x64 | geometry | O(n·m) | AC | 0.906 s | 5464 KB |
| [1599_geometry.rs](1599_geometry.rs) | Rust 1.75 x64 | geometry | O(n·m) | AC | 0.328 s | 612 KB |
