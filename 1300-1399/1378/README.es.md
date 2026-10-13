# 1378. Inteligencia artificial

[Timus 1378](https://acm.timus.ru/problem.aspx?space=1&num=1378) · dificultad 1491 · geometry

Problema original con idea de Alexander Klepinin, preparado por Stanislav Vasiliev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una imagen en blanco y negro de W × H píxeles, 32 ≤ W, H ≤ 1000, muestra
una figura rellena dibujada con un editor gráfico: un círculo, un
cuadrado o un triángulo, de al menos 30 píxeles y sin ángulos de
triángulo menores de 10°. Puede estar girada de cualquier modo. Hay que
imprimir `circle`, `square` o `triangle`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

W y H, luego H líneas de W cifras 0 o 1.

## Salida

`circle`, `square` o `triangle`.

## Ejemplos

### Ejemplo 1

Entrada:

```
32 32
00000000000000000000000000000000
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
01111111111111111111111111111110
00000000000000000000000000000000
```

Salida:

```
square
```

## Solución

Dos números que no dependen del tamaño ni del giro distinguen las
figuras. Se toma el centro de la figura, la distancia r₁ a su píxel más
lejano y el alcance r₂ en perpendicular a esa dirección; a cada uno se
le suma medio píxel, porque un píxel sobresale de su centro. Con A el
número de píxeles:

- A / (π r₁ r₂) vale 1 para cualquier círculo u óvalo, porque r₁ y r₂
  son sus semiejes, pero 2/π ≈ 0,64 para un cuadrado, cuyos r₁ y r₂ son
  sus dos semidiagonales. Por encima de 0,8 es un círculo;
- A / (π r₁²) vale 2/π para un cuadrado y a lo sumo unos 0,41 para
  cualquier triángulo, también el equilátero. Por encima de 0,5 es un
  cuadrado, y si no, un triángulo.

Una figura convexa ocupa un solo tramo de píxeles en cada fila, así que
para r₁ y r₂ solo cuentan los extremos de los tramos. `O(W · H)`.

Detalles a tener en cuenta:

- el primer número es el ancho y el segundo el alto;
- los cuadrados pueden estar girados cualquier ángulo (prueba 03);
- algunos círculos de las pruebas del juez son algo ovalados, y una
  prueba de redondez sola, sin r₂, puede tomarlos por cuadrados
  (prueba 06);
- los triángulos delgados tienen ángulos de hasta 10°.

En figuras aleatorias rasterizadas de 30 a 150 píxeles, la primera
medida fue al menos 0,92 para óvalos cuyo eje corto mide de 0,6 a 1
veces el largo y a lo sumo 0,70 para cuadrados girados, y la segunda al
menos 0,60 para cuadrados y a lo sumo 0,38 para triángulos con todos sus
ángulos de al menos 10°. Otras 600 figuras así se reconocieron todas.

## Notas por lenguaje

- Python une todas las cifras en una cadena y la corta en filas, así que
  sirven filas con o sin espacios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1378_geometry.cpp](1378_geometry.cpp) | G++ 13.2 x64 | geometry | O(W·H) | AC | 0.031 s | 224 KB |
| [1378_geometry.go](1378_geometry.go) | Go 1.14 x64 | geometry | O(W·H) | AC | 0.031 s | 1260 KB |
| [1378_geometry.java](1378_geometry.java) | Java 1.8 | geometry | O(W·H) | AC | 0.109 s | 640 KB |
| [1378_geometry.py](1378_geometry.py) | Python 3.12 x64 | geometry | O(W·H) | AC | 0.093 s | 3384 KB |
| [1378_geometry.rs](1378_geometry.rs) | Rust 1.75 x64 | geometry | O(W·H) | AC | 0.015 s | 3112 KB |
