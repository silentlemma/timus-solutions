# 1246. En qué sentido se recorre un polígono

[Timus 1246](https://acm.timus.ru/problem.aspx?space=1&num=1246) · dificultad 333 · geometry

Problema original de Evgeny Kobzev, del Concurso Individual de la Universidad Estatal de los Urales, 1 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un perro está atado a un poste dentro de una parcela vallada, un polígono
simple de N vértices (3 ≤ N ≤ 200 000, coordenadas enteras de valor
absoluto hasta 50 000). Un corredor da vueltas y vueltas junto a la
valla, pasando por los vértices en el orden dado, y el perro persigue al
corredor por dentro. ¿Hacia dónde se enrolla la cuerda en el poste: en el sentido
de las agujas del reloj (`cw`) o en el contrario (`ccw`)?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N vértices en el orden del corredor.

## Salida

`cw` o `ccw`.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
0 1
1 1
1 0
```

Salida:

```
cw
```

## Solución

El perro sigue al corredor por el interior de la parcela, así que la
cuerda se enrolla en el sentido en que el corredor recorre el polígono.
Ese es el signo del doble del área con signo del polígono por la fórmula del
zapatero, `Σ (x_i·y_{i+1} − x_{i+1}·y_i)`: positivo en sentido contrario a
las agujas del reloj y negativo en el de las agujas. El polígono es
simple y no degenerado, así que la suma nunca es cero. `O(N)`.

Detalles a tener en cuenta:

- el polígono no tiene por qué ser convexo, así que el giro en un vértice
  no dice nada; solo decide el área total (pruebas 04 y 05);
- cada término llega a 5·10⁹, más de 32 bits, así que se usan enteros
  de 64 bits o de precisión arbitraria.

## Soluciones optimizadas

C++ y Rust acumulan el doble del área con signo al leer los vértices. Guardan el primer punto y el anterior, añaden una vez el producto cruzado de cada arista y cierran el polígono. Los productos y la suma usan enteros con signo de 64 bits. El búfer de entrada y el estado geométrico ocupan espacio constante.

Las implementaciones base aceptadas [1246_geometry.go](1246_geometry.go), [1246_geometry.java](1246_geometry.java), [1246_geometry.py](1246_geometry.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

`1246_geometry_optimized.py`. Conserva la orientación por la fórmula del cordón, sumando cada arista al llegar el siguiente vértice y cerrando del último al primero. Solo retiene primer vértice, anterior y doble área exacta con signo: positiva da ccw, en otro caso cw como la base. El lector de 65536 bytes arrastra tokens partidos y elimina la lista de enteros, secciones de coordenadas y copias rotadas. Para B bytes y N vértices, tiempo O(B+N); espacio de bloques acotados y estado aritmético constante bajo los límites. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1246_geometry.py`: tiempo 0.218 s → 0.187 s; memoria 41236 KB → 10 140 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1246_geometry_optimized.py`: puesto de tiempo 2/22 y de memoria 7/22 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1246_geometry.cpp](1246_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.265 s | 128 KB | 11283934 |
| [1246_geometry.go](1246_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.062 s | 4120 KB | 11283936 |
| [1246_geometry.java](1246_geometry.java) \* | Java 1.8 | geometry | O(N) | AC | 0.156 s | 3584 KB | 11283939 |
| [1246_geometry.py](1246_geometry.py) \* | Python 3.12 x64 | geometry | O(N) | AC | 0.218 s | 41236 KB | 11283937 |
| [1246_geometry.rs](1246_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.062 s | 10468 KB | 11283943 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1246_geometry_optimized.cpp](1246_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 76 KB | 11310921 |
| [1246_geometry_optimized.rs](1246_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 196 KB | 11310553 |
| [1246_geometry_optimized.py](1246_geometry_optimized.py) \* | PyPy 3.10 x64 | geometry | O(B+N) | AC | 0.187 s | 10140 KB | 11325066 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
