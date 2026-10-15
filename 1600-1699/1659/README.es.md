# 1659. Triángulos regulares

[Timus 1659](https://acm.timus.ru/problem.aspx?space=1&num=1659) · dificultad 650 · geometry

Problema original de Vladimir Yakovlev, del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da un triángulo regular. Hay que marcar seis puntos más, tres
estrictamente dentro y tres estrictamente fuera, de modo que los nueve
puntos sean vértices de al menos nueve triángulos regulares, incluido el
dado. Dos cualesquiera de los nueve puntos deben distar al menos 1, cada
punto nuevo debe estar a al menos 0,1 de los lados del triángulo, y los
lados se consideran iguales si difieren en a lo sumo 10⁻⁶.

## Entrada

Tres líneas con los vértices del triángulo. Las coordenadas valen a lo
sumo 100 en valor absoluto y los lados miden al menos 10.

## Salida

Los tres puntos interiores y luego los tres exteriores, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 30
-25.9807621135 -15
25.9807621135 -15
```

Salida:

```
0.0000000000 15.0000000000
-12.9903810567 -7.5000000000
12.9903810567 -7.5000000000
0.0000000000 -45.0000000000
38.9711431703 22.5000000000
-38.9711431703 22.5000000000
```

Se acepta cualquier respuesta válida. La respuesta impresa en el
enunciado para este ejemplo es incorrecta a propósito (sus puntos forman
solo tres triángulos regulares), así que arriba aparece la que imprime
esta solución.

## Solución

Se coloca el centro g del triángulo en el origen y se llaman a, b y c los
vectores hacia los vértices A, B y C; tienen la misma longitud, forman
120° entre sí y a + b + c = 0. Los puntos interiores son t·a, t·b, t·c y
los exteriores −s·a, −s·b, −s·c. Cada terna es por sí sola un triángulo
regular, y con el dado suman tres.

Los otros seis salen de ternas como A, el punto interior t·b y el
exterior −s·c. Girar el plano 60° en el sentido adecuado lleva a en −c y
b en −a, así que lleva el lado de t·b a A, es decir a − t·b, a −c + t·a.
Ese vector es igual a −s·c − t·b exactamente cuando s = 1 + t (usando
a + b = −c), y con esa elección la terna es regular. Cada vértice se
combina así con sus dos vecinos, lo que da seis triángulos y nueve en
total.

La solución toma t = 1/2 y s = 3/2. Con lados de al menos 10, todas las
distancias quedan holgadamente por encima de los límites: el triángulo
interior tiene lado de al menos 5, un punto interior está a un cuarto del
radio circunscrito (al menos 1,44) del lado más cercano, y uno exterior
queda un radio entero más allá del lado más cercano. `O(1)`.

Detalles a tener en cuenta:

- los vértices pueden venir en cualquier orden, horario o antihorario; a
  la construcción le da igual;
- los puntos exteriores de un triángulo grande quedan muy fuera del
  cuadrado de la entrada, cosa que el enunciado permite;
- la respuesta no se compara sino que se verifica: el comprobador cuenta
  los triángulos regulares y revisa todas las distancias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1659_geometry.cpp](1659_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1659_geometry.go](1659_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1124 KB |
| [1659_geometry.java](1659_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 1084 KB |
| [1659_geometry.py](1659_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.062 s | 480 KB |
| [1659_geometry.rs](1659_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 268 KB |
