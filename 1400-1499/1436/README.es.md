# 1436. Valla publicitaria

[Timus 1436](https://acm.timus.ru/problem.aspx?space=1&num=1436) · dificultad 830 · geometry

Problema original de Alexey Lakhtin, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La carretera es el eje x y una valla publicitaria es el segmento entre
dos puntos enteros distintos con coordenadas de −1000 a 1000. Hay que
hallar el mayor ángulo, en radianes con 6 cifras tras el punto, bajo el
que se ve la valla desde un punto de la carretera.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

x1, y1, x2, y2, uno por línea.

## Salida

El mayor ángulo.

## Ejemplos

### Ejemplo 1

Entrada:

```
100
200
300
400
```

Salida:

```
0.785398
```

### Ejemplo 2

Entrada:

```
123
456
789
-10
```

Salida:

```
3.141593
```

### Ejemplo 3

Entrada:

```
-800
1
800
1
```

Salida:

```
3.139093
```

### Ejemplo 4

Entrada:

```
9
7
3
0
```

Salida:

```
3.141593
```

## Solución

Si la valla cruza la carretera o la toca, uno puede ponerse sobre ella
y la respuesta es π, como muestran los ejemplos para un cruce y para un
extremo en la carretera. Una nota del foro dice que una valla vertical
apoyada en la carretera da π/2, y las soluciones la siguen.

Si no, se reflejan ambos extremos al mismo lado, y > 0. Los puntos desde
los que AB se ve bajo un ángulo fijo están en circunferencias que pasan
por A y B, y el mayor ángulo corresponde a la menor de ellas que aún
llega a la carretera, la tangente a ella. Si AB corta la recta de la
carretera en Q, el punto de tangencia P cumple QP² = QA·QB (la potencia
del punto Q), así que P está a distancia √(QA·QB) de Q hacia un lado o
hacia el otro; se prueban ambos candidatos. Si AB es paralela a la
carretera, P está bajo su punto medio. El ángulo en P sale de atan2 del
producto vectorial y el escalar. `O(1)`.

Detalles a tener en cuenta:

- el mejor punto puede estar más allá de ambos extremos de la valla
  (prueba 08);
- una valla bajo la carretera es igual a su reflejo (pruebas 09, 14);
- una valla tendida sobre la carretera da π (prueba 10).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1436_geometry.cpp](1436_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 220 KB |
| [1436_geometry.go](1436_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1084 KB |
| [1436_geometry.java](1436_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1828 KB |
| [1436_geometry.py](1436_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 572 KB |
| [1436_geometry.rs](1436_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 244 KB |
