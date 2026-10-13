# 1391. Serpiente

[Timus 1391](https://acm.timus.ru/problem.aspx?space=1&num=1391) · dificultad 5173 · graphs

Problema original de Dmitry Ivankov, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un laberinto de H × W casillas, H ≤ 300 y W ≤ 30, tiene muros 'X' y
casillas libres '.', y una única entrada en el borde. Una serpiente de
longitud L es una cadena de L casillas distintas y vecinas. En cada
unidad de tiempo avanza una casilla hacia delante, a la izquierda o a la
derecha, y el cuerpo sigue a la cabeza; muere si no puede moverse sin
chocar con un muro o consigo misma. En el instante 0 la cabeza está en
la entrada y el resto del cuerpo fuera. Para cada L de 2 a 17 hay que
hallar el primer instante en que la cabeza vuelve a la entrada, o -1.
Ninguna serpiente de longitud 18 sale con vida.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

H y W, la casilla de entrada y luego H filas de W caracteres.

## Salida

16 líneas: el mejor tiempo para las longitudes de 2 a 17, o -1.

## Ejemplos

### Ejemplo 1

Entrada:

```
9 9
1 5
XXXX.XXXX
XXX...XXX
XX..X..XX
....XX..X
X.X.X.X.X
..XX.....
X...XXX..
XXXXX....
X.....XXX
```

Salida:

```
10
10
10
22
22
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
```

## Solución

La serpiente no puede dar media vuelta, así que para salir tiene que
recorrer un ciclo del laberinto. La mejor salida es un lazo: un camino
más corto desde la entrada hasta una casilla J más cercana de un ciclo
simple alcanzable de c casillas, una vuelta al ciclo y el mismo camino
de regreso, en 2·dist(J) + c unidades. La cabeza vuelve a J tras c
movimientos; puede entrar en la casilla que deja la cola, así que la
vuelta funciona justo cuando c ≥ L, y el camino de regreso está libre
detrás del cuerpo. Un ciclo alcanzable de c ≥ 18 casillas dejaría
salir a una serpiente de longitud 18, así que solo cuentan ciclos de
4 a 16 casillas; en una cuadrícula todo ciclo tiene un número par de
casillas.

Para cada c par hace falta la menor distancia de una casilla del
ciclo, sobre todos los ciclos alcanzables de c casillas. Se ordenan
las casillas alcanzables por su distancia en anchura desde la entrada
y se buscan ciclos desde cada casilla por turno, usando solo casillas
posteriores en ese orden, de modo que cada ciclo se encuentra desde su
casilla más cercana. La búsqueda es un recorrido en profundidad de a
lo sumo 16 pasos que se corta cuando la distancia de Manhattan de
vuelta al inicio es demasiado larga. Una longitud queda fijada en la
primera casilla que la cierra, y la búsqueda termina cuando las siete
longitudes están fijadas. La respuesta para L es el mínimo de
2·best(c) + c sobre c ≥ L.

Detalles a tener en cuenta:

- el ciclo necesita al menos L casillas, no L + 1: la cabeza puede
  entrar en la casilla que la cola está dejando (prueba 03);
- los ciclos de la cuadrícula tienen un número par de casillas, así que
  una serpiente de longitud 17 nunca sale (prueba 05);
- según el foro, una prueba del juez tiene un ciclo de más de 17
  casillas, en contra de la promesa, y sus respuestas no lo tienen en
  cuenta; las soluciones cuentan ciclos de a lo sumo 16 casillas, lo que
  además mantiene corta la búsqueda (la prueba 06 es un laberinto así).

Las respuestas se compararon con una búsqueda en anchura sobre
posiciones completas de la serpiente, para todas las longitudes, en 300
laberintos aleatorios de a lo sumo 16 casillas y en todas las demás
pruebas salvo la 06.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1391_graphs.cpp](1391_graphs.cpp) | G++ 13.2 x64 | graphs | O(H·W·3^16) | AC | 0.046 s | 584 KB |
| [1391_graphs.go](1391_graphs.go) | Go 1.14 x64 | graphs | O(H·W·3^16) | AC | 0.078 s | 2148 KB |
| [1391_graphs.java](1391_graphs.java) | Java 1.8 | graphs | O(H·W·3^16) | AC | 0.140 s | 1320 KB |
| [1391_graphs.py](1391_graphs.py) | Python 3.12 x64 | graphs | O(H·W·3^16) | AC | 1.656 s | 2664 KB |
| [1391_graphs.rs](1391_graphs.rs) | Rust 1.75 x64 | graphs | O(H·W·3^16) | AC | 0.046 s | 1036 KB |
