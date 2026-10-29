# 1020. La longitud de un hilo alrededor de clavos redondos

[Timus 1020](https://acm.timus.ru/problem.aspx?space=1&num=1020) · dificultad 100 · geometry

Problema original de la Segunda Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 7 de octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` cabezas redondas de clavos (`1 ≤ N ≤ 16`) del mismo radio `R` están en
los vértices de un polígono convexo, dadas en orden alrededor de él (en
sentido horario o antihorario); las cabezas no se solapan y las coordenadas
no superan 100 en valor absoluto. Un hilo se tensa alrededor de todas las
cabezas. Halla su longitud redondeada a dos decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y el número real `R`, y luego `N` líneas con las coordenadas reales de
los centros, en orden alrededor del polígono.

## Salida

La longitud del hilo con dos decimales.

## Evaluación

La salida se compara token a token; los números pueden diferir como mucho en
0.01.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1
0 0
3 0
0 4
```

Salida:

```
18.28
```

### Ejemplo 2

Entrada:

```
1 2.5
1.5 -2.0
```

Salida:

```
15.71
```

## Solución

El hilo está formado por segmentos rectos y arcos. Cada segmento recto es
tangente por fuera a dos cabezas vecinas, así que es el lado entre sus
centros desplazado hacia fuera `R`: su longitud es la del lado del polígono.
En cada clavo el hilo gira de la dirección de un lado a la del siguiente por
un arco de radio `R`, tanto como el ángulo exterior del polígono en ese
vértice. Los ángulos exteriores de un polígono convexo suman una vuelta
completa, `2π`, así que todos los arcos juntos forman una circunferencia de
radio `R`.

Respuesta: el perímetro del polígono más `2πR`, `O(N)`.

Detalles a tener en cuenta:

- `N = 1`: el hilo es solo la circunferencia `2πR`; `N = 2`: el «perímetro»
  es la distancia de ida y vuelta;
- el polígono puede venir en sentido horario; a la fórmula le da igual;
- imprime exactamente dos decimales.

## Soluciones optimizadas

Las soluciones optimizadas en C++ y Java recorren el polígono mientras
leen, así que nunca guardan los clavos. Java además lee la entrada en
bloques de 1 KB, separa cada número a mano en lugar de usar `Scanner` y
redondea con `BigDecimal` como lo hace `String.format`. C++, 156 KB en
lugar de 224 KB, con el mismo tiempo; Java, 780 KB en lugar de 2096 KB,
con el mismo tiempo.

## Notas por lenguaje

La misma fórmula en todos los lenguajes. La solución simple en Java lee
e imprime con `Locale.US`, para que el separador decimal sea un punto.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1020_geometry.cpp](1020_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 224 KB | 11278243 |
| [1020_geometry.go](1020_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.015 s | 1084 KB | 11278244 |
| [1020_geometry.java](1020_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.109 s | 2096 KB | 11278246 |
| [1020_geometry.py](1020_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.062 s | 392 KB | 11278245 |
| [1020_geometry.rs](1020_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 264 KB | 11278249 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1020_geometry_optimized.cpp](1020_geometry_optimized.cpp) \* | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 156 KB | 11303701 |
| [1020_geometry_optimized.java](1020_geometry_optimized.java) | Java 1.8 | geometry | O(N) | AC | 0.109 s | 780 KB | 11303958 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
