# 1063. Las fichas extra más baratas para una cadena de dominó

[Timus 1063](https://acm.timus.ru/problem.aspx?space=1&num=1063) · dificultad 2206 · dijkstra

Problema original del concurso regional ACM ICPC del noreste de Europa 2000–2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un juego de `N` fichas de dominó (`2 ≤ N ≤ 100`) tiene números del 1 al 6.
Añade fichas (quizá ninguna) con la menor suma de números de modo que todas
las fichas juntas se puedan colocar en una cadena, donde las mitades que se
tocan tienen el mismo número. Imprime la suma, el número de fichas añadidas
y las fichas; se acepta cualquier conjunto más barato.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas con los dos números de una ficha.

## Salida

La menor suma (`0` si no hace falta nada), el número de fichas añadidas y
luego las fichas.

## Evaluación

Se acepta cualquier conjunto más barato. El comprobador verifica que la
suma es la menor posible, que es la suma de las fichas listadas y que
todas las fichas juntas forman una cadena.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
6 1
1 5
5 5
5 2
2 4
4 2
```

Salida:

```
0
0
```

### Ejemplo 2

Entrada:

```
5
1 5
6 1
5 5
2 4
2 4
```

Salida:

```
6
2
1 2
1 2
```

## Solución

Los números 1…6 son vértices y las fichas aristas (una ficha doble es un
lazo). Una cadena con todas las fichas es un camino euleriano, que existe
exactamente cuando los vértices en uso están conectados y como mucho dos
tienen grado impar. Añadir la ficha `(a, b)` cuesta `a + b`, une los grupos
de `a` y `b` y cambia la paridad de ambos números.

Todo lo que importa cabe en un estado pequeño: la partición de los seis
números en grupos conectados, el conjunto de números en uso y el conjunto
de números de grado impar. Las soluciones ejecutan el algoritmo de
Dijkstra sobre estos estados desde el juego dado; los movimientos son las
15 fichas con números distintos (las dobles nunca ayudan), y el primer
estado que permite una cadena da la respuesta, reconstruyendo las fichas
añadidas por el camino. Hay como mucho `203 · 64 · 64` estados y se
alcanzan muchos menos.

La búsqueda encuentra rodeos que una regla sencilla pasaría por alto. Dos
dobles separadas `5 5` y `6 6` se unen con una ficha `5 6` (suma 11). Si las
paridades no deben cambiar, dos fichas a través del 1, `1 5` y `1 6`
(suma 13), son más baratas que la misma ficha dos veces.

Detalles a tener en cuenta:

- las dobles suman 2 al grado y no cambian la paridad;
- los números que no aparecen en ninguna ficha no hace falta conectarlos;
- el arreglo más barato puede usar un número que no está en el juego
  (normalmente el 1).

Las respuestas se comprobaron con una búsqueda exhaustiva sobre todos los
conjuntos de hasta siete fichas extra.

## Notas por lenguaje

- Todos los lenguajes empaquetan un estado en un entero (las etiquetas de
  grupo en base 6 y las dos máscaras) y guardan las distancias y el camino
  en mapas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1063_dijkstra.cpp](1063_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(S log S), S < 203·64·64 states | AC | 0.015 s | 336 KB |
| [1063_dijkstra.go](1063_dijkstra.go) | Go 1.14 x64 | dijkstra | O(S log S), S < 203·64·64 states | AC | 0.031 s | 1884 KB |
| [1063_dijkstra.java](1063_dijkstra.java) | Java 1.8 | dijkstra | O(S log S), S < 203·64·64 states | AC | 0.125 s | 6012 KB |
| [1063_dijkstra.py](1063_dijkstra.py) | Python 3.12 x64 | dijkstra | O(S log S), S < 203·64·64 states | AC | 0.093 s | 1236 KB |
| [1063_dijkstra.rs](1063_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O(S log S), S < 203·64·64 states | AC | 0.046 s | 616 KB |
