# 1400. Caracteres del móvil

[Timus 1400](https://acm.timus.ru/problem.aspx?space=1&num=1400) · dificultad 549 · graphs

Problema original de Vladimir Yakovlev, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 256 caracteres adicionales de un teléfono están en una tabla de M
columnas, llenada por filas, con la última fila quizá más corta. El
cursor se mueve a la izquierda, a la derecha, arriba y abajo; izquierda
y derecha pasan además a la fila anterior o siguiente y de un extremo de
la tabla al otro, mientras que arriba desde la primera fila o abajo
hacia una casilla inexistente lo dejan donde está. Hay que elegir la
casilla inicial con el menor número medio de pulsaciones para llegar a
un carácter, e imprimir esa media y las pulsaciones de cada carácter.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M.

## Salida

«Mean = X» con dos cifras decimales y luego los N números de
pulsaciones, M por línea. Se acepta cualquier mejor casilla inicial.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
```

Salida:

```
Mean = 1.00
1 0 1
2 1
```

## Solución

Se numeran las casillas 0 … N − 1 por filas. Entonces izquierda y
derecha son i − 1 e i + 1 módulo N, arriba es i − M si esa casilla
existe y abajo i + M si existe; si no, el cursor se queda. Una búsqueda
en anchura desde cada casilla inicial da todas sus distancias, y gana el
inicio de menor suma. `O(N²)`.

Detalles a tener en cuenta:

- con un solo carácter la respuesta es Mean = 0.00 y un 0 (prueba 02);
- una media como 13/8 = 1,625 es un empate exacto en la segunda cifra;
  las soluciones imprimen lo mismo que printf de C, 1.62, así que Java
  redondea el valor exacto del double con BigDecimal en lugar de
  String.format (prueba 07);
- según el foro hay pruebas fuera de los límites del enunciado, como 46
  columnas, así que nada depende de esos límites (prueba 06).

Las pruebas se juzgan con un verificador que exige la menor media y unas
distancias que salgan de alguna casilla inicial con esa media.

## Soluciones optimizadas

Go reutiliza una fila de distancias de256 bytes, cola256 y tabla de vecinos256×4 bytes. Las horizontales contienen el ciclo N; distancias≤floor(N/2)≤128,255 indica no visto e índices≤255 caben en un byte. Reflejar v↦N−1−v conserva horizontales y verticales válidas, emparejando inicios con igual suma. Probar ceil(N/2) inicios, recordar el mejor y repetir BFS para su fila. La media conserva división binary64 y formato de dos decimales de la base, incluidos empates. Tiempo O(N²), espacio de trabajo O(N) acotado con N≤256, sin nuevos arreglos por inicio, fmt ni uniones de cadenas. Se conserva Go sencillo; los demás reutilizan originales admitidos.

Las implementaciones base aceptadas [1400_graphs.cpp](1400_graphs.cpp), [1400_graphs.java](1400_graphs.java), [1400_graphs.py](1400_graphs.py), [1400_graphs.rs](1400_graphs.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1400_graphs.cpp](1400_graphs.cpp) | G++ 13.2 x64 | graphs | O(N^2) | AC | 0.015 s | 216 KB | 11286012 |
| [1400_graphs.go](1400_graphs.go) | Go 1.14 x64 | graphs | O(N^2) | AC | 0.031 s | 2780 KB | 11286015 |
| [1400_graphs.java](1400_graphs.java) \* | Java 1.8 | graphs | O(N^2) | AC | 0.125 s | 4384 KB | 11286018 |
| [1400_graphs.py](1400_graphs.py) \* | Python 3.12 x64 | graphs | O(N^2) | AC | 0.125 s | 516 KB | 11286016 |
| [1400_graphs.rs](1400_graphs.rs) \* | Rust 1.75 x64 | graphs | O(N^2) | AC | 0.062 s | 324 KB | 11286020 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1400_graphs_optimized.go](1400_graphs_optimized.go) \* | Go 1.14 x64 | graphs | O(N²) | AC | 0.031 s | 916 KB | 11315773 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
