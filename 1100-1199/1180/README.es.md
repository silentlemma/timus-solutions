# 1180. Quién gana cuando las piedras se toman en potencias de dos

[Timus 1180](https://acm.timus.ru/problem.aspx?space=1&num=1180) · dificultad 89 · games

Problema original de Dmitry Filimonenkov, del Tercer Concurso Individual de Programación de la Universidad Estatal de los Urales, Ekaterimburgo, 16 de febrero de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N ≤ 10²⁵⁰` piedras. Dos jugadores retiran por turnos una potencia de
dos (1, 2, 4, 8, …) de piedras; gana quien se lleva la última. Hay que
decir quién gana con juego perfecto y, si es el primero, el menor número
de piedras que puede tomar en la primera jugada sin perder la victoria.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`, con hasta 251 dígitos.

## Salida

`2`, o `1` y la menor primera jugada ganadora.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
```

Salida:

```
1
2
```

## Solución

Ninguna potencia de dos es divisible entre 3, así que desde un múltiplo
de 3 toda jugada deja un montón que no lo es. Desde cualquier otro montón,
tomar 1 o 2 piedras, el resto módulo 3, deja un múltiplo de 3. El cero es
múltiplo de 3, así que quien deja siempre un múltiplo de 3 se lleva la
última piedra. El segundo jugador gana exactamente cuando `N` es divisible
entre 3; si no, gana el primero, y la menor jugada ganadora es `N mod 3`,
porque ninguna otra jugada de 1 o 2 deja un múltiplo de 3. `N mod 3` es la
suma de dígitos módulo 3. `O(dígitos)`.

Detalles a tener en cuenta:

- `N` tiene hasta 251 dígitos, así que un entero de 64 bits no basta;
- la jugada ganadora debe ser la menor, y tanto 1 como 2 son potencias de
  dos, así que es el propio resto.

Las respuestas se comprobaron contra una búsqueda directa del juego para
todo `N` hasta 399.

## Soluciones optimizadas

Las soluciones optimizadas (C++, Java) suman las cifras una a una a
medida que las leen con `getchar` y `System.in.read`, sin guardar el
número como cadena, y escriben la breve respuesta byte a byte. C++:
88 KB en lugar de 384 KB, con el mismo tiempo; Java: 0.093 s en lugar de
0.125 s y 328 KB en lugar de 1568 KB.

`1180_games_optimized.py`. Conserva la clasificación del juego de potencias de dos por N módulo tres. Resto cero pierde; en otro caso quitar ese resto, una o dos piedras, es la menor jugada ganadora. Procesa los D dígitos sin convertir el número enorme completo a entero. Suma directamente los códigos de los bytes: el cero ASCII vale 48, divisible por tres, y el resto no cambia. Aún guarda la cadena de bytes: tiempo O(D) y almacenamiento de entrada O(D). El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1180_games.py`: tiempo 0.078 s → 0.125 s; memoria 400 KB → 236 KB.

`1180_games_optimized.rs`. Conserva la clasificación del juego de potencias de dos por N módulo tres. Resto cero pierde; en otro caso quitar ese resto, una o dos piedras, es la menor jugada ganadora. Procesa los D dígitos sin convertir el número enorme completo a entero. Actualiza el resto acotado con cada dígito y no conserva la línea de entrada. Tiempo O(D), estado auxiliar O(1). La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1180_games.rs`: tiempo 0.015 s → 0.031 s; memoria 212 KB → 56 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1180_games_optimized.py`: puesto de tiempo 64/77 y de memoria 3/77 en esta muestra comparable.

`1180_games_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1180_games.cpp](1180_games.cpp) | G++ 13.2 x64 | games | O(digits) | AC | 0.015 s | 384 KB | 11283296 |
| [1180_games.go](1180_games.go) | Go 1.14 x64 | games | O(digits) | AC | 0.015 s | 1104 KB | 11283304 |
| [1180_games.java](1180_games.java) | Java 1.8 | games | O(digits) | AC | 0.125 s | 1568 KB | 11283311 |
| [1180_games.py](1180_games.py) | Python 3.12 x64 | games | O(digits) | AC | 0.078 s | 400 KB | 11283308 |
| [1180_games.rs](1180_games.rs) | Rust 1.75 x64 | games | O(digits) | AC | 0.015 s | 212 KB | 11283312 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1180_games_optimized.cpp](1180_games_optimized.cpp) \* | G++ 13.2 x64 | games | O(digits) | AC | 0.031 s | 88 KB | 11303574 |
| [1180_games_optimized.java](1180_games_optimized.java) | Java 1.8 | games | O(digits) | AC | 0.093 s | 328 KB | 11303452 |
| [1180_games_optimized.py](1180_games_optimized.py) \* | PyPy 3.10 x64 | games | O(D) | AC | 0.125 s | 236 KB | 11324925 |
| [1180_games_optimized.rs](1180_games_optimized.rs) \* | Rust 1.75 x64 | games | O(D) | AC | 0.031 s | 56 KB | 11325088 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
