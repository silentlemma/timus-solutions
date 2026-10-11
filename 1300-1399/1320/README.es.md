# 1320. Descomposición de un grafo

[Timus 1320](https://acm.timus.ru/problem.aspx?space=1&num=1320) · dificultad 283 · dsu

Problema original con idea de Alexander Petrov, preparado por Alexander Petrov y Leonid Volkov, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo simple tiene un número par de aristas, de 2 a 1050, con
vértices numerados de 1 a 1000. Hay que decidir si sus aristas se
pueden repartir en pares de aristas adyacentes, es decir, con un
vértice común.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

Las aristas, cada una como un par de números de vértice, hasta el final
de la entrada. No hay lazos ni aristas repetidas.

## Salida

1 si ese reparto existe, si no 0.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2
2 3
3 1
1 10
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
1 2
2 3
3 1
4 10
```

Salida:

```
0
```

## Solución

Dos aristas adyacentes siempre están en la misma componente conexa, así
que cada componente necesita un número par de aristas. Eso también
basta: un grafo conexo con un número par de aristas siempre se puede
repartir. Se toma un árbol de búsqueda en profundidad y se tratan los
vértices desde los más profundos hacia arriba. En un vértice v, las
aristas libres en v, salvo la que va al padre, se emparejan entre sí;
si sobra una, se empareja con la arista al padre, y si no, la arista al
padre queda libre para el padre. Ningún vértice salvo la raíz deja
aristas libres por debajo, y en la raíz las aristas libres se emparejan
entre sí, lo que es posible porque el total es par.

Así que la respuesta solo necesita el número de aristas de cada
componente. Una unión de conjuntos disjuntos sobre los vértices lo
guarda en cada raíz: al unir dos componentes se suman sus cuentas, y
cada arista suma uno. Al final se comprueba que cada raíz tenga una
cuenta par. Aquí V es el rango de vértices y M el número de aristas.
Las raíces se unen sin equilibrar por rango o tamaño, por lo que la
división de caminos a la mitad da una cota total segura de
`O(V + M log V)`, incluidas la inicialización y la comprobación final
de las raíces.

Detalles a tener en cuenta:

- el grafo entero siempre tiene un número par de aristas, pero una
  componente puede no tenerlo: un triángulo y una arista aparte dan 0
  (prueba 02, y también dos triángulos separados en la prueba 06);
- no se da el número de aristas, la entrada simplemente termina;
- dos triángulos con un vértice común forman una sola componente de
  seis aristas y se pueden repartir (prueba 07).

La regla se comparó con una búsqueda sobre todos los emparejamientos en
487 grafos aleatorios de hasta 14 aristas.

## Notas por lenguaje

- Las cinco soluciones usan la misma unión de conjuntos disjuntos, en
  la que cada búsqueda hace saltar cada vértice a su abuelo (división
  de caminos a la mitad).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1320_dsu.cpp](1320_dsu.cpp) | G++ 13.2 x64 | dsu | O(V + M log V) | AC | 0.015 s | 184 KB |
| [1320_dsu.go](1320_dsu.go) | Go 1.14 x64 | dsu | O(V + M log V) | AC | 0.015 s | 1112 KB |
| [1320_dsu.java](1320_dsu.java) | Java 1.8 | dsu | O(V + M log V) | AC | 0.109 s | 420 KB |
| [1320_dsu.py](1320_dsu.py) | Python 3.12 x64 | dsu | O(V + M log V) | AC | 0.093 s | 656 KB |
| [1320_dsu.rs](1320_dsu.rs) | Rust 1.75 x64 | dsu | O(V + M log V) | AC | 0.015 s | 264 KB |
