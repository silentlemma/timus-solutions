# 1781. Código limpio

[Timus 1781](https://acm.timus.ru/problem.aspx?space=1&num=1781) · dificultad 2067 · graphs

Problema original de Alex Samsonov, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tabla de n × n de ceros y unos dice qué aulas usa cada uno de n
concursos, celebrados en orden. El aula i se limpia justo después del
concurso i y ya no puede usarse, así que el concurso i no puede usar un
aula j con j < i. Una operación intercambia las filas i y j y luego las
columnas i y j. Con a lo sumo 200 operaciones, lograr una tabla válida o
informar de que es imposible.

## Entrada

n (2 ≤ n ≤ 100) y luego la tabla.

## Salida

El número de operaciones y los pares i, j, o −1. Se acepta cualquier
respuesta válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 0 0
1 1 0
1 1 0
```

Salida:

```
1
1 3
```

### Ejemplo 2

Entrada:

```
3
1 1 1
1 1 0
1 0 0
```

Salida:

```
-1
```

## Solución

Intercambiar filas y columnas a la vez solo renumera concursos y aulas
por igual, y se puede llegar a cualquier renumeración. La tabla es
válida cuando todo 1 fuera de la diagonal queda por encima de ella, es
decir, un concurso a que usa el aula b ≠ a va antes que el concurso b.
Estas son las aristas a → b de un grafo, y una numeración válida es un
orden topológico suyo; si el grafo tiene un ciclo, nada sirve y la
respuesta es −1.

El orden se alcanza colocando sus concursos en los lugares 1, 2, … uno
a uno, cada uno con a lo sumo un intercambio del concurso que ocupa ese
lugar con el buscado, así que se usan a lo sumo n − 1 ≤ 99 operaciones.
`O(n²)`.

En el primer ejemplo los concursos 2 y 3 usan el aula 1, así que el
concurso 1 debe ir después de ambos; intercambiar 1 y 3 lo pone el
último.

Trampas:

- un concurso puede usar su propia aula, y esos 1 de la diagonal no
  imponen orden;
- cada operación intercambia filas y columnas por igual, así que es una
  renumeración, no un movimiento libre de filas;
- la respuesta no es única, así que el verificador reproduce los
  intercambios.

La existencia de respuesta coincide con una búsqueda sobre todas las
renumeraciones en 300 tablas aleatorias de hasta 5 aulas, y los
intercambios pasan el verificador en 100 tablas aleatorias de hasta 100
aulas, igual que los de una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1781_graphs.cpp](1781_graphs.cpp) | G++ 13.2 x64 | graphs | O(n^2) | AC | 0.015 s | 256 KB |
| [1781_graphs.go](1781_graphs.go) | Go 1.14 x64 | graphs | O(n^2) | AC | 0.031 s | 1204 KB |
| [1781_graphs.java](1781_graphs.java) | Java 1.8 | graphs | O(n^2) | AC | 0.171 s | 5700 KB |
| [1781_graphs.py](1781_graphs.py) | Python 3.12 x64 | graphs | O(n^2) | AC | 0.078 s | 968 KB |
| [1781_graphs.rs](1781_graphs.rs) | Rust 1.75 x64 | graphs | O(n^2) | AC | 0.015 s | 304 KB |
