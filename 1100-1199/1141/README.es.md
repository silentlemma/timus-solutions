# 1141. Descifrar mensajes RSA pequeños factorizando el módulo

[Timus 1141](https://acm.timus.ru/problem.aspx?space=1&num=1141) · dificultad 364 · number_theory

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
Entonces `c^d = m^(e·d) ≡ m (mod n)`: módulo cada primo `r` que divide a
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

## Notas por lenguaje

- Todos los lenguajes factorizan, invierten y elevan igual; Python usa el
  `pow(e, -1, phi)` incorporado para el inverso.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1141_number_theory.cpp](1141_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 216 KB |
| [1141_number_theory.go](1141_number_theory.go) | Go 1.14 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 1156 KB |
| [1141_number_theory.java](1141_number_theory.java) | Java 1.8 | number_theory | O(K (√n + log n)) | AC | 0.046 s | 596 KB |
| [1141_number_theory.py](1141_number_theory.py) | Python 3.12 x64 | number_theory | O(K (√n + log n)) | AC | 0.046 s | 992 KB |
| [1141_number_theory.rs](1141_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K (√n + log n)) | AC | 0.001 s | 352 KB |
