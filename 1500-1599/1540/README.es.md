# 1540. La batalla por el anillo

[Timus 1540](https://acm.timus.ru/problem.aspx?space=1&num=1540) · dificultad 1073 · games

Problema original de Alexander Ipatov, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay K cadenas de anillos (1 ≤ K ≤ 50, hasta 100 anillos cada una), cada
anillo con un contenido de oro de 1 a 100. Una jugada elige una cadena y
un anillo de ella y quita todos los anillos de esa cadena cuyo contenido
no supera el del elegido; la cadena puede romperse en varias. Gana quien
quita el último anillo. Gandalf juega primero: hay que escribir `S` si
gana Saruman, o `G` y la primera jugada ganadora de Gandalf, la cadena y
el anillo, con la menor cadena y luego el menor anillo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

K y luego cada cadena como su longitud seguida de los contenidos de sus
anillos.

## Salida

`S`, o `G` y los números de cadena y anillo de la primera jugada
ganadora.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
3 1 2 1
1 1
```

Salida:

```
G
1 1
```

### Ejemplo 2

Entrada:

```
2
3 2 1 2
1 1
```

Salida:

```
S
```

## Solución

Las cadenas son juegos independientes, así que por Sprague–Grundy la
posición está perdida exactamente cuando el xor de sus valores de Grundy
es 0.

¿Qué trozos pueden aparecer? Quitar los anillos hasta x deja los tramos
máximos de anillos por encima de x. Una jugada posterior dentro de ese
tramo quita los anillos hasta algún y > x y deja los tramos máximos por
encima de y, que también son máximos en toda la cadena. Así, cada trozo
es un tramo máximo por encima de algún contenido; estos tramos se
anidan y forman un árbol cuya raíz es la cadena y donde los hijos de un
tramo son los tramos por encima de su menor contenido.

En un tramo, una jugada con contenido x deja un frente del árbol: los
descendientes cuyo menor contenido supera x mientras el de su padre no.
Recorriendo x en orden creciente con un montículo ordenado por el menor
contenido, cada nodo se sustituye por sus hijos una sola vez, así que
los valores xor de todas las jugadas de un tramo cuestan un tiempo
lineal en su subárbol (por un logaritmo). El valor de Grundy es el mex
de esos valores, calculado desde las hojas; con a lo sumo 2·100 tramos
por cadena esto es rápido.

Si el xor total T no es 0, las jugadas ganadoras en la cadena i son las
que la dejan con xor T ⊕ g(i); recorriendo cadenas y anillos en orden
con la tabla de valores de jugadas de la raíz se obtiene la menor
jugada pedida. Varios anillos pueden compartir el contenido ganador; se
da el primero. `O(K·L² log L)` para cadenas de longitud L.

Detalles a tener en cuenta:

- los anillos iguales se van en una sola jugada, y la respuesta da el
  primero de ellos (pruebas 05, 08);
- la primera jugada ganadora puede estar en una cadena posterior
  (prueba 07);
- una cadena puede partirse en trozos iguales cuyos valores se anulan
  (prueba 06).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1540_games.cpp](1540_games.cpp) | G++ 13.2 x64 | games | O(K * L^2 * log L) | AC | 0.031 s | 580 KB |
| [1540_games.go](1540_games.go) | Go 1.14 x64 | games | O(K * L^2 * log L) | AC | 0.015 s | 6244 KB |
| [1540_games.java](1540_games.java) | Java 1.8 | games | O(K * L^2 * log L) | AC | 0.187 s | 6460 KB |
| [1540_games.py](1540_games.py) | Python 3.12 x64 | games | O(K * L^2 * log L) | AC | 0.203 s | 1180 KB |
| [1540_games.rs](1540_games.rs) | Rust 1.75 x64 | games | O(K * L^2 * log L) | AC | 0.031 s | 816 KB |
