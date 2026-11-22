# 1631. Rey borracho 2

[Timus 1631](https://acm.timus.ru/problem.aspx?space=1&num=1631) · dificultad 493 · math

Problema original de Igor Chevdar, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un rey recorre un tablero m × n de lados impares: empieza y termina en
una esquina, visita cada casilla salvo la primera exactamente una vez,
no cruza su propio camino y, por estar borracho, nunca hace dos
movimientos seguidos en la misma dirección. Hay que hallar la longitud
del recorrido más corto, medida entre centros de casillas (un movimiento
recto vale 1 y uno diagonal √2).

## Entrada

Una línea con m y n (6 < m, n < 500, ambos impares).

## Salida

La longitud del recorrido más corto con precisión 10⁻⁹.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 7
```

Salida:

```
55.213203435596425732025330863145
```

## Solución

El recorrido tiene mn movimientos. Si D son diagonales, su longitud
es mn + D·(√2−1), así que queremos minimizar D. Los programas aceptados
evalúan la fórmula con D=m+n+1 en tiempo y espacio constantes.

Separa las casillas por paridad de fila y columna: A=par/par, B=par/impar,
C=impar/par, D₀=impar/impar. Con dimensiones impares, |A|−|D₀|=(m+n)/2.
El color A∪D₀ tiene una casilla más que B∪C.

Sean x las diagonales B–C e y las A–D₀. Los pasos ortogonales unen
colores distintos y se cancelan al restar las sumas de grados. Cada
diagonal aporta dos extremos a su color, de donde y−x=1. Al restar
la suma de grados de D₀ de la de A también se cancelan las diagonales
A–D₀. Queda una diferencia de m+n entre incidencias ortogonales.

Cuéntala en los otros extremos, en B∪C. Sin diagonal, una casilla tiene
una arista horizontal y otra vertical: dos del mismo eje implicarían
seguir recto o repetir casilla. Un vecino pertenece a A y el otro a D₀,
de modo que el aporte es cero. Con una diagonal aporta como máximo
uno, y con dos vuelve a aportar cero. Hay como máximo 2x casillas
con una diagonal. Luego m+n≤2x y x+y=2x+1≥m+n+1.

El ejemplo de 7×7 alcanza la cota con 15 diagonales. Corta el recorrido
entre las filas 3 y 4, contando desde cero. Solo cruzan aristas verticales
en las columnas 1, 2, 4 y 6. Inserta dos filas y reemplaza esas aristas
por `↓←↓→↓`, `↓→↓←↓`, `↓→↙↓` y `↓↙→↓`, respectivamente.
Cubren las 14 casillas nuevas, usan diagonales en dos cuadrados distintos
y conservan la dirección vertical en los extremos. El corte superior
conserva los mismos cruces y permite repetir la inserción para cualquier
altura impar con ancho siete. La transposición intercambia los lados.
Para ensanchar el ejemplo, refléjalo de izquierda a derecha. Inserta
cuatro columnas después de la columna 4. Las dos aristas que cruzan
el corte parten de (2,4) y (5,4) por la izquierda. Reemplázalas por
`↗↑→↘↑→↓→` y `↘→↑←↑→↑←↑→↑↘→↓←↓→↙↓→↑↘`, respectivamente,
desplazando cuatro columnas sus extremos derechos. Las rutas cubren
el bloque y añaden cuatro diagonales. Sus giros permiten repetir la
inserción en el mismo corte. En el corte por filas, las primeras tres
columnas conservan las dos aristas verticales exteriores, y cada par
restante tiene una. Se puede aplicar la inserción de dos filas a cada
bloque, reflejando la ruta de dos columnas cuando haga falta. Así se
alcanza la cota cuando alguna dimensión es congruente con 3 módulo 4.
[Dibujo oficial](https://sp.urfu.ru/usu/okt_08/USU_champ_08.pdf#page=4)

Binary64
basta para 10⁻⁹ incluso en el tamaño máximo; usa punto decimal con
cualquier configuración regional.

### Ambos lados son congruentes con 1 módulo 4

Parte de este recorrido de 9×9. Visita las casillas en orden y vuelve de 81 a 1. Tiene 19 diagonales.

```text
 1 81 79 78 75 74 72 70 69
 3  2 80 77 76 51 73 71 68
 4  5 45 46 49 50 52 67 66
 6 43 44 47 48 54 53 64 65
 7 42 41 39 38 55 56 63 62
 9  8 40 37 35 34 57 61 60
10 11 19 20 36 33 32 58 59
12 15 18 21 23 24 27 31 30
13 14 16 17 22 25 26 28 29
```

Las rutas de cada inserción de cuatro filas se dan en orden de entrada. Para las entradas 0 y 1 usa `↓↘←↓→↙↓` / `↓→↓→↑→↓↙→↓←↖↓←↓`. Para 0 y 3 usa `↓→↙↓↘←↓` / `↓→↓←↖↓←↓→↓↗→↓←↓`. Cada inserción cubre cuatro filas de cinco casillas, añade cuatro diagonales y conserva los pasos verticales en los extremos. En un bloque de dos columnas con una entrada, repite dos veces la inserción de dos filas en U.

Primero ensancha tras la columna 4. Las aristas horizontales que cruzan el corte están en las filas 0, 2, 5 y 7. Transpone la inserción de entradas 0 y 3 sobre las filas 2–6 y las rutas de dos columnas sobre las filas 0–1 y 7–8. El corte se conserva. Cada inserción añade un cruce vertical por par nuevo de columnas en el corte tras la fila 3. Luego aumenta la altura en ese corte. Usa la inserción de entradas 0 y 1 en las primeras cinco columnas y las rutas de dos columnas en los pares restantes. Cada cuatro filas o columnas nuevas añaden cuatro diagonales. Los dos tableros iniciales cubren todas las dimensiones permitidas.

## Soluciones optimizadas

Go y Java evalúan la misma fórmula mn + (m+n+1)(√2−1). Solo cambia E/S: Go analiza dos enteros con búferes fijos de64bytes y emite directamente las partes entera y fraccionaria de doce cifras, sin fmt, strconv ni guardar la entrada completa; Java lee directamente y emite double sin Scanner, Locale ni String.format. Go imprime doce decimales; Double.toString conserva suficientes cifras significativas. Las comprobaciones independientes con 60 cifras incluyen todos los cuadrados válidos y tableros 7×n; verifican la evaluación, no una nueva prueba del recorrido. Tiempo y espacio O(1). Se conservan las versiones ordinarias; C++, Python y Rust reutilizan las bases admitidas.

Las implementaciones base aceptadas [1631_math.cpp](1631_math.cpp), [1631_math.py](1631_math.py), [1631_math.rs](1631_math.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1631_math.cpp](1631_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 140 KB | 11288421 |
| [1631_math.go](1631_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1084 KB | 11288422 |
| [1631_math.java](1631_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1800 KB | 11288424 |
| [1631_math.py](1631_math.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 412 KB | 11288423 |
| [1631_math.rs](1631_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 252 KB | 11328279 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1631_math_optimized.java](1631_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.109 s | 460 KB | 11315360 |
| [1631_math_optimized.go](1631_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 292 KB | 11315798 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
