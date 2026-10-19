# 1882. Un viejo Nokia

[Timus 1882](https://acm.timus.ru/problem.aspx?space=1&num=1882) · dificultad 2584 · shortest_paths

Problema original de Mikhail Rubinchik, del Concurso Regional Escolar de Programación de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una agenda tiene n nombres distintos en orden alfabético; al principio
se ven todos y el actual es el primero. "Arriba" y "abajo" recorren en
círculo los nombres visibles. Teclear una letra deja visibles solo los
nombres que empiezan por las letras tecleadas y hace actual el primero;
una letra con la que no sigue ningún nombre no se acepta. Borrar la
última letra mantiene el nombre actual y muestra todos los nombres con
el comienzo más corto. Cada pulsación cuesta un segundo; una letra
cuesta tantas pulsaciones como su lugar en la tecla de un teclado de
teléfono normal (abc, def, ghi, jkl, mno, pqrs, tuv, wxyz). Para cada
nombre hay que hallar el menor tiempo para hacerlo actual.

## Entrada

n (1 ≤ n ≤ 10⁵) y luego los nombres en orden alfabético, en minúsculas,
con longitud total de como mucho 10⁵.

## Salida

El menor tiempo para cada nombre.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
a
aaa
aab
b
d
```

Salida:

```
0 1 2 2 1
```

## Solución

Una situación es un par: las letras tecleadas, con las que debe empezar
el nombre actual, y el nombre actual x. Las letras tecleadas son
entonces las d primeras de x, así que el par es (x, d), y hay
Σ (|x| + 1) ≤ 2·10⁵. En orden alfabético los nombres con un comienzo
dado forman un intervalo, el subárbol de un nodo del trie. "Abajo" y
"arriba" pasan al nombre siguiente o anterior de ese intervalo, en
círculo, por un segundo. Borrar lleva a (x, d − 1) por un segundo.
Teclear la letra c lleva al primer nombre del nodo hijo, sea cual sea
x. Así que cada nodo tiene un vértice concentrador: cada par llega gratis
al concentrador de su nodo, y este lleva al primer nombre de cada hijo
por el coste de la letra. Los pesos van de 0 a 4, así que Dijkstra
funciona con cinco cubetas en círculo. La respuesta para x es la menor
distancia entre sus pares. `O(n + L)` para la longitud total L.

En el ejemplo "d" está a un "arriba" de "a", y "b" a dos; "aab" cuesta
dos "abajo" desde "a", y teclear antes "a" no ayuda.

Trampas:

- borrar mantiene el nombre actual, así que una ruta puede teclear
  letras, moverse por la lista corta, borrar y seguir moviéndose;
- "arriba" desde el primer nombre visible pasa al último, lo que abarata
  los últimos nombres;
- una letra cuesta su lugar en la tecla, hasta 4 en s y z, así que
  moverse puede salir más barato que teclear;
- las aristas de teclear una letra no dependen del nombre actual, y los
  concentradores lo aprovechan para que el grafo sea lineal.

Los tiempos coinciden con una búsqueda sobre los estados (letras
tecleadas, nombre actual) en 1500 agendas pequeñas aleatorias, y con una
implementación aceptada independiente en las grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1882_shortest_paths.cpp](1882_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(n + L) | AC | 0.031 s | 7060 KB |
| [1882_shortest_paths.go](1882_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(n + L) | AC | 0.046 s | 20636 KB |
| [1882_shortest_paths.java](1882_shortest_paths.java) | Java 1.8 | shortest_paths | O(n + L) | AC | 0.203 s | 19012 KB |
| [1882_shortest_paths.py](1882_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(n + L) | AC | 0.500 s | 35004 KB |
| [1882_shortest_paths.rs](1882_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(n + L) | AC | 0.031 s | 16020 KB |
