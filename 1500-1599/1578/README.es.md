# 1578. La caza del mamut

[Timus 1578](https://acm.timus.ru/problem.aspx?space=1&num=1578) · dificultad 877 · greedy

Problema original de Alexander Ipatov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados N + 2 puntos distintos de coordenadas enteras (N ≤ 2000), hay que
ordenarlos en una poligonal cuyos giros sean todos agudos: en cada
vértice interior los dos segmentos forman un ángulo menor que 90°, y un
ángulo de 0° (volver hacia atrás) cuenta como agudo. Se imprime `NO` si
es imposible y, si no, `YES` y el orden.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N + 2 puntos.

## Salida

`YES` y los números de los puntos en orden, o `NO`. Se acepta cualquier
orden válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
0 0
1 1
1 2
2 0
```

Salida:

```
YES
1 3 4 2
```

### Ejemplo 2

Entrada:

```
2
0 0
0 1
0 2
0 3
```

Salida:

```
YES
1 3 2 4
```

## Solución

Siempre es posible: se empieza en cualquier punto y se va siempre al
punto libre más lejano. Sea un giro en B, con A antes y C después.
Cuando el camino estaba en A, B y C seguían libres y se eligió B como el
más lejano, así que |AC| ≤ |AB|. El teorema del coseno,
|AC|² = |AB|² + |BC|² − 2·|AB|·|BC|·cos B, da entonces
cos B ≥ |BC| / (2·|AB|) > 0, así que el ángulo en B es menor que 90°.
Nunca se imprime `NO`. Cada paso busca el punto libre más lejano en tiempo lineal:
`O(N²)`, unos 2·10⁶ candidatos en total, con distancias al
cuadrado enteras y exactas.

Detalles a tener en cuenta:

- la respuesta nunca es `NO`, ni siquiera con los puntos en una recta,
  donde el camino zigzaguea adelante y atrás (el segundo ejemplo,
  prueba 12);
- el ángulo es el que forman los dos segmentos en el vértice, así que
  seguir recto son 180° y no vale, y volver atrás son 0° y sí vale;
- hay varios órdenes válidos, así que un verificador comprueba cada
  giro.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1578_greedy.cpp](1578_greedy.cpp) | G++ 13.2 x64 | greedy | O(N^2) | AC | 0.031 s | 232 KB |
| [1578_greedy.go](1578_greedy.go) | Go 1.14 x64 | greedy | O(N^2) | AC | 0.046 s | 1120 KB |
| [1578_greedy.java](1578_greedy.java) | Java 1.8 | greedy | O(N^2) | AC | 0.156 s | 620 KB |
| [1578_greedy.py](1578_greedy.py) | Python 3.12 x64 | greedy | O(N^2) | AC | 0.671 s | 1548 KB |
| [1578_greedy.rs](1578_greedy.rs) | Rust 1.75 x64 | greedy | O(N^2) | AC | 0.031 s | 288 KB |
