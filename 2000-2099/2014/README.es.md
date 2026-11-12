# 2014. Saldo de Crédito con Operaciones Desordenadas

[Timus 2014](https://acm.timus.ru/problem.aspx?space=1&num=2014) · dificultad 547 · segment_tree

Problema original de Nick Burlakov, preparado por Olga Soboleva, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El efectivo y el saldo de crédito empiezan en cero. Un ingreso añade
efectivo. Un gasto usa primero ese efectivo; cualquier déficit reduce el
saldo de crédito. Los ingresos posteriores no amortizan crédito:
permanecen como efectivo. Los informes llegan desordenados, pero
incluyen el momento real de cada operación. Tras recibir cada uno,
reconstruye el saldo usando solo las operaciones conocidas en orden
cronológico. La salida es cero o una deuda negativa.

## Entrada

Primero `n`, `1 ≤ n ≤ 100 000`. Cada línea siguiente contiene una
cantidad `−c` o `+c`, `1 ≤ c ≤ 50 000`, y un instante `dd.MM hh:mm`. Los
instantes son distintos y pertenecen a un mismo año no bisiesto. Se
enumeran en orden de recepción. Tiempo límite 1 segundo, memoria 64 MB.

## Salida

Imprime `n` enteros, uno por informe: el saldo de crédito reconstruido.
No tomes su valor absoluto. Los enteros únicos se comparan por tokens.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
5
-1000 10.09 21:00
+500 09.09 14:00
+1000 02.09 00:00
-1000 17.09 21:00
+500 18.09 13:00
```

```
-1000
-500
0
-500
-500
```

El primer gasto conocido crea −1000. Descubrir un ingreso anterior lo
corrige a −500; otro ingreso anterior elimina esa deuda. El siguiente
gasto produce −500. El último ingreso ocurrió después de la falta de
efectivo, por lo que añade efectivo y deja la deuda en −500.

## Solución

Sea `S` la suma cronológica acumulada y `D` el menor prefijo, incluido
el prefijo vacío cero. El crédito es `D` y el efectivo es `S−D`.
Inicialmente se cumple. Un ingreso aumenta `S` y efectivo sin reducir el
mínimo. Un gasto cubierto conserva `D`; si falta efectivo, el nuevo `S`
cae por debajo de `D`, se agota el efectivo y el crédito pasa a ese
menor valor. La inducción prueba ambas identidades: basta hallar el
mínimo prefijo.

Lee todos los instantes, ordena los índices por mes, día, hora y minuto,
y asigna rangos. Ordenar las cadenas originales que empiezan por el día
sería incorrecto. Construye un árbol de segmentos inicialmente nulo
sobre esos rangos. Los informes futuros contribuyen cero: conocer sus
coordenadas no usa sus cantidades. Procesa las llegadas, asigna a la
hoja su cantidad y escribe el mínimo prefijo de la raíz.

Cada segmento guarda suma `S` y mínimo prefijo `P`, incluyendo el vacío.
Para A seguido de B: `S=A.S+B.S`, `P=min(A.P,A.S+B.P)`. Todo prefijo
termina dentro de A o abarca A completo más un prefijo de B, de modo que
la combinación es exacta. Una hoja de valor `v` guarda `(v,min(0,v))`;
las desconocidas y de relleno guardan `(0,0)`. Por inducción en el
árbol, cada resumen es correcto. La raíz describe exactamente las
operaciones conocidas en orden temporal y, por la identidad del efectivo
y crédito, da la respuesta correcta.

La ordenación y las actualizaciones requieren tiempo `O(n log n)`; el
árbol iterativo y los arrays usan espacio `O(n)`. La magnitud puede
alcanzar `100 000·50 000=5 000 000 000`, por lo que se necesitan enteros
de 64 bits. Otra opción es sumar sobre sufijos de los saldos prefijos
cronológicos y mantener su mínimo global.

El árbol didáctico en C++ asigna una hoja a cada clave de minuto, ordenada por mes, día, hora y minuto. Cada informe escribe su importe directamente en la hoja y combina sumas y mínimos de prefijo hasta la raíz. La raíz da la deuda de inmediato. Las claves sin usar y el relleno tienen importe cero y conservan los mínimos de prefijo. La clave usa U = 12 × 32 × 24 × 60 posiciones. El árbol ocupa 32 MiB. Con N informes, el tiempo es O(U + N log U) y el espacio es O(U).

## Soluciones optimizadas

C++/Go conservan orden cronológico y resúmenes de prefijo mínimo. Empaquetan tiempo, índice de recepción y amount+50000 en uint64: 17 bits para cada uno de los dos últimos y menos de20 para el tiempo,54 en total. Rangos recuperan recepción; los importes futuros preleídos quedan inactivos. Árbol con hojas potencia de dos: cada hoja solo int32, pares int64 suma/prefijo solo en nodos internos. Calcular primer padre desde sus dos hojas y luego combinar normalmente. Evita resúmenes anchos redundantes, texto completo y lista de respuestas. Hojas de relleno cero, caso unitario directo. Totales hasta5×10^9 requieren int64. Tiempo O(N log N), espacio O(N), incluida ordenación/rangos y E/S acotada. Bases conservadas; Java/Python/Rust reutilizan admitidas, Python con su PyPy3.10 original.

Las implementaciones base aceptadas [2014_segment_tree.java](2014_segment_tree.java), [2014_segment_tree.py](2014_segment_tree.py), [2014_segment_tree.rs](2014_segment_tree.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

El orden de recepción no es el cronológico. Un ingreso posterior no
amortiza crédito, pero descubrir uno anterior puede corregirlo. Incluye
el prefijo cero, imprime deuda negativa y compara el mes antes del día.
La unicidad de instantes permite asignar cada hoja. Python usa un array
de rangos y dos listas del árbol y se ejecuta con PyPy: con CPython 3.12
supera el límite de tiempo en la prueba 15 del juez, mientras que con
PyPy 3.10 se acepta en 0.39 s. C++, Go, Java y Rust usan sumas amplias.
Java ordena pares clave/índice empaquetados en un array primitivo long
para evitar objetos; el empaquetado también usa 64 bits. Los lectores
admiten ambos signos y los separadores de fecha y hora.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2014_segment_tree.cpp](2014_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(n log n) | AC | 0.140 s | 6820 KB | 11292513 |
| [2014_segment_tree.go](2014_segment_tree.go) | Go 1.14 x64 | segment_tree | O(n log n) | AC | 0.093 s | 10724 KB | 11292514 |
| [2014_segment_tree.java](2014_segment_tree.java) | Java 1.8 | segment_tree | O(n log n) | AC | 0.250 s | 14608 KB | 11292516 |
| [2014_segment_tree.py](2014_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(n log n) | AC | 0.390 s | 21900 KB | 11295869 |
| [2014_segment_tree.rs](2014_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(n log n) | AC | 0.046 s | 10268 KB | 11292518 |
| [2014_segment_tree_prefix_sums.cpp](2014_segment_tree_prefix_sums.cpp) | G++ 13.2 x64 | segment_tree, prefix_sums | O(U + N log U) | AC | 0.14 s | 17048 KB | 11315932 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2014_segment_tree_optimized.cpp](2014_segment_tree_optimized.cpp) | G++ 13.2 x64 | segment_tree | O(N log N) | AC | 0.062 s | 3444 KB | 11315777 |
| [2014_segment_tree_optimized.go](2014_segment_tree_optimized.go) \* | Go 1.14 x64 | segment_tree | O(N log N) | AC | 0.078 s | 4692 KB | 11315779 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
