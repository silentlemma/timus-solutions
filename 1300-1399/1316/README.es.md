# 1316. Subasta electrónica

[Timus 1316](https://acm.timus.ru/problem.aspx?space=1&num=1316) · dificultad 427 · fenwick

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
suma de prefijo. `O(P + N log P)` para N operaciones y P índices de precios.

Las piezas vendidas se cuentan en un entero, y como cada pieza deja
un céntimo, ese número dividido entre 100 y escrito con dos decimales
es la respuesta.

Detalles a tener en cuenta:

- una oferta de exactamente X compra (prueba 04), y una oferta sigue
  activa para ventas posteriores hasta que se retira (prueba 07);
- 50 000 ofertas y 49 999 ventas de 100 000 piezas venden 2.49995 · 10⁹
  piezas, más de 2³¹, así que los contadores de 32 bits con signo se desbordan
  (prueba gen5);
- los precios pueden venir con un decimal o ninguno, como `5.5` o
  `10000` (pruebas 04 y 05);
- unas ganancias en coma flotante como 0.01 · count pueden imprimir un
  céntimo de menos, cosa que los céntimos enteros evitan.

Los totales se compararon con un conteo directo sobre todas las ofertas
activas en 300 registros aleatorios.

## Soluciones optimizadas

La revisión C++ mantiene la compresión de precios BID y la reproducción del registro con Fenwick. Un lector fijo de 16 KB analiza comandos, precios decimales y cantidades sin scanf. Se conservan los céntimos enteros exactos y la admisión de pujas iguales al precio de venta.

Accepted del fuente exacto (G++ 13.2 x64, #11326642: 0.015 s / 1320 KB); base didáctica `1316_fenwick.cpp`: 0.171 s / 3652 KB. La medición optimizada anterior era 0.156 s / 1344 KB. En la comparación guardada del 20 de noviembre de 2026, el puesto de tiempo es 1/85 y de memoria 1/85; por debajo de 1 MiB la regla evalúa solo el puesto de tiempo.

Las nuevas versiones C++, Go y Rust comprimen solo los precios de BID. Guardan el registro, ordenan y deduplican esos precios, y reproducen las operaciones con un árbol Fenwick. Una venta a X resta los compradores estrictamente más baratos del total activo: los de precio igual participan y la venta no retira ofertas. Los precios se leen como céntimos enteros y los ingresos usan 64 bits o enteros Python. Para como máximo N operaciones, tiempo O(N log N) y espacio O(N) sustituyen al millón de posiciones. C++, Go y Rust reservan capacidad para 100000 operaciones. Python procesa directamente una lista Fenwick densa sobre P=1000000 céntimos con índice P−precio+1. La versión online más sencilla no retiene operaciones ni ordena, busca rangos o construye un diccionario. Tiempo O(P+N log P), espacio O(P): la tabla fija sustituye la entrada retenida y evita el empaquetado por acceso. Go usa manejadores estándar; Rust E/S acotada del C runtime y entrada C. Se conservan las versiones habituales y la base Java ya admitida.

El envío aceptado en Python 3.12 x64 tarda 0.5 s frente a 0.437 s de la base y usa 8 324 KB frente a 32560 KB.

Las implementaciones base aceptadas [1316_fenwick.java](1316_fenwick.java) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Python numera solo los precios que aparecen en el registro, lo que
  mantiene pequeño el árbol; los demás lenguajes indexan directamente
  el millón de precios.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1316_fenwick.cpp](1316_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(P + N log P) | AC | 0.171 s | 3652 KB | 11284923 |
| [1316_fenwick.go](1316_fenwick.go) | Go 1.14 x64 | fenwick | O(P + N log P) | AC | 0.062 s | 11012 KB | 11284924 |
| [1316_fenwick.java](1316_fenwick.java) \* | Java 1.8 | fenwick | O(P + N log P) | AC | 0.156 s | 9428 KB | 11284926 |
| [1316_fenwick.py](1316_fenwick.py) | Python 3.12 x64 | fenwick | O(N log P) | AC | 0.437 s | 32560 KB | 11284925 |
| [1316_fenwick.rs](1316_fenwick.rs) | Rust 1.75 x64 | fenwick | O(P + N log P) | AC | 0.031 s | 10996 KB | 11284927 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1316_fenwick_optimized.cpp](1316_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(N log N) | AC | 0.015 s | 1320 KB | 11326642 |
| [1316_fenwick_optimized.go](1316_fenwick_optimized.go) \* | Go 1.14 x64 | fenwick | O(N log N) | AC | 0.046 s | 3080 KB | 11314836 |
| [1316_fenwick_optimized.rs](1316_fenwick_optimized.rs) \* | Rust 1.75 x64 | fenwick | O(N log N) | AC | 0.015 s | 1628 KB | 11314919 |
| [1316_fenwick_optimized.py](1316_fenwick_optimized.py) \* | Python 3.12 x64 | fenwick | O(P + N log P) | AC | 0.5 s | 8324 KB | 11315039 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
