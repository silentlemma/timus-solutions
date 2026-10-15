# 1664. Transporte por oleoductos

[Timus 1664](https://acm.timus.ru/problem.aspx?space=1&num=1664) · dificultad 1965 · graphs

Problema original de Artem Melentyev, del Ural SU Contest en el campus de invierno de Petrozavodsk, enero de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N estaciones en el plano y M oleoductos rectos unen pares de ellas;
dos oleoductos solo se tocan en una estación común. Cada uno lleva a lo
sumo su capacidad, en cualquier sentido. La estación 1 tiene la menor x
y la estación N la mayor. Hay que hallar el flujo máximo de la estación
1 a la N y un plan: para cada oleoducto, el sentido y la cantidad.

## Entrada

N (2 ≤ N ≤ 10000) y las coordenadas de las estaciones (enteros de valor
absoluto a lo sumo 10⁸), luego M y los oleoductos como dos estaciones y
una capacidad de 1 a 10⁸. El flujo máximo es positivo y a lo sumo 2·10⁹.

## Salida

El flujo máximo y luego M líneas «A B C»: fluyen C unidades de A a B,
con C ≥ 0 y cada oleoducto exactamente una vez.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 0
1 1
2 0
2
1 2 2
2 3 1
```

Salida:

```
1
1 2 1
2 3 1
```

## Solución

Los oleoductos forman un grafo plano con la fuente y el sumidero en la
cara exterior, así que un flujo máximo sale de caminos mínimos en el
grafo dual. Se añade una arista extra que sale de la fuente hacia la
izquierda, rodea todo por fuera y entra en el sumidero por la derecha;
divide la cara exterior en dos, una superior y una inferior. Cada corte
entre fuente y sumidero es un camino en el dual de una de esas caras a
la otra, así que el flujo máximo es el camino más corto de ese tipo con
las capacidades como longitudes.

Las caras salen de ordenar los oleoductos alrededor de cada estación por
ángulo: tras llegar a una estación por un oleoducto, la cara sigue por el
siguiente oleoducto en sentido horario. Dijkstra desde una de las dos
da una distancia d a cada cara, y el flujo por un oleoducto desde su cara
izquierda a la derecha es d(derecha) − d(izquierda). Estas diferencias
nunca superan la capacidad, se cancelan alrededor de cada estación de
tránsito y en la fuente suman la distancia mínima. `O(M log M)`.

Detalles a tener en cuenta:

- con coordenadas de hasta 10⁸ dos direcciones pueden diferir menos de
  lo que distingue un double (prueba 02), así que los ángulos se comparan
  exactamente con productos cruzados enteros; Python ordena primero por
  ángulos en coma flotante y luego corrige con exactitud los vecinos casi
  iguales;
- las partes del mapa que la fuente no alcanza tienen caras fuera del
  alcance de Dijkstra; sus oleoductos no llevan flujo (prueba 04);
- el sentido de la arista extra fija el signo de todas las diferencias,
  así que la solución invierte el plan si el petróleo entrara en la
  fuente.

Un comprobador verifica capacidad, conservación y total de los flujos, y
los totales coinciden con una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1664_graphs.cpp](1664_graphs.cpp) | G++ 13.2 x64 | graphs | O(M log M) | AC | 0.078 s | 5244 KB |
| [1664_graphs.go](1664_graphs.go) | Go 1.14 x64 | graphs | O(M log M) | AC | 0.062 s | 8164 KB |
| [1664_graphs.java](1664_graphs.java) | Java 1.8 | graphs | O(M log M) | AC | 0.187 s | 9512 KB |
| [1664_graphs.py](1664_graphs.py) | Python 3.12 x64 | graphs | O(M log M) | AC | 0.296 s | 33124 KB |
| [1664_graphs.rs](1664_graphs.rs) | Rust 1.75 x64 | graphs | O(M log M) | AC | 0.031 s | 8920 KB |
