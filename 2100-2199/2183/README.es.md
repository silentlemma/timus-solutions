# 2183. Invertir los signos de un segmento para subir el mínimo

[Timus 2183](https://acm.timus.ru/problem.aspx?space=1&num=2183) · dificultad 687 · binary_search, dp

Problema original de Artyom Abaturov, del Concurso de Programación por Equipos de los Urales 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cambiar el signo de todos los números de exactamente un segmento no vacío
de un arreglo para que su mínimo sea lo mayor posible, e imprimir ese
mínimo. El arreglo tiene un número negativo. Los límites son 1 segundo y
256 MB.

## Entrada

n, 1 ≤ n ≤ 10⁵, y luego a₁ … aₙ, −10⁹ ≤ aᵢ ≤ 10⁹.

## Salida

El mayor mínimo posible.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
-1 3 -2 -4 5
```

Salida:

```
-1
```

### Ejemplo 2

Entrada:

```
4
2 -4 -3 -10
```

Salida:

```
2
```

## Solución

Se pregunta si es posible un mínimo de al menos x. Todo número menor que
x debe invertirse, así que el segmento tiene que cubrirlos a todos, y
todo número dentro del segmento debe quedar al menos en x, es decir, ser
a lo sumo −x. Un segmento más largo solo añade condiciones, así que basta
probar el más corto, del primer al último número menor que x. Si ningún
número es menor que x, igualmente hay que invertir un número a lo sumo
−x, lo que se cumple cuando el menor número es a lo sumo −x.

Una x mayor solo hace la prueba más difícil, así que una búsqueda binaria
sobre x de −10⁹ a 10⁹ halla el mayor valor que pasa; la prueba cuesta
O(n), O(n log C) en total.

En el segundo ejemplo invertir −4 −3 −10 da 2 4 3 10, cuyo mínimo es 2.

## Notas por lenguaje

- La solución en Python prescinde de la búsqueda binaria: un recorrido de
  izquierda a derecha guarda el mejor mínimo de prefijo con el cambio de
  signo sin empezar, en curso o terminado, en O(n).

## Soluciones optimizadas

La DP mantiene tres mínimos de prefijo: sin invertir, con el segmento invertido terminando en el elemento actual y con el segmento terminando en cualquier posición del prefijo. Solo requiere un recorrido y espacio auxiliar constante.

**Envíos de las versiones optimizadas en Timus**

G++ 13.2 x64 №11317399 · Go 1.14 x64 №11317402 · Java 1.8 №11317412 · Rust 1.75 x64 №11317407.

**Envíos de las versiones sencillas en Timus**

Python 3.12 x64 №11321738 · G++ 13.2 x64 №11321929 · Java 1.8 №11321932 · Rust 1.75 x64 №11321934.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2183_binary_search.cpp](2183_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n log C) | AC | 0.093 s | 964 KB | 11321929 |
| [2183_binary_search.go](2183_binary_search.go) | Go 1.14 x64 | binary_search | O(n log C) | AC | 0.031 s | 3500 KB | 11322055 |
| [2183_binary_search.java](2183_binary_search.java) | Java 1.8 | binary_search | O(n log C) | AC | 0.14 s | 1296 KB | 11321932 |
| [2183_binary_search.rs](2183_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n log C) | AC | 0.046 s | 3660 KB | 11321934 |
| [2183_dp.py](2183_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.109 s | 8144 KB | 11321738 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2183_dp.cpp](2183_dp.cpp) \* | G++ 13.2 x64 | dp | O(n) | AC | 0.093 s | 116 KB | 11317399 |
| [2183_dp.go](2183_dp.go) \* | Go 1.14 x64 | dp | O(n) | AC | 0.031 s | 1008 KB | 11317402 |
| [2183_dp.rs](2183_dp.rs) \* | Rust 1.75 x64 | dp | O(n) | AC | 0.046 s | 208 KB | 11317407 |
| [2183_dp.java](2183_dp.java) \* | Java 1.8 | dp | O(n) | AC | 0.14 s | 416 KB | 11317412 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
