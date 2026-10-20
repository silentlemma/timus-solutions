# 2147. Las carreteras de un sentido y de doble sentido más baratas para todas las peticiones

[Timus 2147](https://acm.timus.ru/problem.aspx?space=1&num=2147) · dificultad 1890 · graphs

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n casas y m peticiones "a quiere un camino hasta b". Una carretera de
un sentido cuesta x y una de doble sentido cuesta y. Construir
carreteras de coste total mínimo para que cada petición tenga un camino
dirigido. Los límites son 3 segundos y 256 MB.

## Entrada

n, m, x e y, 2 ≤ n ≤ 10⁵, 1 ≤ m ≤ 10⁵, 1 ≤ x, y ≤ 10⁹, y luego las m
peticiones distintas.

## Salida

El coste mínimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3 2 3
1 2
1 3
2 3
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
4 3 2 3
1 2
1 3
2 1
```

Salida:

```
5
```

### Ejemplo 3

Entrada:

```
4 4 2 3
1 2
2 1
1 3
3 1
```

Salida:

```
6
```

## Solución

Las peticiones de componentes débilmente conexas distintas del grafo de
peticiones no interactúan, así que cada componente se resuelve sola.
Supongamos que tiene V casas y C componentes fuertemente conexas (CFC).

Si y ≤ x, un árbol generador de carreteras de doble sentido,
(V − 1) · y, atiende todas las peticiones, y ningún conjunto más barato
conecta V casas.

Si x < y hay dos candidatos. Un único ciclo dirigido por las V casas,
V · x, lo atiende todo. Si no, cada CFC de tamaño s necesita un conjunto
fuertemente conexo de carreteras, y un árbol de doble sentido por
(s − 1) · y lo da; las CFC forman un DAG, y carreteras de un sentido a lo
largo de un orden topológico de las CFC, (C − 1) · x, dan todas las
peticiones entre ellas. Eso es (V − C) · y + (C − 1) · x. Mezclar ambos,
un ciclo para unas CFC y árboles para otras, nunca supera a los dos: en
cuanto una CFC usa un ciclo, cada CFC en árbol de tamaño s junto con su
carretera de un sentido de enlace cuesta (s − 1) · y + x > s · x, lo que
costarían sus casas dentro de un único ciclo grande. Así que la respuesta de la componente es el candidato más
barato.

Las CFC salen del algoritmo de Kosaraju con búsquedas iterativas, y las
componentes débiles de una búsqueda más en ambos sentidos, en
O(n + m). Las sumas necesitan enteros de 64 bits.

En el segundo ejemplo 1 y 2 forman una CFC: una carretera de doble
sentido (3) más una de un sentido hacia 3 (2) cuestan 5, mientras que un
ciclo por 1, 2 y 3 costaría 6.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2147_graphs.cpp](2147_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + m) | AC | 0.093 s | 9164 KB |
| [2147_graphs.go](2147_graphs.go) | Go 1.14 x64 | graphs | O(n + m) | AC | 0.093 s | 17760 KB |
| [2147_graphs.java](2147_graphs.java) | Java 1.8 | graphs | O(n + m) | AC | 0.140 s | 8460 KB |
| [2147_graphs.py](2147_graphs.py) | Python 3.12 x64 | graphs | O(n + m) | AC | 0.687 s | 39596 KB |
| [2147_graphs.rs](2147_graphs.rs) | Rust 1.75 x64 | graphs | O(n + m) | AC | 0.093 s | 19712 KB |
