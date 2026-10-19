# 1949. Horarios con prioridades

[Timus 1949](https://acm.timus.ru/problem.aspx?space=1&num=1949) · difficulty 1400 · matching

Original problem from Open Ural FU Personal Contest 2012 | by Vitaliy Belokobilskiy, Sergey Madzhuga.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n películas y k espectadores. La película i ocupa [a_i,b_i) y tiene
un valor c_i. Cada película debe verse entera, sin solapamientos para una
misma persona y sin disminuir c entre películas sucesivas. Se permiten
finales iguales al siguiente inicio, valores c iguales, pausas y personas
sin películas. No hay tiempo de traslado.

Elegir un conjunto factible cuya cadena binaria de pertenencia, en orden
de entrada, sea lexicográficamente máxima, prefiriendo 1 a 0. Una película
anterior pesa más que todas las posteriores juntas. Límites: 1 s y 64 MB.

## Entrada

n y k, 1≤k≤n≤100, seguidos de n ternas a_i,b_i,c_i en orden de prioridad.
0≤a_i<b_i≤86399 y 1≤c_i≤10000. El orden no tiene por qué ser cronológico.

## Salida

Una cadena de n dígitos: bit i igual a 1 si se incluye la película i en
el mejor conjunto factible. No se solicita asignación de espectadores.

## Evaluación

Las salidas se comparan token a token; la cadena óptima es única.

## Ejemplos

```
4 2
1 5 10
3 6 20
5 10 9
5 10 10
```

```
1101
```

```
4 1
1 5 10
3 6 20
5 10 9
5 10 10
```

```
1001
```

## Solución

Crear una arista i→j cuando b_i≤a_j y c_i≤c_j. El tiempo aumenta
estrictamente, así que el grafo es acíclico y cada horario es un camino.
Para s películas seleccionadas, duplicar los vértices en izquierda y
derecha y conservar las aristas entre copias. Si el emparejamiento máximo
tiene M aristas, hacen falta exactamente s−M espectadores.

Prueba: p caminos producen un emparejamiento de sus aristas consecutivas,
s−p en total. Recíprocamente, cada vértice tiene como máximo un predecesor
y un sucesor por las aristas emparejadas. Al no haber ciclos, forman s−M
caminos disjuntos y cada uno es un horario válido. La factibilidad equivale
por tanto a s−M≤k.

Recorrer la entrada por prioridad e intentar añadir cada película. Si el
conjunto sigue siendo factible, conservarla: los bits futuros pueden ser
cero. Si no, rechazarla. La factibilidad se hereda al quitar películas de
un horario, pues se mantienen tiempo y valores no decrecientes. Ninguna
adición futura puede arreglar un subconjunto imposible. Así se fija en
cada paso el mejor primer bit alcanzable y se prueba la optimalidad voraz.

Mantener el emparejamiento máximo con dos búsquedas ordenadas:

1. Añadir solo la copia izquierda. Buscar desde ella un camino aumentante
   hacia destinos derechos antiguos y activos, actualizando ambos mapas.
2. Activar la copia derecha. Desde ella buscar al revés por las aristas
   de predecesores hasta una copia izquierda libre.

En la primera fase cualquier camino aumentante nuevo debe empezar en la
nueva izquierda libre; el máximo solo puede aumentar en uno. Hallarlo
alcanza esa cota; no hallarlo demuestra que el anterior sigue siendo máximo.
La segunda fase tiene la prueba simétrica. Tras ambas el emparejamiento
es máximo. Buscar solo desde la izquierda nueva omitiría mejoras a través
de la derecha nueva.

Reiniciar las marcas entre fases. Guardar ambos mapas de parejas y M antes
de insertar; si s+1−M>k, desactivar la candidata y restaurarlo todo.
Las películas aceptadas permanecen activas. Imprimir los bits conservados.

O(n³) tiempo y O(n²) espacio. Construir el grafo cuesta O(n²); cada una
de las n candidatas usa dos búsquedas O(n²) y copias O(n). Una búsqueda
visita cada vértice del otro lado como máximo una vez; profundidad ≤n≤100.

No maximizar cantidad de películas ni suma de c_i, ni perder prioridad al
ordenar. Las comparaciones de tiempo y valor permiten igualdad. Ambas
copias importan; la derecha nueva sigue inactiva durante la primera fase.
Las películas rechazadas deben permanecer inactivas.

## Notas por lenguaje

Las versiones nativas usan matrices booleanas, arreglos de actividad y
visitas y mapas enteros de parejas. Una función aumentante genérica sirve
para ambos sentidos intercambiando grafo y mapas. Python usa máscaras
de hasta 100 bits; una sola máscara de 64 bits no basta. Limpiar visitas
entre fases y restaurar ambos mapas al rechazar. Solo biblioteca estándar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1949_matching.cpp](1949_matching.cpp) | G++ 13.2 x64 | matching | O(n^3) | AC | 0.031 s | 440 KB |
| [1949_matching.go](1949_matching.go) | Go 1.14 x64 | matching | O(n^3) | AC | 0.031 s | 1328 KB |
| [1949_matching.java](1949_matching.java) | Java 1.8 | matching | O(n^3) | AC | 0.125 s | 628 KB |
| [1949_matching.py](1949_matching.py) | Python 3.12 x64 | matching | O(n^3) | AC | 0.093 s | 740 KB |
| [1949_matching.rs](1949_matching.rs) | Rust 1.75 x64 | matching | O(n^3) | AC | 0.031 s | 264 KB |
