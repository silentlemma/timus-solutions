# 1611. Decimación

[Timus 1611](https://acm.timus.ru/problem.aspx?space=1&num=1611) · dificultad 698 · dp

Problema original de Alexander Ipatov (idea de Stanislav Vasiliev), del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n ≤ 10000 revisores forman una fila, cada uno bueno (`1`) o malo (`0`);
se multa a toda persona cuyo puesto es múltiplo de 10. Antes de las
multas se pueden meter en la fila, donde se quiera, hasta k ≤ 50 amigos
de los revisores. Hay que minimizar el número de amigos multados más el
de revisores buenos multados, e imprimirlo con los puestos de los amigos
en la nueva fila. Vale cualquier fila óptima.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

n y k, y luego la fila como una cadena de `0` y `1`.

## Salida

El menor número de esas multas, luego m y los m puestos de los amigos.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 2
0000000001
```

Salida:

```
0
2 5 12
```

### Ejemplo 2

Entrada:

```
10 2
1111111111
```

Salida:

```
1
0
```

## Solución

Se construye la nueva fila desde delante. Tras i revisores y j amigos,
la siguiente persona está en el puesto i + j + 1, sea quien sea. Así que
cost[i][j], el menor número de multas hasta ahí, tiene dos movimientos:
entra un amigo, multado si ese puesto es múltiplo de 10, o entra el
revisor i + 1, que suma una multa solo si es bueno y está en un puesto
así. Los amigos tras el último revisor solo podrían recibir multas, así
que nunca hacen falta. La respuesta es el menor cost[n][j] con j ≤ k, y
recorrer la tabla hacia atrás da los puestos de los amigos: `O(n·(k + 1))`.

Las pruebas usan un verificador que reconstruye la fila a partir de los
puestos impresos y cuenta sus multas. Los números se contrastaron con
probar todos los conjuntos de puestos para los amigos en filas cortas.

Detalles a tener en cuenta:

- un amigo desplaza un puesto a todos los revisores que tiene detrás,
  así que un amigo delante puede salvar de golpe a todos los revisores
  buenos (prueba 05), y un segundo amigo puede solo añadir una multa;
- los propios amigos se multan en los puestos décimos, y la fila más
  larga puede alcanzar un nuevo puesto décimo (prueba 08);
- la respuesta no es única: en el primer ejemplo se ponen dos amigos,
  pero uno delante es igual de bueno.

## Soluciones optimizadas

La programación dinámica solo se actualiza en los puestos múltiplos de diez, donde puede haber multa. Una cola monótona elige el estado anterior de menor coste entre los números de amigos factibles y se guarda un byte por estado para reconstruir la fila.

El envío 11317970 en Python tardó 0.093 s y usó 848 KB. La versión sencilla tardó 0.375 s y usó 13328 KB.

El envío 11317975 en Go tardó 0.015 s y usó 1248 KB. La versión sencilla tardó 0.031 s y usó 6184 KB.

El envío 11317985 en Java tardó 0.093 s y usó 660 KB. La versión sencilla tardó 0.125 s y usó 2792 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321890 · Go 1.14 x64 №11322096 · Rust 1.75 x64 №11321891 · Java 1.8 №11322098 · Python 3.12 x64 №11322099.

La versión compacta guarda una fila de costes y un bit por estado para reconstruir la colocación. Rust 1.75 x64, envío 11322342. Tiempo 0,046 → 0,046 s, memoria 4520 → 224 KB.

La versión compacta guarda una fila de costes y un bit por estado para reconstruir la colocación. G++ 13.2 x64, envío 11322343. Tiempo 0,015 → 0,015 s, memoria 2412 → 204 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1611_dp.cpp](1611_dp.cpp) | G++ 13.2 x64 | dp | O(n·(k + 1)) | AC | 0.015 s | 2412 KB | 11321890 |
| [1611_dp.go](1611_dp.go) | Go 1.14 x64 | dp | O(n·(k + 1)) | AC | 0.031 s | 6184 KB | 11322096 |
| [1611_dp.java](1611_dp.java) | Java 1.8 | dp | O(n·(k + 1)) | AC | 0.125 s | 2792 KB | 11322098 |
| [1611_dp.py](1611_dp.py) | Python 3.12 x64 | dp | O(n·(k + 1)) | AC | 0.375 s | 13328 KB | 11322099 |
| [1611_dp.rs](1611_dp.rs) | Rust 1.75 x64 | dp | O(n·(k + 1)) | AC | 0.046 s | 4520 KB | 11321891 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1611_dp_optimized.py](1611_dp_optimized.py) \* | Python 3.12 x64 | dp | O((n + k)·(k + 1)) | AC | 0.093 s | 848 KB | 11317970 |
| [1611_dp_optimized.go](1611_dp_optimized.go) \* | Go 1.14 x64 | dp | O((n + k)·(k + 1)) | AC | 0.015 s | 1248 KB | 11317975 |
| [1611_dp_optimized.java](1611_dp_optimized.java) \* | Java 1.8 | dp | O((n + k)·(k + 1)) | AC | 0.093 s | 660 KB | 11317985 |
| [1611_dp_optimized.rs](1611_dp_optimized.rs) | Rust 1.75 x64 | dp | O(n·(k + 1)) | AC | 0.046 s | 224 KB | 11322342 |
| [1611_dp_optimized.cpp](1611_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(n·(k + 1)) | AC | 0.015 s | 204 KB | 11322343 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
