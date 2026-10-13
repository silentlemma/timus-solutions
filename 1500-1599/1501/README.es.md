# 1501. Sentido de la belleza

[Timus 1501](https://acm.timus.ru/problem.aspx?space=1&num=1501) · dificultad 268 · dp

Problema original de Leonid Volkov y Stanislav Vasiliev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos montones de N cartas cada uno (4 ≤ N ≤ 1000) tienen en total N
cartas rojas y N negras. El crupier toma una y otra vez la carta de
arriba de uno de los montones y la pone en un montón rojo o negro, hasta
pasar todas las cartas. En todo momento los montones rojo y negro pueden
diferir en una carta como mucho. Hay que escribir de qué montón se toma
cada carta, como 2N cifras 1 y 2, o «Impossible».

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego los dos montones de arriba abajo, 1 para roja y 0 para negra.

## Salida

Las 2N cifras o «Impossible». Se acepta cualquier orden válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0011
0110
```

Salida:

```
22121112
```

### Ejemplo 2

Entrada:

```
4
1100
1100
```

Salida:

```
Impossible
```

## Solución

Un momento se describe con los números i y j de cartas tomadas de los
dos montones. Con d = 2 · (cartas rojas) − (cartas) sobre la parte
tomada de cada montón, los montones rojo y negro difieren en
d1[i] + d2[j], así que el estado es válido cuando eso vale −1, 0 o 1.
Un estado es alcanzable si es válido y lo es el estado de encima o el
de la izquierda; (0, 0) es el inicio. Si (N, N) es alcanzable, se
vuelve desde él tomando cualquier predecesor alcanzable y se leen los
movimientos al revés. `O(N²)`.

Detalles a tener en cuenta:

- la condición rige tras cada movimiento, no solo al final (prueba 02,
  gen4);
- puede haber muchos órdenes correctos, así que las pruebas usan un
  comprobador (todas las pruebas);
- con el límite de 0,5 segundos la tabla de N² estados debe ser barata;
  la solución en Python guarda cada fila como una máscara entera y
  extiende la alcanzabilidad por los tramos de estados válidos con una
  sola suma.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1501_dp.cpp](1501_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.015 s | 856 KB |
| [1501_dp.go](1501_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.031 s | 2216 KB |
| [1501_dp.java](1501_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.109 s | 2704 KB |
| [1501_dp.py](1501_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.093 s | 836 KB |
| [1501_dp.rs](1501_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.031 s | 1164 KB |
