# 1608. Billetes de la suerte 2008

[Timus 1608](https://acm.timus.ru/problem.aspx?space=1&num=1608) · dificultad 1042 · math

Problema original de Sergey Pupyrev, del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los billetes se numeran 1, 2, 3, … sin ceros a la izquierda. Un billete
d₁d₂…dₙ es de la suerte si no hay dos cifras simétricas iguales:
dᵢ ≠ dₙ₊₁₋ᵢ siempre que i ≠ n + 1 − i. Hay que contar los billetes de la
suerte de a a b (1 ≤ a ≤ b ≤ 10¹⁸).

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

a y b.

## Salida

El número de billetes de la suerte.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 10
```

Salida:

```
10
```

### Ejemplo 2

Entrada:

```
100 2000
```

Salida:

```
1620
```

## Solución

Se cuentan los billetes de la suerte hasta n, f(n), y se imprime
f(b) − f(a − 1).

Las cifras se agrupan en pares simétricos y, si la longitud es impar,
una cifra central. Con algunas cifras iniciales fijadas, el resto se
cuenta par a par: un par con las dos cifras fijadas debe tenerlas
distintas (si no, la cuenta es 0), un par con solo la cifra izquierda
fijada deja 9 opciones para la derecha, un par con las dos libres deja
10·9 = 90, y una cifra central libre 10. Un prefijo siempre se fija por
la izquierda, así que un par nunca tiene fijada solo la cifra derecha.

f(n) suma todos los números más cortos según su primera cifra de 1 a 9,
y los de la longitud de n menores que n según la primera posición en que
quedan por debajo de n y la cifra menor puesta allí; se suma n si es de
la suerte. Con 19 cifras como mucho son unos pocos miles de pasos.

Las cuentas se contrastaron con comprobar todos los números hasta
300000.

Detalles a tener en cuenta:

- la primera cifra no puede ser 0, tampoco al contar los números más
  cortos;
- la cifra central de una longitud impar no tiene pareja y siempre es
  libre;
- la cuenta hasta 10¹⁸ es de unos 3,9·10¹⁷ y cabe en 64 bits, pero a − 1
  puede ser 0, y entonces la cuenta es 0.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1608_math.cpp](1608_math.cpp) | G++ 13.2 x64 | math | O(L²) | AC | 0.031 s | 196 KB |
| [1608_math.go](1608_math.go) | Go 1.14 x64 | math | O(L²) | AC | 0.046 s | 1084 KB |
| [1608_math.java](1608_math.java) | Java 1.8 | math | O(L²) | AC | 0.109 s | 1644 KB |
| [1608_math.py](1608_math.py) | Python 3.12 x64 | math | O(L²) | AC | 0.062 s | 576 KB |
| [1608_math.rs](1608_math.rs) | Rust 1.75 x64 | math | O(L²) | AC | 0.031 s | 228 KB |
