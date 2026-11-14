# 1463. ¡Alegría para la gente!

[Timus 1463](https://acm.timus.ru/problem.aspx?space=1&num=1463) · dificultad 598 · dp

Problema original de Alexander Toropov, con agradecimiento especial a Alexander Ipatov, del concurso de la Universidad Estatal de los Urales en el campus de invierno de Petrozavodsk, enero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N ciudades (1 ≤ N ≤ 50000) que dan una alegría A[i] al visitarlas,
y K enlaces entre pares de ciudades que dan una alegría c al volar por
ellos, todos enteros no negativos hasta 10000. Entre dos ciudades hay
como mucho una ruta, así que los enlaces forman un bosque. Hay que
hallar una ruta por ciudades distintas, empezando donde sea, con la
mayor alegría total de sus ciudades y vuelos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y K, luego las alegrías A[i] y después K líneas a, b, c.

## Salida

La mayor alegría, el número de ciudades de la ruta y la ruta. Se acepta
cualquier ruta óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1
1 1
1 2 1
```

Salida:

```
3
2
1 2
```

### Ejemplo 2

Entrada:

```
8 7
1 5 4 6 10 1 2 2
1 2 1
2 3 10
2 4 1
4 5 1
4 6 2
6 7 2
6 8 3
```

Salida:

```
37
4
5 4 2 3
```

## Solución

Una ruta en un bosque es un camino dentro de un árbol, y todo camino
tiene una ciudad más alta cuando su árbol se cuelga de una raíz. Se
enraíza cada árbol en cualquier ciudad y se procesan las ciudades desde
las hojas hacia arriba. Para cada ciudad v se guarda la mejor ruta que
empieza en v y baja, down[v] = A[v] más el mejor valor de c + down[w]
entre sus hijos w, junto con el hijo que lo da. La mejor ruta cuya
ciudad más alta es v une a A[v] los dos mejores de esos valores; todos
los valores son no negativos, así que tomar dos hijos (o uno, o
ninguno) nunca empeora. La ruta se reconstruye bajando por los hijos
guardados por las dos ramas elegidas.

Los árboles pueden tener 50000 ciudades de profundidad, así que el
recorrido usa una pila explícita en lugar de recursión. `O(N + K)`.

Detalles a tener en cuenta:

- puede no haber ningún enlace, y la mejor ruta puede ser una sola
  ciudad (pruebas 03, 04, 07, gen5);
- una cadena larga desborda la recursión (gen2);
- con alegrías nulas cualquier ruta es óptima (prueba 05).

## Soluciones optimizadas

La versión en C++ retira las hojas sucesivamente. Para cada ciudad mantiene su grado actual, el XOR de los vecinos que quedan y el XOR de las alegrías de los vuelos restantes. En una hoja esos dos valores identifican su único vuelo restante. Las dos mejores ramas retiradas permiten calcular y reconstruir la mejor ruta que pasa por la ciudad. El tiempo es O(N + K) y el espacio adicional es O(N). Las métricas corresponden al envío 11317012.

La versión en Python retira las hojas del mismo modo. Combina cada rama retirada con la mejor rama hallada hasta entonces en su vértice padre y después actualiza esa mejor rama. Basta guardar los dos vértices donde empiezan las ramas elegidas para reconstruir la ruta óptima. El tiempo es O(N + K) y el espacio adicional es O(N). Las métricas corresponden al envío 11317010.

La versión en Go retira las hojas con un arreglo compacto de registros de ciudades. La operación XOR permite hallar el vecino y el peso restantes sin listas de adyacencia. El envío 11317154 tardó 0,078 s y usó 1976 KB frente a 0,125 s y 11580 KB en la base.

Rust retira las hojas con registros compactos y recupera el vecino restante y el peso mediante XOR. El envío 11317155 tardó 0,015 s y usó 980 KB frente a 0,031 s y 10112 KB en la base.

Java retira las hojas y recupera el vecino restante y el peso mediante XOR. El envío 11317156 tardó 0,140 s y usó 1276 KB frente a 0,156 s y 3896 KB en la base.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322150 · Go 1.14 x64 №11322151 · Java 1.8 №11322152 · Python 3.12 x64 №11322154 · Rust 1.75 x64 №11322155.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1463_dp.cpp](1463_dp.cpp) | G++ 13.2 x64 | dp | O(N + K) | AC | 0.14 s | 5372 KB | 11322150 |
| [1463_dp.go](1463_dp.go) | Go 1.14 x64 | dp | O(N + K) | AC | 0.125 s | 11580 KB | 11322151 |
| [1463_dp.java](1463_dp.java) | Java 1.8 | dp | O(N + K) | AC | 0.156 s | 3896 KB | 11322152 |
| [1463_dp.py](1463_dp.py) | Python 3.12 x64 | dp | O(N + K) | AC | 0.312 s | 34776 KB | 11322154 |
| [1463_dp.rs](1463_dp.rs) | Rust 1.75 x64 | dp | O(N + K) | AC | 0.031 s | 10112 KB | 11322155 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1463_trees.cpp](1463_trees.cpp) \* | G++ 13.2 x64 | trees | O(N + K) | AC | 0.109 s | 1504 KB | 11317012 |
| [1463_trees.py](1463_trees.py) | Python 3.12 x64 | trees | O(N + K) | AC | 0.203 s | 10696 KB | 11317010 |
| [1463_trees.go](1463_trees.go) | Go 1.14 x64 | trees | O(N + K) | AC | 0.078 s | 1976 KB | 11317154 |
| [1463_trees.rs](1463_trees.rs) \* | Rust 1.75 x64 | trees | O(N + K) | AC | 0.015 s | 980 KB | 11317155 |
| [1463_trees.java](1463_trees.java) | Java 1.8 | trees | O(N + K) | AC | 0.140 s | 1276 KB | 11317156 |

\* El juez aceptó el envío. Aún queda por alcanzar el objetivo de clasificación de C++. Aceptada. El corte de clasificación no contiene envíos comparables en Rust de otros autores.
