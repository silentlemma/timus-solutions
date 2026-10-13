# 1435. Error financiero

[Timus 1435](https://acm.timus.ru/problem.aspx?space=1&num=1435) · dificultad 989 · math

Problema original de Evgeny Krokhalev, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se copiaron N números (N ≤ 200 000, cada uno como mucho 2³¹ − 1) de un
informe, y su suma difiere del total del informe (como mucho 10¹⁶). El
error de copia intercambió dos cifras vecinas de un número; ni la copia
ni el número real tienen ceros a la izquierda. Hay que imprimir «Input
has no error.» si las sumas coinciden, «Error in record #L. Correct
number is: K.» para un registro que un intercambio explica, o
«Unrecoverable error.».

Límite de tiempo: 0.4 segundos. Límite de memoria: 64 MB.

## Entrada

N, los N números copiados y luego el total del informe.

## Salida

Una de las tres líneas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
12
26
45
119
```

Salida:

```
Error in record #2. Correct number is: 62.
```

## Solución

Intercambiar las cifras a en 10^(i+1) y b en 10^i cambia un número en
(b − a)·10^(i+1) + (a − b)·10^i = 9·(b − a)·10^i. Así que la diferencia D
entre el total y la suma debe ser 9·c·10^i con 1 ≤ |c| ≤ 9: se divide D
entre 9, se quitan los factores de 10 para obtener i, y lo que queda es
c. Luego se recorren los registros como cadenas buscando uno cuyas
cifras en 10^(i+1) y 10^i difieran exactamente en c, saltando el
intercambio que llevaría un cero al principio, y se informa del primero
con las dos cifras devueltas a su sitio. `O(N)`.

Detalles a tener en cuenta:

- el número real puede pasar de 32 bits, como 9100000000 en lugar de
  1900000000 (prueba 04);
- 90 no puede ser copia de 09 ni 10 de 01 (pruebas 02, 06);
- el total mismo no se copió mal (prueba 07);
- leer 200 000 números en 0,4 segundos exige una entrada rápida; las
  soluciones lo leen todo de una vez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1435_math.cpp](1435_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.046 s | 8972 KB |
| [1435_math.go](1435_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.093 s | 14588 KB |
| [1435_math.java](1435_math.java) | Java 1.8 | math | O(N) | AC | 0.171 s | 18360 KB |
| [1435_math.py](1435_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.187 s | 15852 KB |
| [1435_math.rs](1435_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.046 s | 8336 KB |
