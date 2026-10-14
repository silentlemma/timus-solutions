# 1570. Cenando en las alturas

[Timus 1570](https://acm.timus.ru/problem.aspx?space=1&num=1570) · dificultad 896 · dp

Problema original de Vladimir Yakovlev, del XII Campeonato de Programación de la Universidad Estatal de los Urales, 6 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un menú tiene N ≤ 100 platos, cada uno con un precio de 1 … 10000
rublos y una saciedad de 0.1 a 10 (con como mucho tres cifras tras el
punto), el número de personas a las que alimenta. Hay que pedir
cualquier número de raciones de cualquier plato para que las saciedades
sumen al menos M ≤ 20 al menor coste, y entre esos pedidos tomar uno
con el mayor número de platos distintos. Se imprimen el coste y los
platos con su número de raciones.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, y luego cada plato con su nombre, su precio y su saciedad.

## Salida

El coste y luego un plato y su número de raciones por línea. Se acepta
cualquier pedido óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 6
pizza 320 2.4
turkey 1050 3.5
lasagna 150 0.9
pasta 75 0.45
```

Salida:

```
865
pizza 2
lasagna 1
pasta 1
```

## Solución

La saciedad se lee exacta en milésimas, así que el objetivo es
T = 1000·M, y cualquier total de T o más cuenta como T. Una mochila no
acotada sobre esos totales guarda para cada total el menor coste y, en
caso de empate, el mayor número de platos distintos, juntos en un solo
número coste·128 − platos, donde menos es mejor.

El número de platos distintos no se suma por raciones, así que los
platos se añaden de uno en uno. Para cada plato, los pedidos que lo
incluyen empiezan con una primera ración sobre un pedido sin él, que
cuenta un plato más, y luego crecen con más raciones de él, que no
cuentan ninguno; se guarda el mejor de estos y de los pedidos sin el
plato. Cada paso anota de dónde viene, así que el pedido se reconstruye
hacia atrás plato a plato desde el total T. Esto tarda O(N·T), unos
2·10⁶ pasos. Los resultados se contrastaron con probar todos los
números de raciones en 300 menús pequeños aleatorios.

Detalles a tener en cuenta:

- un pedido más barato puede pasarse de M, así que los totales por
  encima de T deben seguir siendo posibles (prueba 03: 200 raciones
  pequeñas);
- el empate en coste se resuelve por el número de platos distintos, no
  por el de raciones (el ejemplo y las pruebas 04, 05);
- la saciedad puede escribirse sin punto (prueba 04);
- Python se ejecuta con PyPy: las pruebas más grandes tardan unos 0.8 s
  con CPython frente a un límite de 1 s, y unos 0.1 s con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1570_dp.cpp](1570_dp.cpp) | G++ 13.2 x64 | dp | O(N M) | AC | 0.031 s | 12116 KB |
| [1570_dp.go](1570_dp.go) | Go 1.14 x64 | dp | O(N M) | AC | 0.031 s | 14396 KB |
| [1570_dp.java](1570_dp.java) | Java 1.8 | dp | O(N M) | AC | 0.140 s | 13196 KB |
| [1570_dp.py](1570_dp.py) | PyPy 3.10 x64 | dp | O(N M) | AC | 0.312 s | 18672 KB |
| [1570_dp.rs](1570_dp.rs) | Rust 1.75 x64 | dp | O(N M) | AC | 0.062 s | 12176 KB |
