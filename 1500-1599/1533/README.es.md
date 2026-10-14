# 1533. Hobbits gordos

[Timus 1533](https://acm.timus.ru/problem.aspx?space=1&num=1533) · dificultad 978 · matching

Problema original de Alexander Ipatov, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N hobbits (2 ≤ N ≤ 100) tienen pesos distintos. Algunas parejas se
pesaron entre sí, y todos conocen todos los resultados, incluido lo que
se deduce de cadenas de ellos. Un hobbit se niega a ir si va también un
hobbit que se sabe más ligero. Hay que hallar un grupo lo más grande
posible en el que de nadie se sepa que pesa más que otro.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego una matriz N × N de ceros y unos: un 1 en la fila i, columna j
indica que los hobbits i y j se pesaron e i resultó más pesado.

## Salida

El tamaño del grupo y luego los números de sus hobbits en una línea. Se
acepta cualquier grupo máximo.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 1
0 0
```

Salida:

```
1
2
```

### Ejemplo 2

Entrada:

```
3
0 0 0
0 0 0
0 0 0
```

Salida:

```
3
1 2 3
```

## Solución

Se cierran transitivamente las pesadas (Floyd–Warshall con booleanos);
queda un orden parcial estricto, y se pide su mayor anticadena. Por el
teorema de Dilworth su tamaño es el menor número de cadenas que cubren
a todos los hobbits, es decir, N menos un emparejamiento máximo en el
grafo bipartito con una copia «pesada» y otra «ligera» de cada hobbit y
una arista i → j cuando i pesa más que j. El algoritmo de Kuhn halla el
emparejamiento.

Para listar a los hobbits se sigue la construcción de König: se parte de
las copias pesadas sin pareja y se recorren caminos alternantes
(cualquier arista hacia una copia ligera y luego su arista emparejada de
vuelta). Las copias pesadas no alcanzadas y las ligeras alcanzadas
forman una cobertura mínima de vértices; un hobbit sin ninguna copia en
ella está en la anticadena, y hay exactamente N menos el emparejamiento.
Dos de ellos no pueden ser comparables, porque la arista entre ellos
quedaría sin cubrir. `O(N³)`.

Detalles a tener en cuenta:

- hay que cerrar el orden primero: en la prueba 03 el hobbit 1 pesa más
  que el 3 solo a través del 2 (también pruebas 05, 07);
- la respuesta no son sin más los hobbits más ligeros o más pesados: en
  la prueba 04 la capa central de cuatro supera a los extremos;
- hay varios grupos máximos, así que las pruebas usan un verificador
  (todas las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1533_matching.cpp](1533_matching.cpp) | G++ 13.2 x64 | matching | O(N^3) | AC | 0.015 s | 204 KB |
| [1533_matching.go](1533_matching.go) | Go 1.14 x64 | matching | O(N^3) | AC | 0.046 s | 1244 KB |
| [1533_matching.java](1533_matching.java) | Java 1.8 | matching | O(N^3) | AC | 0.093 s | 588 KB |
| [1533_matching.py](1533_matching.py) | Python 3.12 x64 | matching | O(N^3) | AC | 0.093 s | 852 KB |
| [1533_matching.rs](1533_matching.rs) | Rust 1.75 x64 | matching | O(N^3) | AC | 0.046 s | 300 KB |
