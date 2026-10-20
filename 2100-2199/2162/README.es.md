# 2162. Contar segmentos de un arreglo que codifican un grafo simple

[Timus 2162](https://acm.timus.ru/problem.aspx?space=1&num=2162) · dificultad 1088 · hashing, segment_tree

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2021.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo simple se escribe como N, M y luego M pares de vértices de 1 a
N, con N ≥ 1, sin lazos ni aristas repetidas. Contar los segmentos
contiguos de un arreglo de K números que son un registro así. Los límites
son 2 segundos y 256 MB.

## Entrada

K, 1 ≤ K ≤ 10⁵, y luego los números, cada uno de 0 a 10⁹.

## Salida

El número de segmentos.

## Ejemplos

### Ejemplo 1

Entrada:

```
12
2 2 2 2 1 1 2 1 2 1 0 0
```

Salida:

```
3
```

## Solución

Un inicio s fija todo el segmento: N = a[s], M = a[s + 1], y las aristas
son los M pares siguientes, así que hay a lo sumo K candidatos. Un
candidato es válido cuando N ≥ 1, el segmento cabe y sus pares

- no contienen 0 ni pares de números iguales,
- no repiten ningún par no ordenado,
- solo usan números hasta N.

Los pares de un candidato empiezan en posiciones de una misma paridad,
así que las dos primeras condiciones se preparan para ambas paridades de
derecha a izquierda: para cada posición de par p, good(p) es dónde debe
parar la racha de pares aceptables desde p, el primer par malo o la
siguiente aparición de un par ya visto, hallada con una tabla hash de
cada par no ordenado a su posición posterior más cercana. Un candidato
las cumple si su final no pasa de good(s + 2). La tercera condición es un
máximo en un rango, tomado de un árbol de segmentos. Con M = 0 el
registro es solo "N 0". El trabajo es O(K log K).

En el ejemplo "2 1 1 2", "2 1 2 1" y "1 0" son los tres registros
válidos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2162_hashing_segment_tree.cpp](2162_hashing_segment_tree.cpp) | G++ 13.2 x64 | hashing, segment_tree | O(K log K) | AC | 0.031 s | 3988 KB |
| [2162_hashing_segment_tree.go](2162_hashing_segment_tree.go) | Go 1.14 x64 | hashing, segment_tree | O(K log K) | AC | 0.046 s | 8964 KB |
| [2162_hashing_segment_tree.java](2162_hashing_segment_tree.java) | Java 1.8 | hashing, segment_tree | O(K log K) | AC | 0.125 s | 13232 KB |
| [2162_hashing_segment_tree.py](2162_hashing_segment_tree.py) | Python 3.12 x64 | hashing, segment_tree | O(K log K) | AC | 0.687 s | 15264 KB |
| [2162_hashing_segment_tree.rs](2162_hashing_segment_tree.rs) | Rust 1.75 x64 | hashing, segment_tree | O(K log K) | AC | 0.031 s | 5560 KB |
