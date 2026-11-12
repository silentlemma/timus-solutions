# 1236. Recuperar una clave XOR a partir de un mensaje desplazado

[Timus 1236](https://acm.timus.ru/problem.aspx?space=1&num=1236) · dificultad 499 · math

Problema original de Elena Kruchkova, del concurso regional ACM ICPC del noreste de Europa 2002–2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los mensajes se cifran byte a byte como `E[i] = K[i] xor C[i]` con una
clave secreta K. El mismo texto claro de N bytes (1 ≤ N ≤ 10 000) se
envió dos veces: tal cual y con un espacio (byte 32) delante. Dados los
dos mensajes cifrados, hay que recuperar los primeros N + 1 bytes de la
clave.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Dos líneas de dígitos hexadecimales: el mensaje cifrado de N bytes y
luego el de N + 1 bytes.

## Salida

Los N + 1 bytes de la clave en la misma forma hexadecimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
05262C5269143F314C2A69651A264B
610728413B63072C52222169720B425E
```

Salida:

```
41434D2049435043204E454552432732
```

## Solución

Llamamos S (corto) y L (largo) a los mensajes cifrados. El texto largo
empieza con el espacio conocido, así que `K[0] = L[0] xor 32`. Después,
el byte i + 1 del mensaje largo y el byte i del corto esconden el mismo
byte claro C[i]:

```text
C[i] = S[i] xor K[i],   K[i+1] = L[i+1] xor C[i] = L[i+1] xor S[i] xor K[i]
```

Cada byte de la clave da el siguiente, así que una sola pasada recupera
los N + 1. `O(N)`.

Detalles a tener en cuenta:

- cada byte se imprime como dos dígitos en mayúscula, con un cero delante
  si es menor que 16 (prueba gen3).

## Soluciones optimizadas

Sean P el texto claro, K la clave, S el cifrado corto y L el largo. El espacio inicial da `K[0] = L[0] XOR espacio`. En la posición i, `S[i] = P[i] XOR K[i]` y `L[i+1] = P[i] XOR K[i+1]`. El XOR cancela P[i] y da `K[i+1] = K[i] XOR S[i] XOR L[i+1]`. Cada byte de la clave se emite al recuperarlo. C++, Go, Java y Rust guardan el cifrado corto en 10000 bytes y usan bloques de 4096 bytes para entrada y salida. Java convierte bytes con signo mediante la máscara 255. El recorrido cuesta O(N). Python reutiliza la implementación base.

El envío aceptado en Java 1.8 tarda 0.125 s frente a 0.109 s de la base y usa 408 KB frente a 1756 KB.

El envío aceptado en Rust 1.75 x64 tarda 0.046 s frente a 0.015 s de la base y usa 208 KB frente a 368 KB.

Las implementaciones base aceptadas [1236_math.py](1236_math.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Go/Python originales usan conversión hex de biblioteca; C++/Go/Java/Rust nuevos analizan dígitos y emiten la recurrencia. Java amplía bytes con máscara255. Python conserva su versión de biblioteca.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1236_math.cpp](1236_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 376 KB | 11283792 |
| [1236_math.go](1236_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1364 KB | 11283795 |
| [1236_math.java](1236_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 1756 KB | 11283798 |
| [1236_math.py](1236_math.py) \* | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 488 KB | 11283796 |
| [1236_math.rs](1236_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 368 KB | 11283799 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1236_math_optimized.cpp](1236_math_optimized.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.001 s | 76 KB | 11315388 |
| [1236_math_optimized.go](1236_math_optimized.go) \* | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 824 KB | 11315392 |
| [1236_math_optimized.java](1236_math_optimized.java) \* | Java 1.8 | math | O(N) | AC | 0.125 s | 408 KB | 11315395 |
| [1236_math_optimized.rs](1236_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.046 s | 208 KB | 11315404 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
