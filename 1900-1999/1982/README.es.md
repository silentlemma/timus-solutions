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

## Notas por lenguaje

Las cinco versiones usan Prim denso con costes enteros y almacenan la
matriz completa. C++, Go, Java y Rust usan enteros amplios para claves y
total; Python usa enteros exactos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1982_greedy.cpp](1982_greedy.cpp) | G++ 13.2 x64 | greedy | O(n^2) | AC | 0.015 s | 496 KB |
| [1982_greedy.go](1982_greedy.go) | Go 1.14 x64 | greedy | O(n^2) | AC | 0.031 s | 1260 KB |
| [1982_greedy.java](1982_greedy.java) | Java 1.8 | greedy | O(n^2) | AC | 0.093 s | 648 KB |
| [1982_greedy.py](1982_greedy.py) | Python 3.12 x64 | greedy | O(n^2) | AC | 0.078 s | 1492 KB |
| [1982_greedy.rs](1982_greedy.rs) | Rust 1.75 x64 | greedy | O(n^2) | AC | 0.015 s | 440 KB |
