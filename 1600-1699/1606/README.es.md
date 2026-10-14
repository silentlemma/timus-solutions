# 1606. Eslalon

[Timus 1606](https://acm.timus.ru/problem.aspx?space=1&num=1606) · dificultad 714 · greedy

Problema original de Alexander Toropov, preparado por Alexander Ipatov, del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En una pendiente hay hasta 50000 banderines, todos con x distintas e y
distintas. Petya esquía desde la línea de salida y = 100000 hasta la de
meta y = 0 por una línea quebrada con vértices en banderines, siempre
hacia abajo, y debe cambiar de dirección izquierda/derecha en cada
banderín que toca; también se puede pasar por un banderín en línea
recta sin tocarlo. Hay que tocar tantos banderines como sea posible e
imprimirlos en orden. Vale cualquier lista óptima.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y luego las coordenadas de los banderines.

## Salida

El número de banderines y luego sus números en el orden en que se tocan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
5 2
6 5
1 1
4 3
2 4
```

Salida:

```
4
2 5 4 3
```

### Ejemplo 2

Entrada:

```
4
1 6
3 4
5 2
4 1
```

Salida:

```
3
1 3 4
```

## Solución

El esquiador siempre baja, así que los banderines tocados van por y
decreciente. En ese orden, sus coordenadas x deben ir en zigzag: cada
paso va hacia el lado contrario al del paso anterior. A las líneas de
salida y meta se puede llegar en cualquier punto, así que el primer y el
último paso no imponen nada. El problema es la subsecuencia en zigzag
más larga de las coordenadas x.

Se divide la secuencia ordenada en tramos máximos en los que x solo
crece o solo decrece. Tomar el primer banderín, el banderín donde gira
cada tramo y el último da un zigzag con un banderín más que tramos, y
ningún zigzag puede ser más largo, porque cada uno de sus pasos necesita
un tramo propio. Tras ordenar es una sola pasada: `O(n log n)`.

Las pruebas usan un verificador que acepta cualquier lista de la
longitud correcta que baje y gire en cada banderín. La longitud se
contrastó con una búsqueda exhaustiva sobre todos los subconjuntos de
hasta 8 banderines.

Detalles a tener en cuenta:

- la respuesta no es única: en el primer ejemplo el tercer banderín
  puede ser el de x = 4 o el de x = 5, y la salida puede diferir del
  ejemplo;
- un solo banderín es un descenso válido con un toque (prueba 03);
- si x solo crece pendiente abajo, solo se pueden tocar el primer y el
  último banderín (prueba 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1606_greedy.cpp](1606_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.062 s | 1388 KB |
| [1606_greedy.go](1606_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.078 s | 7300 KB |
| [1606_greedy.java](1606_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.171 s | 7232 KB |
| [1606_greedy.py](1606_greedy.py) | Python 3.12 x64 | greedy | O(n log n) | AC | 0.187 s | 18416 KB |
| [1606_greedy.rs](1606_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.031 s | 6028 KB |
