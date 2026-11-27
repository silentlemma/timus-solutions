# 1121. Los tipos de las sucursales más cercanas en una cuadrícula de calles

[Timus 1121](https://acm.timus.ru/problem.aspx?space=1&num=1121) · dificultad 354 · bruteforce

Problema original de Leonid Volkov y Alexander Somov, del USU Open Collegiate Programming Contest, octubre de 2001, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cuadrícula de `H × W` cruces (`1 ≤ H, W ≤ 150`) guarda en cada cruce
una máscara de bits con los tipos de sucursales que hay allí (los tipos
son potencias de dos, como mucho 11; 0 significa ninguna sucursal). La
distancia es el número de tramos de calle recorridos, es decir, la
distancia Manhattan. Para cada cruce con sucursales imprime `-1`; para
cada cruce vacío imprime la unión bit a bit de los tipos de sus sucursales
más cercanas, o `0` si no hay ninguna a distancia 5 o menos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`H W` y luego `H` líneas de `W` máscaras.

## Salida

`H` líneas de `W` números.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 5
0 0 2 0 2
0 0 0 0 0
0 0 0 0 0
0 0 0 5 0
1 0 0 4 0
```

Salida:

```
2 2 -1 2 -1
3 2 2 7 2
1 7 7 5 7
1 5 5 -1 5
-1 1 4 -1 4
```

## Solución

Solo importan las distancias de 1 a 5, así que para cada cruce vacío se
miran los cruces a distancia 1, luego 2, y así sucesivamente: el anillo a
distancia `d` tiene `4d` celdas, 60 hasta la distancia 5. En la primera
distancia donde aparece alguna sucursal, la respuesta es el «o» bit a bit
de las máscaras de ese anillo; ahí se para. Los desplazamientos de cada
anillo se listan una vez de antemano. `O(H · W · 60)`, unos 1,4 millones
de comprobaciones.

Las bases retienen H*W máscaras y 60 desplazamientos: O(HW) palabras
con radio cinco fijo. C++/Java/Python/Rust acumulan P bytes de salida;
Rust además una fila de cadenas. Go emite con búfer fijo. Python/Rust
conservan I bytes de entrada, Python añade tokens: contar O(I+P) donde
corresponda. BFS Python guarda HW etiquetas, HW bytes de distancia y
hasta HW índices de cola más texto de fila: aún O(HW), sin representación
por anillos de offsets.

Detalles a tener en cuenta:

- los tipos se combinan con «o», no se suman: dos sucursales del mismo
  tipo a la distancia mínima cuentan una vez (en `3 0 6` el centro recibe
  `7`, no `9`);
- solo cuenta la distancia mínima, aunque sucursales más lejanas añadirían
  tipos;
- las sucursales a seis calles o más dan `0`, no sus tipos.

Las respuestas se comprobaron con una búsqueda en anchura desde todas las
sucursales a la vez hasta la distancia 5, donde los tipos más cercanos de
un cruce son la unión de los de sus vecinos una capa más cerca, en todas
las pruebas y 40 mapas aleatorios.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

C++, Go y Rust guardan la cuadrícula en un vector plano de máscaras de 16 bits, rodeado por cinco celdas de ceros. Los desplazamientos lineales precalculados recorren cada anillo de Manhattan sin comprobar límites de coordenadas. El primer anillo con una unión no nula da la respuesta, que se escribe inmediatamente con salida almacenada en búfer. Go usa vectores fijos para la cuadrícula y los anillos, lee enteros desde un búfer reutilizable de bytes y escribe las cifras sin crear cadenas.

El envío aceptado en Rust 1.75 x64 tarda 0.031 s frente a 0.015 s de la base y usa 240 KB frente a 628 KB.

La caché del fuente confirma Java simple por ambos puestos ordinarios.
Python simple falla la comparación aplicable de gran memoria; el BFS
Python distinto de 1148 KB cubre el lenguaje por ambas métricas
pequeñas. Otras variantes nativas que cumplen tienen su propia evidencia.
No se duplica una base que cumple ni se atribuye el recibo BFS al
barrido simple por radios.

La revisión actual de 1121_bfs_optimized.py solo corrige el comentario
BFS y nombra el límite intacto de espacios 32 y centinela no alcanzado
255. Accepted #11328770 (0.125 s / 1148 KB) pertenece a los bytes
anteriores.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1121_bfs_optimized.py`. Se sustituye el barrido de radios por BFS multifuente hasta distancia cinco. Las distancias usan bytes y las etiquetas enteros de 16 bits; se unen etiquetas en caminos de igual distancia. Las capas FIFO reúnen todas las contribuciones antes de expandir. Tiempo y espacio O(nm). El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328770 (Python 3.12 x64): **0.125 s / 1148 KB**. Comparación archivada: `1121_bruteforce.py` (Python 3.12 x64) — 0.406 s / 2512 KB (#11279280).

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes recorren los mismos anillos precalculados.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1121_bruteforce.cpp](1121_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(H·W·60) | AC | 0.031 s | 256 KB | 11279278 |
| [1121_bruteforce.go](1121_bruteforce.go) | Go 1.14 x64 | bruteforce | O(H·W·60) | AC | 0.031 s | 1376 KB | 11279279 |
| [1121_bruteforce.java](1121_bruteforce.java) | Java 1.8 | bruteforce | O(H·W·60) | AC | 0.109 s | 3664 KB | 11279282 |
| [1121_bruteforce.py](1121_bruteforce.py) | Python 3.12 x64 | bruteforce | O(H·W·60) | AC | 0.406 s | 2512 KB | 11279280 |
| [1121_bruteforce.rs](1121_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(H·W·60) | AC | 0.015 s | 628 KB | 11279284 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1121_bruteforce_optimized.cpp](1121_bruteforce_optimized.cpp) | G++ 13.2 x64 | bruteforce | O(H·W·60) | AC | 0.015 s | 160 KB | 11311133 |
| [1121_bruteforce_optimized.go](1121_bruteforce_optimized.go) | Go 1.14 x64 | bruteforce | O(H·W·60) | AC | 0.031 s | 848 KB | 11311112 |
| [1121_bruteforce_optimized.rs](1121_bruteforce_optimized.rs) | Rust 1.75 x64 | bruteforce | O(H·W·60) | AC | 0.031 s | 240 KB | 11311088 |
| [1121_bfs_optimized.py](1121_bfs_optimized.py) | Python 3.12 x64 | bfs | O(nm) time and space | AC | 0.109 s | 944 KB | 11331072 |
