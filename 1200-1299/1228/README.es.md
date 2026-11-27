# 1228. Los límites de un arreglo a partir de sus multiplicadores de índice

[Timus 1228](https://acm.timus.ru/problem.aspx?space=1&num=1228) · dificultad 109 · math

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo de `n` dimensiones `array[0..k1, 0..k2, …, 0..kn]`, `n ≤ 20`,
se dispone con el último índice cambiando más rápido, así que el elemento
`X[i1, …, in]` tiene número `1 + D1·i1 + … + Dn·in` para ciertos
multiplicadores `Di`. Dados los multiplicadores y el número total de
elementos `s`, hay que hallar los límites superiores `k1, …, kn`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` (`1 ≤ n ≤ 20`) y `s` (`1 ≤ s < 2³¹ − 1`), y luego `D1, …, Dn`.

## Salida

`k1, …, kn` (`0 < ki ≤ 1000`) separados por espacios o saltos de
línea.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 180
90
18
6
1
```

Salida:

```
1 4 2 5
```

## Solución

Aumentar en uno el índice `i` salta un bloque entero de las dimensiones
siguientes, así que `D(i−1) = Di · (ki + 1)`, y el arreglo entero es un
bloque de la primera dimensión: `s = D1 · (k1 + 1)`. Leyendo los
multiplicadores con `s` delante, cada límite es uno menos que el
cociente de dos vecinos: `k1 = s/D1 − 1` y `ki = D(i−1)/Di − 1`. `O(n)`.

Con enteros acotados la aritmética cuesta O(n). C++/Go/Java sencillos guardan n+1 tamaños, O(n) entradas; Python/Rust sencillos retienen además entrada, enteros y respuestas: O(I+n) para I bytes. C++/Rust optimizados emiten al leer, estado aritmético O(1) más búferes. Java optimizado mantiene entrada escalar pero acumula StringBuilder, O(n) salida. Python optimizado guarda bloque de 65536 bytes/tokens y n respuestas, O(n+B+T), con bloque B y token máximo T. Go optimizado conserva array y toda la entrada O(I+n); cambiar I/O no eliminó el array.

Detalles a tener en cuenta:

- el último multiplicador es siempre 1, y el primer límite sale de `s`,
  no de un multiplicador;
- los productos son menores que `2³¹ − 1`, así que bastan enteros de
  32 bits con signo para las cuentas.

Los límites se comprobaron multiplicando `ki + 1` hasta `s` en 59
arreglos generados, y se compararon con una solución escrita aparte en
todas las pruebas.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

La solución optimizada en C++ lee los multiplicadores de uno en uno y
guarda solo el anterior, imprimiendo cada cota en cuanto llega su
divisor, en lugar de guardar `s` y todos los multiplicadores en un
`std::vector`: {1228_math_optimized.cpp}.

La solución optimizada en Java analiza los números cifra a cifra
directamente desde `System.in` en lugar de crear un `Scanner`, y guarda
solo el multiplicador anterior en lugar de un arreglo con todos:
{1228_math_optimized.java}.

### Mejora medida

Son diferencias históricas entre valores Accepted originales, no admisión universal por mejora del 30%. C++ de 0.015 a 0.001 s da 93.33% reducción original, pero ambos se comparan como 0.015 s tras el mínimo. Porcentajes bajo un tick no garantizan aceleración portátil. Se conservan bases significativas.

El par Go actual es base #11283735 de 0.001 s / 1136 KB y optimizado #11328526 de 0.015 s / 956 KB: 15.85% menos memoria, no 30%, y más tiempo original. Ambos tiempos de comparación tienen mínimo 0.015 s. Rige la política común, no una ganancia obligatoria.

- `1228_math_optimized.cpp`: reducción de tiempo +93.33%; reducción de
  memoria +36.00%; base: `1228_math.cpp`.

- `1228_math_optimized.java`: reducción de tiempo +50.40%; reducción de
  memoria +78.22%; base: `1228_math.java`.

`1228_math_optimized.py`. Conserva la reconstrucción por cocientes consecutivos: empieza con el tamaño total s y emite previous/current-1 por cada multiplicador. El último se procesa igual; la entrada válida proporciona cocientes enteros positivos. Hace O(n) divisiones de enteros acotados. El lector por bloques de 65536 bytes arrastra solo el token incompleto, sin entrada decodificada completa ni todos los enteros. Aún construye y une la lista de respuestas: O(n) espacio de salida más almacenamiento del analizador acotado por el tamaño de tokens. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1228_math.py`: tiempo 0.078 s → 0.109 s; memoria 424 KB → 212 KB.

`1228_math_optimized.rs`. Conserva la reconstrucción por cocientes consecutivos: empieza con el tamaño total s y emite previous/current-1 por cada multiplicador. El último se procesa igual; la entrada válida proporciona cocientes enteros positivos. Hace O(n) divisiones de enteros acotados. Lee y emite cada cociente inmediatamente, conservando solo el anterior y actual. Sin vector de entrada, cadenas por respuesta ni salida unida: estado auxiliar O(1). La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1228_math.rs`: tiempo 0.015 s → 0.015 s; memoria 216 KB → 52 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1228_math_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328526 (Go 1.14 x64): **0.015 s / 956 KB**. Comparación archivada: `1228_math.go` (Go 1.14 x64) — 0.001 s / 1136 KB (#11283735).

Go Accepted #11328526 y su admisión corresponden a bytes históricos exactos. Esta revisión nombra `numericBitSize` la anchura existente de 64 bits en cuatro llamadas strconv; sustituir 64 restaura exactamente el archivo previo. Se conservan algoritmo, comentarios y Go sencillo.

## Notas por lenguaje

La caché exacta y los [criterios compartidos](../../RATING_CRITERIA.md) confirman ambos C++, Go/Java optimizados, CPython sencillo y ambos Rust históricos. Go/Java sencillos quedan didácticos sin estrella. PyPy de 0.109 s / 212 KB falla tiempo y mantiene marca; puestos antiguos 21/32 tiempo y 1/32 memoria no imponen primer puesto separado. Los Go/Java optimizados que cumplen están bajo 1024 KB, solo exigen tiempo. Go sencillo 1136 KB falla memoria exigida pese al menor tiempo original. Rust usa grupo del mismo lenguaje y cumple numéricamente, no por tabla vacía ni excepción de ahorro.

Solo se completa el comentario de prueba en `1228_math.rs`: multiplicador por tamaño de su dimensión iguala el multiplicador anterior, o tamaño total para la primera. Revertir las dos líneas restaura bytes exactos, conservando texto ejecutable y demás comentarios. La base #11283740 de 0.015 s / 216 KB es del fuente histórico exacto.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1228_math.cpp](1228_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 200 KB | 11283732 |
| [1228_math.go](1228_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.001 s | 1136 KB | 11283735 |
| [1228_math.java](1228_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1616 KB | 11283739 |
| [1228_math.py](1228_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.078 s | 424 KB | 11283737 |
| [1228_math.rs](1228_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 208 KB | 11331096 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1228_math_optimized.cpp](1228_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.001 s | 128 KB | 11304270 |
| [1228_math_optimized.java](1228_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.062 s | 352 KB | 11304271 |
| [1228_math_optimized.py](1228_math_optimized.py) \* | PyPy 3.10 x64 | math | O(n) | AC | 0.109 s | 212 KB | 11325065 |
| [1228_math_optimized.rs](1228_math_optimized.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 52 KB | 11324870 |
| [1228_math_optimized.go](1228_math_optimized.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 988 KB | 11330997 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
