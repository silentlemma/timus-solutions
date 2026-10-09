# 1077. El mayor número de recorridos que tienen cada uno una carretera propia

[Timus 1077](https://acm.timus.ru/problem.aspx?space=1&num=1077) · dificultad 395 · bfs, graphs

Problema original de Nguyen Xuan My (adaptado por Dinh Quang Hiep y Tran Nam Trung), del tercer concurso del Departamento de Matemáticas e Informática de la Facultad de Ciencias Naturales de la Universidad Nacional de Vietnam, Hanói.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` ciudades (`1 ≤ N ≤ 200`) están unidas por `M` carreteras de doble
sentido, como mucho una entre dos ciudades. Un recorrido visita en ciclo
`K > 2` ciudades distintas. Organiza tantos recorridos como sea posible
de modo que cada uno tenga una carretera que ningún otro recorrido use.
Imprime su número `T` y los recorridos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `M`, y luego `M` líneas con las dos ciudades de una carretera.

## Salida

`T` y luego `T` líneas, cada una con `K` y las `K` ciudades de un
recorrido en orden.

## Evaluación

Se acepta cualquier conjunto válido de recorridos. El comprobador
verifica que `T` es el mayor posible, que cada recorrido es un ciclo de
más de dos ciudades distintas unidas por carreteras y que cada recorrido
tiene una carretera que no usa ningún otro.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 7
1 2
1 3
1 4
2 4
2 3
3 4
5 4
```

Salida:

```
3
3 2 1 4
3 2 1 3
3 3 1 4
```

## Solución

Los recorridos se ven como vectores sobre `GF(2)` con una coordenada por
carretera. Un recorrido dueño de una carretera es el único con un 1 en
esa coordenada, así que ninguna combinación de los demás lo produce: los
recorridos son linealmente independientes. Los ciclos viven en el
espacio de ciclos del grafo, de dimensión `M − N + C` para `C` componentes
conexas, así que `T ≤ M − N + C`.

Esa cota la alcanzan los ciclos fundamentales de un bosque generador.
Cada carretera fuera del bosque, junto con el camino del bosque entre sus
extremos, forma un ciclo, y esa carretera no pertenece a ningún otro
ciclo así. Hay exactamente `M − (N − C)` carreteras de este tipo. Un
bosque de búsqueda en anchura mantiene cortos los caminos. Para escribir
un ciclo se sube el extremo más profundo hasta la profundidad del otro y
luego se suben ambos hasta que se encuentran.
`O(N + M + tamaño de la salida)`.

Detalles a tener en cuenta:

- el grafo puede ser no conexo o tener ciudades aisladas, así que el
  bosque crece desde cada ciudad aún no alcanzada;
- un árbol o un grafo sin carreteras dan `T = 0` y ninguna línea más;
- con las 19 900 carreteras entre 200 ciudades hay 19 701 recorridos, así
  que la salida se arma en un solo búfer.

El comprobador calcula `M − N + C` con conjuntos disjuntos y comprueba
cada recorrido de forma independiente de las soluciones.

## Notas por lenguaje

- Python lee todos los números de una vez y los empareja con cortes:
  `zip(rest[0::2], rest[1::2])` da las carreteras.
- Java lee con `StreamTokenizer` y reúne la salida en un
  `StringBuilder`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1077_bfs.cpp](1077_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + M + output) | AC | 0.015 s | 304 KB |
| [1077_bfs.go](1077_bfs.go) | Go 1.14 x64 | bfs | O(N + M + output) | AC | 0.015 s | 2400 KB |
| [1077_bfs.java](1077_bfs.java) | Java 1.8 | bfs | O(N + M + output) | AC | 0.140 s | 2716 KB |
| [1077_bfs.py](1077_bfs.py) | Python 3.12 x64 | bfs | O(N + M + output) | AC | 0.109 s | 2524 KB |
| [1077_bfs.rs](1077_bfs.rs) | Rust 1.75 x64 | bfs | O(N + M + output) | AC | 0.031 s | 804 KB |
