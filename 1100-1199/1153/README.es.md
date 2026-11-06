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
| [1153_math.java](1153_math.java) \* | Java 1.8 | math | O(L²) | AC | 0.140 s | 1676 KB | 11280808 |
| [1153_math.py](1153_math.py) | Python 3.12 x64 | math | O(L²) | AC | 0.093 s | 480 KB | 11280773 |
| [1153_math.rs](1153_math.rs) \* | Rust 1.75 x64 | math | O(L²) | AC | 0.046 s | 456 KB | 11280829 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1153_math_greedy.go](1153_math_greedy.go) \* | Go 1.14 x64 | math, greedy | O(L²) | AC | 0.031 s | 800 KB | 11311117 |
| [1153_math_optimized.py](1153_math_optimized.py) \* | Python 3.12 x64 | math | O(L² log(L+1)) | AC | 0.093 s | 408 KB | 11311055 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
