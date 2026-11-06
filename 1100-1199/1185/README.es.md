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

La muralla más corta es convexa y rodea la envolvente convexa del
castillo; es el conjunto de puntos a distancia exactamente `L` de la
envolvente. A lo largo de cada lado de la envolvente
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

## Soluciones optimizadas

La versión Go suma 10 000 a ambas coordenadas y empaqueta cada punto en un entero de 32 bits, con x en los bits altos. Al ordenar esos enteros se obtiene el orden lexicográfico. Se recorre en ambos sentidos y se reutiliza una pila para las dos cadenas monótonas. Al perímetro se le sigue sumando 2πL.

Las implementaciones base aceptadas [1185_geometry.cpp](1185_geometry.cpp), [1185_geometry.java](1185_geometry.java), [1185_geometry.py](1185_geometry.py), [1185_geometry.rs](1185_geometry.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes construyen la envolvente igual sobre coordenadas
  enteras (de precisión arbitraria en Python, de 64 bits en los demás)
  y suman las longitudes de los lados en coma flotante.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1185_geometry.cpp](1185_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 236 KB | 11283368 |
| [1185_geometry.go](1185_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1204 KB | 11283369 |
| [1185_geometry.java](1185_geometry.java) \* | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 3144 KB | 11283377 |
| [1185_geometry.py](1185_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 752 KB | 11283372 |
| [1185_geometry.rs](1185_geometry.rs) \* | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 264 KB | 11283379 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1185_geometry_optimized.go](1185_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 824 KB | 11310857 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
