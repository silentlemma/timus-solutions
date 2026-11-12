# 2108. Clausura de un conjunto de figuras bajo reglas de deseos

[Timus 2108](https://acm.timus.ru/problem.aspx?space=1&num=2108) · dificultad 461 · bitmask

Problema original de Kirill Borozdin, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n figuras de colección. Cada uno de los m deseos dice: en cuanto se
tienen todas las figuras de un conjunto A, también se quieren todas las
de un conjunto B. A partir de las figuras ya obtenidas, hallar el menor
conjunto que satisface todos los deseos, es decir, el que se alcanza
cumpliendo deseos hasta que no se quiere nada nuevo. Los límites son 0.9
segundos y 64 MB.

## Entrada

n y m, 1 ≤ n ≤ 1000, 0 ≤ m ≤ 4000, luego m líneas con los conjuntos A y
B como cadenas de n ceros y unos, y el conjunto obtenido con el mismo
formato.

## Salida

El conjunto final con el mismo formato.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 4
111000 101000
110000 111000
010000 100000
000010 000001
010100
```

Salida:

```
111100
```

## Solución

Un conjunto que satisface todos los deseos y contiene las figuras
obtenidas tiene que contener cada figura a la que lleva alguna cadena de
deseos, y el conjunto de exactamente esas figuras satisface todos los
deseos. Así que se repiten pasadas sobre los deseos: un deseo cuyo A está
dentro del conjunto obtenido añade B. Una pasada que no añade nada
termina el proceso, y cualquier otra añade al menos una figura, así que
hay a lo sumo n + 1 pasadas.

Los conjuntos son bitsets de palabras de 64 bits: "A dentro del conjunto
obtenido" es A AND NOT owned = 0, y añadir B es un OR, ambas n / 64
operaciones de palabra. El trabajo total es O(n · m · n / 64), unas
6 · 10⁷ operaciones de palabra.

En el ejemplo las figuras obtenidas 2 y 4 activan el tercer deseo, que
añade 1; luego el segundo deseo añade 3, y el resultado es 111100.

## Soluciones optimizadas

C++, Go y Rust transponen las premisas en bitsets de reglas por figura y guardan cuántas premisas faltan por regla. Cada figura nueva entra una vez en la cola; al procesarla se decrementan sus reglas. Un contador cero dispara la regla una vez y añade consecuencias aún desconocidas. Las premisas vacías se disparan tras leer la entrada. Solo reglas habilitadas añaden figuras y todas se han disparado al terminar: se obtiene el cierre mínimo sin pasadas completas repetidas. Tiempo con lectura O(nm+n+m), almacenamiento O(n⌈m/64⌉+m⌈n/64⌉+n+m). Las dos matrices máximas ocupan 1016000 bytes. Go/C++ usan arreglos máximos acotados; Rust dimensiona vectores y usa E/S acotada del C runtime sin retener la entrada. Se conservan las bases; Java/Python reutilizan las admitidas.

El envío aceptado en G++ 13.2 x64 tarda 0.093 s frente a 0.046 s de la base y usa 1 080 KB frente a 1808 KB.

El envío aceptado en Go 1.14 x64 tarda 0.125 s frente a 0.062 s de la base y usa 1 284 KB frente a 18712 KB.

Las implementaciones base aceptadas [2108_bitmask.java](2108_bitmask.java), [2108_bitmask.py](2108_bitmask.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

La solución en Python traspone el problema, porque las pasadas son
demasiado lentas allí cuando una cadena de deseos aparece en orden
inverso. Para cada figura construye el conjunto de deseos que la
necesitan como un único entero grande (una columna de la matriz de
cadenas A). Un árbol de segmentos sobre las figuras guarda la unión de
esos conjuntos sobre las figuras que aún faltan, que es exactamente el
conjunto de deseos todavía no activados. Cada ronda cumple todos los
deseos recién activados y pone a cero las hojas de las figuras recién
obtenidas. Cada deseo se cumple como máximo una vez y la hoja de cada
figura se pone a cero como máximo una vez.

Sea w el número de bits por dígito de un entero de Python,
N = ceil(n / w), M = ceil(m / w) y L = 1 + ceil(log2 n). Para m > 0,
el tiempo es O(nm + (nL + m)M + nN): leer y trasponer cuesta O(nm),
actualizar el árbol y comprobar la activación cuesta O(nLM), enumerar
los deseos activados cuesta O(mM) y enumerar las figuras nuevas cuesta
O(nN). Unir los resultados cuesta O(mN), ya incluido en O(nm).
Para m = 0, el tiempo es O(n).

Trampa (prueba 15, resultados vacíos): un deseo que no añade nada aún
debe procesarse. Enumerar bits activos en Python no cuesta tiempo
constante por bit: `mask & -mask` y `mask ^= low` recorren los dígitos
del entero. Con n = 1 y m = 4000 deseos A = B = 0, la respuesta sigue
siendo 0, pero enumerar los deseos activados requiere Θ(m² / w)
operaciones sobre dígitos. Por eso, la cota O(n^2 m / 64) de las pasadas
repetidas no describe la solución en Python.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2108_bitmask.cpp](2108_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(n^2 m / 64) | AC | 0.046 s | 1808 KB | 11294887 |
| [2108_bitmask.go](2108_bitmask.go) | Go 1.14 x64 | bitmask | O(n^2 m / 64) | AC | 0.062 s | 18712 KB | 11294892 |
| [2108_bitmask.java](2108_bitmask.java) | Java 1.8 | bitmask | O(n^2 m / 64) | AC | 0.234 s | 1792 KB | 11294899 |
| [2108_bitmask.py](2108_bitmask.py) \* | Python 3.12 x64 | bitmask | O(nm + (nL + m)M + nN) | AC | 0.171 s | 17336 KB | 11294894 |
| [2108_bitmask.rs](2108_bitmask.rs) | Rust 1.75 x64 | bitmask | O(n^2 m / 64) | AC | 0.062 s | 9312 KB | 11294901 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2108_graphs_bitmask.cpp](2108_graphs_bitmask.cpp) \* | G++ 13.2 x64 | graphs, bitmask | O(nm + n + m) | AC | 0.093 s | 1080 KB | 11315229 |
| [2108_graphs_bitmask.go](2108_graphs_bitmask.go) \* | Go 1.14 x64 | graphs, bitmask | O(nm + n + m) | AC | 0.125 s | 1284 KB | 11315237 |
| [2108_graphs_bitmask.rs](2108_graphs_bitmask.rs) \* | Rust 1.75 x64 | graphs, bitmask | O(nm + n + m) | AC | 0.046 s | 1072 KB | 11315242 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
