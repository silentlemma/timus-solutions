# 1758. La calva, otra vez 2

[Timus 1758](https://acm.timus.ru/problem.aspx?space=1&num=1758) · dificultad 2676 · backtracking

Problema original de Ekaterina Vasilyeva, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las tabernas se numeran de 1 a n. Un recorrido empieza en la taberna 1
y solo puede pasar de una taberna a otra si uno de sus números divide
al otro, sin visitar ninguna dos veces. Hallar un recorrido por el
mayor número posible de tabernas.

## Entrada

n (2 ≤ n ≤ 50).

## Salida

El número de tabernas del recorrido más largo y luego las tabernas en
el orden del recorrido. Se acepta cualquier recorrido más largo.

## Ejemplos

### Ejemplo 1

Entrada:

```
9
```

Salida:

```
7
1 9 3 6 2 4 8
```

## Solución

Es el camino simple más largo en el grafo de divisibilidad, un problema
difícil en general, pero solo hay 49 entradas. Las soluciones guardan
una tabla de recorridos más largos, hallados de antemano con una
búsqueda exhaustiva ([1758_backtracking_table.py](1758_backtracking_table.py)),
e imprimen la entrada del mayor n' ≤ n donde la
longitud crece: un recorrido para n' sigue siéndolo para n, y entre
esos puntos la mejor longitud no cambia. La tabla tiene 26 entradas y
la respuesta es `O(1)`.

La búsqueda alarga el recorrido desde su última taberna de todas las
formas posibles y poda una rama cuando ni en el mejor caso puede batir
el récord. La cota superior cuenta las tabernas libres alcanzables desde
la última a través de tabernas libres. Entre ellas, cuenta las que tienen
a lo sumo un vecino en el conjunto de tabernas libres alcanzables más
el extremo actual del recorrido. Solo una de ellas puede visitarse,
y solo al final, así que, si hay al menos dos, resta su cantidad menos
uno. El récord empieza en cero y se actualiza al encontrar un prefijo
más largo. La búsqueda completa prueba que no hay nada más largo,
pero es demasiado lenta para el límite de un segundo, por lo que se
hace de antemano.

Para n = 9 el recorrido 1 9 3 6 2 4 8 deja fuera 5 y 7: cada uno solo
está unido a la taberna 1, que ocupa el inicio.

Trampas:

- un primo p mayor que n / 2 solo está unido a 1, así que solo puede
  ser la segunda taberna y el recorrido acabaría ahí;
- el recorrido debe empezar en la taberna 1, aunque puede terminar en
  cualquiera;
- un recorrido voraz pierde la mejor longitud ya para n pequeños.
- la cota de poda debe contar el extremo actual como vecino: en la
  prueba `gen1` (n = 4), el recorrido óptimo es 1 2 4; contar solo los
  vecinos libres daría una cota superior incorrecta de 2 al inicio.

Las longitudes coinciden con una implementación aceptada independiente
para cada n de 2 a 50, y el verificador comprueba los recorridos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1758_backtracking.cpp](1758_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.015 s | 376 KB |
| [1758_backtracking.go](1758_backtracking.go) | Go 1.14 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.031 s | 1128 KB |
| [1758_backtracking.java](1758_backtracking.java) | Java 1.8 | backtracking | O(1) with a table of 26 walks | AC | 0.140 s | 1752 KB |
| [1758_backtracking.py](1758_backtracking.py) | Python 3.12 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.078 s | 412 KB |
| [1758_backtracking.rs](1758_backtracking.rs) | Rust 1.75 x64 | backtracking | O(1) with a table of 26 walks | AC | 0.062 s | 228 KB |
