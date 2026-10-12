# 1341. Aparato

[Timus 1341](https://acm.timus.ru/problem.aspx?space=1&num=1341) · dificultad 1130 · geometry

Problema original de Stanislav Vasiliev, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un aparato vuela a una distancia fija de 6400 km del centro de la
Tierra. Partiendo de la latitud W y la longitud L, recorre un
«cuadrado»: una distancia dada hacia el norte, la misma hacia el este,
luego hacia el sur y hacia el oeste. Nunca llega a un polo. Hay que
imprimir la latitud y la longitud donde termina, con tres cifras tras el
punto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

W, L y el lado del cuadrado en kilómetros, uno por línea.

## Salida

La latitud y la longitud finales, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
56.846841
53.36673
1124.427
```

Salida:

```
56.847
60.631
```

## Solución

El norte y el sur van por meridianos y cambian la latitud en el mismo
ángulo a = lado / 6400 en radianes, así que el aparato vuelve a la
latitud W. El este y el oeste van por paralelos: a la latitud φ un
paralelo tiene radio 6400 · cos φ, así que un vuelo de la longitud del
lado gira la longitud en a / cos φ. El tramo hacia el este vuela por el
paralelo de W + a y el tramo hacia el oeste por el de W. Así la longitud
cambia en a / cos(W + a) − a / cos(W), pasado a grados y devuelto a
(−180, 180]. `O(1)`.

En el hemisferio norte el tramo hacia el este está más cerca del polo y
gira más, así que el aparato acaba al este del inicio; en el sur el
tramo hacia el este está más cerca del ecuador y el aparato acaba al
oeste.

Detalles a tener en cuenta:

- la longitud final puede cruzar el meridiano 180 en cualquier sentido
  (pruebas 04 y 05);
- un inicio en el hemisferio sur desplaza el aparato hacia el oeste
  (prueba 02);
- los valores pequeños no deben imprimirse como `-0.000`.

## Notas por lenguaje

- Las cinco soluciones usan la misma fórmula.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1341_geometry.cpp](1341_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1341_geometry.go](1341_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1096 KB |
| [1341_geometry.java](1341_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1944 KB |
| [1341_geometry.py](1341_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 416 KB |
| [1341_geometry.rs](1341_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 264 KB |
