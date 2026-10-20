# 2169. Orientar un grafo con a lo sumo una arista saliente y tres entrantes

[Timus 2169](https://acm.timus.ru/problem.aspx?space=1&num=2169) · dificultad 1858 · dsu, graphs

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo simple no dirigido tiene N vértices y M aristas. Contar, módulo
10⁹ + 7, las formas de orientar todas las aristas de modo que cada
vértice tenga a lo sumo una arista saliente y a lo sumo tres entrantes.
Los límites son 2 segundos y 256 MB.

## Entrada

N y M, 1 ≤ N ≤ 10⁵, 0 ≤ M ≤ 10⁵, y luego M aristas sin lazos ni
repeticiones.

## Salida

El número de orientaciones módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4
1 2
1 3
1 4
1 5
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
6 4
1 2
1 3
2 3
4 5
```

Salida:

```
4
```

## Solución

Con a lo sumo una arista saliente por vértice, una componente conexa de
V vértices tiene a lo sumo V aristas, así que las componentes se cuentan
por separado y se multiplican.

- **Más aristas que vértices:** no hay orientación, la respuesta es 0.
- **Un árbol (V − 1 aristas):** exactamente un vértice, el sumidero, no
  tiene arista saliente, y todas las aristas apuntan hacia él. El
  sumidero recibe todas sus aristas y cualquier otro vértice todas menos
  una, así que se puede elegir cualquier vértice de grado a lo sumo 3,
  siempre que ningún vértice tenga grado mayor que 4.
- **Un ciclo (V aristas):** todo vértice tiene arista saliente, así que
  el ciclo se orienta de una de dos formas y los árboles colgados
  apuntan hacia él. Cada vértice recibe todas sus aristas menos una, lo
  que solo pide grado a lo sumo 4, y hay 2 formas.

Una unión de conjuntos disjuntos reúne el número de vértices y aristas
de cada componente, y la comprobación de grados recorre todos los
vértices.

En el primer ejemplo el centro tiene grado 4 y no puede ser el
sumidero, así que el sumidero es una de las cuatro hojas.

Esto cuesta O((N + M) α(N)).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2169_dsu_graphs.cpp](2169_dsu_graphs.cpp) | G++ 13.2 x64 | dsu, graphs | O((N + M) α(N)) | AC | 0.046 s | 1784 KB |
| [2169_dsu_graphs.go](2169_dsu_graphs.go) | Go 1.14 x64 | dsu, graphs | O((N + M) α(N)) | AC | 0.046 s | 8108 KB |
| [2169_dsu_graphs.java](2169_dsu_graphs.java) | Java 1.8 | dsu, graphs | O((N + M) α(N)) | AC | 0.125 s | 2352 KB |
| [2169_dsu_graphs.py](2169_dsu_graphs.py) | Python 3.12 x64 | dsu, graphs | O((N + M) α(N)) | AC | 0.406 s | 18680 KB |
| [2169_dsu_graphs.rs](2169_dsu_graphs.rs) | Rust 1.75 x64 | dsu, graphs | O((N + M) α(N)) | AC | 0.046 s | 6876 KB |
