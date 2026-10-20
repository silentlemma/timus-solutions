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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2216_prefix_sums.cpp](2216_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + K) | AC | 0.031 s | 604 KB |
| [2216_prefix_sums.go](2216_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + K) | AC | 0.046 s | 5596 KB |
| [2216_prefix_sums.java](2216_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + K) | AC | 0.093 s | 784 KB |
| [2216_prefix_sums.py](2216_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + K) | AC | 0.140 s | 15108 KB |
| [2216_prefix_sums.rs](2216_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + K) | AC | 0.031 s | 2948 KB |
