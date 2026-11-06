# 1141. Descifrar mensajes RSA pequeños factorizando el módulo

[Timus 1141](https://acm.timus.ru/problem.aspx?space=1&num=1141) · dificultad 363 · number_theory

Problema original de Mikhail Medvedev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para hasta `K ≤ 2000` consultas `e, n, c ≤ 32000`, donde `n = p·q` con dos
primos impares distintos y `e < (p − 1)(q − 1)` es coprimo con
`(p − 1)(q − 1)`, halla el mensaje `m` con `m^e ≡ c (mod n)`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`K` y luego `K` líneas con `e`, `n` y `c`.

## Salida

Un `m` por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
9 187 129
11 221 56
7 391 204
```

Salida:

```
7
23
17
```

## Solución

Es RSA con un módulo diminuto, así que basta con romperlo. La división
por impares desde 3 encuentra `p` en como mucho `√n < 179` pasos, y
entonces `φ = (p − 1)(q − 1)`. Como `e` es coprimo con `φ`, tiene un
inverso `d` módulo `φ`, que da el algoritmo de Euclides extendido.
Entonces `c^d ≡ m^(e·d) ≡ m (mod n)`: módulo cada primo `r` que divide a
`n`, `e·d = 1 + t·φ` es `1` más un múltiplo de `r − 1`, así que el pequeño
teorema de Fermat da `m^(e·d) ≡ m (mod r)`, también cuando `r` divide a
`m`, y el teorema chino del resto une los dos primos. Por tanto
`m = c^d mod n`, calculado por exponenciación rápida.
`O(√n + log n)` por consulta.

Detalles a tener en cuenta:

- `c` puede ser mayor que `n`; la exponenciación lo reduce primero;
- el mensaje puede compartir un factor con `n`; el descifrado sigue
  funcionando porque `n` no tiene factores cuadrados;
- el inverso del algoritmo de Euclides extendido puede salir negativo,
  así que se lleva a `[0, φ)`;
- todos los productos quedan por debajo de `32000²`, que cabe en enteros
  de 64 bits.

Las respuestas se compararon en todas las pruebas con probar cada `m` de
`0` a `n − 1`, lo que además confirmó que la respuesta es única.

## Soluciones optimizadas

Go y Rust criban una vez los primos impares hasta 178 y usan solo esos primos para factorizar cada módulo n ≤ 32000. Después calculan el exponente inverso con Euclides extendido y descifran por exponenciación binaria. Go usa búferes fijos de bytes y escribe las cifras directamente; Rust procesa la entrada y salida de forma incremental. La tabla de primos usa vectores de tamaño fijo.

Las implementaciones base aceptadas [1141_number_theory.cpp](1141_number_theory.cpp), [1141_number_theory.java](1141_number_theory.java), [1141_number_theory.py](1141_number_theory.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes factorizan, invierten y elevan igual; Python usa el
  `pow(e, -1, phi)` incorporado para el inverso.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1141_number_theory.cpp](1141_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 216 KB | 11279444 |
| [1141_number_theory.go](1141_number_theory.go) | Go 1.14 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 1156 KB | 11279445 |
| [1141_number_theory.java](1141_number_theory.java) \* | Java 1.8 | number_theory | O(K (√n + log n)) | AC | 0.046 s | 596 KB | 11279448 |
| [1141_number_theory.py](1141_number_theory.py) \* | Python 3.12 x64 | number_theory | O(K (√n + log n)) | AC | 0.046 s | 992 KB | 11279446 |
| [1141_number_theory.rs](1141_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 352 KB | 11279449 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1141_number_theory_optimized.go](1141_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(K (√n + log n)) | AC | 0.015 s | 772 KB | 11311153 |
| [1141_number_theory_optimized.rs](1141_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 200 KB | 11311025 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
