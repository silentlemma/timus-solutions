# 1652. Crisis bancaria

[Timus 1652](https://acm.timus.ru/problem.aspx?space=1&num=1652) · dificultad 2611 · matching

Problema original de Pavel Atnashev, del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n bancos, cada uno con un país y algo de dinero libre, tienen m deudas
interbancarias. Un banco cuenta como «responsable» si presta a un banco
de su propio país. Antes de comprobarlo, los bancos pueden comprar deudas
enteras a sus acreedores, pagando solo con su dinero libre inicial; los
vendedores siempre aceptan. Hay que hallar el mayor número posible de
bancos responsables.

## Entrada

n (2 ≤ n ≤ 1000), luego n líneas «país dinero» (1 ≤ país ≤ 100,
0 ≤ dinero ≤ 10⁹), luego m (0 ≤ m ≤ 10000) y m líneas
«acreedor deudor suma» (0 ≤ suma ≤ 10⁹).

## Salida

El mayor número de bancos responsables.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1 100000
1 200000
1 300000
2 400000
2 500000
4
1 2 200000
1 3 200000
2 4 500000
3 5 500000
```.

Salida:

```
3
```

## Solución

A un banco le basta una deuda de un banco de su país, así que solo
importa el tenedor final de cada deuda. El banco b puede acabar con la
deuda d si el deudor de d es de su país, b no es el propio deudor y b ya
tiene d o la suma de d cabe en su dinero. Cada deuda tiene un solo
tenedor, así que los bancos responsables se emparejan con deudas
distintas: la respuesta es la suma de los emparejamientos bipartitos
máximos de cada país. Las deudas sin emparejar se quedan
donde estaban, y comprar más de una deuda nunca ayuda.

Puede haber diez millones de pares banco–deuda, pero las deudas que un
banco puede pagar forman un prefijo de las deudas ordenadas por suma, así
que no se construye la lista completa de aristas. Los caminos aumentantes
de Kuhn recorren el prefijo con un puntero de «siguiente deuda no vista»
con compresión de caminos, omitiendo las deudas marcadas. Primero van los
bancos que ya tienen una deuda de su país; cada grupo se ordena por
longitud creciente del prefijo asequible. Tras una búsqueda fallida las
marcas se conservan: el emparejamiento no cambió, así que las deudas
alcanzadas siguen sin llevar a ningún sitio.

Aquí N = n + m y k es el número de búsquedas con éxito.

Detalles a tener en cuenta:

- un banco no puede prestarse a sí mismo, así que nunca tiene una deuda
  que debe el propio banco, aunque pudiera pagarla (prueba 04);
- una deuda de un banco de otro país no ayuda;
- el dinero de vender una deuda no se puede gastar, así que cada compra se
  compara solo con el dinero inicial.

Las respuestas coinciden con una búsqueda exhaustiva de tenedores en 150
mercados pequeños y con una implementación aceptada independiente en los
grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1652_matching.cpp](1652_matching.cpp) | G++ 13.2 x64 | matching | O(N log² N + (k + 1) · N log N) | AC | 0.031 s | 720 KB |
| [1652_matching.go](1652_matching.go) | Go 1.14 x64 | matching | O(N log² N + (k + 1) · N log N) | AC | 0.046 s | 3456 KB |
| [1652_matching.java](1652_matching.java) | Java 1.8 | matching | O((k + 1) · N log N) | AC | 0.187 s | 6540 KB |
| [1652_matching.py](1652_matching.py) | Python 3.12 x64 | matching | O((k + 1) · N log N) | AC | 0.718 s | 4624 KB |
| [1652_matching.rs](1652_matching.rs) | Rust 1.75 x64 | matching | O((k + 1) · N log N) | AC | 0.031 s | 1684 KB |
