# 1346. Intervalos de monotonía

[Timus 1346](https://acm.timus.ru/problem.aspx?space=1&num=1346) · dificultad 297 · greedy

Problema original de Alexander Klepinin, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una función F está dada en la rejilla entera A, A + 1, …, B, con
0 ≤ A < B ≤ 100 000 y valores enteros de −100 000 a 100 000. Hay que partir la
rejilla en el menor número de intervalos en cada uno de los cuales F no
decrece o no crece, e imprimir cuántos son.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

A y B, luego los valores enteros F(A), …, F(B), separados por espacios o saltos
de línea.

## Salida

El menor número de intervalos.

## Evaluación

Comparación de tokens (`judging: tokens`): un entero, el mínimo
número de intervalos monótonos disjuntos de puntos de la rejilla.
No se piden límites ni partición concreta; el espacio no importa.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 10
1 2 3 4 2 1 -1 3 6 7
```

Salida:

```
3
```

## Solución

Los intervalos reparten los puntos de la rejilla, así que el paso entre
el último punto de un intervalo y el primero del siguiente es libre.
Cualquier parte de un intervalo monótono vuelve a ser monótona. Por eso
nunca estorba alargar el primer intervalo todo lo posible, y lo mismo
vale para cada siguiente: el conteo voraz es el mínimo.

Un intervalo se alarga mientras siga siendo monótono. Su sentido lo
fija su primer paso que no es plano, y los pasos planos valen para
cualquier sentido. El primer paso contra ese sentido acaba el
intervalo, y el siguiente empieza en el punto siguiente. `O(B − A)`.

Detalles a tener en cuenta:

- el paso entre dos intervalos es libre: 1 3 2 4 solo necesita 2
  intervalos, 1 3 y 2 4 (prueba 02);
- los pasos planos pertenecen al intervalo vaya en el sentido que vaya,
  y una función constante es un solo intervalo (pruebas 03, 05 y 06);
- los valores pueden venir en varias líneas.

Los conteos se compararon con una programación dinámica sobre todos los
repartos en 500 funciones aleatorias de hasta 12 puntos.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1346_greedy_optimized.cpp`. Mantiene el recorrido voraz de monotonía. Al invertir una dirección no nula abre otro intervalo y borra su dirección: el paso de frontera no pertenece a ninguno. Valores iguales no fijan dirección. Solo conserva valor anterior, dirección y conteo: O(B-A+1) tiempo, O(1) espacio auxiliar. Sustituye entrada formateada por fread de 16384 bytes y un byte centinela, conservando signos/dígitos parciales entre recargas y detectando EOF sin bucle infinito en entrada vacía. Escribe el conteo como bytes decimales. Escáner compartido probado con ambos tamaños, AddressSanitizer/UndefinedBehaviorSanitizer y 100019 valores por tamaño. Conserva la implementación didáctica.

C++ #11327408 `0.015 s / 92 KB` cumple con puesto temporal 1/71
según los [criterios comunes](../../RATING_CRITERIA.md): bajo
1024 KB sólo tiempo, sin meta separada de C++. #11310334
`0.031 s / 84 KB` sigue como otro par histórico.

- `1346_greedy_optimized.cpp`: 0.015 s / 92 KB; base didáctica conservada `1346_greedy.cpp`: 0.062 s / 588 KB.

Comparación histórica de la revisión anterior: Las versiones en C++ y Go conservan el recorrido voraz y procesan cada valor al leerlo. Solo guardan el valor anterior, la dirección del intervalo actual y el número de intervalos. El búfer de entrada tiene tamaño fijo, así que el recorrido tarda O(B − A + 1) y requiere O(1) espacio adicional. El envío aceptado de C++ tardó 0,031 s y usó 84 KB, frente a 0,062 s y 588 KB de la versión base. Go usó 1588 KB en lugar de 2512 KB, con 0,031 s en ambas versiones.

Java reutiliza la base: 900 KB, sólo tiempo, puesto 2/28. Python
cumple con el archivo en flujo `0.109 s / 724 KB`, no con la base
`0.140 s / 11140 KB`: seis rivales exactos CPython activan la tercera
referencia temporal 0.12535 s. Rust cumple con el archivo nativo
`0.015 s / 56 KB`; la base de 2632 KB supera el límite de 2047 KB.
Un rival Rust exacto fija tiempo 0.031 s. No se duplican bases
que cumplen y se conservan todas las versiones didácticas.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1346_greedy_optimized.py`. Se procesa la secuencia en flujo, guardando solo el valor anterior, la dirección y el número de intervalos. Los valores iguales no fijan dirección; un cambio inicia otro intervalo. El tiempo es lineal y el estado del algoritmo constante. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328773 (Python 3.12 x64): **0.109 s / 724 KB**. Comparación archivada: `1346_greedy.py` (Python 3.12 x64) — 0.14 s / 11140 KB (#11285126).

`1346_implementation_parsing_optimized.rs` conserva el barrido
voraz en flujo. NativeNumbers analiza i64 con signo atravesando
rellenos de su búfer de 4096 bytes. NativeOutput imprime el contador
sin signo con 20 bytes de dígitos y 256 de salida, completa las
escrituras y vacía la nueva línea. Windows usa _read/_write del
entorno C en modo binario; otras plataformas read/write. No usa
impresión numérica con signo ni formato genérico. Tiempo O(B-A+1),
estado fijo y almacenamiento de E/S acotado.

Este código exacto tiene su propio Accepted y cumple los [criterios compartidos](../../RATING_CRITERIA.md). El tiempo y la memoria siguientes proceden de una misma ejecución; las mediciones repetidas pueden variar. Se conservan las versiones sencillas y optimizadas distintas existentes.

Accepted #11329367 (Rust 1.75 x64): **0.015 s / 56 KB**.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Las cinco soluciones hacen la misma pasada.

En `1346_greedy_optimized.py` sólo se nombran constantes exigidas por el lint; valores, algoritmo y comentarios no cambian. Accepted #11328773 y sus medidas corresponden a los bytes exactos previos.

En `1346_implementation_parsing_optimized.rs` sólo se nombran constantes exigidas por el lint; valores, algoritmo y comentarios no cambian. Accepted #11329367 y sus medidas corresponden a los bytes exactos previos.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1346_greedy.cpp](1346_greedy.cpp) | G++ 13.2 x64 | greedy | O(B - A) | AC | 0.062 s | 588 KB | 11285122 |
| [1346_greedy.go](1346_greedy.go) | Go 1.14 x64 | greedy | O(B - A) | AC | 0.031 s | 2512 KB | 11285125 |
| [1346_greedy.java](1346_greedy.java) | Java 1.8 | greedy | O(B - A) | AC | 0.109 s | 900 KB | 11285127 |
| [1346_greedy.py](1346_greedy.py) | Python 3.12 x64 | greedy | O(B - A) | AC | 0.14 s | 11140 KB | 11285126 |
| [1346_greedy.rs](1346_greedy.rs) | Rust 1.75 x64 | greedy | O(B - A) | AC | 0.015 s | 2632 KB | 11285128 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1346_greedy_optimized.cpp](1346_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(B-A+1) time; O(1) auxiliary storage | AC | 0.015 s | 92 KB | 11327408 |
| [1346_greedy_optimized.go](1346_greedy_optimized.go) | Go 1.14 x64 | greedy | O(B - A + 1) | AC | 0.031 s | 1588 KB | 11310367 |
| [1346_greedy_optimized.py](1346_greedy_optimized.py) | Python 3.12 x64 | greedy | O(B-A+1) time; O(1) state + bounded input buffer | AC | 0.093 s | 792 KB | 11331069 |
| [1346_implementation_parsing_optimized.rs](1346_implementation_parsing_optimized.rs) | Rust 1.75 x64 | implementation, parsing | O(B-A+1) time; O(1) state + bounded input buffer | AC | 0.031 s | 60 KB | 11331112 |
