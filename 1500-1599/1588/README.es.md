# 1588. Jamaica

[Timus 1588](https://acm.timus.ru/problem.aspx?space=1&num=1588) · dificultad 327 · geometry

Problema original de Andrey Demidov, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n ciudades distintas (1 ≤ n ≤ 300) en puntos enteros con
coordenadas de 0 a 10000. Cada dos ciudades se unen por una carretera
recta, y una carretera sirve a todas las ciudades de su recta. Hay que
hallar la longitud total de las carreteras, redondeada a un número
entero de millas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y luego las coordenadas de cada ciudad.

## Salida

La longitud total, redondeada.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
0 100
100 0
50 50
```

Salida:

```
412
```

## Solución

Cada recta con dos o más ciudades lleva una carretera, de su primera
ciudad a la última. Desde la ciudad i, cada otra ciudad está en alguna
dirección reducida (dx/g, dy/g), con g = mcd(dx, dy), a g pasos. La
ciudad i es un extremo de la carretera en una dirección exactamente
cuando no hay ninguna ciudad en la dirección opuesta, y entonces la
carretera mide g·|(dx/g, dy/g)| para la ciudad más lejana en esa
dirección. Al sumar sobre todas las ciudades cada carretera aparece dos
veces, una desde cada extremo, así que la suma se divide entre dos. Con
las direcciones en una tabla hash el trabajo esperado es `O(n²)`; C++
usa un mapa ordenado y Java ordena, lo que da `O(n² log n)`.

Los resultados se contrastaron con agrupar explícitamente las ciudades
de la recta de cada par.

Detalles a tener en cuenta:

- una recta con tres o más ciudades es una sola carretera, no una por
  par: en el ejemplo la diagonal por (50, 50) cuenta una vez;
- las direcciones deben reducirse por el mcd, o ciudades de una misma
  recta a distinto número de pasos parecen carreteras distintas;
- la suma se divide entre dos antes de redondear.
- las ciudades en varias rectas que pasan por un punto también crean
  carreteras entre esas rectas; hay que contarlas (prueba generada `gen3`).

## Soluciones optimizadas

Se ordenan las ciudades lexicográficamente y cada carretera se cuenta solo desde su primera ciudad. Desde una ciudad, ambos sentidos de una dirección reducida comparten clave. Si el grupo contiene una ciudad anterior, se omite. En caso contrario la ciudad más lejana determina la longitud. Go reutiliza una tabla hash y Rust un vector que ordena. Ambas versiones usan suma compensada antes de redondear el total.

Las implementaciones base aceptadas [1588_geometry.cpp](1588_geometry.cpp), [1588_geometry.java](1588_geometry.java), [1588_geometry.py](1588_geometry.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1588_geometry.cpp](1588_geometry.cpp) | G++ 13.2 x64 | geometry | O(n² log n) | AC | 0.031 s | 240 KB | 11287971 |
| [1588_geometry.go](1588_geometry.go) | Go 1.14 x64 | geometry | O(n² log n) | AC | 0.046 s | 6288 KB | 11287972 |
| [1588_geometry.java](1588_geometry.java) \* | Java 1.8 | geometry | O(n² log n) | AC | 0.171 s | 1344 KB | 11287979 |
| [1588_geometry.py](1588_geometry.py) \* | Python 3.12 x64 | geometry | O(n² log n) | AC | 0.187 s | 572 KB | 11287976 |
| [1588_geometry.rs](1588_geometry.rs) | Rust 1.75 x64 | geometry | O(n² log n) | AC | 0.031 s | 452 KB | 11287980 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1588_geometry_optimized.go](1588_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(n²) expected | AC | 0.046 s | 1020 KB | 11310418 |
| [1588_geometry_optimized.rs](1588_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n² log n) | AC | 0.015 s | 236 KB | 11310417 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
