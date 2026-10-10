# 1160. Conectar todos los concentradores con el cable más largo lo más corto posible

[Timus 1160](https://acm.timus.ru/problem.aspx?space=1&num=1160) · dificultad 146 · dsu

Problema original de Andrew Stankevich, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 1000` concentradores pueden unirse con `M ≤ 15000` cables posibles de
longitudes dadas. Elige cables que conecten cada concentrador con todos
los demás, directamente o a través de otros, de modo que el cable más
largo elegido sea lo más corto posible. Imprime esa longitud, luego el
número de cables y los cables.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `M`, y luego `M` líneas con dos concentradores y una longitud.

## Salida

El cable más largo, el número de cables `P` y luego `P` pares de
concentradores.

## Evaluación

Se acepta cualquier plan que conecte todos los concentradores con cables
posibles y cuyo cable más largo sea el menor posible. El comprobador halla
por su cuenta esa longitud mínima, con búsqueda binaria sobre las
longitudes y una prueba de conectividad, y verifica la longitud y el plan
impresos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 6
1 2 1
1 3 1
1 4 2
2 3 1
3 4 1
2 4 1
```

Salida:

```
1
3
1 2
1 3
3 4
```

## Solución

El algoritmo de Kruskal construye un árbol generador desde los cables más
cortos, saltando un cable cuyos extremos ya están conectados, lo que dice
una unión de conjuntos disjuntos. El árbol que construye es un árbol
generador mínimo, y un árbol generador mínimo también minimiza su arista
más larga: cuando Kruskal añade su última arista, la más larga `e`, los
cables más cortos que `e` dejan los concentradores en al menos dos grupos
separados, así que todo plan conectado necesita un cable al menos tan
largo como `e`. La respuesta es la longitud de la última arista tomada, y
los `N − 1` cables del árbol son un plan válido. `O(M log M)`.

Detalles a tener en cuenta:

- el plan no tiene que ser un árbol, y se acepta cualquier plan con el
  menor cable más largo;
- hay que llegar a todos los concentradores, así que la respuesta la da la
  última arista que toma Kruskal, no la última considerada;
- las longitudes iguales no necesitan nada especial.

Las respuestas se comprobaron con el comprobador en todas las pruebas y en
60 redes aleatorias.

## Notas por lenguaje

- Todos los lenguajes ordenan los cables y aplican la misma unión con
  reducción a la mitad de caminos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1160_dsu.cpp](1160_dsu.cpp) | G++ 13.2 x64 | dsu | O(M log M) | AC | 0.031 s | 436 KB |
| [1160_dsu.go](1160_dsu.go) | Go 1.14 x64 | dsu | O(M log M) | AC | 0.046 s | 1448 KB |
| [1160_dsu.java](1160_dsu.java) | Java 1.8 | dsu | O(M log M) | AC | 0.171 s | 3500 KB |
| [1160_dsu.py](1160_dsu.py) | Python 3.12 x64 | dsu | O(M log M) | AC | 0.078 s | 5864 KB |
| [1160_dsu.rs](1160_dsu.rs) | Rust 1.75 x64 | dsu | O(M log M) | AC | 0.015 s | 1104 KB |
