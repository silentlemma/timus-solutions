# 1227. Una ruta de rally de longitud dada por carreteras de un solo sentido

[Timus 1227](https://acm.timus.ru/problem.aspx?space=1&num=1227) · dificultad 301 · graphs

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `M ≤ 100` ciudades y `N ≤ 10⁴` carreteras de doble sentido de
longitudes dadas. Por seguridad, cada carretera de la ruta del rally se
recorre en un solo sentido, y la ruta puede empezar y acabar en cualquier
punto de una carretera. Hay que decidir si existe una ruta de longitud
exactamente `S ≤ 2·10⁶`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`M`, `N` y `S`, y luego cada carretera como dos ciudades y una longitud.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2 20
1 2 10
2 3 5
```

Salida:

```
NO
```

### Ejemplo 2

Entrada:

```
3 3 1000
1 2 1
2 3 1
1 3 1
```

Salida:

```
YES
```

## Solución

Si las carreteras contienen un ciclo, la ruta puede darle vueltas una y
otra vez en el mismo sentido, así que cualquier longitud es posible. Un
bucle de una ciudad a sí misma, o una segunda carretera entre las mismas
dos ciudades, también es un ciclo. Una estructura de conjuntos disjuntos
detecta la primera carretera cuyos extremos ya están conectados.

Si no, las carreteras forman un bosque. Recorrer cada carretera en un
solo sentido significa que la ruta nunca puede dar la vuelta, así que
sigue un camino simple, y como puede empezar y parar a mitad de una
carretera, se alcanza cualquier longitud hasta la del camino más largo.
El camino más largo de un árbol es su diámetro: desde cualquier ciudad se
va a la más lejana, y desde allí otra vez a la más lejana. La respuesta
es `YES` exactamente cuando el diámetro de algún árbol es al menos `S`.
`O(N α(M) + M)`.

Detalles a tener en cuenta:

- una carretera de una ciudad a sí misma cuenta como ciclo;
- dos carreteras entre el mismo par de ciudades también permiten dar
  vueltas sin fin;
- el bosque puede tener varios árboles, y cada uno necesita su propio
  diámetro;
- una ruta exactamente tan larga como el diámetro está permitida.

Las respuestas se compararon con una solución escrita aparte en 200
mapas aleatorios con y sin ciclos, con `S` cerca del diámetro.

## Notas por lenguaje

- Todos los lenguajes usan conjuntos disjuntos con compresión de caminos
  a la mitad y una pila explícita para las distancias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1227_graphs.cpp](1227_graphs.cpp) | G++ 13.2 x64 | graphs | O(N α(M) + M) | AC | 0.015 s | 204 KB |
| [1227_graphs.go](1227_graphs.go) | Go 1.14 x64 | graphs | O(N α(M) + M) | AC | 0.031 s | 1268 KB |
| [1227_graphs.java](1227_graphs.java) | Java 1.8 | graphs | O(N α(M) + M) | AC | 0.093 s | 800 KB |
| [1227_graphs.py](1227_graphs.py) | Python 3.12 x64 | graphs | O(N α(M) + M) | AC | 0.078 s | 2608 KB |
| [1227_graphs.rs](1227_graphs.rs) | Rust 1.75 x64 | graphs | O(N α(M) + M) | AC | 0.015 s | 464 KB |
