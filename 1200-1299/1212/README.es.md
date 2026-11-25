# 1212. Sitios para un barco más en la batalla naval

[Timus 1212](https://acm.timus.ru/problem.aspx?space=1&num=1212) · dificultad 493 · geometry

Problema original de Anton Botov y Anatoly Uglov, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tablero de batalla naval tiene `N` filas y `M` columnas, ambas hasta
30000, y en él ya hay hasta 30 barcos de una a cuatro casillas. Los
barcos no pueden tocarse, ni siquiera por una esquina. Hay que contar las
formas de colocar un barco más de `K` casillas, en horizontal o en
vertical.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`, `M` y el número de barcos `L`; luego cada barco como la columna y
la fila de su casilla superior izquierda, su longitud y `V` o `H`; y
luego `K`.

## Salida

El número de sitios para el barco nuevo.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4 2
1 2 2 V
3 1 2 H
2
```

Salida:

```
4
```

## Solución

Cada barco colocado prohíbe el rectángulo que lo rodea, una casilla más
ancho por cada lado. Primero se cuentan los sitios horizontales. Las
filas se parten en franjas en el borde superior y justo debajo del borde
inferior de cada rectángulo prohibido; dentro de una franja cada fila
corta los mismos rectángulos, así que todas sus filas cuentan lo mismo.
Para una fila de la franja se toman en orden los tramos de columnas
prohibidos y se suma `max(0, longitud − K + 1)` por cada tramo libre
entre ellos; se multiplica por la altura de la franja. Los sitios
verticales son la misma cuenta con el tablero girado. Un barco de una
casilla es igual en ambos sentidos, así que entonces se cuenta una sola
vez. Con como mucho 61 franjas, `O(L² log L)`.

Detalles a tener en cuenta:

- el primer número de un barco es su columna y el segundo su fila;
- un barco de una casilla no debe contarse dos veces;
- los rectángulos prohibidos sobresalen del tablero; al formar franjas
  se ignoran los cortes fuera del tablero;
- la respuesta puede llegar a unos `1.8·10⁹`, dentro de 32 bits con signo.

Las respuestas se compararon con una fuerza bruta casilla a casilla en
450 tableros pequeños aleatorios, y con una solución escrita aparte en
todas las pruebas.

La versión didáctica en Python cuenta directamente los inicios prohibidos. Para una colocación horizontal, amplía el rectángulo prohibido de cada barco K − 1 columnas a la izquierda y lo recorta al dominio de inicios válidos. Inserta cada inicio en un conjunto para contar una sola vez los solapamientos. Resta el tamaño del conjunto del total de inicios y transpone el tablero para el otro sentido, salvo si K = 1. Cada barco aporta hasta 36 celdas por orientación. Tiempo esperado O(L), espacio O(L).

## Soluciones optimizadas

C++, Go y Rust cuentan los inicios prohibidos. Para una colocación horizontal, amplían cada rectángulo prohibido K − 1 columnas a la izquierda y lo recortan al dominio de inicios válidos. Cada barco aporta hasta 36 celdas. Codifican cada una como (fila − 1)M + columna − 1, ordenan los códigos y cuentan los distintos. Para las colocaciones verticales, transponen el tablero.

La versión PyPy optimiza la memoria contando las celdas finales prohibidas. Un barco horizontal que termina en la columna x intersecta el intervalo [a,b] si y solo si x ≥ a y x − K + 1 ≤ b. Ordena los rectángulos prohibidos una vez por su borde izquierdo. Amplía K − 1 celdas a la derecha para colocaciones horizontales o hacia abajo para las verticales, y recorta al dominio de finales válidos. Para cada fila afectada guarda el extremo cubierto más a la derecha y resta solo las celdas recién cubiertas. Cada rectángulo afecta a lo sumo nueve filas. Ambos métodos cuentan K = 1 una vez y usan tiempo O(L log L) y espacio O(L).

El envío aceptado en PyPy 3.10 x64 tarda 0.14 s frente a 0.078 s de la base y usa 340 KB frente a 684 KB.

Las implementaciones base aceptadas [1212_geometry.java](1212_geometry.java) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

C++, Go y Rust ordenan inicios codificados en arreglos fijos. Go usa uint32, descriptores estándar y búferes fijos. PyPy guarda un extremo derecho por fila afectada y usa el mismo orden de rectángulos para ambos sentidos. Java conserva el algoritmo original por franjas de filas.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1212_geometry.cpp](1212_geometry.cpp) | G++ 13.2 x64 | geometry | O(L² log L) | AC | 0.031 s | 432 KB | 11283646 |
| [1212_geometry.go](1212_geometry.go) | Go 1.14 x64 | geometry | O(L² log L) | AC | 0.031 s | 1144 KB | 11283647 |
| [1212_geometry.java](1212_geometry.java) \* | Java 1.8 | geometry | O(L² log L) | AC | 0.140 s | 1940 KB | 11283649 |
| [1212_geometry.py](1212_geometry.py) | Python 3.12 x64 | geometry | O(L² log L) | AC | 0.078 s | 684 KB | 11283648 |
| [1212_geometry.rs](1212_geometry.rs) | Rust 1.75 x64 | geometry | O(L² log L) | AC | 0.046 s | 232 KB | 11283650 |
| [1212_hashing.py](1212_hashing.py) | Python 3.12 x64 | hashing | O(L) expected | AC | 0.093 s | 580 KB | 11315800 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1212_sorting.cpp](1212_sorting.cpp) | G++ 13.2 x64 | sorting | O(L log L) | AC | 0.015 s | 124 KB | 11315806 |
| [1212_sorting.rs](1212_sorting.rs) | Rust 1.75 x64 | sorting | O(L log L) | AC | 0.015 s | 220 KB | 11315821 |
| [1212_sorting.go](1212_sorting.go) \* | Go 1.14 x64 | sorting | O(L log L) | AC | 0.015 s | 308 KB | 11315959 |
| [1212_sorting.py](1212_sorting.py) | PyPy 3.10 x64 | sorting | O(L log L) | AC | 0.14 s | 340 KB | 11316273 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
