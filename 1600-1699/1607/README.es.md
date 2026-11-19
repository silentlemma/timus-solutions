# 1607. Taxi

[Timus 1607](https://acm.timus.ru/problem.aspx?space=1&num=1607) · dificultad 46 · implementation

Problema original de Denis Musin, del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Petya regatea con un taxista. Petya empieza en a y sube la oferta en b
cada vez; el taxista empieza en c y baja el precio en d cada vez;
hablan por turnos, primero Petya. Ninguno nombra un precio que pase el
del otro: el taxista acepta la oferta de Petya en vez de pedir menos, y
Petya acepta el precio del taxista en vez de ofrecer más. ¿Cuánto paga
Petya? Todos los números van de 1 a 10000.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

a, b, c y d.

## Salida

El precio del viaje.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
150 50 1000 100
```

Salida:

```
450
```

## Solución

Se simula el regateo. Si a ya es al menos c, el taxista lo acepta. Si
no, Petya sube b; si eso alcanza el precio del taxista, Petya acepta ese
precio. Luego el taxista baja d; si eso alcanza la oferta de Petya, el
taxista la acepta. La distancia se reduce al menos en 2 por ronda, así
que hay como mucho unas 5000 rondas: `O(max(1, c - a))`. Los resultados se
compararon con una implementación independiente en 800 entradas
aleatorias.

Detalles a tener en cuenta:

- el lado que pasaría el precio del otro cede al precio del otro, así
  que la respuesta siempre es un precio que se llegó a nombrar (pruebas
  04 y 05);
- Petya puede empezar por encima del precio del taxista; entonces no hay
  regateo y Petya paga a (prueba 02).

## Soluciones optimizadas

La solución optimizada en Java analiza los números byte a byte desde
`System.in` en lugar de usar `Scanner`: 316 KB en lugar de 1600 KB, con
el mismo tiempo.

`1607_math.py`. Sustituye el regateo por rondas por una fórmula. Si a>=c devuelve a. En otro caso q=(c-a-1)//(b+d) cuenta rondas completas tras las que aún no hay acuerdo; la siguiente oferta o réplica acuerda min(a+(q+1)*b,c-q*d). b,d positivos validan la división. Es la variante math; conserva aparte la simulación. Tiempo y espacio enteros acotados O(1). El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1607_implementation.py`: tiempo 0.093 s → 0.156 s; memoria 416 KB → 200 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1607_math.py`: puesto de tiempo 97/97 y de memoria 1/97 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1607_implementation.cpp](1607_implementation.cpp) | G++ 13.2 x64 | implementation | O(max(1, c - a)) | AC | 0.015 s | 132 KB | 11288177 |
| [1607_implementation.go](1607_implementation.go) | Go 1.14 x64 | implementation | O(max(1, c - a)) | AC | 0.015 s | 1112 KB | 11288180 |
| [1607_implementation.java](1607_implementation.java) | Java 1.8 | implementation | O(max(1, c - a)) | AC | 0.140 s | 1600 KB | 11288188 |
| [1607_implementation.py](1607_implementation.py) | Python 3.12 x64 | implementation | O(max(1, c - a)) | AC | 0.093 s | 416 KB | 11288185 |
| [1607_implementation.rs](1607_implementation.rs) | Rust 1.75 x64 | implementation | O(max(1, c - a)) | AC | 0.031 s | 224 KB | 11288189 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1607_implementation_optimized.java](1607_implementation_optimized.java) \* | Java 1.8 | implementation | O(max(1, c - a)) | AC | 0.125 s | 316 KB | 11303763 |
| [1607_math.py](1607_math.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.156 s | 200 KB | 11324835 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
