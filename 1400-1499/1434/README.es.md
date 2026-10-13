# 1434. Los autobuses de Vasyuki

[Timus 1434](https://acm.timus.ru/problem.aspx?space=1&num=1434) · dificultad 885 · bfs

Problema original de Evgeny Krokhalev y Ekaterina Vasilyeva, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad tiene N líneas de autobús (N ≤ 1000) sobre M paradas
(M ≤ 10⁵), con como mucho 200 000 números en todas las listas. Un viaje
cuesta un rublo sea cual sea el número de paradas, y un autobús lleva
entre dos paradas cualesquiera de su línea. Hay que hallar la forma más
barata de ir de la parada A a la B: imprimir el coste y las paradas
donde se sube, se cambia y se baja, o −1 si no se puede llegar a B.

Límite de tiempo: 1.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y M, luego las N líneas como cantidad y paradas, luego A y B.

## Salida

−1, o el coste y la lista de paradas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 10
5 2 4 6 8 10
3 3 6 9
2 5 10
5 9
```

Salida:

```
3
5 10 6 9
```

## Solución

Búsqueda en anchura sobre las paradas, donde un paso es un viaje
entero: desde una parada se toma cada línea que pasa por ella y aún no
se ha tomado, y se marcan todas sus paradas un viaje más allá. Cada
línea se abre una sola vez, la primera vez que se alcanza alguna de sus
paradas, así que el trabajo es la longitud total de las líneas. Cada
parada recuerda la línea que la alcanzó y cada línea la parada donde se
tomó por primera vez, lo que da los cambios hacia atrás desde B.
`O(N + M + S)` con S números en las líneas.

Detalles a tener en cuenta:

- los autobuses van en ambos sentidos: en el ejemplo la línea 1 se
  recorre de 10 hacia atrás hasta 6 (prueba 01);
- la respuesta es −1 cuando B no está en ninguna línea alcanzable desde
  A (pruebas 02, 04, gen3);
- cada línea debe abrirse una sola vez, o las líneas largas con muchas
  paradas se recorren una y otra vez (gen4).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1434_bfs.cpp](1434_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + M + S) | AC | 0.140 s | 6252 KB |
| [1434_bfs.go](1434_bfs.go) | Go 1.14 x64 | bfs | O(N + M + S) | AC | 0.062 s | 15812 KB |
| [1434_bfs.java](1434_bfs.java) | Java 1.8 | bfs | O(N + M + S) | AC | 0.171 s | 16480 KB |
| [1434_bfs.py](1434_bfs.py) | Python 3.12 x64 | bfs | O(N + M + S) | AC | 0.171 s | 31732 KB |
| [1434_bfs.rs](1434_bfs.rs) | Rust 1.75 x64 | bfs | O(N + M + S) | AC | 0.046 s | 14188 KB |
