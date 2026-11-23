# 1371. Agencia de transportes

[Timus 1371](https://acm.timus.ru/problem.aspx?space=1&num=1371) · dificultad 516 · dp

Problema original con idea de Den Raskovalov, preparado por Alexander Klepinin, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 50 000 sucursales están unidas por N − 1 carreteras en un árbol, y
cada carretera tiene un tiempo de entrega de 0 a 1000. Hay que imprimir
el tiempo medio de entrega sobre todos los pares ordenados de sucursales
distintas, la suma de todas las distancias dividida entre N(N − 1), con
4 decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego N − 1 líneas con los extremos de una carretera y su tiempo.

## Salida

El tiempo medio.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 2 1
2 3 1
2 4 1
```

Salida:

```
1.5
```

## Solución

Se cuenta cada carretera una vez por cada par que la usa. Quitar una
carretera parte el árbol en trozos de s y N − s sucursales, y
exactamente los s · (N − s) pares con un extremo en cada trozo pasan por
ella. Así que la suma sobre pares ordenados es 2 · Σ c · s · (N − s).

Se enraíza el árbol en la sucursal 1 y se enumeran las sucursales con
los padres antes que los hijos, recorriendo en anchura. Leída al revés,
esa lista da los tamaños de los subárboles: cada sucursal suma su
tamaño al de su padre. `O(N)`.

Detalles a tener en cuenta:

- la suma llega a 4·10¹⁶ en un camino de las carreteras más caras, así
  que hacen falta enteros de 64 bits (prueba generada 2);
- un camino de 50 000 sucursales es demasiado profundo para la
  recursión, de ahí el orden en anchura;
- se admiten carreteras gratuitas, con tiempo 0 (prueba 03).

Las respuestas se compararon con sumar todas las distancias con una
búsqueda desde cada sucursal, en 300 árboles aleatorios de hasta 30
sucursales.

## Soluciones optimizadas

C++ conserva la suma por cortes con estrella plana. Cada arista dirigida tiene siguiente32, destino y peso16; padres, costes paternos, orden y tamaños también caben en16 pues N≤50000 y peso≤1000. Procesar al revés un orden iterativo padres-primero; multiplicar weight·s·(N−s) tras promover a64 bits. Suma doble y N(N−1) caben en64 con signo. Se divide primero por el denominador d para obtener la parte entera y el resto r. Las cuatro cifras decimales se calculan con floor((10000r+floor(d/2))/d). Si el resultado es 10000, se lleva uno a la parte entera. El resto escalado es menor que 2.5·10¹³ y el error no supera 0.00005. Tiempo y espacio O(N), sin recursión ni contenedores por vértice. Se conservan bases; las otras familias reutilizan las admitidas.

En la instantánea de comparación anterior, las implementaciones base [1371_dp.go](1371_dp.go), [1371_dp.java](1371_dp.java), [1371_dp.py](1371_dp.py), [1371_dp.rs](1371_dp.rs) cumplían la regla de inclusión del 15% superior o de las diez primeras posiciones en ambas métricas. Sus mediciones se conservan en la tabla de versiones sencillas.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1371_dp_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328658 (Go 1.14 x64): **0.046 s / 10744 KB**. Comparación archivada: `1371_dp.go` (Go 1.14 x64) — 0.109 s / 10604 KB (#11285602).

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Java guarda el árbol en arreglos planos; todos los lenguajes imprimen
  con punto decimal.

Retirar las hojas del árbol. En cada hoja, los acumuladores XOR recuperan su último vecino y el peso de la arista sin guardar listas de adyacencia. El envío aceptado 11324213 tardó 0.156 s y usó 5 856 KB. La versión sencilla tardó 0.218 s y usó 29648 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1371_dp.cpp](1371_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.078 s | 3976 KB | 11285601 |
| [1371_dp.go](1371_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.109 s | 10604 KB | 11285602 |
| [1371_dp.java](1371_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 3308 KB | 11285604 |
| [1371_dp.py](1371_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.218 s | 29648 KB | 11285603 |
| [1371_dp.rs](1371_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.046 s | 9444 KB | 11285607 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1371_dp_optimized.cpp](1371_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 1120 KB | 11315476 |
| [1371_graphs.py](1371_graphs.py) | PyPy 3.10 x64 | graphs | O(N) | AC | 0.156 s | 5 856 KB | 11324213 |
| [1371_dp_optimized.go](1371_dp_optimized.go) | Go 1.14 x64 | dp | O(N) | AC | 0.046 s | 10744 KB | 11328658 |
