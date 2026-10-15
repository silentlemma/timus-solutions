# 1667. País Cuadrado 3

[Timus 1667](https://acm.timus.ru/problem.aspx?space=1&num=1667) · dificultad 1847 · constructive

Problema original de Ivan Burmistrov (preparado por Alexander Ipatov), del Ural SU Contest en el campus de invierno de Petrozavodsk, enero de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada una de T pruebas, llenar una tabla N × M con cuadrados de
enteros positivos distintos, cada cuadrado a lo sumo 10¹⁷, de modo que cada
fila y cada columna sume un cuadrado; imprimir `-1` si es imposible. Las
tablas de pruebas distintas se separan con una línea vacía.

## Entrada

T (1 ≤ T ≤ 20) y luego T pares N M (1 ≤ N, M ≤ 20).

## Salida

Las tablas, o `-1`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 2
3 1
2 2
```

Salida:

```
9 16

1024
25
274576

4761 8464
627264 1115136
```

Se acepta cualquier tabla válida; esta solución imprime otras.

## Solución

Se toman dos listas de enteros positivos distintos a₁ … a_N y b₁ … b_M
cuyas sumas de cuadrados son cuadrados, y se pone (aᵢ·bⱼ)² en la casilla
(i, j). La fila i suma entonces aᵢ² · Σbⱼ², un cuadrado por un cuadrado,
y lo mismo vale para las columnas. Siempre existe una tabla; el trabajo
está en hallar listas con números lo bastante pequeños y productos
distintos.

- Un número: 1. Dos números: catetos de una terna pitagórica, m² − n²
  y 2mn.
- k + 1 ≥ 3 números: para enteros positivos u₁ … u_k con S = Σuᵢ²,
  sirven 2u₁, …, 2u_k y S − 1, porque 4S + (S − 1)² = (S + 1)².
  Las u se toman como progresiones aritméticas y como tramos de primos
  consecutivos, y se descartan las listas con un número repetido.

Dos productos aᵢbⱼ y a_kb_l son iguales exactamente cuando
aᵢ / a_k = b_l / bⱼ, así que las listas no deben compartir razones menores
que 1. Cada lista guarda sus razones reducidas en un conjunto o un
arreglo ordenado; para cada prueba la solución recorre pares de listas
según sus números mayores y toma el primer par con conjuntos de razones
disjuntos y max(a) · max(b) ≤ √10¹⁷. Solo con progresiones aritméticas
algunos tamaños grandes fallan (ningún par disjunto respeta la cota),
y solo con primos los números crecen demasiado, pero juntas resuelven
los 400 tamaños, con un producto máximo de unos 1,9 · 10⁸. Los tamaños
1, 2, 3 y 4…20 tienen 1, 315, 203 y 204 candidatos, respectivamente;
K es el máximo número de candidatos y D = max(N, M).

Detalles a tener en cuenta:

- con tamaños iguales mayores que 1 no se puede usar dos veces la misma
  lista: sus razones coincidirían;
- las casillas llegan a unos 3,5 · 10¹⁶, así que hacen falta enteros de
  64 bits.

Los 400 tamaños se comprobaron con el comprobador, que revisa que los
números sean distintos, la cota y cada fila y columna.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1667_constructive.cpp](1667_constructive.cpp) | G++ 13.2 x64 | constructive | O(K^2 D^2 + K D^2 log(KD)) | AC | 0.046 s | 4092 KB |
| [1667_constructive.go](1667_constructive.go) | Go 1.14 x64 | constructive | O(K^2 D^2 + K D^2 log(KD)) | AC | 0.078 s | 7680 KB |
| [1667_constructive.java](1667_constructive.java) | Java 1.8 | constructive | O(K^2 D^2 + K D^2 log(KD)) | AC | 0.234 s | 8600 KB |
| [1667_constructive.py](1667_constructive.py) | Python 3.12 x64 | constructive | O(K^2 D^2 + K D^2 log(KD)) | AC | 0.281 s | 35156 KB |
| [1667_constructive.rs](1667_constructive.rs) | Rust 1.75 x64 | constructive | O(K^2 D^2 + K D^2 log(KD)) | AC | 0.046 s | 5028 KB |
