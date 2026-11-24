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

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

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

`1185_geometry_optimized.java`. Conserva la envolvente por cadena monótona y su perímetro más 2πL, redondeando solo al final. Empaqueta cada punto en long: x con signo en los32 bits altos, y con el bit de signo invertido para mantener su orden en la mitad baja. La ordenación primitiva da el mismo orden lexicográfico. La envolvente usa índices int, sin objetos ni listas temporales. Productos cruzados exactos en long; solo longitudes usan hypot. Espacio O(N). Si S(N) es ordenar, el recorrido añade O(N); Java8 suele costar O(N log N), permitiendo conservadoramente un peor caso cuadrático.

Frente a `1185_geometry.java`: tiempo 0.140 s → 0.109 s; memoria 3144 KB → 556 KB.

La versión Go suma 10 000 a ambas coordenadas y empaqueta cada punto en un entero de 32 bits, con x en los bits altos. Al ordenar esos enteros se obtiene el orden lexicográfico. Se recorre en ambos sentidos y se reutiliza una pila para las dos cadenas monótonas. Al perímetro se le sigue sumando 2πL.

Las implementaciones base aceptadas [1185_geometry.cpp](1185_geometry.cpp), [1185_geometry.java](1185_geometry.java), [1185_geometry.py](1185_geometry.py), [1185_geometry.rs](1185_geometry.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1185_geometry_parsing_optimized.go`. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios.

Accepted #11328893 (Go 1.14 x64): **0.015 s / 1072 KB**. Comparación archivada: `1185_geometry.go` (Go 1.14 x64) — 0.031 s / 1204 KB (#11283369).

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1185_geometry_implementation_parsing_optimized.rs`. Se usan lecturas nativas acotadas y escrituras nativas completas, descriptores binarios de Windows y entrada C. Los números se convierten directamente desde bytes a enteros con signo sin reservar tokens; las entradas sensibles a líneas conservan líneas completas. Los puntos se ordenan en su lugar sin estabilidad; los puntos iguales son intercambiables en la misma envolvente convexa.

Accepted #11329170 (Rust 1.75 x64): **0.015 s / 124 KB**. Comparación archivada: `1185_geometry.rs` (Rust 1.75 x64) — 0.031 s / 264 KB (#11283379).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1185_geometry_optimized.java`: puesto de tiempo 5/27 y de memoria 1/27 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1185_geometry.cpp](1185_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 236 KB | 11283368 |
| [1185_geometry.go](1185_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1204 KB | 11283369 |
| [1185_geometry.java](1185_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.140 s | 3144 KB | 11283377 |
| [1185_geometry.py](1185_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 752 KB | 11283372 |
| [1185_geometry.rs](1185_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 264 KB | 11283379 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1185_geometry_optimized.go](1185_geometry_optimized.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 824 KB | 11310857 |
| [1185_geometry_optimized.java](1185_geometry_optimized.java) | Java 1.8 | geometry | O(N+S(N)) | AC | 0.109 s | 556 KB | 11325011 |
| [1185_geometry_parsing_optimized.go](1185_geometry_parsing_optimized.go) | Go 1.14 x64 | geometry, parsing | O(N log N) | AC | 0.015 s | 1072 KB | 11328893 |
| [1185_geometry_implementation_parsing_optimized.rs](1185_geometry_implementation_parsing_optimized.rs) | Rust 1.75 x64 | geometry, implementation, parsing | O(N log N) | AC | 0.015 s | 124 KB | 11329170 |
