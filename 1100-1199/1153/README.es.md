# 1153. Recuperar N a partir de la suma 1 + 2 + … + N de hasta 600 cifras

[Timus 1153](https://acm.timus.ru/problem.aspx?space=1&num=1153) · dificultad 332 · math

Problema original de Evgeny Bryzgalov, del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda en inglés.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un ordenador sumó los enteros de 1 a `N`, `0 < N < 10³⁰⁰`, e imprimió la
suma `S`, pero `N` se ha perdido. Dado `S`, que siempre es una suma así,
halla `N`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`S`.

## Salida

`N`.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
28
```

Salida:

```
7
```

## Solución

`S = N(N + 1)/2`, así que `8S + 1 = 4N² + 4N + 1 = (2N + 1)²` es un
cuadrado perfecto y `N = (√(8S + 1) − 1) / 2`. La única dificultad es el
tamaño: `S` tiene hasta 600 cifras, así que la raíz necesita enteros
grandes.

El método escolar de la raíz cuadrada a mano va cifra a cifra y solo
necesita multiplicar por números pequeños, sumar, comparar y restar. Se
parte `8S + 1` en pares de cifras desde la derecha. Se guarda la raíz
hallada hasta ahora, `r`, y un resto. Para cada par siguiente se añade al
resto (multiplicar por 100 y sumar), se busca la mayor cifra `x` con
`(20r + x)·x` no mayor que el resto, se resta ese producto y se añade `x` a
la raíz. Tras el último par la raíz es `2N + 1`; se resta uno y se divide
entre dos desde la cifra más alta. Con unos 300 pares y como mucho nueve
intentos cada uno sobre números de 600 cifras, son unos pocos millones de
operaciones con cifras.

Detalles a tener en cuenta:

- ni `S` ni `N` caben en ningún entero de máquina;
- `8S + 1` puede tener un número impar de cifras; un cero a la izquierda
  alinea los pares;
- `N = 1` da `S = 1`, y la raíz de `9` es `3`.

Las respuestas se comprobaron en todas las pruebas calculando de vuelta
`N(N + 1)/2` con enteros de Python.

## Soluciones optimizadas

Ambas versiones invierten la misma identidad 8S + 1 = (2N + 1)² mediante la raíz cuadrada entera exacta. Go usa vectores decimales fijos y baja las cifras por parejas. Para el prefijo de raíz r, elige la mayor cifra x cuyo (20r + x)x no supera el resto, resta esa contribución y añade x a la raíz. Después resta uno y divide por dos. Usa O(L²) tiempo y O(L) espacio, sin enteros grandes generales ni cadenas temporales. Python parte de una potencia de dos superior a la raíz y aplica pasos enteros de Newton mientras disminuyan. Con L cifras de entrada, O(L² log(L+1)) es una cota conservadora con división cuadrática.

Las implementaciones base aceptadas [1153_math.cpp](1153_math.cpp), [1153_math.java](1153_math.java), [1153_math.rs](1153_math.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

`1153_math_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado. Para esta implementación Java se usa la misma cota conservadora que en la variante Python de Newton existente: O(L² log(L+1)) con división cuadrática de enteros grandes, donde L es la longitud decimal de entrada. Comenzar por encima de la raíz da O(log(L+1)) pasos de Newton, cada uno con división de números de O(L) cifras. Se aclara la complejidad tanto del código sencillo Java sin modificar como de la nueva variante que cambia solo la entrada.

Frente a `1153_math.java`: tiempo 0.140 s → 0.125 s; memoria 1676 KB → 736 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1153_math_implementation_optimized.rs`. La entrada de C llama directamente al solucionador y vacía la salida de Rust antes de volver; se conserva la implementación de entrada habitual.

Accepted #11328983 (Rust 1.75 x64): **0.031 s / 356 KB**. Comparación archivada: `1153_math.rs` (Rust 1.75 x64) — 0.046 s / 456 KB (#11280829).


`1153_math_binary_search_parsing_optimized.go`. Se calcula la raíz de 8S+1 con aritmética decimal exacta en arreglos fijos. Cada dígito se elige por búsqueda binaria en lugar de probar desde nueve, conservando la comparación y resta exactas del resto. Se resta uno y se divide entre dos. La E/S de bytes evita inicializar math/big y reservar tokens. Para L dígitos, tiempo O(L²) y almacenamiento acotado por los 600 dígitos de entrada.

Este código exacto tiene su propio Accepted y cumple los [criterios compartidos](../../RATING_CRITERIA.md). El tiempo y la memoria siguientes proceden de una misma ejecución; las mediciones repetidas pueden variar. Se conservan las versiones sencillas y optimizadas distintas existentes.

Accepted #11329520 (Go 1.14 x64): **0.015 s / 312 KB**.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Python usa `math.isqrt` sobre sus enteros incorporados y Go usa
  `big.Int.Sqrt`.
- Java 8 no tiene `BigInteger.sqrt`, así que aplica el método de Newton,
  `x ← (x + D/x)/2`, desde una potencia de dos mayor que la raíz.
- C++ y Rust no tienen enteros grandes en la biblioteca estándar y hacen
  la raíz a mano sobre cifras decimales.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1153_math.cpp](1153_math.cpp) | G++ 13.2 x64 | math | O(L²) | AC | 0.015 s | 504 KB | 11280703 |
| [1153_math.go](1153_math.go) | Go 1.14 x64 | math | O(L²) | AC | 0.031 s | 1212 KB | 11280739 |
| [1153_math.java](1153_math.java) | Java 1.8 | math | O(L² log(L+1)) | AC | 0.140 s | 1676 KB | 11280808 |
| [1153_math.py](1153_math.py) | Python 3.12 x64 | math | O(L²) | AC | 0.093 s | 480 KB | 11280773 |
| [1153_math.rs](1153_math.rs) | Rust 1.75 x64 | math | O(L²) | AC | 0.046 s | 456 KB | 11280829 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1153_math_greedy.go](1153_math_greedy.go) | Go 1.14 x64 | math, greedy | O(L²) | AC | 0.031 s | 800 KB | 11311117 |
| [1153_math_optimized.py](1153_math_optimized.py) | Python 3.12 x64 | math | O(L² log(L+1)) | AC | 0.093 s | 408 KB | 11311055 |
| [1153_math_optimized.java](1153_math_optimized.java) | Java 1.8 | math | O(L² log(L+1)) | AC | 0.125 s | 736 KB | 11324796 |
| [1153_math_implementation_optimized.rs](1153_math_implementation_optimized.rs) | Rust 1.75 x64 | math, implementation | O(L²) | AC | 0.031 s | 356 KB | 11328983 |
| [1153_math_binary_search_parsing_optimized.go](1153_math_binary_search_parsing_optimized.go) | Go 1.14 x64 | math, binary_search, parsing | O(L²) time; bounded decimal arrays | AC | 0.015 s | 312 KB | 11329520 |
