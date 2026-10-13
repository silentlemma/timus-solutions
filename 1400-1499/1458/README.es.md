# 1458. Maniobras militares

[Timus 1458](https://acm.timus.ru/problem.aspx?space=1&num=1458) · dificultad 1223 · constructive

Problema original de Dmitry Kovalioff, Nikita Rybak e Ilya Grebnov, con agradecimiento a Sergey Sofronov por la idea, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un campo de desfile de N × N casillas (N par, 2 ≤ N ≤ 1000) tiene un
soldado en cada casilla, en una de dos posiciones, W o B. La orden
«casilla (i, j)» hace que todos los soldados de la fila i o de la
columna j, 2N − 1 en total, cambien a la otra posición. Hay que hallar
la lista de órdenes más corta tras la cual todos los soldados estén en
la misma posición, sea cual sea.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego N líneas de N letras W y B.

## Salida

El número de órdenes y luego sus casillas. Se acepta cualquier lista
más corta.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
WBWB
BWWW
WWBW
WBWB
```

Salida:

```
2
2 3
3 1
```

## Solución

Las órdenes conmutan y una orden repetida se anula, así que una
solución es un conjunto de casillas. Dar todas las órdenes de la fila a
y de la columna b cambia al soldado de (a, b) 2N − 1 veces, a cada otro
soldado de esa fila o columna N veces y a todos los demás dos veces;
con N par solo cambia (a, b). Así que cualquier soldado puede cambiarse
por separado, y para que todos queden en W hay que cambiar a los que
están en B: sumando sus cruces, la casilla (i, j) recibe orden cuando la
fila i, la columna j y la propia casilla tienen en total un número impar
de B. Como cada soldado puede cambiarse por separado, los 2^(N²)
conjuntos de casillas alcanzan las 2^(N²) disposiciones, así que no hay
dos conjuntos con el mismo efecto y este es el único para su objetivo.

Para que todos queden en B hacen falta justo las demás casillas, porque
el conjunto de todas las casillas cambia a todos. Así que se toma el
menor de los dos conjuntos: k o N² − k órdenes. `O(N²)`.

Detalles a tener en cuenta:

- si todos ya están igual, en cualquiera de las dos posiciones, no hace
  falta ninguna orden (pruebas 02, 03);
- un solo soldado distinto necesita una cruz entera de 2N − 1 órdenes
  (pruebas 07, gen2);
- hasta medio millón de órdenes deben imprimirse deprisa (gen1, gen3,
  gen4).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1458_constructive.cpp](1458_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.218 s | 5236 KB |
| [1458_constructive.go](1458_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.078 s | 15380 KB |
| [1458_constructive.java](1458_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.218 s | 25812 KB |
| [1458_constructive.py](1458_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.453 s | 42840 KB |
| [1458_constructive.rs](1458_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.062 s | 7264 KB |
