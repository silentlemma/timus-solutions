# 1982. Bosque mínimo que alcanza vértices abastecidos

[Timus 1982](https://acm.timus.ru/problem.aspx?space=1&num=1982) · dificultad 128 · graphs, greedy

Problema original de Mikhail Rubinchik, del Campeonato Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo completo no dirigido tiene `n` vértices y un conjunto no vacío
de `k` vértices ya abastecidos. Elija aristas de coste total mínimo para
que cada vértice pueda alcanzar al menos uno abastecido. Los propios
vértices abastecidos pueden permanecer en componentes distintas.

Todos los datos son enteros, `1≤k≤n≤100`. La matriz de costes es
simétrica, su diagonal es cero y sus demás entradas están entre 1 y
`10⁵`. Tiempo: 0,5 segundos; memoria: 64 MB.

## Entrada

Lea `n k`, después `k` números distintos de vértices abastecidos entre 1
y `n`, y la matriz de costes `n×n`.

## Salida

Un entero: el coste total mínimo.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

Entrada:

```
4 2
1 4
0 2 4 3
2 0 5 2
4 5 0 1
3 2 1 0
```

Salida:

```
3
```

## Solución

Añada un vértice imaginario unido mediante aristas de coste cero a todos
los abastecidos. Un árbol de expansión mínima del grafo aumentado
resuelve el problema. Cualquier red original factible se vuelve conexa
al añadir esas aristas gratuitas, así que un árbol aumentado no cuesta
más. A la inversa, quitar el vértice imaginario de un árbol aumentado
deja componentes que contienen cada una un vértice abastecido,
conservando el coste de las aristas pagadas. Los dos óptimos son
iguales.

Use Prim denso sin almacenar explícitamente el vértice adicional.
Inicialice a cero las claves de todos los vértices abastecidos y a
infinito las restantes. Es el estado después de procesar el vértice
imaginario. Seleccione repetidamente el vértice sin usar de menor clave,
añada esta al resultado y actualice los demás vértices sin usar con su
fila de la matriz.

Una clave representa la arista más barata hacia la parte procesada del
árbol aumentado. La propiedad del corte garantiza que cada elección de
Prim es segura. La inicialización incluye todos los vértices
abastecidos. Al terminar, la suma es el coste del árbol mínimo aumentado
y, por tanto, el óptimo buscado.

También puede verse como un bosque con raíces. Los ciclos de coste
positivo se pueden eliminar. Si un árbol contiene varios vértices
abastecidos, corte una arista entre ellos para conservar abastecimiento
en ambos lados. Así, un óptimo puede tener exactamente `k` componentes y
`n−k` aristas pagadas. Para `k=n`, el coste es cero.

En el ejemplo, seleccione la arista 1–2 de coste 2 y la 3–4 de coste 1.
Cada componente contiene un vértice abastecido y el total es 3.

Hay `n` búsquedas de clave mínima y `n` actualizaciones de fila, cada
una `O(n)`. Tiempo total `O(n²)`; memoria `O(n²)` para la matriz y
`O(n)` adicional para claves y marcas. El resultado no supera
`(n−k)·10⁵≤9 900 000`.

Trampas:

- Inicialice a cero todos los vértices abastecidos, independientemente
  del orden de entrada.
- Un vértice no abastecido no debe obtener una clave cero inicial.
- Conectar vértices no abastecidos entre sí puede reducir el coste.
- El cero diagonal no es una conexión gratuita entre vértices distintos.
- Si todos los vértices están abastecidos, no se necesita ninguna arista pagada.

## Soluciones optimizadas

La solución optimizada en C++ analiza los números a mano desde un búfer
de 4 KB que rellena con `fread`, en lugar de `iostream`, y guarda los
costes en una matriz fija de 100 × 100 `int` en lugar de un vector de
filas de `long long`. Como `n≤100` y cada coste no pasa de `10⁵`, las
claves y la respuesta, como mucho 9 900 000, también caben en `int`, y
`10⁵ + 1` sirve de infinito: {1982_greedy_optimized.cpp}.

La solución optimizada en Python toma los tokens línea a línea de un
generador sobre `sys.stdin.buffer` en lugar de partir toda la entrada de
golpe, y guarda cada fila de costes en un `array("I")` de números de
32 bits sin signo en lugar de una lista de objetos enteros; los costes
de hasta `10⁵` caben ahí. Además elige el vértice de clave mínima con un
bucle simple en lugar de construir una tupla por cada candidato, y usa
`10⁵ + 1` como infinito: {1982_greedy_optimized.py}.

La solución optimizada en Rust analiza los números desde un `BufReader`
de 4 KB que se rellena solo, en lugar de leer toda la entrada en una
cadena, y guarda los costes en un único vector plano de `u32` en lugar
de un vector de filas de `u64`. Como `n≤100` y cada coste no pasa de
`10⁵`, las claves y la respuesta, como mucho 9 900 000, también caben en
`u32`, y `10⁵ + 1` sirve de infinito: {1982_greedy_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1982_greedy_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +76.61%; base: `1982_greedy.cpp`.

- `1982_greedy_optimized.py`: reducción de tiempo -19.23%; reducción de
  memoria +65.15%; base: `1982_greedy.py`.

- `1982_greedy_optimized.rs`: reducción de tiempo -106.67%; reducción de
  memoria +46.36%; base: `1982_greedy.rs`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1982_greedy.go](1982_greedy.go).

Las cinco versiones usan Prim denso con costes enteros y almacenan la
matriz completa. C++, Go, Java y Rust usan enteros amplios para claves y
total; Python usa enteros exactos.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1982_greedy.cpp](1982_greedy.cpp) | G++ 13.2 x64 | greedy | O(n^2) | AC | 0.015 s | 496 KB | 11292336 |
| [1982_greedy.go](1982_greedy.go) | Go 1.14 x64 | greedy | O(n^2) | AC | 0.031 s | 1260 KB | 11292337 |
| [1982_greedy.java](1982_greedy.java) | Java 1.8 | greedy | O(n^2) | AC | 0.093 s | 552 KB | 11304431 |
| [1982_greedy.py](1982_greedy.py) | Python 3.12 x64 | greedy | O(n^2) | AC | 0.078 s | 1492 KB | 11292338 |
| [1982_greedy.rs](1982_greedy.rs) | Rust 1.75 x64 | greedy | O(n^2) | AC | 0.015 s | 440 KB | 11292340 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1982_greedy_optimized.cpp](1982_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n^2) | AC | 0.015 s | 116 KB | 11304427 |
| [1982_greedy_optimized.py](1982_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(n^2) | AC | 0.093 s | 520 KB | 11304429 |
| [1982_greedy_optimized.rs](1982_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(n^2) | AC | 0.031 s | 236 KB | 11304428 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
