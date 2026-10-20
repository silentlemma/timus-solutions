# 2208. Hallar dos números con un factor común en un rango con cambios

[Timus 2208](https://acm.timus.ru/problem.aspx?space=1&num=2208) · dificultad 1469 · number_theory, segment_tree

Problema original de Konstantin Rychkov, de la Olimpiada Académica Universitaria Escolar de Informática 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo de N números entre 2 y 10⁶ recibe Q operaciones: cambiar un
elemento, o dar dos posiciones de un rango [l, r] cuyos números no son
coprimos, o −1 si no las hay. Se acepta cualquier par válido. Los
límites son 2 segundos y 256 MB.

## Entrada

N y Q, 2 ≤ N ≤ 10⁵, 1 ≤ Q ≤ 10⁵, luego el arreglo, y luego las
operaciones "1 l r" y "2 p x".

## Salida

Un par de posiciones o −1 para cada consulta de rango.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4
2 3 4 5 6
1 1 5
1 2 4
2 3 6
1 2 4
```

Salida:

```
1 3
-1
2 3
```

## Solución

Dos números no son coprimos exactamente cuando comparten un primo, y un
número hasta 10⁶ tiene a lo sumo 7 primos distintos. Para cada posición
i sea prev(i) el mayor j < i cuyo número comparte un primo con el de i,
que es la última aparición anterior de alguno de sus primos.

Un rango [l, r] tiene un par válido exactamente cuando algún i del rango
tiene prev(i) ≥ l, y entonces (prev(i), i) es un par así. Un árbol de
segmentos sobre los valores prev responde una consulta bajando al primer
i ≥ l del rango cuyo prev llega a l.

Un cambio en p modifica prev solo en p y, para cada primo que p pierde o
gana, en la siguiente aparición de ese primo después de p. Cada primo
guarda sus apariciones en una estructura ordenada (un conjunto
equilibrado en C++, un árbol de Fenwick sobre las posiciones que puede
llegar a ocupar, reunidas de antemano, en los otros lenguajes), y se
recalculan las a lo sumo 15 posiciones afectadas.

La versión en Python ahorra tiempo con los primos pequeños: los 25
primos hasta 100 se vuelven una máscara de bits que cabe en una palabra
de máquina, y un nodo del árbol guarda además si dos de sus elementos ya
comparten un primo pequeño. Como 101 · 103 · 107 > 10⁶, un número tiene
a lo sumo dos primos mayores que 100, y solo ellos usan el árbol de
prev. Sus apariciones, incluidas las que crearán los cambios, se
numeran de antemano con una sola ordenación, y las presentes se guardan
en un conjunto de bits con niveles de resumen de palabras de 30 bits,
que encuentra la aparición anterior con unas pocas operaciones de
palabra. Una consulta recorre desde la izquierda los segmentos del
árbol del rango con el OR de las máscaras ya pasadas y desciende al
primer segmento que contiene un par.

En el ejemplo 2 y 4 comparten el factor 2, el rango 3, 4, 5 no tiene
par, y tras el cambio 3 y 6 comparten 3.

Tras una criba de menores primos hasta 10⁶, cada operación cuesta unos
7 log N pasos.

## Notas por lenguaje

- Python se ejecuta con PyPy: con CPython 3.12 supera el límite de tiempo
  en el test 34 (2.046 s), mientras que con PyPy 3.10 se acepta en 1.64 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2208_number_theory_segment_tree.cpp](2208_number_theory_segment_tree.cpp) | G++ 13.2 x64 | number_theory, segment_tree | O((N + Q) 7 log N) | AC | 0.937 s | 76668 KB |
| [2208_number_theory_segment_tree.go](2208_number_theory_segment_tree.go) | Go 1.14 x64 | number_theory, segment_tree | O((N + Q) 7 log N) | AC | 0.578 s | 121460 KB |
| [2208_number_theory_segment_tree.java](2208_number_theory_segment_tree.java) | Java 1.8 | number_theory, segment_tree | O((N + Q) 7 log N) | AC | 0.906 s | 61776 KB |
| [2208_number_theory_segment_tree.py](2208_number_theory_segment_tree.py) | PyPy 3.10 x64 | number_theory, segment_tree | O((N + Q) 7 log N) | AC | 1.640 s | 48276 KB |
| [2208_number_theory_segment_tree.rs](2208_number_theory_segment_tree.rs) | Rust 1.75 x64 | number_theory, segment_tree | O((N + Q) 7 log N) | AC | 0.375 s | 61924 KB |
