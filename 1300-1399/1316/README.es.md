# 1316. Subasta electrónica

[Timus 1316](https://acm.timus.ru/problem.aspx?space=1&num=1316) · dificultad 436 · fenwick

Problema original con idea de Pavel Atnashev, preparado por Pavel Atnashev y Pavel Egorov, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El registro de una bolsa tiene hasta 100 000 operaciones:

- `BID X`: un comprador está dispuesto a comprar una pieza a precio X;
- `DEL X`: se retira una oferta a precio X;
- `SALE X K`: se ofrecen K piezas a precio X, y las primeras K ofertas
  de X o más reciben una cada una; el resto se funde.

Una oferta sigue activa tras comprar, hasta que se retira. Los precios
van de 0.01 a 10 000.00 con como mucho dos decimales, K ≤ 100 000, y el
registro termina con `QUIT`. La bolsa gana 0.01 por pieza vendida. Hay
que imprimir su total.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

El registro, una operación por línea, terminado en `QUIT`.

## Salida

Las ganancias de la bolsa con dos decimales.

## Ejemplos

### Ejemplo 1

Entrada:

```
BID 0.01
BID 10000
BID 5000
BID 5000
SALE 7945.14 3
DEL 5000
SALE 3487.45 3
SALE 0.01 3
QUIT
```

Salida:

```
0.06
```

## Solución

Una venta vende min(K, número de ofertas activas a X o más) piezas, así
que solo hace falta un conteo de ofertas activas por precio, con la
consulta «cuántas a X o más».

Los precios se leen de forma exacta como céntimos enteros, de 1 a
1 000 000. Numerando los céntimos desde el precio más alto hacia abajo,
«a X o más» es un prefijo, y un árbol de Fenwick guarda los conteos.
Una oferta suma 1 en su precio, una retirada resta 1 y una venta lee una
suma de prefijo. `O(N log P)`.

Las piezas vendidas se cuentan en un entero de 64 bits, y como cada
pieza deja un céntimo, ese número escrito con dos decimales es la
respuesta.

Detalles a tener en cuenta:

- una oferta de exactamente X compra (prueba 04), y una oferta sigue
  comprando en cada venta posterior hasta que se retira (prueba 07);
- 50 000 ofertas y 50 000 ventas de 100 000 piezas venden 2.5 · 10⁹
  piezas, más de 2³¹, así que los contadores de 32 bits se desbordan
  (prueba gen5);
- los precios pueden venir con un decimal o ninguno, como `5.5` o
  `10000` (pruebas 04 y 05);
- unas ganancias en coma flotante como 0.01 · count pueden imprimir un
  céntimo de menos, cosa que los céntimos enteros evitan.

Los totales se compararon con un conteo directo sobre todas las ofertas
activas en 300 registros aleatorios.

## Notas por lenguaje

- Python numera solo los precios que aparecen en el registro, lo que
  mantiene pequeño el árbol; los demás lenguajes indexan directamente
  el millón de precios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1316_fenwick.cpp](1316_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(N log P) | AC | 0.171 s | 3652 KB |
| [1316_fenwick.go](1316_fenwick.go) | Go 1.14 x64 | fenwick | O(N log P) | AC | 0.062 s | 11012 KB |
| [1316_fenwick.java](1316_fenwick.java) | Java 1.8 | fenwick | O(N log P) | AC | 0.156 s | 9428 KB |
| [1316_fenwick.py](1316_fenwick.py) | Python 3.12 x64 | fenwick | O(N log P) | AC | 0.437 s | 32560 KB |
| [1316_fenwick.rs](1316_fenwick.rs) | Rust 1.75 x64 | fenwick | O(N log P) | AC | 0.031 s | 10996 KB |
