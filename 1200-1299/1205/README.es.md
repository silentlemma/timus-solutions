# 1205. La forma más rápida de cruzar la ciudad a pie y en metro

[Timus 1205](https://acm.timus.ru/problem.aspx?space=1&num=1205) · dificultad 235 · graphs

Problema original de Alexander Klepinin, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se puede caminar a cualquier sitio a una velocidad o ir en metro a una
velocidad no menor, entre `2 ≤ N ≤ 200` estaciones unidas por hasta 400
tramos rectos de doble sentido; solo se sube, se baja y se cambia de
tren en las estaciones, sin coste de tiempo. Hay que hallar el camino
más rápido del punto A al punto B y las estaciones por las que pasa.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las velocidades a pie y en metro; `N` y las coordenadas de las
estaciones; los tramos como pares de números de estación, terminados en
`0 0`; y luego A y B.

## Salida

El menor tiempo, con precisión `10⁻⁶`, y luego el número de estaciones
de la ruta seguido de las estaciones en el orden en que se visitan.

## Evaluación

Varias rutas pueden tardar lo mismo, así que se acepta cualquiera si su
tiempo impreso coincide con el de la propia ruta (a pie de A a la
primera estación, en tren entre estaciones consecutivas unidas, a pie
entre las no unidas y a pie de la última estación a B) y si ese tiempo
es el menor.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 100
4
0 0
1 0
9 0
9 9
1 2
1 3
2 4
0 0
10 10
10 0
```

Salida:

```
2.6346295
4 4 2 1 3
```

## Solución

Se forma un grafo completo sobre las estaciones, A y B: entre dos puntos
cualesquiera el coste es el tiempo a pie, salvo entre estaciones unidas,
donde es el tiempo en tren; por la misma recta el tren nunca es más
lento. El algoritmo de Dijkstra sobre este grafo denso de `N + 2` nodos,
eligiendo el siguiente nodo con un recorrido lineal, da el menor tiempo,
y los predecesores dan la ruta; sus estaciones son la ruta sin A ni B.
`O(N²)`.

Detalles a tener en cuenta:

- la ruta puede estar vacía: con velocidades iguales, o cuando el metro
  no ayuda, la respuesta es ir a pie en línea recta e imprimir `0`
  estaciones;
- caminar entre dos estaciones está permitido y puede formar parte de la
  mejor ruta, por ejemplo para cambiar a una línea cercana;
- la lista de tramos puede estar vacía, con `0 0` justo después de las
  estaciones.

Las rutas se compararon con una solución escrita aparte en 200 ciudades
aleatorias y en todas las pruebas, con el verificador en ambos sentidos.

## Notas por lenguaje

- Todos los lenguajes ejecutan el mismo Dijkstra cuadrático sobre una
  matriz de adyacencia e imprimen diez decimales; Java formatea el
  tiempo con `Locale.US`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1205_graphs.cpp](1205_graphs.cpp) | G++ 13.2 x64 | graphs | O(N²) | AC | 0.015 s | 256 KB |
| [1205_graphs.go](1205_graphs.go) | Go 1.14 x64 | graphs | O(N²) | AC | 0.031 s | 1208 KB |
| [1205_graphs.java](1205_graphs.java) | Java 1.8 | graphs | O(N²) | AC | 0.125 s | 1416 KB |
| [1205_graphs.py](1205_graphs.py) | Python 3.12 x64 | graphs | O(N²) | AC | 0.062 s | 1012 KB |
| [1205_graphs.rs](1205_graphs.rs) | Rust 1.75 x64 | graphs | O(N²) | AC | 0.046 s | 344 KB |
