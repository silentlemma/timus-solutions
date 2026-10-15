# 1733. Tecnología olvidada

[Timus 1733](https://acm.timus.ru/problem.aspx?space=1&num=1733) · dificultad 4267 · geometry

Problema original de Pavel Atnashev (idea de Alex Samsonov), del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un libro rectangular está sobre un paño, y sobre el libro hay un disco
con el centro dentro del libro o en su borde. Un ratón corre solo por el
paño, así que no puede cruzar el libro, y quiere llegar a un punto del
disco que cuelgue sobre el paño, estrictamente fuera del libro. Hallar
la longitud del camino más corto.

## Entrada

Las cuatro esquinas del libro en sentido antihorario, luego el centro y
el radio del disco (radio al menos 1) y luego el ratón. Todos los
números son enteros de valor absoluto hasta 1000. El ratón no toca ni
el libro ni el disco, y existe un camino.

## Salida

La longitud del camino más corto, con un error de a lo sumo 10⁻⁵.

## Ejemplos

### Ejemplo 1

Entrada:

```
-4 -3 8 6 5 10 -7 1
1 7 5
7 -1
```

Salida:

```
12.07107
```

## Solución

El objetivo es la parte del disco fuera del libro, junto con su borde.
Un camino más corto que rodea un obstáculo convexo va en línea recta
entre el ratón y esquinas del libro, así que es un tramo recto desde el
ratón o desde una esquina hasta el objetivo, tras el camino más corto a
esa esquina. Dijkstra sobre el ratón y las cuatro esquinas da esos
caminos: el ratón se une a cada esquina que ve, y cada esquina a sus
dos vecinas.

Desde un punto s, se prueban estos candidatos del objetivo:

- el punto de la circunferencia en el rayo del centro hacia s, si está
  fuera del libro y s lo ve;
- el punto más cercano de la cuerda de un lado dentro del disco, si s
  está del lado exterior de ese lado o en su recta; entonces el lado se
  ve entero.

Los demás puntos del objetivo no importan. La distancia a lo largo de
la circunferencia tiene un solo mínimo, así que en un arco es el punto
del rayo o un extremo del arco, que también es extremo de una cuerda; a
lo largo de una cuerda la distancia es convexa. Si el mejor punto
quedara cortado por el borde de lo que s ve, el camino hasta él pasaría
por una esquina, y esa esquina como punto de partida da al menos lo
mismo. La respuesta es la menor suma del camino más corto hasta un
punto y la distancia de este a su candidato más cercano.
`O(1)`.

En el ejemplo el ratón corre 7.071 hasta la esquina (8, 6) y luego 5 a
lo largo del lado hasta la esquina (5, 10), que está en la
circunferencia.

Trampas:

- un lado que toca la circunferencia por dentro da un solo punto que no
  está estrictamente fuera del libro, así que se saltan las cuerdas de
  longitud cero;
- una esquina puede estar dentro del disco, y entonces es ella misma un
  punto del objetivo;
- el ratón puede estar en la recta de un lado, así que las pruebas de
  lado admiten una pequeña tolerancia;
- la parte del disco a la vista no siempre es la más cercana: rodear
  una esquina hacia el otro lado del libro puede ser más corto, así que
  se prueban todas las esquinas aunque el ratón vea el objetivo.

Las respuestas coinciden con una búsqueda sobre una muestra densa del
objetivo, con los segmentos comprobados punto a punto, hasta la
precisión de la muestra en 210 casos aleatorios. Una implementación
aceptada independiente coincide en 209 de ellos; en el otro, la prueba
07, se detiene en la parte del disco a la vista, 1068.837, mientras que
el camino rodeando la esquina (−2, 16) mide 1060.690, como confirma la
muestra.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1733_geometry.cpp](1733_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 460 KB |
| [1733_geometry.go](1733_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1120 KB |
| [1733_geometry.java](1733_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1892 KB |
| [1733_geometry.py](1733_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 1140 KB |
| [1733_geometry.rs](1733_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 280 KB |
