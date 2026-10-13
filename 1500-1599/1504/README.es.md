# 1504. Buenos modales

[Timus 1504](https://acm.timus.ru/problem.aspx?space=1&num=1504) · dificultad 2173 · geometry

Problema original de Stanislav Vasiliev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

K trozos de tarta (2 ≤ K ≤ 1000) están en puntos distintos de una mesa
redonda de radio R (1 ≤ R ≤ 100) centrada en el origen, cada uno con un
peso de 1 a 10000 gramos. Quien se sienta en un punto del borde toma
con educación el trozo más cercano, el más pesado si varios están igual
de cerca. Hay que hallar un asiento en el borde que consiga el trozo
más pesado posible.

Límite de tiempo: 1.5 segundos. Límite de memoria: 64 MB.

## Entrada

R y K, y luego K líneas con las coordenadas de un trozo (números
reales) y su peso.

## Salida

Las dos coordenadas del asiento, con precisión de 7 cifras. Se acepta
cualquier asiento óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 3
1 -1 100
2 2 200
-2.5 -2.56 1
```

Salida:

```
6 8
```

## Solución

Los puntos más cercanos al trozo i que a cualquier otro forman su celda
de Voronoi: la intersección de los semiplanos limitados por las
mediatrices, un polígono convexo que contiene el trozo. Un asiento
consigue el trozo i cuando está en esa celda, así que la respuesta es
el trozo más pesado cuya celda llega al borde. El trozo está en la mesa
y la celda es convexa, por lo que la celda llega al borde justo cuando
su vértice más lejano del centro está a distancia R o más.

Se prueban los trozos del más pesado hacia abajo. Para cada uno se
parte de un cuadrado alrededor de la mesa y se corta con las mediatrices
con los demás trozos, de los más cercanos a los más lejanos. Se falla en
cuanto todos los vértices quedan dentro de la mesa, y se deja de cortar
cuando el siguiente trozo está a más del doble del alcance de la celda,
porque su mediatriz ya no la toca. El asiento está donde el segmento del
trozo al vértice más lejano cruza el borde. Cada corte es lineal en el
tamaño de la celda, y las celdas de los trozos que fallan se encogen
dentro de la mesa tras unos pocos vecinos cercanos, así que el trabajo
ronda `O(K² log K)` en el peor caso.

Detalles a tener en cuenta:

- la celda puede tocar el borde en un solo punto, donde el asiento está
  a la misma distancia de varios trozos y se toma el más pesado, así
  que la comprobación necesita una pequeña tolerancia (prueba 02);
- una celda que no llega al borde por unas centésimas debe fallar
  (prueba 07);
- el trozo más pesado puede quedar rodeado de otros más ligeros
  (prueba 05, gen2);
- un trozo puede estar justo en el borde (prueba 04);
- con pesos iguales cualquier asiento es correcto (prueba 06);
- hay muchos asientos correctos, así que las pruebas usan un comprobador
  (todas las pruebas);
- cortar cada celda pesada con todos los trozos lleva unos 3 segundos en
  Python; las paradas tempranas lo bajan a unas décimas (gen2, gen6).

## Notas por lenguaje

- Python se ejecuta con PyPy: CPython excede el límite de 1,5 s en la
  prueba 32 del juez, y PyPy tarda unos 1,1 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1504_geometry.cpp](1504_geometry.cpp) | G++ 13.2 x64 | geometry | O(K^2 log K) | AC | 0.359 s | 292 KB |
| [1504_geometry.go](1504_geometry.go) | Go 1.14 x64 | geometry | O(K^2 log K) | AC | 0.546 s | 7708 KB |
| [1504_geometry.java](1504_geometry.java) | Java 1.8 | geometry | O(K^2 log K) | AC | 0.343 s | 6796 KB |
| [1504_geometry.py](1504_geometry.py) | PyPy 3.10 x64 | geometry | O(K^2 log K) | AC | 1.125 s | 9332 KB |
| [1504_geometry.rs](1504_geometry.rs) | Rust 1.75 x64 | geometry | O(K^2 log K) | AC | 0.109 s | 1288 KB |
