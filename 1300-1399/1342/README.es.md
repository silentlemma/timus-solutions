# 1342. Empresa

[Timus 1342](https://acm.timus.ru/problem.aspx?space=1&num=1342) · dificultad 735 · dp

Problema original de Magaz Asanov y Pavel Egorov, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una empresa tiene N ≤ 1000 fábricas y necesita M ≤ 1000 escobas. La
fábrica i puede hacer de 0 a K_i ≤ 100 escobas al día; su primera
escoba cuesta P_i, la K_i-ésima cuesta Q_i, y el precio de la j-ésima
cambia linealmente entre ambas. Hay que hallar el menor coste total de
M escobas, con dos cifras tras el punto. Si entre todas las fábricas no
se llega a M escobas, primero se imprime la mayor cantidad V que pueden
hacer y luego el menor coste de V escobas.

Límite de tiempo: 2,5 segundos. Límite de memoria: 64 MB.

## Entrada

N y M, luego N líneas con K_i, P_i y Q_i.

## Salida

`Maximum possible amount: V` si no se llega a M, y luego
`Minimum possible cost: C`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 10
6 20 15
100 100 100
```

Salida:

```
Minimum possible cost: 505.00
```

### Ejemplo 2

Entrada:

```
2 10
5 30 14
1 20 20
```

Salida:

```
Maximum possible amount: 6
Minimum possible cost: 130.00
```

## Solución

La j-ésima escoba de una fábrica cuesta P + (j − 1) · (Q − P) / (K − 1),
así que x escobas cuestan x · P + (Q − P) / (K − 1) · x (x − 1) / 2. El
objetivo es T = min(M, ΣK). Cuando los precios bajan, una fábrica solo
compensa si hace muchas escobas, y cuando suben solo son baratas las
primeras. Con ambos tipos mezclados ningún orden voraz funciona, así que
es una mochila: best[j] es el menor coste de exactamente j escobas con
las fábricas vistas hasta ahora. Una fábrica nueva la actualiza probando
cada cantidad x de 0 a K para cada j hasta T. Son como mucho
N · T · K = 10⁸ pasos sencillos. `O(N · M · K)`.

Detalles a tener en cuenta:

- una fábrica de precios decrecientes puede ganar a otra que parece más
  barata solo si trabaja a pleno (prueba 04);
- cuando la capacidad total no alcanza, se imprimen las dos líneas y el
  coste es el de V escobas (pruebas 02 y 06);
- una fábrica con K = 1 tiene una sola escoba de precio P.

Los costes se compararon con probar todos los repartos del pedido entre
hasta 3 fábricas en 400 casos aleatorios.

## Notas por lenguaje

- CPython necesita unos 4 segundos en el caso más grande, por encima del
  límite de 2,5 segundos, así que la solución en Python se envía con
  PyPy 3.10, donde tarda unos 0,1 segundos.
- Java compara los double directamente en el bucle interior: `Math.min`
  con double también trata NaN y −0 y hacía la solución varias veces más
  lenta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1342_dp.cpp](1342_dp.cpp) | G++ 13.2 x64 | dp | O(N·M·K) | AC | 0.078 s | 244 KB |
| [1342_dp.go](1342_dp.go) | Go 1.14 x64 | dp | O(N·M·K) | AC | 0.171 s | 2088 KB |
| [1342_dp.java](1342_dp.java) | Java 1.8 | dp | O(N·M·K) | AC | 0.250 s | 5520 KB |
| [1342_dp.py](1342_dp.py) | PyPy 3.10 x64 | dp | O(N·M·K) | AC | 0.375 s | 6840 KB |
| [1342_dp.rs](1342_dp.rs) | Rust 1.75 x64 | dp | O(N·M·K) | AC | 0.218 s | 308 KB |
