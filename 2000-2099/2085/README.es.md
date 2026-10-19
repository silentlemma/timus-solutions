# 2085. Un camino del árbol que usa cada tecnología una vez

[Timus 2085](https://acm.timus.ru/problem.aspx?space=1&num=2085) · dificultad 1643 · hashing, trees

Problema original de Alexander Fetisov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n proyectos forman un árbol, y cada proyecto usa un conjunto de las m
tecnologías. Hallar un camino simple (quizá de un solo proyecto) en el
que cada tecnología aparezca en exactamente un proyecto, e imprimir sus
extremos, o "No solution". Se acepta cualquier camino válido. Los
límites son 5 segundos y 256 MB.

## Entrada

n y m, 1 ≤ n, m ≤ 10⁵, las n − 1 aristas y después, para cada proyecto,
el número de sus tecnologías y sus números; los conjuntos tienen a lo
sumo 10⁶ elementos en total.

## Salida

Los dos extremos del camino, o `No solution`.

## Evaluación

Un comprobador acepta "No solution" solo cuando la salida esperada lo
dice, y si no recorre el camino impreso y cuenta las tecnologías.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
1 2
1 3
3 4
3 5
1 1
1 3
0
2 1 3
1 2
```

Salida:

```
2 5
```

### Ejemplo 2

Entrada:

```
3 3
1 2
1 3
2 2 3
3 1 2 3
1 3
```

Salida:

```
2 2
```

### Ejemplo 3

Entrada:

```
2 3
1 2
2 1 2
2 1 3
```

Salida:

```
No solution
```

## Solución

Se da a cada tecnología un peso aleatorio de 64 bits y a cada proyecto
la suma de los pesos de sus tecnologías. En un camino donde cada
tecnología se usa una vez, los valores de los proyectos suman la suma G
de todos los pesos; si alguna tecnología se usa dos veces o falta, la
suma es otra combinación lineal de números aleatorios independientes,
que vale G solo con probabilidad de unos 2⁻⁶⁴. Así el problema pasa a
ser: hallar un camino cuyos valores sumen G módulo 2⁶⁴.

Se enraíza el árbol y depth(v) es la suma de los valores desde la raíz
hasta v. Un camino u … v por su vértice más alto x suma
depth(u) + depth(v) − 2 depth(x) + value(x). Para cada x los vértices de
su subárbol se guardan en una tabla hash de profundidad a vértice,
construida de menor a mayor: x empieza con su propia tabla {depth(x)},
y la tabla de cada hijo se funde con ella, la menor en la mayor. Antes de
fundir, cada profundidad d de la tabla menor busca en la mayor
G + 2 depth(x) − value(x) − d; un acierto es un camino por x, pues los
dos lados están en hijos distintos de x (o un extremo es x). Un solo
proyecto con valor G es un camino por sí mismo. Cada vértice se mueve
O(log n) veces, así que el trabajo esperado es O(n log n + Σ aᵢ).

El árbol se recorre en anchura, con los hijos antes que los padres a la
vuelta, así que los árboles profundos no necesitan recursión. En el
primer ejemplo el camino 5, 3, 4 usa la tecnología 2, luego ninguna y
luego 1 y 3; la respuesta del ejemplo 2 … 5 es igual de buena.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2085_hashing_trees.cpp](2085_hashing_trees.cpp) | G++ 13.2 x64 | hashing, trees | O(n log n + sum a) | AC | 0.937 s | 23040 KB |
| [2085_hashing_trees.go](2085_hashing_trees.go) | Go 1.14 x64 | hashing, trees | O(n log n + sum a) | AC | 0.343 s | 44040 KB |
| [2085_hashing_trees.java](2085_hashing_trees.java) | Java 1.8 | hashing, trees | O(n log n + sum a) | AC | 0.593 s | 50248 KB |
| [2085_hashing_trees.py](2085_hashing_trees.py) | Python 3.12 x64 | hashing, trees | O(n log n + sum a) | AC | 1.312 s | 101000 KB |
| [2085_hashing_trees.rs](2085_hashing_trees.rs) | Rust 1.75 x64 | hashing, trees | O(n log n + sum a) | AC | 0.156 s | 31624 KB |
