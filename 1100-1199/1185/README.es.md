# 1185. La muralla más corta a una distancia dada de un castillo poligonal

[Timus 1185](https://acm.timus.ru/problem.aspx?space=1&num=1185) · dificultad 301 · geometry

Problema original de Sergey Volchenkov y Roman Elizarov, del concurso regional ACM ICPC del noreste de Europa 2001–2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un castillo es un polígono simple con `3 ≤ N ≤ 1000` vértices enteros
dados en sentido horario. Hay que hallar la longitud de la muralla cerrada
más corta a su alrededor que nunca se acerque al castillo a menos de `L`
pies, redondeada a pies enteros.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `L`, y luego los vértices.

## Salida

La longitud en pies, con un error de a lo sumo 8 pulgadas.

## Ejemplos

### Ejemplo 1

Entrada:

```
9 100
200 400
300 400
300 300
400 300
400 400
500 400
500 200
350 200
200 200
```

Salida:

```
1628
```

## Solución

La muralla debe rodear el castillo, así que también rodea su envolvente
convexa, y la mejor muralla es el conjunto de puntos a distancia
exactamente `L` de la envolvente. A lo largo de cada lado de la envolvente
corre en paralelo a distancia `L`, sumando la longitud del lado. En cada
vértice de la envolvente gira por un arco de radio `L` el ángulo exterior
de ese vértice, y los ángulos exteriores de un polígono convexo suman una
vuelta completa. Así que la longitud es el perímetro de la envolvente más
`2πL`.

La envolvente sale de la cadena monótona de Andrew: se ordenan los
puntos, se construyen la cadena inferior y la superior y se descartan los
puntos que no giran a la izquierda, incluidos los colineales. Redondear
al pie más cercano deja un error de a lo sumo 6 pulgadas. `O(N log N)`.

Detalles a tener en cuenta:

- el castillo no tiene por qué ser convexo, así que su propio perímetro es
  demasiado largo; las entrantes quedan cubiertas por lados de la
  envolvente, como en el ejemplo;
- los vértices en medio de un lado recto no deben romper la envolvente,
  por eso se descartan los puntos colineales;
- la respuesta se redondea, no se trunca.

Las respuestas se compararon con una solución escrita aparte en 200
castillos aleatorios y en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes construyen la envolvente igual sobre coordenadas
  enteras de 64 bits y suman las longitudes de los lados en coma
  flotante.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1185_geometry.cpp](1185_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 236 KB |
| [1185_geometry.go](1185_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1204 KB |
| [1185_geometry.java](1185_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 3144 KB |
| [1185_geometry.py](1185_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 752 KB |
| [1185_geometry.rs](1185_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 264 KB |
