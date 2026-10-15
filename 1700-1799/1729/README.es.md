# 1729. El cofre del hombre muerto

[Timus 1729](https://acm.timus.ru/problem.aspx?space=1&num=1729) · dificultad 630 · geometry

Problema original de Fedor Fominykh (preparado por Denis Dublennykh), del Concurso Regional por Equipos de Programación de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Jack está en el centro de una isla redonda de radio r cubierta de
selva, así que solo ve el mar desde la orilla. Su bote está junto a la
orilla en algún lugar, y se ve desde los puntos de la orilla a lo sumo
a a grados del punto de la orilla más cercano a él. Hallar la longitud
mínima de una ruta que le permita ver el bote en el peor caso.

## Entrada

r y a (1 ≤ r ≤ 1000, 0.001 ≤ a ≤ 45), con a lo sumo tres cifras tras
el punto decimal.

## Salida

La distancia en el peor caso para la mejor ruta, con al menos seis
cifras tras el punto decimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
1.000 30.000
```

Salida:

```
6.0000000
```

## Solución

Llegar a la orilla cuesta r. Desde ahí, cada punto de la orilla que
Jack visita le muestra un arco de 2a grados centrado en él, y en el
peor caso el bote solo se ve desde el último. Entre dos puntos de la
orilla el camino más corto es la cuerda; puntos consecutivos pueden
distar a lo sumo 2a, mientras que el barrido del primero al último debe
cubrir al menos 360 − 2a para que los arcos se cierren alrededor de la isla.

Así la ruta es r más cuerdas cuyos ángulos suman 360 − 2a, cada uno a
lo sumo 2a. Una cuerda de ángulo θ mide 2r·sin(θ/2), que crece más
despacio que θ, así que con el total fijo la suma es mínima cuando los
trozos son lo más desiguales posible: k − 1 cuerdas completas de 2a,
con k = ⌊180/a⌋, y una cuerda corta para el resto, 360 − 2ka grados,
vacía cuando 2a divide a 360. `O(1)`.

En el ejemplo a = 30: seis puntos separados 60°, cinco cuerdas de
longitud r, así que la respuesta es 1 + 5 = 6.

Trampas:

- ⌊180/a⌋ calculado en coma flotante puede salir uno menos; las
  soluciones leen a exactamente en milésimas de grado. Ese error, de
  todos modos, daría la misma longitud, porque la cuerda completa que
  falta vuelve como una cuerda corta de 2a;
- para a = 0.001 la ruta tiene 179 999 cuerdas, así que la suma es un
  producto y no un bucle sobre ellas.

Las respuestas coinciden con una implementación aceptada independiente
en las siete cifras impresas en 300 casos aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1729_geometry.cpp](1729_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 468 KB |
| [1729_geometry.go](1729_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1100 KB |
| [1729_geometry.java](1729_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 1840 KB |
| [1729_geometry.py](1729_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 520 KB |
| [1729_geometry.rs](1729_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 260 KB |
