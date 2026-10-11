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

## Notas por lenguaje

- Go y Python codifican y decodifican el hexadecimal con funciones de la
  biblioteca; C++, Java y Rust convierten ellos mismos los pares de
  dígitos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1236_math.cpp](1236_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 376 KB |
| [1236_math.go](1236_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1364 KB |
| [1236_math.java](1236_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 1756 KB |
| [1236_math.py](1236_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 488 KB |
| [1236_math.rs](1236_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 368 KB |
