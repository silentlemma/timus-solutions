# 1378. Inteligencia artificial

[Timus 1378](https://acm.timus.ru/problem.aspx?space=1&num=1378) · dificultad 1448 · geometry

Problema original con idea de Alexander Klepinin, preparado por Stanislav Vasiliev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una imagen en blanco y negro de W × H píxeles, 32 ≤ W, H ≤ 1000, muestra
una figura rellena dibujada con un editor gráfico:
un círculo, un cuadrado o un triángulo. Su lado más largo o diámetro
mide al menos 30 píxeles y ningún ángulo del triángulo es menor de 10°.
Puede estar girada de cualquier modo. Hay que imprimir `circle`,
`square` o `triangle`.

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

Dos cocientes de áreas no dependen del tamaño ni del giro en figuras
ideales, y lo cumplen aproximadamente tras rasterizar. Se toma el
centroide, la distancia r₁ al centro del píxel más lejano y el alcance
máximo r₂ en perpendicular a esa dirección. Con A el área:

- Para un círculo o una elipse ideal, A / (π r₁ r₂) vale 1, porque r₁
  y r₂ son sus semiejes; para un cuadrado vale 2/π ≈ 0,64, porque son
  sus dos semidiagonales;
- para un cuadrado ideal, A / (π r₁²) vale 2/π, y para cualquier
  triángulo es a lo sumo unos 0,4135, valor que alcanza el equilátero.

En el código, A es el número de píxeles; se suma medio píxel a ambas
distancias para aproximar su extensión. Primer cociente mayor de 0,8:
`circle`; si no, segundo mayor de 0,5: `square`; en otro caso, `triangle`.

Una figura convexa ocupa un solo tramo de píxeles en cada fila, así que
para r₁ y r₂ solo cuentan los extremos de los tramos. `O(W · H)`.

Detalles a tener en cuenta:

- el primer número es el ancho y el segundo el alto;
- los cuadrados pueden estar girados cualquier ángulo (prueba 03);
- las pruebas locales incluyen figuras ovaladas con respuesta `circle`,
  y una prueba de redondez sola, sin r₂, puede tomarlas por cuadrados
  (prueba 06);
- los triángulos delgados pueden tener ángulos de solo 10°.

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
