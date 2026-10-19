# 1867. Nanotecnologías

[Timus 1867](https://acm.timus.ru/problem.aspx?space=1&num=1867) · dificultad 2551 · geometry

Problema original de Sergey Pupyrev (preparado por Ivan Burmistrov), del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan los cuadrados de las distancias entre cada dos de n átomos. Hay
que colocar los átomos en puntos de coordenadas enteras con valor
absoluto de como mucho 10⁶ de modo que todos los cuadrados de las
distancias sean los dados, o decir que es imposible. Varios átomos
pueden compartir un punto.

## Entrada

n (2 ≤ n ≤ 100), luego la matriz simétrica n × n de enteros aᵢⱼ
(0 ≤ aᵢⱼ ≤ 10⁹, aᵢᵢ = 0).

## Salida

n líneas con las coordenadas de los átomos, o "Impossible". Se acepta
cualquier colocación válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 1 4
1 0 1
4 1 0
```

Salida:

```
0 0
1 0
2 0
```

### Ejemplo 2

Entrada:

```
3
0 1 5
1 0 1
5 1 0
```

Salida:

```
Impossible
```

### Ejemplo 3

Entrada:

```
3
0 1 0
1 0 1
0 1 0
```

Salida:

```
5 -5
5 -4
5 -5
```

## Solución

Las traslaciones conservan la cuadrícula, así que el átomo 1 puede ir
al origen. Sea p el primer átomo a una distancia al cuadrado D positiva de él. Los
giros de un cuarto de vuelta y las reflexiones en los ejes y las
diagonales también conservan la cuadrícula, así que p puede tomarse en
(a, b) con 0 ≤ a ≤ b y a² + b² = D. Estos pares se hallan probando cada
a hasta √(D/2), y se prueba cada uno.

Con los átomos 1 y p fijos, otro átomo (x, y) a distancias al cuadrado
d₁ y dₚ de ellos tiene producto escalar ax + by = (d₁ − dₚ + D)/2. Su
producto vectorial bx − ay vale ±√(D·d₁ − dot²), porque
dot² + cross² = D·(x² + y²). Entonces x = (a·dot + b·cross)/D e
y = (b·dot − a·cross)/D, y todo ello debe ser entero. Los átomos sobre
la recta que pasa por 1 y p tienen cross 0. El primer átomo fuera de
esa recta puede ir a cualquiera de sus lados, y se prueban ambos: la
imagen especular de un punto entero en una recta inclinada no suele ser
entera. Después solo un signo concuerda con la distancia a ese átomo.
Cada átomo se compara con todos los colocados antes, así que una
colocación que llega al final es una respuesta. Sus coordenadas quedan
a menos de √10⁹ del origen, muy dentro del límite.
`O(√D + r·n²)`, donde r, el número de formas de escribir D como
a² + b², es como mucho unas decenas.

Para el primer ejemplo esto da (0, 0), (0, 1), (0, 2) y para el
tercero (0, 0), (0, 1), (0, 0); ambas valen tanto como las del
enunciado.

Trampas:

- las distintas formas de escribir D no son iguales:
  25 = 0² + 5² = 3² + 4², y los átomos en (0, 0), (3, 4) y (4, 3) solo
  encajan con la segunda;
- por la misma razón hay que probar los dos lados de la primera recta
  inclinada;
- los átomos pueden compartir punto, también con el átomo 1, y todas
  las distancias pueden ser 0;
- los productos llegan a 10¹⁸, así que hacen falta enteros de 64 bits.

Las respuestas pasan un comprobador en todas las matrices de 3 átomos
con elementos hasta 13 y de 4 átomos con elementos hasta 5, comparadas
con todas las colocaciones pequeñas, y en casos grandes aleatorios. Las
respuestas "Impossible" coinciden con una implementación aceptada
independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1867_geometry.cpp](1867_geometry.cpp) | G++ 13.2 x64 | geometry | O(sqrt(D) + r n^2) | AC | 0.015 s | 280 KB |
| [1867_geometry.go](1867_geometry.go) | Go 1.14 x64 | geometry | O(sqrt(D) + r n^2) | AC | 0.031 s | 1340 KB |
| [1867_geometry.java](1867_geometry.java) | Java 1.8 | geometry | O(sqrt(D) + r n^2) | AC | 0.140 s | 636 KB |
| [1867_geometry.py](1867_geometry.py) | Python 3.12 x64 | geometry | O(sqrt(D) + r n^2) | AC | 0.093 s | 1676 KB |
| [1867_geometry.rs](1867_geometry.rs) | Rust 1.75 x64 | geometry | O(sqrt(D) + r n^2) | AC | 0.046 s | 440 KB |
