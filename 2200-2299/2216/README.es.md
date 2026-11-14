# 2216. Menos ascensores vigilados que toda ruta de abajo arriba debe usar

[Timus 2216](https://acm.timus.ru/problem.aspx?space=1&num=2216) · dificultad 662 · prefix_sums

Problema original de Matvey Dmitriev, de la clasificatoria del Campeonato Regional de los Urales ICPC 2025.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un edificio tiene los pisos 1 … N y K ascensores, y el ascensor i se
mueve entre cualesquiera pisos de [lᵢ, rᵢ]. Poner cámaras en el menor
número de ascensores para que todo el que va del piso 1 al piso N use
al menos un ascensor vigilado, o imprimir −1. Solo se puede ir de un piso
a otro en ascensor, y se garantiza que cualquier piso es accesible desde
cualquier otro. Los límites son 1 segundo y 256 MB.

## Entrada

N y K, 1 ≤ N, K ≤ 10⁵, y luego los K segmentos con 1 ≤ lᵢ ≤ rᵢ ≤ N.

## Salida

El menor número de cámaras, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
1984 1
1 1984
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
2 2
1 2
1 2
```

Salida:

```
2
```

## Solución

Con N = 1 nadie necesita un ascensor, así que ninguna elección de
cámaras sirve y la respuesta es −1.

Si no, se mira el hueco entre los pisos f y f + 1. Toda ruta de 1 a N
debe cruzarlo, y solo lo cruzan los ascensores con l ≤ f < r, así que
vigilarlos todos atrapa a todo el mundo. Al revés, si alguna elección
deja al menos un ascensor sin vigilar sobre cada hueco, los segmentos de
los ascensores sin vigilar se solapan de 1 a N y forman una ruta sin
vigilar. Así la respuesta es el menor número de ascensores sobre un
solo hueco.

Un arreglo de diferencias (+1 en l, −1 en r) da el número de ascensores
sobre cada hueco como suma acumulada, y el mínimo sobre f = 1 … N − 1
es la respuesta.

La conectividad garantiza un mínimo positivo cuando N > 1. Un error es
exigir un hueco compartido para hacer transbordo: basta con que los
segmentos tengan un piso en común (prueba 12).

En el segundo ejemplo los dos ascensores cruzan el único hueco, así que
ambos necesitan cámara.

Esto cuesta O(N + K).

## Soluciones optimizadas

Se leen los intervalos de los ascensores en flujo y se registran sus extremos en un arreglo compacto de diferencias. La menor suma prefija entre pisos consecutivos es la respuesta.

El envío 11317733 en Python tardó 0.156 s y usó 1560 KB. La versión sencilla tardó 0.14 s y usó 14948 KB.

El envío 11317737 en Go tardó 0.031 s y usó 1312 KB. La versión sencilla tardó 0.015 s y usó 5784 KB.

El envío 11317747 en Rust tardó 0.015 s y usó 596 KB. La versión sencilla tardó 0.062 s y usó 3156 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321723 · Java 1.8 №11321729 · Go 1.14 x64 №11322089 · Python 3.12 x64 №11322090 · Rust 1.75 x64 №11322092.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2216_prefix_sums.cpp](2216_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + K) | AC | 0.046 s | 800 KB | 11321723 |
| [2216_prefix_sums.go](2216_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + K) | AC | 0.015 s | 5784 KB | 11322089 |
| [2216_prefix_sums.java](2216_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + K) | AC | 0.125 s | 960 KB | 11321729 |
| [2216_prefix_sums.py](2216_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + K) | AC | 0.14 s | 14948 KB | 11322090 |
| [2216_prefix_sums.rs](2216_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + K) | AC | 0.062 s | 3156 KB | 11322092 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2216_prefix_sums_optimized.py](2216_prefix_sums_optimized.py) \* | Python 3.12 x64 | prefix_sums | O(N + K) | AC | 0.156 s | 1560 KB | 11317733 |
| [2216_prefix_sums_optimized.go](2216_prefix_sums_optimized.go) | Go 1.14 x64 | prefix_sums | O(N + K) | AC | 0.031 s | 1312 KB | 11317737 |
| [2216_prefix_sums_optimized.rs](2216_prefix_sums_optimized.rs) | Rust 1.75 x64 | prefix_sums | O(N + K) | AC | 0.015 s | 596 KB | 11317747 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
