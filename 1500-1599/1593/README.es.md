# 1593. El país cuadrado. Versión 2

[Timus 1593](https://acm.timus.ru/problem.aspx?space=1&num=1593) · dificultad 729 · math

Problema original preparado por Fedor Menshikov, con agradecimiento especial a Svyatoslav Demidov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La tierra se vende en parcelas cuadradas de lado entero, y una parcela de
lado a cuesta a². Hay que gastar exactamente N ≤ 10¹⁵ en el menor número
posible de parcelas e imprimir cuántas hacen falta. Es el
[problema 1073](../../1000-1099/1073/README.es.md) con un N mucho mayor.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

El menor número de cuadrados que suman N.

## Ejemplos

### Ejemplo 1

Entrada:

```
344
```

Salida:

```
3
```

## Solución

Por el teorema de Lagrange todo N es suma de cuatro cuadrados, así que la
respuesta va de 1 a 4, y teoremas clásicos dicen cuál:

- 1 cuando N es un cuadrado perfecto;
- 2 cuando cada primo de la forma 4k + 3 divide a N un número par de
  veces (teorema de Fermat sobre sumas de dos cuadrados);
- 4 cuando N = 4ᵃ(8b + 7), tras quitar todos los factores 4 (teorema de
  los tres cuadrados de Legendre);
- 3 en otro caso.

Solo la prueba de dos cuadrados necesita factorizar N. En C++, Go, Java
y Rust basta la división por tanteo entre impares hasta √N, como mucho
unos 1,6·10⁷; lo que queda al final es 1 o un primo. En Python ese bucle
es demasiado lento, así que los divisores pequeños hasta 1000 se quitan
por tanteo y el resto se parte con el método ρ de Pollard, con una
prueba de Miller–Rabin con los doce primeros primos como bases, que es
exacta mucho más allá de 10¹⁵.

Las respuestas se contrastaron con una programación dinámica sobre todos
los N hasta 20000.

Detalles a tener en cuenta:

- la raíz cuadrada exige cuidado: la raíz en coma flotante de un número
  cercano a 10¹⁵ puede fallar por uno, así que se corrige con pasos
  enteros;
- el producto de dos primos cercanos a √N, ambos 4k + 3, no tiene
  factores pequeños y deja resto 1 módulo 4, así que parar la división
  por tanteo en la raíz cúbica y adivinar el resto da una respuesta
  errónea (prueba 06);
- el factor que queda tras la división por tanteo también hay que
  comprobarlo: si N es él mismo un primo 4k + 3, nada lo divide por
  debajo de √N (prueba 08); el primo 2 nunca importa, porque
  2 = 1 + 1.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1593_math.cpp](1593_math.cpp) | G++ 13.2 x64 | math | O(√N) | AC | 0.171 s | 132 KB |
| [1593_math.go](1593_math.go) | Go 1.14 x64 | math | O(√N) | AC | 0.203 s | 1080 KB |
| [1593_math.java](1593_math.java) | Java 1.8 | math | O(√N) | AC | 0.546 s | 1632 KB |
| [1593_math.py](1593_math.py) | Python 3.12 x64 | math | O(√N) | AC | 0.109 s | 928 KB |
| [1593_math.rs](1593_math.rs) | Rust 1.75 x64 | math | O(√N) | AC | 0.171 s | 224 KB |
