# 2096. Todo incluido

[Timus 2096](https://acm.timus.ru/problem.aspx?space=1&num=2096) · dificultad 2629 · dfs, trees

Problema original de Egor Shchelkonogov, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El plan 0 da una actividad para cada uno de n días. El plan i
(i = 1 … m) primero hace preguntas "qué hay el día x en el plan f" sobre
planes anteriores f, y después copia un plan anterior pᵢ y aplica
cambios, cada uno de los cuales pone en los días d, d + p, …,
d + (k − 1)p una actividad nueva (gana el cambio posterior). Responder
todas las preguntas. Los límites son 2 segundos y 64 MB.

## Entrada

n y m (hasta 10⁵), las n actividades del plan 0 y después, para cada
plan, sus preguntas y su plan base con los cambios; a lo sumo 10⁵
preguntas y 10⁵ cambios en total, y los cambios tocan a lo sumo 5·10⁶
días en total.

## Salida

Para cada plan, una línea con las respuestas a sus preguntas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2
1 2 3
1
0 3
0 2
1 2 2 4
2 2 1 5
3
1 1
1 2
1 3
0 0
```

Salida:

```
3
4 5 5
```

## Solución

Cada plan es su plan base más sus propios cambios, así que los planes
forman un árbol con raíz en el plan 0, y cada pregunta se refiere a un
plan fijo. Todas se responden fuera de línea en un recorrido del árbol
con un único array de actividades: al entrar en un plan se aplican sus
cambios guardando los valores viejos de los días que sobrescribe, se
responden las preguntas sobre ese plan, se visitan los hijos y al salir
se restauran los valores guardados en orden inverso. Cada día cambiado
se escribe y se restaura una vez, así que el trabajo es
O(n + m + Σ k + q). El recorrido usa una pila explícita, porque el árbol
puede ser un camino de 10⁵ planes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2096_dfs_trees.cpp](2096_dfs_trees.cpp) | G++ 13.2 x64 | dfs, trees | O(n + m + sum k + q) | AC | 0.078 s | 24856 KB |
| [2096_dfs_trees.go](2096_dfs_trees.go) | Go 1.14 x64 | dfs, trees | O(n + m + sum k + q) | AC | 0.093 s | 28888 KB |
| [2096_dfs_trees.java](2096_dfs_trees.java) | Java 1.8 | dfs, trees | O(n + m + sum k + q) | AC | 0.156 s | 30380 KB |
| [2096_dfs_trees.py](2096_dfs_trees.py) | Python 3.12 x64 | dfs, trees | O(n + m + sum k + q) | AC | 1.312 s | 36924 KB |
| [2096_dfs_trees.rs](2096_dfs_trees.rs) | Rust 1.75 x64 | dfs, trees | O(n + m + sum k + q) | AC | 0.078 s | 25888 KB |
