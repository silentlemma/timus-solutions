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

## Notas por lenguaje

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

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2014_segment_tree.cpp](2014_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(n log n) | AC | 0.140 s | 6820 KB |
| [2014_segment_tree.go](2014_segment_tree.go) | Go 1.14 x64 | segment_tree | O(n log n) | AC | 0.093 s | 10724 KB |
| [2014_segment_tree.java](2014_segment_tree.java) | Java 1.8 | segment_tree | O(n log n) | AC | 0.250 s | 14608 KB |
| [2014_segment_tree.py](2014_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(n log n) | AC | 0.390 s | 21900 KB |
| [2014_segment_tree.rs](2014_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(n log n) | AC | 0.046 s | 10268 KB |
