# 1910. La terna consecutiva de mayor suma

[Timus 1910](https://acm.timus.ru/problem.aspx?space=1&num=1910) · difficulty 34 · two_pointers

Problema original de Denis Dublennykh, NEERC 2012, Eastern subregional contest.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una secuencia de valores positivos, encuentra los tres consecutivos
con mayor suma. Imprime esa suma y la posición del elemento central,
numerada desde uno. Se garantiza que la terna óptima es única.
Límites: 1 segundo y 64 MB.

## Entrada

Primero n, 3≤n≤1000, seguido de n enteros aᵢ con 1≤aᵢ≤10⁶.
Los espacios y los saltos de línea son separadores equivalentes.

## Salida

La suma máxima y la posición central numerada desde uno.

## Evaluación

Dos enteros exactos, comparados por tokens.

## Ejemplos

```
6
1 4 4 4 1 1
```

```
12 3
```

## Solución

Mantén una ventana de longitud tres. Su suma inicial contiene los tres
primeros valores y su posición central es 2. Al mover el inicio desde
s−1 hasta s, con índices del arreglo desde cero, resta a[s−1] y añade
a[s+2]. Si la suma supera la mejor conocida, guarda la suma y el centro s+2.

La actualización mantiene que la suma actual pertenece exactamente a la
terna actual. Al inicio, la mejor corresponde a la primera ventana;
tras cada comparación es máxima entre todas las ventanas examinadas.
Cada inicio permitido 0,…,n−3 se visita una vez, por lo que la suma final
es óptima y la posición guardada pertenece a la única terna que la alcanza.

Con n=3 solo existe la ventana inicial y el bucle de actualización está
vacío. Hay que imprimir el centro, no el inicio ni el final. En el ejemplo
las posiciones 2,3,4 suman 12 y la posición central es 3.

Tiempo O(n), espacio O(n) para los valores de entrada y O(1) adicional.
La suma no supera 3·10⁶, así que cabe en un entero con signo de 32 bits.

## Notas por lenguaje

C++, Go 1.14, Java 8 y Rust 1.75 usan arreglos o vectores enteros.
Python 3.12 lee tokens enteros y aplica la misma actualización. No hacen
falta coma flotante ni enteros grandes. Actualiza solo con una suma
estrictamente mayor; el enunciado excluye empates del máximo.

Las respuestas coinciden con sumar directamente todas las ternas en las
14 157 secuencias de longitud 3 a 7 con valores de 1 a 4 y una única
terna óptima.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1910_two_pointers.cpp](1910_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n) | AC | 0.015 s | 432 KB |
| [1910_two_pointers.go](1910_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n) | AC | 0.015 s | 1096 KB |
| [1910_two_pointers.java](1910_two_pointers.java) | Java 1.8 | two_pointers | O(n) | AC | 0.125 s | 2376 KB |
| [1910_two_pointers.py](1910_two_pointers.py) | Python 3.12 x64 | two_pointers | O(n) | AC | 0.078 s | 496 KB |
| [1910_two_pointers.rs](1910_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n) | AC | 0.015 s | 240 KB |
